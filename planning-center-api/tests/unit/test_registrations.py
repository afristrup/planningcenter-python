"""Tests for Planning Center Registrations API."""

from datetime import datetime
from unittest.mock import AsyncMock

import pytest

from planning_center_api.client import PCOClient
from planning_center_api.config import PCOConfig, PCOProduct
from planning_center_api.models.base import PCOCollection, PCOResource
from planning_center_api.products.registrations import (
    PCORegistration,
    PCORegistrationEvent,
    PCORegistrationForm,
    PCORegistrationInstancePerson,
)


@pytest.fixture
def client():
    """Create a test client."""
    config = PCOConfig(
        app_id="test_app_id",
        secret="test_secret",
    )
    client = PCOClient(config=config)
    client._http_client = AsyncMock()
    return client


@pytest.fixture
def mock_registration_event_data():
    """Mock registration event data."""
    return {
        "data": {
            "id": "123",
            "type": "events",
            "attributes": {
                "name": "Test Event",
                "description": "A test registration event",
                "start_time": "2024-01-15T10:00:00Z",
                "end_time": "2024-01-15T12:00:00Z",
                "registration_start_time": "2024-01-01T00:00:00Z",
                "registration_end_time": "2024-01-14T23:59:59Z",
                "capacity": 100,
                "registered_count": 25,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z",
            },
        }
    }


@pytest.fixture
def mock_registration_data():
    """Mock registration data."""
    return {
        "data": {
            "id": "456",
            "type": "registrations",
            "attributes": {
                "name": "Test Registration",
                "description": "A test registration",
                "registration_start_time": "2024-01-01T00:00:00Z",
                "registration_end_time": "2024-01-14T23:59:59Z",
                "capacity": 50,
                "registered_count": 10,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z",
            },
        }
    }


@pytest.fixture
def mock_collection_data():
    """Mock collection data."""
    return {
        "data": [
            {
                "id": "123",
                "type": "events",
                "attributes": {
                    "name": "Event 1",
                    "capacity": 100,
                    "registered_count": 25,
                },
            },
            {
                "id": "124",
                "type": "events",
                "attributes": {
                    "name": "Event 2",
                    "capacity": 50,
                    "registered_count": 10,
                },
            },
        ],
        "links": {
            "self": {"href": "https://api.planningcenteronline.com/registrations/v2/events"},
            "next": {"href": "https://api.planningcenteronline.com/registrations/v2/events?page=2"},
        },
    }


class TestRegistrationsAPI:
    """Test cases for Registrations API functionality."""

    async def test_get_registration_events(self, client, mock_collection_data):
        """Test getting registration events."""
        client._http_client.get.return_value = PCOCollection(**mock_collection_data)

        result = await client.get_registration_events(per_page=25)

        assert isinstance(result, PCOCollection)
        assert len(result.data) == 2
        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "registrations/v2"
        assert call_args[1]["endpoint"] == "events"
        assert call_args[1]["per_page"] == 25

    async def test_get_registration_event(self, client, mock_registration_event_data):
        """Test getting a specific registration event."""
        client._http_client.get.return_value = PCOResource(**mock_registration_event_data["data"])

        result = await client.get_registration_event("123")

        assert isinstance(result, PCOResource)
        assert result.id == "123"
        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "registrations/v2"
        assert call_args[1]["endpoint"] == "events"
        assert call_args[1]["resource_id"] == "123"

    async def test_get_registrations(self, client, mock_collection_data):
        """Test getting registrations."""
        client._http_client.get.return_value = PCOCollection(**mock_collection_data)

        result = await client.get_registrations(per_page=10)

        assert isinstance(result, PCOCollection)
        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "registrations/v2"
        assert call_args[1]["endpoint"] == "registrations"
        assert call_args[1]["per_page"] == 10

    async def test_get_registration(self, client, mock_registration_data):
        """Test getting a specific registration."""
        client._http_client.get.return_value = PCOResource(**mock_registration_data["data"])

        result = await client.get_registration("456")

        assert isinstance(result, PCOResource)
        assert result.id == "456"
        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "registrations/v2"
        assert call_args[1]["endpoint"] == "registrations"
        assert call_args[1]["resource_id"] == "456"

    async def test_get_registration_instances(self, client, mock_collection_data):
        """Test getting registration instances."""
        client._http_client.get.return_value = PCOCollection(**mock_collection_data)

        result = await client.get_registration_instances(registration_id="456")

        assert isinstance(result, PCOCollection)
        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "registrations/v2"
        assert call_args[1]["endpoint"] == "registration_instances"
        assert call_args[1]["filter_params"]["registration"] == "456"

    async def test_get_registration_forms(self, client, mock_collection_data):
        """Test getting registration forms."""
        client._http_client.get.return_value = PCOCollection(**mock_collection_data)

        result = await client.get_registration_forms(registration_id="456")

        assert isinstance(result, PCOCollection)
        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "registrations/v2"
        assert call_args[1]["endpoint"] == "registration_forms"
        assert call_args[1]["filter_params"]["registration"] == "456"

    async def test_get_registration_instance_people(self, client, mock_collection_data):
        """Test getting registered people for an instance."""
        client._http_client.get.return_value = PCOCollection(**mock_collection_data)

        result = await client.get_registration_instance_people(instance_id="789")

        assert isinstance(result, PCOCollection)
        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "registrations/v2"
        assert call_args[1]["endpoint"] == "registration_instances_people"
        assert call_args[1]["filter_params"]["registration_instance"] == "789"

    async def test_get_open_registrations(self, client, mock_collection_data):
        """Test getting open registrations."""
        client._http_client.get.return_value = PCOCollection(**mock_collection_data)

        result = await client.get_open_registrations()

        assert isinstance(result, PCOCollection)
        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["filter_params"]["status"] == "open"

    async def test_get_closed_registrations(self, client, mock_collection_data):
        """Test getting closed registrations."""
        client._http_client.get.return_value = PCOCollection(**mock_collection_data)

        result = await client.get_closed_registrations()

        assert isinstance(result, PCOCollection)
        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["filter_params"]["status"] == "closed"

    async def test_get_registrations_by_capacity(self, client, mock_collection_data):
        """Test getting registrations filtered by capacity."""
        client._http_client.get.return_value = PCOCollection(**mock_collection_data)

        result = await client.get_registrations_by_capacity(min_capacity=10, max_capacity=100)

        assert isinstance(result, PCOCollection)
        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["filter_params"]["min_capacity"] == 10
        assert call_args[1]["filter_params"]["max_capacity"] == 100


class TestRegistrationsModels:
    """Test cases for Registrations model functionality."""

    def test_registration_event_model(self, mock_registration_event_data):
        """Test PCORegistrationEvent model methods."""
        event = PCORegistrationEvent(**mock_registration_event_data["data"])

        assert event.get_name() == "Test Event"
        assert event.get_description() == "A test registration event"
        assert event.get_capacity() == 100
        assert event.get_registered_count() == 25
        assert event.get_available_spots() == 75
        assert isinstance(event.get_start_time(), datetime)
        assert isinstance(event.get_end_time(), datetime)
        assert isinstance(event.get_registration_start_time(), datetime)
        assert isinstance(event.get_registration_end_time(), datetime)

    def test_registration_model(self, mock_registration_data):
        """Test PCORegistration model methods."""
        registration = PCORegistration(**mock_registration_data["data"])

        assert registration.get_name() == "Test Registration"
        assert registration.get_description() == "A test registration"
        assert registration.get_capacity() == 50
        assert registration.get_registered_count() == 10
        assert registration.get_available_spots() == 40
        assert isinstance(registration.get_registration_start_time(), datetime)
        assert isinstance(registration.get_registration_end_time(), datetime)

    def test_registration_event_is_open(self):
        """Test registration event open status."""
        # Test with registration times that are definitely in the past and future
        from datetime import UTC
        past_start = datetime.now(UTC).replace(year=2020, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        future_end = datetime.now(UTC).replace(year=2030, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)

        event_data = {
            "id": "123",
            "type": "events",
            "attributes": {
                "name": "Open Event",
                "registration_start_time": past_start.isoformat().replace("+00:00", "Z"),
                "registration_end_time": future_end.isoformat().replace("+00:00", "Z"),
            },
        }

        event = PCORegistrationEvent(**event_data)
        assert event.is_registration_open() is True

    def test_registration_event_is_closed(self):
        """Test registration event closed status."""
        # Test with past registration times
        past_start = datetime.utcnow().replace(year=2023, month=1, day=1)
        past_end = datetime.utcnow().replace(year=2023, month=1, day=31)

        event_data = {
            "id": "123",
            "type": "events",
            "attributes": {
                "name": "Past Event",
                "registration_start_time": past_start.isoformat() + "Z",
                "registration_end_time": past_end.isoformat() + "Z",
            },
        }

        event = PCORegistrationEvent(**event_data)
        assert event.is_registration_open() is False

    def test_registration_instance_person_model(self):
        """Test PCORegistrationInstancePerson model methods."""
        person_data = {
            "id": "789",
            "type": "registration_instances_people",
            "attributes": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john@example.com",
                "phone": "555-123-4567",
                "registration_date": "2024-01-10T10:00:00Z",
                "created_at": "2024-01-10T10:00:00Z",
                "updated_at": "2024-01-10T10:00:00Z",
            },
        }

        person = PCORegistrationInstancePerson(**person_data)

        assert person.get_first_name() == "John"
        assert person.get_last_name() == "Doe"
        assert person.get_full_name() == "John Doe"
        assert person.get_email() == "john@example.com"
        assert person.get_phone() == "555-123-4567"
        assert isinstance(person.get_registration_date(), datetime)

    def test_registration_form_model(self):
        """Test PCORegistrationForm model methods."""
        form_data = {
            "id": "101",
            "type": "registration_forms",
            "attributes": {
                "name": "Event Registration Form",
                "description": "Form for event registration",
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z",
            },
        }

        form = PCORegistrationForm(**form_data)

        assert form.get_name() == "Event Registration Form"
        assert form.get_description() == "Form for event registration"
        assert isinstance(form.get_created_at(), datetime)
        assert isinstance(form.get_updated_at(), datetime)


class TestRegistrationsIntegration:
    """Integration tests for Registrations API."""

    async def test_paginate_registration_events(self, client):
        """Test paginating through registration events."""
        # Mock the HTTP client
        client._http_client = AsyncMock()

        # Mock first page
        first_page = {
            "data": [
                {"id": "1", "type": "events", "attributes": {"name": "Event 1"}},
                {"id": "2", "type": "events", "attributes": {"name": "Event 2"}},
            ],
            "links": {
                "self": {"href": "https://api.planningcenteronline.com/registrations/v2/events"},
                "next": {"href": "https://api.planningcenteronline.com/registrations/v2/events?page=2"},
            },
        }

        # Mock second page
        second_page = {
            "data": [
                {"id": "3", "type": "events", "attributes": {"name": "Event 3"}},
            ],
            "links": {
                "self": {"href": "https://api.planningcenteronline.com/registrations/v2/events?page=2"},
            },
        }

        client._http_client.get.side_effect = [
            PCOCollection(**first_page),
            PCOCollection(**second_page),
        ]

        # Test pagination
        events = []
        async for event in client.paginate_all(
            product=PCOProduct.REGISTRATIONS,
            resource="events",
            per_page=2
        ):
            events.append(event)

        assert len(events) == 3
        assert events[0].get_attribute("name") == "Event 1"
        assert events[1].get_attribute("name") == "Event 2"
        assert events[2].get_attribute("name") == "Event 3"

    async def test_generic_crud_operations(self, client):
        """Test generic CRUD operations for registrations."""
        client._http_client = AsyncMock()

        # Test GET
        mock_data = {
            "data": {
                "id": "123",
                "type": "registrations",
                "attributes": {"name": "Test Registration"},
            }
        }
        client._http_client.get.return_value = PCOResource(**mock_data["data"])

        result = await client.get(
            PCOProduct.REGISTRATIONS,
            "registrations",
            "123"
        )

        assert result.id == "123"
        client._http_client.get.assert_called_once()

        # Test CREATE
        client._http_client.post.return_value = PCOResource(**mock_data["data"])

        result = await client.create(
            PCOProduct.REGISTRATIONS,
            "registrations",
            {"name": "New Registration"}
        )

        assert result.id == "123"
        client._http_client.post.assert_called_once()

        # Test UPDATE
        client._http_client.patch.return_value = PCOResource(**mock_data["data"])

        result = await client.update(
            PCOProduct.REGISTRATIONS,
            "registrations",
            "123",
            {"name": "Updated Registration"}
        )

        assert result.id == "123"
        client._http_client.patch.assert_called_once()

        # Test DELETE
        client._http_client.delete.return_value = True

        result = await client.delete(
            PCOProduct.REGISTRATIONS,
            "registrations",
            "123"
        )

        assert result is True
        client._http_client.delete.assert_called_once()
