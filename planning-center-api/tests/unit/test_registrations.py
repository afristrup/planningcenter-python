"""Tests for Planning Center Registrations API."""

import pytest

from planning_center_api.client import PCOClient
from planning_center_api.config import PCOConfig, PCOProduct
from planning_center_api.products.registrations import (
    PCOAttendee,
    PCOEmergencyContact,
    PCORegistration,
    PCORegistrationsPerson,
    PCOSelectionType,
    PCOSignup,
)


@pytest.fixture
def client():
    """Create a test client."""
    config = PCOConfig(
        application_id="test_app_id",
        secret="test_secret",
        products=[PCOProduct.REGISTRATIONS],
    )
    return PCOClient(config)


@pytest.fixture
def mock_signup_data():
    """Mock signup data."""
    return {
        "data": {
            "id": "1",
            "type": "signups",
            "attributes": {
                "name": "Test Signup",
                "description": "A test signup",
                "archived": False,
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
            "id": "1",
            "type": "registrations",
            "attributes": {
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z",
            },
        }
    }


class TestRegistrationsModels:
    """Test cases for Registrations model functionality."""

    def test_signup_model(self, mock_signup_data):
        """Test PCOSignup model methods."""
        signup = PCOSignup(**mock_signup_data["data"])

        assert signup.get_name() == "Test Signup"
        assert signup.get_description() == "A test signup"
        assert signup.get_archived() is False
        assert isinstance(signup.get_created_at(), str)
        assert isinstance(signup.get_updated_at(), str)

    def test_registration_model(self, mock_registration_data):
        """Test PCORegistration model methods."""
        registration = PCORegistration(**mock_registration_data["data"])

        assert isinstance(registration.get_created_at(), str)
        assert isinstance(registration.get_updated_at(), str)

    def test_attendee_model(self):
        """Test PCOAttendee model methods."""
        attendee_data = {
            "id": "123",
            "type": "attendees",
            "attributes": {
                "complete": True,
                "active": True,
                "canceled": False,
                "waitlisted": False,
                "created_at": "2024-01-10T10:00:00Z",
                "updated_at": "2024-01-10T10:00:00Z",
            },
        }

        attendee = PCOAttendee(**attendee_data)
        assert attendee.get_complete() is True
        assert attendee.get_active() is True
        assert attendee.get_canceled() is False
        assert attendee.get_waitlisted() is False

    def test_selection_type_model(self):
        """Test PCOSelectionType model methods."""
        selection_type_data = {
            "id": "456",
            "type": "selection_types",
            "attributes": {
                "name": "Adult Registration",
                "publicly_available": True,
                "price_cents": 5000,
                "price_currency": "USD",
                "price_currency_symbol": "$",
                "price_formatted": "50.00",
                "created_at": "2024-01-10T10:00:00Z",
                "updated_at": "2024-01-10T10:00:00Z",
            },
        }

        selection_type = PCOSelectionType(**selection_type_data)
        assert selection_type.get_name() == "Adult Registration"
        assert selection_type.get_publicly_available() is True
        assert selection_type.get_price_cents() == 5000
        assert selection_type.get_price_currency() == "USD"

    def test_registrations_person_model(self):
        """Test PCORegistrationsPerson model methods."""
        person_data = {
            "id": "789",
            "type": "people",
            "attributes": {
                "first_name": "John",
                "last_name": "Doe",
                "name": "John Doe",
            },
        }

        person = PCORegistrationsPerson(**person_data)

        assert person.get_first_name() == "John"
        assert person.get_last_name() == "Doe"
        assert person.get_name() == "John Doe"

    def test_emergency_contact_model(self):
        """Test PCOEmergencyContact model methods."""
        contact_data = {
            "id": "101",
            "type": "emergency_contacts",
            "attributes": {
                "name": "Jane Doe",
                "phone_number": "555-987-6543",
            },
        }

        contact = PCOEmergencyContact(**contact_data)

        assert contact.get_name() == "Jane Doe"
        assert contact.get_phone_number() == "555-987-6543"
