"""Main Planning Center API client."""

from collections.abc import AsyncGenerator
from typing import Any, TypeVar

from .config import API_ENDPOINTS, PCOConfig, PCOProduct
from .http_client import PCOHttpClient
from .models.base import PCOCollection, PCOResource

T = TypeVar("T", bound=PCOResource)


class PCOClient:
    """Main client for Planning Center API operations."""

    def __init__(
        self,
        app_id: str | None = None,
        secret: str | None = None,
        access_token: str | None = None,
        webhook_secret: str | None = None,
        config: PCOConfig | None = None,
    ):
        """Initialize the Planning Center API client.

        Args:
            app_id: Planning Center application ID
            secret: Planning Center application secret
            access_token: OAuth access token
            webhook_secret: Webhook secret for signature verification
            config: Custom configuration object
        """
        if config:
            self.config = config
        else:
            self.config = PCOConfig(
                app_id=app_id,
                secret=secret,
                access_token=access_token,
                webhook_secret=webhook_secret,
            )

        self._http_client: PCOHttpClient | None = None

    async def __aenter__(self):
        """Async context manager entry."""
        self._http_client = PCOHttpClient(self.config)
        await self._http_client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self._http_client:
            await self._http_client.__aexit__(exc_type, exc_val, exc_tb)
            self._http_client = None

    def _ensure_client(self) -> PCOHttpClient:
        """Ensure HTTP client is initialized."""
        if not self._http_client:
            raise RuntimeError("Client not initialized. Use async context manager.")
        return self._http_client

    def _get_product_base(self, product: PCOProduct) -> str:
        """Get the base path for a product."""
        return API_ENDPOINTS[product]["base"]

    def _get_resource_endpoint(self, product: PCOProduct, resource: str) -> str:
        """Get the endpoint for a specific resource."""
        endpoints = API_ENDPOINTS[product]["resources"]
        if resource not in endpoints:
            raise ValueError(
                f"Unknown resource '{resource}' for product '{product.value}'"
            )
        return endpoints[resource]

    # Generic CRUD operations

    async def get(
        self,
        product: PCOProduct,
        resource: str,
        resource_id: str | None = None,
        per_page: int | None = None,
        offset: int | None = None,
        include: list[str] | None = None,
        filter_params: dict[str, Any] | None = None,
        sort: str | None = None,
        **kwargs: Any,
    ) -> PCOResource | PCOCollection:
        """Get a resource or collection of resources.

        Args:
            product: Planning Center product
            resource: Resource type (e.g., 'people', 'services')
            resource_id: Specific resource ID (optional)
            per_page: Number of items per page
            offset: Offset for pagination
            include: Related resources to include
            filter_params: Filter parameters
            sort: Sort order
            **kwargs: Additional query parameters

        Returns:
            Single resource or collection of resources
        """
        client = self._ensure_client()
        product_base = self._get_product_base(product)
        endpoint = self._get_resource_endpoint(product, resource)

        return await client.get(
            product=product_base,
            endpoint=endpoint,
            resource_id=resource_id,
            per_page=per_page,
            offset=offset,
            include=include,
            filter_params=filter_params,
            sort=sort,
            **kwargs,
        )

    async def create(
        self,
        product: PCOProduct,
        resource: str,
        data: dict[str, Any],
        include: list[str] | None = None,
    ) -> PCOResource:
        """Create a new resource.

        Args:
            product: Planning Center product
            resource: Resource type
            data: Resource data
            include: Related resources to include

        Returns:
            Created resource
        """
        client = self._ensure_client()
        product_base = self._get_product_base(product)
        endpoint = self._get_resource_endpoint(product, resource)

        return await client.post(
            product=product_base,
            endpoint=endpoint,
            data=data,
            include=include,
        )

    async def update(
        self,
        product: PCOProduct,
        resource: str,
        resource_id: str,
        data: dict[str, Any],
        include: list[str] | None = None,
    ) -> PCOResource:
        """Update an existing resource.

        Args:
            product: Planning Center product
            resource: Resource type
            resource_id: Resource ID
            data: Updated resource data
            include: Related resources to include

        Returns:
            Updated resource
        """
        client = self._ensure_client()
        product_base = self._get_product_base(product)
        endpoint = self._get_resource_endpoint(product, resource)

        return await client.patch(
            product=product_base,
            endpoint=endpoint,
            resource_id=resource_id,
            data=data,
            include=include,
        )

    async def delete(
        self,
        product: PCOProduct,
        resource: str,
        resource_id: str,
    ) -> bool:
        """Delete a resource.

        Args:
            product: Planning Center product
            resource: Resource type
            resource_id: Resource ID

        Returns:
            True if deletion was successful
        """
        client = self._ensure_client()
        product_base = self._get_product_base(product)
        endpoint = self._get_resource_endpoint(product, resource)

        return await client.delete(
            product=product_base,
            endpoint=endpoint,
            resource_id=resource_id,
        )

    # Pagination helpers

    async def paginate_all(
        self,
        product: PCOProduct,
        resource: str,
        per_page: int | None = None,
        include: list[str] | None = None,
        filter_params: dict[str, Any] | None = None,
        sort: str | None = None,
        **kwargs: Any,
    ) -> AsyncGenerator[PCOResource, None]:
        """Paginate through all resources of a type.

        Args:
            product: Planning Center product
            resource: Resource type
            per_page: Number of items per page
            include: Related resources to include
            filter_params: Filter parameters
            sort: Sort order
            **kwargs: Additional query parameters

        Yields:
            Individual resources
        """
        offset = 0
        per_page = per_page or self.config.default_per_page

        while True:
            collection = await self.get(
                product=product,
                resource=resource,
                per_page=per_page,
                offset=offset,
                include=include,
                filter_params=filter_params,
                sort=sort,
                **kwargs,
            )

            if not isinstance(collection, PCOCollection):
                break

            if not collection.data:
                break

            for item in collection.data:
                yield item

            # Check if there are more pages
            if collection.links and collection.links.has_next_page():
                offset += per_page
            else:
                break

    # People-specific convenience methods

    async def get_people(
        self,
        per_page: int | None = None,
        offset: int | None = None,
        include: list[str] | None = None,
        filter_params: dict[str, Any] | None = None,
        sort: str | None = None,
        **kwargs: Any,
    ) -> PCOCollection:
        """Get people from Planning Center People."""
        result = await self.get(
            product=PCOProduct.PEOPLE,
            resource="people",
            per_page=per_page,
            offset=offset,
            include=include,
            filter_params=filter_params,
            sort=sort,
            **kwargs,
        )
        return result

    async def get_person(
        self,
        person_id: str,
        include: list[str] | None = None,
    ) -> PCOResource:
        """Get a specific person from Planning Center People."""
        return await self.get(
            product=PCOProduct.PEOPLE,
            resource="people",
            resource_id=person_id,
            include=include,
        )

    async def create_person(
        self,
        data: dict[str, Any],
        include: list[str] | None = None,
    ) -> PCOResource:
        """Create a new person in Planning Center People."""
        return await self.create(
            product=PCOProduct.PEOPLE,
            resource="people",
            data=data,
            include=include,
        )

    async def update_person(
        self,
        person_id: str,
        data: dict[str, Any],
        include: list[str] | None = None,
    ) -> PCOResource:
        """Update a person in Planning Center People."""
        return await self.update(
            product=PCOProduct.PEOPLE,
            resource="people",
            resource_id=person_id,
            data=data,
            include=include,
        )

    async def delete_person(self, person_id: str) -> bool:
        """Delete a person from Planning Center People."""
        return await self.delete(
            product=PCOProduct.PEOPLE,
            resource="people",
            resource_id=person_id,
        )

    # Services-specific convenience methods

    async def get_services(
        self,
        per_page: int | None = None,
        offset: int | None = None,
        include: list[str] | None = None,
        filter_params: dict[str, Any] | None = None,
        sort: str | None = None,
        **kwargs: Any,
    ) -> PCOCollection:
        """Get services from Planning Center Services."""
        result = await self.get(
            product=PCOProduct.SERVICES,
            resource="services",
            per_page=per_page,
            offset=offset,
            include=include,
            filter_params=filter_params,
            sort=sort,
            **kwargs,
        )
        return result

    async def get_service(
        self,
        service_id: str,
        include: list[str] | None = None,
    ) -> PCOResource:
        """Get a specific service from Planning Center Services."""
        return await self.get(
            product=PCOProduct.SERVICES,
            resource="services",
            resource_id=service_id,
            include=include,
        )

    async def get_plans(
        self,
        service_id: str | None = None,
        per_page: int | None = None,
        offset: int | None = None,
        include: list[str] | None = None,
        filter_params: dict[str, Any] | None = None,
        sort: str | None = None,
        **kwargs: Any,
    ) -> PCOCollection:
        """Get plans from Planning Center Services."""
        if service_id:
            # Get plans for a specific service
            result = await self.get(
                product=PCOProduct.SERVICES,
                resource="plans",
                per_page=per_page,
                offset=offset,
                include=include,
                filter_params={**(filter_params or {}), "service": service_id},
                sort=sort,
                **kwargs,
            )
        else:
            # Get all plans
            result = await self.get(
                product=PCOProduct.SERVICES,
                resource="plans",
                per_page=per_page,
                offset=offset,
                include=include,
                filter_params=filter_params,
                sort=sort,
                **kwargs,
            )
        return result

    async def get_plan(
        self,
        plan_id: str,
        include: list[str] | None = None,
    ) -> PCOResource:
        """Get a specific plan from Planning Center Services."""
        return await self.get(
            product=PCOProduct.SERVICES,
            resource="plans",
            resource_id=plan_id,
            include=include,
        )

    # Utility methods

    async def search_people(
        self,
        query: str,
        per_page: int | None = None,
        include: list[str] | None = None,
    ) -> PCOCollection:
        """Search for people by name or email."""
        return await self.get_people(
            per_page=per_page,
            include=include,
            filter_params={"search": query},
        )

    async def get_people_by_email(
        self,
        email: str,
        include: list[str] | None = None,
    ) -> PCOCollection:
        """Get people by email address."""
        return await self.get_people(
            include=include,
            filter_params={"email": email},
        )

    async def get_people_by_phone(
        self,
        phone: str,
        include: list[str] | None = None,
    ) -> PCOCollection:
        """Get people by phone number."""
        return await self.get_people(
            include=include,
            filter_params={"phone": phone},
        )

    async def get_active_people(
        self,
        per_page: int | None = None,
        include: list[str] | None = None,
    ) -> PCOCollection:
        """Get active people only."""
        return await self.get_people(
            per_page=per_page,
            include=include,
            filter_params={"status": "active"},
        )

    async def get_inactive_people(
        self,
        per_page: int | None = None,
        include: list[str] | None = None,
    ) -> PCOCollection:
        """Get inactive people only."""
        return await self.get_people(
            per_page=per_page,
            include=include,
            filter_params={"status": "inactive"},
        )

    # Registrations-specific convenience methods

    async def get_registration_events(
        self,
        per_page: int | None = None,
        offset: int | None = None,
        include: list[str] | None = None,
        filter_params: dict[str, Any] | None = None,
        sort: str | None = None,
        **kwargs: Any,
    ) -> PCOCollection:
        """Get registration events from Planning Center Registrations."""
        result = await self.get(
            product=PCOProduct.REGISTRATIONS,
            resource="events",
            per_page=per_page,
            offset=offset,
            include=include,
            filter_params=filter_params,
            sort=sort,
            **kwargs,
        )
        return result

    async def get_registration_event(
        self,
        event_id: str,
        include: list[str] | None = None,
    ) -> PCOResource:
        """Get a specific registration event from Planning Center Registrations."""
        return await self.get(
            product=PCOProduct.REGISTRATIONS,
            resource="events",
            resource_id=event_id,
            include=include,
        )

    async def get_registrations(
        self,
        per_page: int | None = None,
        offset: int | None = None,
        include: list[str] | None = None,
        filter_params: dict[str, Any] | None = None,
        sort: str | None = None,
        **kwargs: Any,
    ) -> PCOCollection:
        """Get registrations from Planning Center Registrations."""
        result = await self.get(
            product=PCOProduct.REGISTRATIONS,
            resource="registrations",
            per_page=per_page,
            offset=offset,
            include=include,
            filter_params=filter_params,
            sort=sort,
            **kwargs,
        )
        return result

    async def get_registration(
        self,
        registration_id: str,
        include: list[str] | None = None,
    ) -> PCOResource:
        """Get a specific registration from Planning Center Registrations."""
        return await self.get(
            product=PCOProduct.REGISTRATIONS,
            resource="registrations",
            resource_id=registration_id,
            include=include,
        )

    async def get_registration_instances(
        self,
        registration_id: str | None = None,
        per_page: int | None = None,
        offset: int | None = None,
        include: list[str] | None = None,
        filter_params: dict[str, Any] | None = None,
        sort: str | None = None,
        **kwargs: Any,
    ) -> PCOCollection:
        """Get registration instances from Planning Center Registrations."""
        if registration_id:
            # Get instances for a specific registration
            result = await self.get(
                product=PCOProduct.REGISTRATIONS,
                resource="registration_instances",
                per_page=per_page,
                offset=offset,
                include=include,
                filter_params={**(filter_params or {}), "registration": registration_id},
                sort=sort,
                **kwargs,
            )
        else:
            # Get all instances
            result = await self.get(
                product=PCOProduct.REGISTRATIONS,
                resource="registration_instances",
                per_page=per_page,
                offset=offset,
                include=include,
                filter_params=filter_params,
                sort=sort,
                **kwargs,
            )
        return result

    async def get_registration_instance(
        self,
        instance_id: str,
        include: list[str] | None = None,
    ) -> PCOResource:
        """Get a specific registration instance from Planning Center Registrations."""
        return await self.get(
            product=PCOProduct.REGISTRATIONS,
            resource="registration_instances",
            resource_id=instance_id,
            include=include,
        )

    async def get_registration_forms(
        self,
        registration_id: str | None = None,
        per_page: int | None = None,
        offset: int | None = None,
        include: list[str] | None = None,
        filter_params: dict[str, Any] | None = None,
        sort: str | None = None,
        **kwargs: Any,
    ) -> PCOCollection:
        """Get registration forms from Planning Center Registrations."""
        if registration_id:
            # Get forms for a specific registration
            result = await self.get(
                product=PCOProduct.REGISTRATIONS,
                resource="registration_forms",
                per_page=per_page,
                offset=offset,
                include=include,
                filter_params={**(filter_params or {}), "registration": registration_id},
                sort=sort,
                **kwargs,
            )
        else:
            # Get all forms
            result = await self.get(
                product=PCOProduct.REGISTRATIONS,
                resource="registration_forms",
                per_page=per_page,
                offset=offset,
                include=include,
                filter_params=filter_params,
                sort=sort,
                **kwargs,
            )
        return result

    async def get_registration_form(
        self,
        form_id: str,
        include: list[str] | None = None,
    ) -> PCOResource:
        """Get a specific registration form from Planning Center Registrations."""
        return await self.get(
            product=PCOProduct.REGISTRATIONS,
            resource="registration_forms",
            resource_id=form_id,
            include=include,
        )

    async def get_registration_instance_people(
        self,
        instance_id: str | None = None,
        per_page: int | None = None,
        offset: int | None = None,
        include: list[str] | None = None,
        filter_params: dict[str, Any] | None = None,
        sort: str | None = None,
        **kwargs: Any,
    ) -> PCOCollection:
        """Get people registered for registration instances."""
        if instance_id:
            # Get people for a specific instance
            result = await self.get(
                product=PCOProduct.REGISTRATIONS,
                resource="registration_instances_people",
                per_page=per_page,
                offset=offset,
                include=include,
                filter_params={**(filter_params or {}), "registration_instance": instance_id},
                sort=sort,
                **kwargs,
            )
        else:
            # Get all registered people
            result = await self.get(
                product=PCOProduct.REGISTRATIONS,
                resource="registration_instances_people",
                per_page=per_page,
                offset=offset,
                include=include,
                filter_params=filter_params,
                sort=sort,
                **kwargs,
            )
        return result

    async def get_registration_instance_person(
        self,
        person_id: str,
        include: list[str] | None = None,
    ) -> PCOResource:
        """Get a specific registered person from Planning Center Registrations."""
        return await self.get(
            product=PCOProduct.REGISTRATIONS,
            resource="registration_instances_people",
            resource_id=person_id,
            include=include,
        )

    # Utility methods for registrations

    async def get_open_registrations(
        self,
        per_page: int | None = None,
        include: list[str] | None = None,
    ) -> PCOCollection:
        """Get registrations that are currently open."""
        return await self.get_registrations(
            per_page=per_page,
            include=include,
            filter_params={"status": "open"},
        )

    async def get_closed_registrations(
        self,
        per_page: int | None = None,
        include: list[str] | None = None,
    ) -> PCOCollection:
        """Get registrations that are currently closed."""
        return await self.get_registrations(
            per_page=per_page,
            include=include,
            filter_params={"status": "closed"},
        )

    async def get_registrations_by_capacity(
        self,
        min_capacity: int | None = None,
        max_capacity: int | None = None,
        per_page: int | None = None,
        include: list[str] | None = None,
    ) -> PCOCollection:
        """Get registrations filtered by capacity."""
        filter_params = {}
        if min_capacity is not None:
            filter_params["min_capacity"] = min_capacity
        if max_capacity is not None:
            filter_params["max_capacity"] = max_capacity

        return await self.get_registrations(
            per_page=per_page,
            include=include,
            filter_params=filter_params,
        )
