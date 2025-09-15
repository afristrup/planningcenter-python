"""Custom exceptions for Planning Center API."""

from typing import Any

from .models.base import PCOErrorResponse


class PCOError(Exception):
    """Base exception for Planning Center API errors."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        error_response: PCOErrorResponse | None = None,
        response_data: dict[str, Any] | None = None,
    ):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.error_response = error_response
        self.response_data = response_data

    def get_error_details(self) -> list[str]:
        """Get detailed error messages."""
        if self.error_response:
            return self.error_response.get_error_messages()
        return [self.message]


class PCOAuthenticationError(PCOError):
    """Raised when authentication fails."""

    def __init__(self, message: str = "Authentication failed", **kwargs):
        super().__init__(message, status_code=401, **kwargs)


class PCOPermissionError(PCOError):
    """Raised when the user doesn't have permission to perform an action."""

    def __init__(self, message: str = "Permission denied", **kwargs):
        super().__init__(message, status_code=403, **kwargs)


class PCONotFoundError(PCOError):
    """Raised when a resource is not found."""

    def __init__(self, message: str = "Resource not found", **kwargs):
        super().__init__(message, status_code=404, **kwargs)


class PCOValidationError(PCOError):
    """Raised when request validation fails."""

    def __init__(self, message: str = "Validation failed", **kwargs):
        super().__init__(message, status_code=422, **kwargs)


class PCORateLimitError(PCOError):
    """Raised when rate limit is exceeded."""

    def __init__(
        self,
        message: str = "Rate limit exceeded",
        retry_after: int | None = None,
        **kwargs,
    ):
        super().__init__(message, status_code=429, **kwargs)
        self.retry_after = retry_after


class PCOServerError(PCOError):
    """Raised when a server error occurs."""

    def __init__(self, message: str = "Server error", **kwargs):
        super().__init__(message, status_code=500, **kwargs)


class PCOWebhookError(PCOError):
    """Raised when webhook processing fails."""

    def __init__(self, message: str = "Webhook processing failed", **kwargs):
        super().__init__(message, **kwargs)


class PCOWebhookSignatureError(PCOWebhookError):
    """Raised when webhook signature verification fails."""

    def __init__(
        self, message: str = "Webhook signature verification failed", **kwargs
    ):
        super().__init__(message, **kwargs)


def raise_for_status(
    status_code: int, response_data: dict[str, Any] | None = None
) -> None:
    """Raise appropriate exception based on HTTP status code."""

    error_response = None
    if response_data and "errors" in response_data:
        try:
            error_response = PCOErrorResponse(**response_data)
        except Exception:
            pass  # If we can't parse the error response, we'll use the raw data

    message = "Request failed"
    if error_response:
        message = error_response.get_first_error_message() or message
    elif response_data and "error" in response_data:
        message = str(response_data["error"])

    if status_code == 401:
        raise PCOAuthenticationError(
            message, error_response=error_response, response_data=response_data
        )
    elif status_code == 403:
        raise PCOPermissionError(
            message, error_response=error_response, response_data=response_data
        )
    elif status_code == 404:
        raise PCONotFoundError(
            message, error_response=error_response, response_data=response_data
        )
    elif status_code == 422:
        raise PCOValidationError(
            message, error_response=error_response, response_data=response_data
        )
    elif status_code == 429:
        retry_after = None
        if response_data and "retry_after" in response_data:
            retry_after = response_data["retry_after"]
        raise PCORateLimitError(
            message,
            retry_after=retry_after,
            error_response=error_response,
            response_data=response_data,
        )
    elif status_code >= 500:
        raise PCOServerError(
            message, error_response=error_response, response_data=response_data
        )
    else:
        raise PCOError(
            message,
            status_code=status_code,
            error_response=error_response,
            response_data=response_data,
        )
