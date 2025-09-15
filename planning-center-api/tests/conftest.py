"""Pytest configuration and fixtures."""

import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest

from planning_center_api import PCOClient, PCOConfig
from planning_center_api.models.base import PCOCollection, PCOResource


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def config():
    """Create test configuration."""
    return PCOConfig(
        app_id="test_app_id",
        secret="test_secret",
        access_token="test_token",
        webhook_secret="test_webhook_secret",
    )


@pytest.fixture
def mock_client(config):
    """Create mock client for testing."""
    client = PCOClient(config=config)
    client._http_client = AsyncMock()
    return client


@pytest.fixture
def sample_person():
    """Create sample person resource."""
    return PCOResource(
        id="123",
        type="people",
        attributes={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "555-123-4567",
            "status": "active",
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-02T00:00:00Z",
        },
    )


@pytest.fixture
def sample_people_collection(sample_person):
    """Create sample people collection."""
    person2 = PCOResource(
        id="456",
        type="people",
        attributes={
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane.smith@example.com",
            "phone": "555-987-6543",
            "status": "active",
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-02T00:00:00Z",
        },
    )

    return PCOCollection(data=[sample_person, person2])


@pytest.fixture
def sample_service():
    """Create sample service resource."""
    return PCOResource(
        id="789",
        type="services",
        attributes={
            "name": "Sunday Service",
            "description": "Weekly worship service",
            "start_time": "2023-01-01T10:00:00Z",
            "end_time": "2023-01-01T11:00:00Z",
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-02T00:00:00Z",
        },
    )


@pytest.fixture
def sample_services_collection(sample_service):
    """Create sample services collection."""
    service2 = PCOResource(
        id="101",
        type="services",
        attributes={
            "name": "Wednesday Service",
            "description": "Midweek service",
            "start_time": "2023-01-04T19:00:00Z",
            "end_time": "2023-01-04T20:00:00Z",
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-02T00:00:00Z",
        },
    )

    return PCOCollection(data=[sample_service, service2])


@pytest.fixture
def sample_plan():
    """Create sample plan resource."""
    return PCOResource(
        id="202",
        type="plans",
        attributes={
            "title": "Easter Service",
            "series_title": "Resurrection",
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-02T00:00:00Z",
        },
    )


@pytest.fixture
def sample_plans_collection(sample_plan):
    """Create sample plans collection."""
    plan2 = PCOResource(
        id="303",
        type="plans",
        attributes={
            "title": "Christmas Service",
            "series_title": "Advent",
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-02T00:00:00Z",
        },
    )

    return PCOCollection(data=[sample_plan, plan2])


@pytest.fixture
def sample_webhook_payload():
    """Create sample webhook payload."""
    return {
        "event_type": "people.created",
        "resource": {
            "id": "123",
            "type": "people",
            "attributes": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
            },
        },
        "timestamp": "2023-01-01T00:00:00Z",
        "webhook_id": "webhook_123",
        "organization_id": "org_123",
    }


@pytest.fixture
def mock_http_response():
    """Create mock HTTP response."""
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {
        "data": {
            "id": "123",
            "type": "people",
            "attributes": {"first_name": "John", "last_name": "Doe"},
        }
    }
    return response


@pytest.fixture
def mock_http_collection_response():
    """Create mock HTTP collection response."""
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {
        "data": [
            {
                "id": "123",
                "type": "people",
                "attributes": {"first_name": "John", "last_name": "Doe"},
            },
            {
                "id": "456",
                "type": "people",
                "attributes": {"first_name": "Jane", "last_name": "Smith"},
            },
        ],
        "meta": {
            "count": 2,
            "total_count": 100,
            "total_pages": 4,
            "current_page": 1,
            "per_page": 25,
        },
        "links": {
            "self": {
                "href": "https://api.planningcenteronline.com/people/v2/people?page=1"
            },
            "next": {
                "href": "https://api.planningcenteronline.com/people/v2/people?page=2"
            },
            "last": {
                "href": "https://api.planningcenteronline.com/people/v2/people?page=4"
            },
        },
    }
    return response


@pytest.fixture
def mock_http_error_response():
    """Create mock HTTP error response."""
    response = MagicMock()
    response.status_code = 404
    response.json.return_value = {
        "errors": [
            {
                "status": "404",
                "title": "Not Found",
                "detail": "The requested resource was not found",
            }
        ]
    }
    return response


# Markers for different test types
def pytest_configure(config):
    """Configure pytest markers."""
    config.addinivalue_line("markers", "unit: mark test as a unit test")
    config.addinivalue_line("markers", "integration: mark test as an integration test")
    config.addinivalue_line("markers", "slow: mark test as slow running")
    config.addinivalue_line(
        "markers", "requires_auth: mark test as requiring authentication"
    )


# Async test helper
@pytest.fixture
def async_test():
    """Helper for async tests."""

    def _async_test(coro):
        return asyncio.get_event_loop().run_until_complete(coro)

    return _async_test
