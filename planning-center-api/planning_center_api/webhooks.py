"""Webhook handling for Planning Center API."""

import hashlib
import hmac
import json
from collections.abc import Callable
from datetime import datetime

# Forward reference to avoid circular imports
from typing import TYPE_CHECKING, Any

from .config import PCOConfig
from .exceptions import PCOWebhookError, PCOWebhookSignatureError
from .models.base import PCOWebhookEvent, PCOWebhookPayload

if TYPE_CHECKING:
    from .client import PCOClient


class PCOWebhookHandler:
    """Handles webhook events from Planning Center."""

    def __init__(self, config: PCOConfig):
        """Initialize webhook handler.

        Args:
            config: Planning Center configuration
        """
        self.config = config
        self.event_handlers: dict[str, Callable] = {}

    def register_handler(self, event_type: str, handler: Callable) -> None:
        """Register an event handler.

        Args:
            event_type: Event type (e.g., 'people.created')
            handler: Handler function
        """
        self.event_handlers[event_type] = handler

    def unregister_handler(self, event_type: str) -> None:
        """Unregister an event handler.

        Args:
            event_type: Event type to unregister
        """
        if event_type in self.event_handlers:
            del self.event_handlers[event_type]

    def verify_signature(self, payload: str, signature: str) -> bool:
        """Verify webhook signature.

        Args:
            payload: Webhook payload
            signature: Webhook signature from headers

        Returns:
            True if signature is valid

        Raises:
            PCOWebhookSignatureError: If signature verification fails
        """
        if not self.config.webhook_secret:
            raise PCOWebhookError("Webhook secret not configured")

        if not signature:
            raise PCOWebhookSignatureError("No signature provided")

        # Extract signature from header (format: "sha256=<signature>")
        if signature.startswith("sha256="):
            signature = signature[7:]

        # Calculate expected signature
        expected_signature = hmac.new(
            self.config.webhook_secret.encode(), payload.encode(), hashlib.sha256
        ).hexdigest()

        # Compare signatures
        if not hmac.compare_digest(signature, expected_signature):
            raise PCOWebhookSignatureError("Invalid webhook signature")

        return True

    def parse_webhook_payload(self, payload: str) -> PCOWebhookEvent:
        """Parse webhook payload into structured data.

        Args:
            payload: Raw webhook payload

        Returns:
            Parsed webhook event

        Raises:
            PCOWebhookError: If payload parsing fails
        """
        try:
            data = json.loads(payload)
        except json.JSONDecodeError as e:
            raise PCOWebhookError(f"Invalid JSON payload: {e}") from e

        try:
            # Extract event information
            event_type = data.get("event_type")
            if not event_type:
                raise PCOWebhookError("Missing event_type in payload")

            # Parse resource data
            resource_data = data.get("resource", {})
            resource = PCOWebhookPayload(**resource_data)

            # Parse timestamp
            timestamp_str = data.get("timestamp")
            if timestamp_str:
                timestamp = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
            else:
                timestamp = datetime.utcnow()

            # Create webhook event
            webhook_event = PCOWebhookEvent(
                event_type=event_type,
                resource=resource,
                timestamp=timestamp,
                webhook_id=data.get("webhook_id"),
                organization_id=data.get("organization_id"),
            )

            return webhook_event

        except Exception as e:
            raise PCOWebhookError(f"Failed to parse webhook payload: {e}") from e

    async def handle_webhook(
        self,
        payload: str,
        signature: str | None = None,
        verify_signature: bool = True,
    ) -> Any | None:
        """Handle a webhook event.

        Args:
            payload: Webhook payload
            signature: Webhook signature (optional)
            verify_signature: Whether to verify signature

        Returns:
            Result from event handler if one exists

        Raises:
            PCOWebhookError: If webhook handling fails
        """
        # Verify signature if requested
        if verify_signature and signature:
            self.verify_signature(payload, signature)

        # Parse payload
        webhook_event = self.parse_webhook_payload(payload)

        # Find and execute handler
        handler = self.event_handlers.get(webhook_event.event_type)
        if handler:
            try:
                if callable(handler):
                    # Check if handler is async
                    if callable(handler):
                        import asyncio

                        if asyncio.iscoroutinefunction(handler):
                            return await handler(webhook_event)
                        else:
                            return handler(webhook_event)
                    else:
                        return handler(webhook_event)
                else:
                    raise PCOWebhookError(
                        f"Handler for {webhook_event.event_type} is not callable"
                    )
            except Exception as e:
                raise PCOWebhookError(f"Handler execution failed: {e}") from e

        return None

    def get_registered_events(self) -> list[str]:
        """Get list of registered event types."""
        return list(self.event_handlers.keys())

    def has_handler(self, event_type: str) -> bool:
        """Check if a handler is registered for an event type."""
        return event_type in self.event_handlers


async def handle_webhook_event(
    client: "PCOClient",
    payload: str,
    signature: str | None = None,
    event_handlers: dict[str, Callable] | None = None,
    verify_signature: bool = True,
) -> Any | None:
    """Convenience function to handle a webhook event.

    Args:
        client: Planning Center client
        payload: Webhook payload
        signature: Webhook signature
        event_handlers: Event handlers dictionary
        verify_signature: Whether to verify signature

    Returns:
        Result from event handler if one exists
    """
    handler = PCOWebhookHandler(client.config)

    # Register event handlers
    if event_handlers:
        for event_type, event_handler in event_handlers.items():
            handler.register_handler(event_type, event_handler)

    return await handler.handle_webhook(
        payload=payload,
        signature=signature,
        verify_signature=verify_signature,
    )


# Common webhook event handlers


async def log_webhook_event(webhook_event: PCOWebhookEvent) -> None:
    """Log webhook event to console."""
    print(f"Webhook Event: {webhook_event.event_type}")
    print(f"Resource: {webhook_event.resource.type} (ID: {webhook_event.resource.id})")
    print(f"Timestamp: {webhook_event.timestamp}")
    if webhook_event.resource.attributes:
        print(f"Attributes: {webhook_event.resource.attributes}")


async def store_webhook_event(
    webhook_event: PCOWebhookEvent, storage: dict[str, Any]
) -> None:
    """Store webhook event in memory storage.

    Args:
        webhook_event: Webhook event to store
        storage: Storage dictionary
    """
    event_key = f"{webhook_event.event_type}_{webhook_event.resource.id}_{webhook_event.timestamp.isoformat()}"
    storage[event_key] = {
        "event_type": webhook_event.event_type,
        "resource": webhook_event.resource.model_dump(),
        "timestamp": webhook_event.timestamp.isoformat(),
        "webhook_id": webhook_event.webhook_id,
        "organization_id": webhook_event.organization_id,
    }


# Webhook event type constants
class WebhookEventTypes:
    """Common webhook event types."""

    # People events
    PEOPLE_CREATED = "people.created"
    PEOPLE_UPDATED = "people.updated"
    PEOPLE_DELETED = "people.deleted"

    # Email events
    EMAILS_CREATED = "emails.created"
    EMAILS_UPDATED = "emails.updated"
    EMAILS_DELETED = "emails.deleted"

    # Phone number events
    PHONE_NUMBERS_CREATED = "phone_numbers.created"
    PHONE_NUMBERS_UPDATED = "phone_numbers.updated"
    PHONE_NUMBERS_DELETED = "phone_numbers.deleted"

    # Address events
    ADDRESSES_CREATED = "addresses.created"
    ADDRESSES_UPDATED = "addresses.updated"
    ADDRESSES_DELETED = "addresses.deleted"

    # Services events
    SERVICES_CREATED = "services.created"
    SERVICES_UPDATED = "services.updated"
    SERVICES_DELETED = "services.deleted"

    # Plan events
    PLANS_CREATED = "plans.created"
    PLANS_UPDATED = "plans.updated"
    PLANS_DELETED = "plans.deleted"

    # Song events
    SONGS_CREATED = "songs.created"
    SONGS_UPDATED = "songs.updated"
    SONGS_DELETED = "songs.deleted"

    # Check-in events
    CHECK_INS_CREATED = "check_ins.created"
    CHECK_INS_UPDATED = "check_ins.updated"
    CHECK_INS_DELETED = "check_ins.deleted"

    # Event events
    EVENTS_CREATED = "events.created"
    EVENTS_UPDATED = "events.updated"
    EVENTS_DELETED = "events.deleted"

    # Donation events
    DONATIONS_CREATED = "donations.created"
    DONATIONS_UPDATED = "donations.updated"
    DONATIONS_DELETED = "donations.deleted"

    # Group events
    GROUPS_CREATED = "groups.created"
    GROUPS_UPDATED = "groups.updated"
    GROUPS_DELETED = "groups.deleted"

    # Group membership events
    GROUP_MEMBERSHIPS_CREATED = "group_memberships.created"
    GROUP_MEMBERSHIPS_UPDATED = "group_memberships.updated"
    GROUP_MEMBERSHIPS_DELETED = "group_memberships.deleted"
