"""Unit tests for webhook handling."""

from datetime import datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from planning_center_api.config import PCOConfig
from planning_center_api.exceptions import PCOWebhookError, PCOWebhookSignatureError
from planning_center_api.webhooks import (
    PCOWebhookHandler,
    WebhookEventTypes,
    handle_webhook_event,
)


class TestPCOWebhookHandler:
    """Test PCOWebhookHandler class."""

    @pytest.fixture
    def config(self):
        """Create test configuration."""
        return PCOConfig(webhook_secret="test_secret")

    @pytest.fixture
    def handler(self, config):
        """Create test webhook handler."""
        return PCOWebhookHandler(config)

    def test_init(self, handler, config):
        """Test handler initialization."""
        assert handler.config == config
        assert handler.event_handlers == {}

    def test_register_handler(self, handler):
        """Test registering event handlers."""

        def test_handler(event):
            return "processed"

        handler.register_handler("people.created", test_handler)

        assert "people.created" in handler.event_handlers
        assert handler.event_handlers["people.created"] == test_handler

    def test_unregister_handler(self, handler):
        """Test unregistering event handlers."""

        def test_handler(event):
            return "processed"

        handler.register_handler("people.created", test_handler)
        assert "people.created" in handler.event_handlers

        handler.unregister_handler("people.created")
        assert "people.created" not in handler.event_handlers

    def test_unregister_nonexistent_handler(self, handler):
        """Test unregistering non-existent handler."""
        # Should not raise an error
        handler.unregister_handler("nonexistent.event")

    @patch("planning_center_api.webhooks.hmac.compare_digest")
    @patch("planning_center_api.webhooks.hmac.new")
    def test_verify_signature_valid(self, mock_hmac_new, mock_compare_digest, handler):
        """Test signature verification with valid signature."""
        mock_hmac_new.return_value.hexdigest.return_value = "expected_signature"
        mock_compare_digest.return_value = True

        result = handler.verify_signature("test_payload", "sha256=expected_signature")

        assert result is True
        mock_compare_digest.assert_called_once_with(
            "expected_signature", "expected_signature"
        )

    @patch("planning_center_api.webhooks.hmac.compare_digest")
    @patch("planning_center_api.webhooks.hmac.new")
    def test_verify_signature_invalid(
        self, mock_hmac_new, mock_compare_digest, handler
    ):
        """Test signature verification with invalid signature."""
        mock_hmac_new.return_value.hexdigest.return_value = "expected_signature"
        mock_compare_digest.return_value = False

        with pytest.raises(PCOWebhookSignatureError, match="Invalid webhook signature"):
            handler.verify_signature("test_payload", "sha256=invalid_signature")

    def test_verify_signature_no_secret(self):
        """Test signature verification without webhook secret."""
        config = PCOConfig()  # No webhook secret
        handler = PCOWebhookHandler(config)

        with pytest.raises(PCOWebhookError, match="Webhook secret not configured"):
            handler.verify_signature("test_payload", "sha256=signature")

    def test_verify_signature_no_signature(self, handler):
        """Test signature verification without signature."""
        with pytest.raises(PCOWebhookSignatureError, match="No signature provided"):
            handler.verify_signature("test_payload", None)

    def test_verify_signature_empty_signature(self, handler):
        """Test signature verification with empty signature."""
        with pytest.raises(PCOWebhookSignatureError, match="No signature provided"):
            handler.verify_signature("test_payload", "")

    def test_parse_webhook_payload_valid(self, handler):
        """Test parsing valid webhook payload."""
        payload = """
        {
            "event_type": "people.created",
            "resource": {
                "id": "123",
                "type": "people",
                "attributes": {
                    "first_name": "John",
                    "last_name": "Doe"
                }
            },
            "timestamp": "2023-01-01T00:00:00Z",
            "webhook_id": "webhook_123",
            "organization_id": "org_123"
        }
        """

        event = handler.parse_webhook_payload(payload)

        assert event.event_type == "people.created"
        assert event.resource.id == "123"
        assert event.resource.type == "people"
        assert event.resource.get_attribute("first_name") == "John"
        assert event.resource.get_attribute("last_name") == "Doe"
        assert event.webhook_id == "webhook_123"
        assert event.organization_id == "org_123"

    def test_parse_webhook_payload_invalid_json(self, handler):
        """Test parsing invalid JSON payload."""
        payload = "invalid json"

        with pytest.raises(PCOWebhookError, match="Invalid JSON payload"):
            handler.parse_webhook_payload(payload)

    def test_parse_webhook_payload_missing_event_type(self, handler):
        """Test parsing payload without event_type."""
        payload = """
        {
            "resource": {
                "id": "123",
                "type": "people",
                "attributes": {}
            }
        }
        """

        with pytest.raises(PCOWebhookError, match="Missing event_type in payload"):
            handler.parse_webhook_payload(payload)

    def test_parse_webhook_payload_missing_timestamp(self, handler):
        """Test parsing payload without timestamp."""
        payload = """
        {
            "event_type": "people.created",
            "resource": {
                "id": "123",
                "type": "people",
                "attributes": {}
            }
        }
        """

        event = handler.parse_webhook_payload(payload)

        # Should use current time if timestamp is missing
        assert isinstance(event.timestamp, datetime)

    @pytest.mark.asyncio
    async def test_handle_webhook_with_handler(self, handler):
        """Test handling webhook with registered handler."""

        # Register handler
        async def test_handler(event):
            return f"Processed {event.event_type}"

        handler.register_handler("people.created", test_handler)

        payload = """
        {
            "event_type": "people.created",
            "resource": {
                "id": "123",
                "type": "people",
                "attributes": {
                    "first_name": "John"
                }
            }
        }
        """

        with patch.object(handler, "verify_signature"):
            result = await handler.handle_webhook(payload, verify_signature=False)

            assert result == "Processed people.created"

    @pytest.mark.asyncio
    async def test_handle_webhook_sync_handler(self, handler):
        """Test handling webhook with synchronous handler."""

        # Register synchronous handler
        def test_handler(event):
            return f"Processed {event.event_type}"

        handler.register_handler("people.created", test_handler)

        payload = """
        {
            "event_type": "people.created",
            "resource": {
                "id": "123",
                "type": "people",
                "attributes": {
                    "first_name": "John"
                }
            }
        }
        """

        with patch.object(handler, "verify_signature"):
            result = await handler.handle_webhook(payload, verify_signature=False)

            assert result == "Processed people.created"

    @pytest.mark.asyncio
    async def test_handle_webhook_no_handler(self, handler):
        """Test handling webhook without registered handler."""
        payload = """
        {
            "event_type": "people.created",
            "resource": {
                "id": "123",
                "type": "people",
                "attributes": {
                    "first_name": "John"
                }
            }
        }
        """

        with patch.object(handler, "verify_signature"):
            result = await handler.handle_webhook(payload, verify_signature=False)

            assert result is None

    @pytest.mark.asyncio
    async def test_handle_webhook_handler_error(self, handler):
        """Test handling webhook with handler that raises error."""

        # Register handler that raises error
        def test_handler(event):
            raise ValueError("Handler error")

        handler.register_handler("people.created", test_handler)

        payload = """
        {
            "event_type": "people.created",
            "resource": {
                "id": "123",
                "type": "people",
                "attributes": {
                    "first_name": "John"
                }
            }
        }
        """

        with patch.object(handler, "verify_signature"):
            with pytest.raises(PCOWebhookError, match="Handler execution failed"):
                await handler.handle_webhook(payload, verify_signature=False)

    @pytest.mark.asyncio
    async def test_handle_webhook_with_signature_verification(self, handler):
        """Test handling webhook with signature verification."""
        payload = """
        {
            "event_type": "people.created",
            "resource": {
                "id": "123",
                "type": "people",
                "attributes": {
                    "first_name": "John"
                }
            }
        }
        """

        with patch.object(handler, "verify_signature") as mock_verify:
            mock_verify.return_value = True

            _ = await handler.handle_webhook(
                payload, signature="sha256=test_signature", verify_signature=True
            )

            mock_verify.assert_called_once_with(payload, "sha256=test_signature")

    def test_get_registered_events(self, handler):
        """Test getting registered event types."""
        handler.register_handler("people.created", lambda x: None)
        handler.register_handler("people.updated", lambda x: None)

        events = handler.get_registered_events()

        assert "people.created" in events
        assert "people.updated" in events
        assert len(events) == 2

    def test_has_handler(self, handler):
        """Test checking if handler exists."""
        handler.register_handler("people.created", lambda x: None)

        assert handler.has_handler("people.created") is True
        assert handler.has_handler("people.updated") is False


class TestHandleWebhookEvent:
    """Test handle_webhook_event convenience function."""

    @pytest.fixture
    def mock_client(self):
        """Create mock client."""
        client = MagicMock()
        client.config = PCOConfig(webhook_secret="test_secret")
        return client

    @pytest.mark.asyncio
    async def test_handle_webhook_event_with_handlers(self, mock_client):
        """Test handle_webhook_event with event handlers."""

        async def person_created_handler(event):
            return f"Created person: {event.resource.get_attribute('first_name')}"

        event_handlers = {"people.created": person_created_handler}

        payload = """
        {
            "event_type": "people.created",
            "resource": {
                "id": "123",
                "type": "people",
                "attributes": {
                    "first_name": "John"
                }
            }
        }
        """

        with patch(
            "planning_center_api.webhooks.PCOWebhookHandler"
        ) as mock_handler_class:
            mock_handler = MagicMock()
            mock_handler.handle_webhook = AsyncMock(return_value="Created person: John")
            mock_handler_class.return_value = mock_handler

            result = await handle_webhook_event(
                client=mock_client,
                payload=payload,
                event_handlers=event_handlers,
                verify_signature=False,
            )

            assert result == "Created person: John"
            mock_handler.register_handler.assert_called_once_with(
                "people.created", person_created_handler
            )
            mock_handler.handle_webhook.assert_called_once_with(
                payload=payload, signature=None, verify_signature=False
            )

    @pytest.mark.asyncio
    async def test_handle_webhook_event_without_handlers(self, mock_client):
        """Test handle_webhook_event without event handlers."""
        payload = """
        {
            "event_type": "people.created",
            "resource": {
                "id": "123",
                "type": "people",
                "attributes": {
                    "first_name": "John"
                }
            }
        }
        """

        with patch(
            "planning_center_api.webhooks.PCOWebhookHandler"
        ) as mock_handler_class:
            mock_handler = MagicMock()
            mock_handler.handle_webhook = AsyncMock(return_value=None)
            mock_handler_class.return_value = mock_handler

            result = await handle_webhook_event(
                client=mock_client, payload=payload, verify_signature=False
            )

            assert result is None
            mock_handler.handle_webhook.assert_called_once_with(
                payload=payload, signature=None, verify_signature=False
            )


class TestWebhookEventTypes:
    """Test WebhookEventTypes constants."""

    def test_people_events(self):
        """Test people event types."""
        assert WebhookEventTypes.PEOPLE_CREATED == "people.created"
        assert WebhookEventTypes.PEOPLE_UPDATED == "people.updated"
        assert WebhookEventTypes.PEOPLE_DELETED == "people.deleted"

    def test_email_events(self):
        """Test email event types."""
        assert WebhookEventTypes.EMAILS_CREATED == "emails.created"
        assert WebhookEventTypes.EMAILS_UPDATED == "emails.updated"
        assert WebhookEventTypes.EMAILS_DELETED == "emails.deleted"

    def test_phone_number_events(self):
        """Test phone number event types."""
        assert WebhookEventTypes.PHONE_NUMBERS_CREATED == "phone_numbers.created"
        assert WebhookEventTypes.PHONE_NUMBERS_UPDATED == "phone_numbers.updated"
        assert WebhookEventTypes.PHONE_NUMBERS_DELETED == "phone_numbers.deleted"

    def test_services_events(self):
        """Test services event types."""
        assert WebhookEventTypes.SERVICES_CREATED == "services.created"
        assert WebhookEventTypes.SERVICES_UPDATED == "services.updated"
        assert WebhookEventTypes.SERVICES_DELETED == "services.deleted"

    def test_plans_events(self):
        """Test plans event types."""
        assert WebhookEventTypes.PLANS_CREATED == "plans.created"
        assert WebhookEventTypes.PLANS_UPDATED == "plans.updated"
        assert WebhookEventTypes.PLANS_DELETED == "plans.deleted"

    def test_check_ins_events(self):
        """Test check-ins event types."""
        assert WebhookEventTypes.CHECK_INS_CREATED == "check_ins.created"
        assert WebhookEventTypes.CHECK_INS_UPDATED == "check_ins.updated"
        assert WebhookEventTypes.CHECK_INS_DELETED == "check_ins.deleted"

    def test_donations_events(self):
        """Test donations event types."""
        assert WebhookEventTypes.DONATIONS_CREATED == "donations.created"
        assert WebhookEventTypes.DONATIONS_UPDATED == "donations.updated"
        assert WebhookEventTypes.DONATIONS_DELETED == "donations.deleted"

    def test_groups_events(self):
        """Test groups event types."""
        assert WebhookEventTypes.GROUPS_CREATED == "groups.created"
        assert WebhookEventTypes.GROUPS_UPDATED == "groups.updated"
        assert WebhookEventTypes.GROUPS_DELETED == "groups.deleted"

    def test_group_memberships_events(self):
        """Test group memberships event types."""
        assert (
            WebhookEventTypes.GROUP_MEMBERSHIPS_CREATED == "group_memberships.created"
        )
        assert (
            WebhookEventTypes.GROUP_MEMBERSHIPS_UPDATED == "group_memberships.updated"
        )
        assert (
            WebhookEventTypes.GROUP_MEMBERSHIPS_DELETED == "group_memberships.deleted"
        )
