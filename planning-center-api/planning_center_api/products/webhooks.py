"""Webhooks API models and services for Planning Center API."""

from datetime import datetime
from typing import Any

from ..models.base import PCOBaseModel
from ..models.links import PCOLinks
from ..models.relationships import PCORelationships


class PCOWebhookSubscription(PCOBaseModel):
    """Represents a webhook subscription in Planning Center."""

    id: str
    type: str = "WebhookSubscription"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def name(self) -> str | None:
        """Get the subscription name."""
        return self.attributes.get("name")

    @property
    def url(self) -> str | None:
        """Get the webhook URL."""
        return self.attributes.get("url")

    @property
    def active(self) -> bool | None:
        """Get whether the subscription is active."""
        return self.attributes.get("active")

    @property
    def created_at(self) -> datetime | None:
        """Get the creation timestamp."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the last update timestamp."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at

    @property
    def authenticity_secret(self) -> str | None:
        """Get the authenticity secret for webhook verification."""
        return self.attributes.get("authenticity_secret")

    @property
    def application_id(self) -> str | None:
        """Get the application ID."""
        return self.attributes.get("application_id")


class PCOWebhookEvent(PCOBaseModel):
    """Represents a webhook event in Planning Center."""

    id: str
    type: str = "Event"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def created_at(self) -> datetime | None:
        """Get the creation timestamp."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def status(self) -> str | None:
        """Get the event status."""
        return self.attributes.get("status")

    @property
    def updated_at(self) -> datetime | None:
        """Get the last update timestamp."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at

    @property
    def uuid(self) -> str | None:
        """Get the event UUID."""
        return self.attributes.get("uuid")

    @property
    def payload(self) -> str | None:
        """Get the event payload as a JSON string."""
        return self.attributes.get("payload")


class PCOWebhookDelivery(PCOBaseModel):
    """Represents a webhook delivery in Planning Center."""

    id: str
    type: str = "Delivery"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def status(self) -> int | None:
        """Get the delivery status."""
        return self.attributes.get("status")

    @property
    def request_headers(self) -> str | None:
        """Get the request headers."""
        return self.attributes.get("request_headers")

    @property
    def request_body(self) -> str | None:
        """Get the request body."""
        return self.attributes.get("request_body")

    @property
    def response_headers(self) -> str | None:
        """Get the response headers."""
        return self.attributes.get("response_headers")

    @property
    def response_body(self) -> str | None:
        """Get the response body."""
        return self.attributes.get("response_body")

    @property
    def created_at(self) -> datetime | None:
        """Get the creation timestamp."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the last update timestamp."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at

    @property
    def timing(self) -> float | None:
        """Get the delivery timing in seconds."""
        return self.attributes.get("timing")

    @property
    def object_url(self) -> str | None:
        """Get the object URL."""
        return self.attributes.get("object_url")


class PCOAvailableEvent(PCOBaseModel):
    """Represents an available webhook event type in Planning Center."""

    id: str
    type: str = "AvailableEvent"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def name(self) -> str | None:
        """Get the event name."""
        return self.attributes.get("name")

    @property
    def app(self) -> str | None:
        """Get the app name."""
        return self.attributes.get("app")

    @property
    def version(self) -> str | None:
        """Get the version."""
        return self.attributes.get("version")

    @property
    def event_type(self) -> str | None:
        """Get the event type."""
        return self.attributes.get("type")

    @property
    def resource(self) -> str | None:
        """Get the resource type."""
        return self.attributes.get("resource")

    @property
    def action(self) -> str | None:
        """Get the action."""
        return self.attributes.get("action")


class PCOWebhookOrganization(PCOBaseModel):
    """Represents a webhook organization in Planning Center."""

    id: str
    type: str = "Organization"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None


class PCOWebhookService:
    """Service for managing webhook subscriptions and events."""

    def __init__(self, client):
        """Initialize the webhook service.

        Args:
            client: Planning Center API client
        """
        self.client = client
        self.base_url = "/webhooks/v2"

    async def get_webhook_subscriptions(
        self,
        application_id: str | None = None,
        per_page: int | None = None,
        offset: int | None = None,
    ) -> list[PCOWebhookSubscription]:
        """Get all webhook subscriptions.

        Args:
            application_id: Filter by application ID
            per_page: Number of records per page (1-100, default 25)
            offset: Offset for pagination

        Returns:
            List of webhook subscriptions
        """
        params = {}
        if application_id:
            params["where[application_id]"] = application_id
        if per_page is not None:
            params["per_page"] = per_page
        if offset is not None:
            params["offset"] = offset

        response = await self.client.get(
            f"{self.base_url}/webhook_subscriptions", params=params
        )
        return [PCOWebhookSubscription(**item) for item in response.get("data", [])]

    async def get_webhook_subscription(
        self, subscription_id: str
    ) -> PCOWebhookSubscription:
        """Get a specific webhook subscription.

        Args:
            subscription_id: The subscription ID

        Returns:
            The webhook subscription
        """
        response = await self.client.get(
            f"{self.base_url}/webhook_subscriptions/{subscription_id}"
        )
        return PCOWebhookSubscription(**response["data"])

    async def create_webhook_subscription(
        self,
        name: str,
        url: str,
        active: bool = True,
    ) -> PCOWebhookSubscription:
        """Create a new webhook subscription.

        Args:
            name: Subscription name
            url: Webhook URL
            active: Whether the subscription is active

        Returns:
            The created webhook subscription
        """
        data = {
            "data": {
                "type": "WebhookSubscription",
                "attributes": {
                    "name": name,
                    "url": url,
                    "active": active,
                },
            }
        }
        response = await self.client.post(
            f"{self.base_url}/webhook_subscriptions", json=data
        )
        return PCOWebhookSubscription(**response["data"])

    async def update_webhook_subscription(
        self,
        subscription_id: str,
        active: bool | None = None,
    ) -> PCOWebhookSubscription:
        """Update a webhook subscription.

        Args:
            subscription_id: The subscription ID
            active: Whether the subscription is active

        Returns:
            The updated webhook subscription
        """
        attributes = {}
        if active is not None:
            attributes["active"] = active

        data = {
            "data": {
                "type": "WebhookSubscription",
                "id": subscription_id,
                "attributes": attributes,
            }
        }
        response = await self.client.patch(
            f"{self.base_url}/webhook_subscriptions/{subscription_id}", json=data
        )
        return PCOWebhookSubscription(**response["data"])

    async def delete_webhook_subscription(self, subscription_id: str) -> None:
        """Delete a webhook subscription.

        Args:
            subscription_id: The subscription ID
        """
        await self.client.delete(
            f"{self.base_url}/webhook_subscriptions/{subscription_id}"
        )

    async def rotate_webhook_secret(
        self, subscription_id: str
    ) -> PCOWebhookSubscription:
        """Rotate the authenticity secret for a webhook subscription.

        Args:
            subscription_id: The subscription ID

        Returns:
            The updated webhook subscription
        """
        response = await self.client.post(
            f"{self.base_url}/webhook_subscriptions/{subscription_id}/rotate_secret"
        )
        return PCOWebhookSubscription(**response["data"])

    async def get_webhook_events(
        self,
        subscription_id: str,
        status: str | None = None,
        uuid: str | None = None,
        per_page: int | None = None,
        offset: int | None = None,
        order: str | None = None,
    ) -> list[PCOWebhookEvent]:
        """Get webhook events for a subscription.

        Args:
            subscription_id: The subscription ID
            status: Filter by status
            uuid: Filter by UUID
            per_page: Number of records per page (1-100, default 25)
            offset: Offset for pagination
            order: Order by field (prefix with - to reverse)

        Returns:
            List of webhook events
        """
        params = {}
        if status:
            params["where[status]"] = status
        if uuid:
            params["where[uuid]"] = uuid
        if per_page is not None:
            params["per_page"] = per_page
        if offset is not None:
            params["offset"] = offset
        if order:
            params["order"] = order

        response = await self.client.get(
            f"{self.base_url}/webhook_subscriptions/{subscription_id}/events",
            params=params,
        )
        return [PCOWebhookEvent(**item) for item in response.get("data", [])]

    async def get_webhook_event(
        self, subscription_id: str, event_id: str
    ) -> PCOWebhookEvent:
        """Get a specific webhook event.

        Args:
            subscription_id: The subscription ID
            event_id: The event ID

        Returns:
            The webhook event
        """
        response = await self.client.get(
            f"{self.base_url}/webhook_subscriptions/{subscription_id}/events/{event_id}"
        )
        return PCOWebhookEvent(**response["data"])

    async def ignore_webhook_event(self, subscription_id: str, event_id: str) -> None:
        """Ignore a webhook event.

        Args:
            subscription_id: The subscription ID
            event_id: The event ID
        """
        await self.client.post(
            f"{self.base_url}/webhook_subscriptions/{subscription_id}/events/{event_id}/ignore"
        )

    async def redeliver_webhook_event(
        self, subscription_id: str, event_id: str
    ) -> None:
        """Redeliver a webhook event.

        Args:
            subscription_id: The subscription ID
            event_id: The event ID
        """
        await self.client.post(
            f"{self.base_url}/webhook_subscriptions/{subscription_id}/events/{event_id}/redeliver"
        )

    async def get_webhook_deliveries(
        self,
        subscription_id: str,
        event_id: str,
        per_page: int | None = None,
        offset: int | None = None,
        order: str | None = None,
    ) -> list[PCOWebhookDelivery]:
        """Get deliveries for a webhook event.

        Args:
            subscription_id: The subscription ID
            event_id: The event ID
            per_page: Number of records per page (1-100, default 25)
            offset: Offset for pagination
            order: Order by field (prefix with - to reverse)

        Returns:
            List of webhook deliveries
        """
        params = {}
        if per_page is not None:
            params["per_page"] = per_page
        if offset is not None:
            params["offset"] = offset
        if order:
            params["order"] = order

        response = await self.client.get(
            f"{self.base_url}/webhook_subscriptions/{subscription_id}/events/{event_id}/deliveries",
            params=params,
        )
        return [PCOWebhookDelivery(**item) for item in response.get("data", [])]

    async def get_webhook_delivery(
        self, subscription_id: str, event_id: str, delivery_id: str
    ) -> PCOWebhookDelivery:
        """Get a specific webhook delivery.

        Args:
            subscription_id: The subscription ID
            event_id: The event ID
            delivery_id: The delivery ID

        Returns:
            The webhook delivery
        """
        response = await self.client.get(
            f"{self.base_url}/webhook_subscriptions/{subscription_id}/events/{event_id}/deliveries/{delivery_id}"
        )
        return PCOWebhookDelivery(**response["data"])

    async def get_available_events(
        self,
        per_page: int | None = None,
        offset: int | None = None,
    ) -> list[PCOAvailableEvent]:
        """Get all available webhook event types.

        Args:
            per_page: Number of records per page (1-100, default 25)
            offset: Offset for pagination

        Returns:
            List of available events
        """
        params = {}
        if per_page is not None:
            params["per_page"] = per_page
        if offset is not None:
            params["offset"] = offset

        response = await self.client.get(
            f"{self.base_url}/available_events", params=params
        )
        return [PCOAvailableEvent(**item) for item in response.get("data", [])]

    async def get_webhook_organization(
        self, organization_id: str | None = None
    ) -> PCOWebhookOrganization:
        """Get webhook organization information.

        Args:
            organization_id: The organization ID (optional)

        Returns:
            The webhook organization
        """
        url = f"{self.base_url}"
        if organization_id:
            url += f"/{organization_id}"

        response = await self.client.get(url)
        return PCOWebhookOrganization(**response["data"])
