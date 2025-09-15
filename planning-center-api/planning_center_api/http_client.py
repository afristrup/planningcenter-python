"""HTTP client for Planning Center API."""

import asyncio
from typing import Any

import httpx
from httpx import Response

from .auth import PCOAuth
from .config import PCOConfig
from .exceptions import raise_for_status
from .models.base import PCOCollection, PCOResource
from .rate_limiter import PCORateLimiter


class PCOHttpClient:
    """HTTP client for Planning Center API with rate limiting and retry logic."""

    def __init__(self, config: PCOConfig):
        self.config = config
        self.auth = PCOAuth(config)
        self.rate_limiter = PCORateLimiter(
            max_requests=config.rate_limit_requests,
            window_seconds=config.rate_limit_window,
            backoff_factor=config.backoff_factor,
            max_retries=config.max_retries,
        )

        self._client: httpx.AsyncClient | None = None

    async def __aenter__(self):
        """Async context manager entry."""
        self._client = httpx.AsyncClient(
            timeout=httpx.Timeout(self.config.timeout),
            headers=self.auth.get_headers(),
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self._client:
            await self._client.aclose()
            self._client = None

    async def _make_request(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None = None,
        json_data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> Response:
        """Make an HTTP request with rate limiting and retry logic."""
        if not self._client:
            raise RuntimeError(
                "HTTP client not initialized. Use async context manager."
            )

        # Apply rate limiting
        await self.rate_limiter.acquire()

        # Prepare request
        request_headers = self.auth.get_headers()
        if headers:
            request_headers.update(headers)

        # Make request with retry logic
        for attempt in range(self.config.max_retries + 1):
            try:
                response = await self._client.request(
                    method=method,
                    url=url,
                    params=params,
                    json=json_data,
                    headers=request_headers,
                )

                # Handle rate limiting
                if response.status_code == 429:
                    retry_after = response.headers.get("Retry-After")
                    retry_after_int = int(retry_after) if retry_after else None
                    await self.rate_limiter.handle_rate_limit_error(retry_after_int)
                    continue

                # Raise for other error status codes
                if response.status_code >= 400:
                    try:
                        error_data = response.json()
                    except Exception:
                        error_data = {"error": response.text}
                    raise_for_status(response.status_code, error_data)

                return response

            except httpx.RequestError as e:
                print(f"Request error: {e}")
                if attempt == self.config.max_retries:
                    raise

                # Exponential backoff for network errors
                wait_time = self.config.retry_delay * (
                    self.config.backoff_factor**attempt
                )
                await asyncio.sleep(wait_time)

        raise RuntimeError("Max retries exceeded")

    def _build_url(
        self, product: str, endpoint: str, resource_id: str | None = None
    ) -> str:
        """Build API URL for a specific endpoint."""
        base_url = f"{self.config.base_url}/{product}/{self.config.api_version}"

        if resource_id:
            url = f"{base_url}/{endpoint}/{resource_id}"
        else:
            url = f"{base_url}/{endpoint}"

        return url

    def _build_params(
        self,
        per_page: int | None = None,
        offset: int | None = None,
        include: list[str] | None = None,
        filter_params: dict[str, Any] | None = None,
        sort: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Build query parameters for API requests."""
        params = {}

        if per_page is not None:
            params["per_page"] = min(per_page, self.config.max_per_page)

        if offset is not None:
            params["offset"] = offset

        if include:
            params["include"] = ",".join(include)

        if filter_params:
            for key, value in filter_params.items():
                if isinstance(value, list):
                    params[f"where[{key}]"] = ",".join(str(v) for v in value)
                else:
                    params[f"where[{key}]"] = str(value)

        if sort:
            params["order"] = sort

        # Add any additional parameters
        params.update(kwargs)

        return params

    async def get(
        self,
        product: str,
        endpoint: str,
        resource_id: str | None = None,
        per_page: int | None = None,
        offset: int | None = None,
        include: list[str] | None = None,
        filter_params: dict[str, Any] | None = None,
        sort: str | None = None,
        **kwargs: Any,
    ) -> PCOResource | PCOCollection:
        """Make a GET request to the API."""
        url = self._build_url(product, endpoint, resource_id)
        params = self._build_params(
            per_page=per_page,
            offset=offset,
            include=include,
            filter_params=filter_params,
            sort=sort,
            **kwargs,
        )

        response = await self._make_request("GET", url, params=params)
        data = response.json()

        # Determine if this is a single resource or collection
        if "data" in data:
            if isinstance(data["data"], list):
                return PCOCollection(**data)
            else:
                return PCOResource(**data)
        else:
            return PCOResource(**data)

    async def post(
        self,
        product: str,
        endpoint: str,
        data: dict[str, Any],
        include: list[str] | None = None,
    ) -> PCOResource:
        """Make a POST request to create a resource."""
        url = self._build_url(product, endpoint)
        params = {}
        if include:
            params["include"] = ",".join(include)

        response = await self._make_request("POST", url, params=params, json_data=data)
        response_data = response.json()

        return PCOResource(**response_data)

    async def patch(
        self,
        product: str,
        endpoint: str,
        resource_id: str,
        data: dict[str, Any],
        include: list[str] | None = None,
    ) -> PCOResource:
        """Make a PATCH request to update a resource."""
        url = self._build_url(product, endpoint, resource_id)
        params = {}
        if include:
            params["include"] = ",".join(include)

        response = await self._make_request("PATCH", url, params=params, json_data=data)
        response_data = response.json()

        return PCOResource(**response_data)

    async def delete(
        self,
        product: str,
        endpoint: str,
        resource_id: str,
    ) -> bool:
        """Make a DELETE request to delete a resource."""
        url = self._build_url(product, endpoint, resource_id)

        response = await self._make_request("DELETE", url)

        return response.status_code in [200, 204]
