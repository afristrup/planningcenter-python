"""Tests for webhooks functionality."""

from datetime import datetime
from unittest.mock import AsyncMock

import pytest

from planning_center_api.products.webhooks import (
    PCOAvailableEvent,
    PCOWebhookDelivery,
    PCOWebhookEvent,
    PCOWebhookOrganization,
    PCOWebhookService,
    PCOWebhookSubscription,
)


class TestPCOWebhookSubscription:
    """Test PCOWebhookSubscription model."""

    def test_webhook_subscription_creation(self):
        """Test webhook subscription creation."""
        data = {
            "id": "1",
            "type": "WebhookSubscription",
            "attributes": {
                "name": "Test Subscription",
                "url": "https://example.com/webhook",
                "active": True,
                "created_at": "2023-01-01T12:00:00Z",
                "updated_at": "2023-01-01T12:00:00Z",
                "authenticity_secret": "secret123",
                "application_id": "app123",
            },
        }
        subscription = PCOWebhookSubscription(**data)

        assert subscription.id == "1"
        assert subscription.type == "WebhookSubscription"
        assert subscription.name == "Test Subscription"
        assert subscription.url == "https://example.com/webhook"
        assert subscription.active is True
        assert subscription.authenticity_secret == "secret123"
        assert subscription.application_id == "app123"
        assert isinstance(subscription.created_at, datetime)
        assert isinstance(subscription.updated_at, datetime)

    def test_webhook_subscription_properties(self):
        """Test webhook subscription property access."""
        data = {
            "id": "1",
            "type": "WebhookSubscription",
            "attributes": {
                "name": "Test Subscription",
                "url": "https://example.com/webhook",
                "active": False,
            },
        }
        subscription = PCOWebhookSubscription(**data)

        assert subscription.name == "Test Subscription"
        assert subscription.url == "https://example.com/webhook"
        assert subscription.active is False
        assert subscription.created_at is None
        assert subscription.updated_at is None
        assert subscription.authenticity_secret is None
        assert subscription.application_id is None


class TestPCOWebhookEvent:
    """Test PCOWebhookEvent model."""

    def test_webhook_event_creation(self):
        """Test webhook event creation."""
        data = {
            "id": "1",
            "type": "Event",
            "attributes": {
                "created_at": "2023-01-01T12:00:00Z",
                "status": "delivered",
                "updated_at": "2023-01-01T12:00:00Z",
                "uuid": "uuid123",
                "payload": '{"data": {"type": "Person", "id": "1"}}',
            },
        }
        event = PCOWebhookEvent(**data)

        assert event.id == "1"
        assert event.type == "Event"
        assert event.status == "delivered"
        assert event.uuid == "uuid123"
        assert event.payload == '{"data": {"type": "Person", "id": "1"}}'
        assert isinstance(event.created_at, datetime)
        assert isinstance(event.updated_at, datetime)

    def test_webhook_event_properties(self):
        """Test webhook event property access."""
        data = {
            "id": "1",
            "type": "Event",
            "attributes": {
                "status": "pending",
                "uuid": "uuid456",
            },
        }
        event = PCOWebhookEvent(**data)

        assert event.status == "pending"
        assert event.uuid == "uuid456"
        assert event.created_at is None
        assert event.updated_at is None
        assert event.payload is None


class TestPCOWebhookDelivery:
    """Test PCOWebhookDelivery model."""

    def test_webhook_delivery_creation(self):
        """Test webhook delivery creation."""
        data = {
            "id": "1",
            "type": "Delivery",
            "attributes": {
                "status": 200,
                "request_headers": "Content-Type: application/json",
                "request_body": '{"test": "data"}',
                "response_headers": "HTTP/1.1 200 OK",
                "response_body": '{"success": true}',
                "created_at": "2023-01-01T12:00:00Z",
                "updated_at": "2023-01-01T12:00:00Z",
                "timing": 1.5,
                "object_url": "https://api.planningcenteronline.com/people/v2/people/1",
            },
        }
        delivery = PCOWebhookDelivery(**data)

        assert delivery.id == "1"
        assert delivery.type == "Delivery"
        assert delivery.status == 200
        assert delivery.request_headers == "Content-Type: application/json"
        assert delivery.request_body == '{"test": "data"}'
        assert delivery.response_headers == "HTTP/1.1 200 OK"
        assert delivery.response_body == '{"success": true}'
        assert delivery.timing == 1.5
        assert (
            delivery.object_url
            == "https://api.planningcenteronline.com/people/v2/people/1"
        )
        assert isinstance(delivery.created_at, datetime)
        assert isinstance(delivery.updated_at, datetime)

    def test_webhook_delivery_properties(self):
        """Test webhook delivery property access."""
        data = {
            "id": "1",
            "type": "Delivery",
            "attributes": {
                "status": 404,
                "timing": 0.5,
            },
        }
        delivery = PCOWebhookDelivery(**data)

        assert delivery.status == 404
        assert delivery.timing == 0.5
        assert delivery.request_headers is None
        assert delivery.request_body is None
        assert delivery.response_headers is None
        assert delivery.response_body is None
        assert delivery.created_at is None
        assert delivery.updated_at is None
        assert delivery.object_url is None


class TestPCOAvailableEvent:
    """Test PCOAvailableEvent model."""

    def test_available_event_creation(self):
        """Test available event creation."""
        data = {
            "id": "1",
            "type": "AvailableEvent",
            "attributes": {
                "name": "people.created",
                "app": "people",
                "version": "v2",
                "type": "created",
                "resource": "Person",
                "action": "create",
            },
        }
        event = PCOAvailableEvent(**data)

        assert event.id == "1"
        assert event.type == "AvailableEvent"
        assert event.name == "people.created"
        assert event.app == "people"
        assert event.version == "v2"
        assert event.event_type == "created"
        assert event.resource == "Person"
        assert event.action == "create"

    def test_available_event_properties(self):
        """Test available event property access."""
        data = {
            "id": "1",
            "type": "AvailableEvent",
            "attributes": {
                "name": "services.updated",
                "app": "services",
            },
        }
        event = PCOAvailableEvent(**data)

        assert event.name == "services.updated"
        assert event.app == "services"
        assert event.version is None
        assert event.event_type is None
        assert event.resource is None
        assert event.action is None


class TestPCOWebhookOrganization:
    """Test PCOWebhookOrganization model."""

    def test_webhook_organization_creation(self):
        """Test webhook organization creation."""
        data = {
            "id": "1",
            "type": "Organization",
            "attributes": {},
        }
        org = PCOWebhookOrganization(**data)

        assert org.id == "1"
        assert org.type == "Organization"


class TestPCOWebhookService:
    """Test PCOWebhookService."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock client."""
        client = AsyncMock()
        client.get = AsyncMock()
        client.post = AsyncMock()
        client.patch = AsyncMock()
        client.delete = AsyncMock()
        return client

    @pytest.fixture
    def webhook_service(self, mock_client):
        """Create a webhook service with mock client."""
        return PCOWebhookService(mock_client)

    async def test_get_webhook_subscriptions(self, webhook_service, mock_client):
        """Test getting webhook subscriptions."""
        mock_response = {
            "data": [
                {
                    "id": "1",
                    "type": "WebhookSubscription",
                    "attributes": {
                        "name": "Test Subscription",
                        "url": "https://example.com/webhook",
                        "active": True,
                    },
                }
            ]
        }
        mock_client.get.return_value = mock_response

        subscriptions = await webhook_service.get_webhook_subscriptions()

        assert len(subscriptions) == 1
        assert subscriptions[0].id == "1"
        assert subscriptions[0].name == "Test Subscription"
        mock_client.get.assert_called_once_with(
            "/webhooks/v2/webhook_subscriptions", params={}
        )

    async def test_get_webhook_subscription(self, webhook_service, mock_client):
        """Test getting a specific webhook subscription."""
        mock_response = {
            "data": {
                "id": "1",
                "type": "WebhookSubscription",
                "attributes": {
                    "name": "Test Subscription",
                    "url": "https://example.com/webhook",
                    "active": True,
                },
            }
        }
        mock_client.get.return_value = mock_response

        subscription = await webhook_service.get_webhook_subscription("1")

        assert subscription.id == "1"
        assert subscription.name == "Test Subscription"
        mock_client.get.assert_called_once_with("/webhooks/v2/webhook_subscriptions/1")

    async def test_create_webhook_subscription(self, webhook_service, mock_client):
        """Test creating a webhook subscription."""
        mock_response = {
            "data": {
                "id": "1",
                "type": "WebhookSubscription",
                "attributes": {
                    "name": "New Subscription",
                    "url": "https://example.com/webhook",
                    "active": True,
                },
            }
        }
        mock_client.post.return_value = mock_response

        subscription = await webhook_service.create_webhook_subscription(
            name="New Subscription", url="https://example.com/webhook", active=True
        )

        assert subscription.id == "1"
        assert subscription.name == "New Subscription"
        mock_client.post.assert_called_once()
        call_args = mock_client.post.call_args
        assert call_args[0][0] == "/webhooks/v2/webhook_subscriptions"
        assert call_args[1]["json"]["data"]["attributes"]["name"] == "New Subscription"

    async def test_delete_webhook_subscription(self, webhook_service, mock_client):
        """Test deleting a webhook subscription."""
        await webhook_service.delete_webhook_subscription("1")

        mock_client.delete.assert_called_once_with(
            "/webhooks/v2/webhook_subscriptions/1"
        )

    async def test_get_available_events(self, webhook_service, mock_client):
        """Test getting available events."""
        mock_response = {
            "data": [
                {
                    "id": "1",
                    "type": "AvailableEvent",
                    "attributes": {
                        "name": "people.created",
                        "app": "people",
                    },
                }
            ]
        }
        mock_client.get.return_value = mock_response

        events = await webhook_service.get_available_events()

        assert len(events) == 1
        assert events[0].id == "1"
        assert events[0].name == "people.created"
        mock_client.get.assert_called_once_with(
            "/webhooks/v2/available_events", params={}
        )
