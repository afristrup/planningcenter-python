"""Tests for Planning Center Organization API."""

from datetime import datetime
from unittest.mock import AsyncMock

import pytest

from planning_center_api.client import PCOClient
from planning_center_api.config import PCOConfig
from planning_center_api.models.base import PCOCollection, PCOResource
from planning_center_api.products.organization import (
    PCOConnectedApplication,
    PCOConnectedApplicationPerson,
    PCOOauthApplication,
    PCOOauthApplicationMau,
    PCOOrganization,
    PCOOrganizationPerson,
    PCOPersonalAccessToken,
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
def mock_connected_application_data():
    """Mock connected application data."""
    return {
        "data": {
            "id": "1",
            "type": "ConnectedApplication",
            "attributes": {
                "name": "Test App",
                "url": "https://testapp.com",
                "description": "A test connected application",
            },
            "relationships": {},
        }
    }


@pytest.fixture
def mock_connected_application_person_data():
    """Mock connected application person data."""
    return {
        "data": {
            "id": "1",
            "type": "ConnectedApplicationPerson",
            "attributes": {
                "first_name": "John",
                "last_name": "Doe",
                "avatar_url": "https://example.com/avatar.jpg",
                "connected_at": "2024-01-01T12:00:00Z",
            },
            "relationships": {},
        }
    }


@pytest.fixture
def mock_oauth_application_data():
    """Mock OAuth application data."""
    return {
        "data": {
            "id": "1",
            "type": "OauthApplication",
            "attributes": {
                "name": "Test OAuth App",
                "url": "https://oauthapp.com",
                "description": "A test OAuth application",
            },
            "relationships": {},
        }
    }


@pytest.fixture
def mock_oauth_application_mau_data():
    """Mock OAuth application MAU data."""
    from planning_center_api.models.relationships import PCORelationships

    return {
        "data": {
            "id": "1",
            "type": "OauthApplicationMau",
            "attributes": {
                "count": 150,
                "month": 3,
                "year": 2024,
            },
            "relationships": PCORelationships(
                oauth_application={
                    "data": {
                        "type": "OauthApplication",
                        "id": "1",
                    }
                }
            ),
        }
    }


@pytest.fixture
def mock_organization_data():
    """Mock organization data."""
    from planning_center_api.models.relationships import PCORelationships

    return {
        "data": {
            "id": "1",
            "type": "Organization",
            "attributes": {},
            "relationships": PCORelationships(
                connected_applications={
                    "data": [
                        {"type": "ConnectedApplication", "id": "1"},
                        {"type": "ConnectedApplication", "id": "2"},
                    ]
                },
                oauth_applications={
                    "data": [
                        {"type": "OauthApplication", "id": "1"},
                    ]
                },
                personal_access_tokens={
                    "data": [
                        {"type": "PersonalAccessToken", "id": "1"},
                    ]
                },
            ),
        }
    }


@pytest.fixture
def mock_person_data():
    """Mock person data."""
    return {
        "data": {
            "id": "1",
            "type": "Person",
            "attributes": {
                "first_name": "Jane",
                "last_name": "Smith",
            },
            "relationships": {},
        }
    }


@pytest.fixture
def mock_personal_access_token_data():
    """Mock personal access token data."""
    return {
        "data": {
            "id": "1",
            "type": "PersonalAccessToken",
            "attributes": {
                "name": "Test Token",
            },
            "relationships": {},
        }
    }


class TestConnectedApplications:
    """Test connected applications functionality."""

    async def test_get_connected_applications(
        self, client, mock_connected_application_data
    ):
        """Test getting all connected applications."""
        # Create a proper collection response with specific model types
        collection_data = {
            "data": [
                PCOConnectedApplication(**mock_connected_application_data["data"])
            ],
            "included": None,
            "links": None,
            "meta": None,
        }
        client._http_client.get.return_value = PCOCollection(**collection_data)

        result = await client.get_connected_applications()

        assert isinstance(result, PCOCollection)
        assert len(result) == 1
        assert result[0].id == "1"
        assert result[0].type == "ConnectedApplication"
        assert result[0].get_name() == "Test App"
        assert result[0].get_url() == "https://testapp.com"
        assert result[0].get_description() == "A test connected application"

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == "connected_applications"

    async def test_get_connected_application(
        self, client, mock_connected_application_data
    ):
        """Test getting a specific connected application."""
        client._http_client.get.return_value = PCOConnectedApplication(
            **mock_connected_application_data["data"]
        )

        result = await client.get_connected_application("1")

        assert isinstance(result, PCOResource)
        assert result.id == "1"
        assert result.get_name() == "Test App"

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == "connected_applications"
        assert call_args[1]["resource_id"] == "1"

    async def test_get_connected_application_people(
        self, client, mock_connected_application_person_data
    ):
        """Test getting people connected to an application."""
        collection_data = {
            "data": [
                PCOConnectedApplicationPerson(
                    **mock_connected_application_person_data["data"]
                )
            ],
            "included": None,
            "links": None,
            "meta": None,
        }
        client._http_client.get.return_value = PCOCollection(**collection_data)

        result = await client.get_connected_application_people("1")

        assert isinstance(result, PCOCollection)
        assert len(result) == 1
        assert result[0].id == "1"
        assert result[0].get_first_name() == "John"
        assert result[0].get_last_name() == "Doe"
        assert result[0].get_full_name() == "John Doe"
        assert result[0].get_avatar_url() == "https://example.com/avatar.jpg"
        assert isinstance(result[0].get_connected_at(), datetime)

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == "people"
        assert call_args[1]["filter_params"]["connected_application"] == "1"

    async def test_get_connected_application_person(
        self, client, mock_connected_application_person_data
    ):
        """Test getting a specific person connected to an application."""
        client._http_client.get.return_value = PCOConnectedApplicationPerson(
            **mock_connected_application_person_data["data"]
        )

        result = await client.get_connected_application_person("1", "1")

        assert isinstance(result, PCOResource)
        assert result.id == "1"
        assert result.get_full_name() == "John Doe"

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == "people"
        assert call_args[1]["resource_id"] == "1"
        assert call_args[1]["filter_params"]["connected_application"] == "1"


class TestOAuthApplications:
    """Test OAuth applications functionality."""

    async def test_get_oauth_applications(self, client, mock_oauth_application_data):
        """Test getting all OAuth applications."""
        collection_data = {
            "data": [PCOOauthApplication(**mock_oauth_application_data["data"])],
            "included": None,
            "links": None,
            "meta": None,
        }
        client._http_client.get.return_value = PCOCollection(**collection_data)

        result = await client.get_oauth_applications()

        assert isinstance(result, PCOCollection)
        assert len(result) == 1
        assert result[0].id == "1"
        assert result[0].type == "OauthApplication"
        assert result[0].get_name() == "Test OAuth App"
        assert result[0].get_url() == "https://oauthapp.com"
        assert result[0].get_description() == "A test OAuth application"

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == "oauth_applications"

    async def test_get_oauth_application(self, client, mock_oauth_application_data):
        """Test getting a specific OAuth application."""
        client._http_client.get.return_value = PCOOauthApplication(
            **mock_oauth_application_data["data"]
        )

        result = await client.get_oauth_application("1")

        assert isinstance(result, PCOResource)
        assert result.id == "1"
        assert result.get_name() == "Test OAuth App"

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == "oauth_applications"
        assert call_args[1]["resource_id"] == "1"

    async def test_get_oauth_application_mau(
        self, client, mock_oauth_application_mau_data
    ):
        """Test getting monthly active users for an OAuth application."""
        collection_data = {
            "data": [PCOOauthApplicationMau(**mock_oauth_application_mau_data["data"])],
            "included": None,
            "links": None,
            "meta": None,
        }
        client._http_client.get.return_value = PCOCollection(**collection_data)

        result = await client.get_oauth_application_mau("1")

        assert isinstance(result, PCOCollection)
        assert len(result) == 1
        assert result[0].id == "1"
        assert result[0].type == "OauthApplicationMau"
        assert result[0].get_count() == 150
        assert result[0].get_month() == 3
        assert result[0].get_year() == 2024
        assert result[0].get_oauth_application_id() == "1"

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == "mau"
        assert call_args[1]["filter_params"]["oauth_application"] == "1"

    async def test_get_oauth_application_mau_by_id(
        self, client, mock_oauth_application_mau_data
    ):
        """Test getting a specific MAU record for an OAuth application."""
        client._http_client.get.return_value = PCOOauthApplicationMau(
            **mock_oauth_application_mau_data["data"]
        )

        result = await client.get_oauth_application_mau_by_id("1", "1")

        assert isinstance(result, PCOResource)
        assert result.id == "1"
        assert result.get_count() == 150

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == "mau"
        assert call_args[1]["resource_id"] == "1"
        assert call_args[1]["filter_params"]["oauth_application"] == "1"


class TestOrganization:
    """Test organization functionality."""

    async def test_get_organization(self, client, mock_organization_data):
        """Test getting organization information."""
        client._http_client.get.return_value = PCOOrganization(
            **mock_organization_data["data"]
        )

        result = await client.get_organization()

        assert isinstance(result, PCOResource)
        assert result.id == "1"
        assert result.type == "Organization"

        # Test relationship data access
        connected_apps = result.get_connected_applications()
        assert connected_apps is not None
        assert len(connected_apps) == 2

        oauth_apps = result.get_oauth_applications()
        assert oauth_apps is not None
        assert len(oauth_apps) == 1

        tokens = result.get_personal_access_tokens()
        assert tokens is not None
        assert len(tokens) == 1

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == ""

    async def test_get_organization_with_id(self, client, mock_organization_data):
        """Test getting organization information with specific ID."""
        client._http_client.get.return_value = PCOOrganization(
            **mock_organization_data["data"]
        )

        result = await client.get_organization("1")

        assert isinstance(result, PCOResource)
        assert result.id == "1"

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == ""
        assert call_args[1]["resource_id"] == "1"


class TestPerson:
    """Test person functionality."""

    async def test_get_person(self, client, mock_person_data):
        """Test getting person information."""
        client._http_client.get.return_value = PCOOrganizationPerson(
            **mock_person_data["data"]
        )

        result = await client.get_organization_person()

        assert isinstance(result, PCOResource)
        assert result.id == "1"
        assert result.type == "Person"
        assert result.get_first_name() == "Jane"
        assert result.get_last_name() == "Smith"
        assert result.get_full_name() == "Jane Smith"

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == ""

    async def test_get_person_with_id(self, client, mock_person_data):
        """Test getting person information with specific ID."""
        client._http_client.get.return_value = PCOOrganizationPerson(
            **mock_person_data["data"]
        )

        result = await client.get_organization_person("1")

        assert isinstance(result, PCOResource)
        assert result.id == "1"
        assert result.get_full_name() == "Jane Smith"

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == ""
        assert call_args[1]["resource_id"] == "1"


class TestPersonalAccessTokens:
    """Test personal access tokens functionality."""

    async def test_get_personal_access_tokens(
        self, client, mock_personal_access_token_data
    ):
        """Test getting all personal access tokens."""
        collection_data = {
            "data": [PCOPersonalAccessToken(**mock_personal_access_token_data["data"])],
            "included": None,
            "links": None,
            "meta": None,
        }
        client._http_client.get.return_value = PCOCollection(**collection_data)

        result = await client.get_personal_access_tokens()

        assert isinstance(result, PCOCollection)
        assert len(result) == 1
        assert result[0].id == "1"
        assert result[0].type == "PersonalAccessToken"
        assert result[0].get_name() == "Test Token"

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == "personal_access_tokens"

    async def test_get_personal_access_token(
        self, client, mock_personal_access_token_data
    ):
        """Test getting a specific personal access token."""
        client._http_client.get.return_value = PCOPersonalAccessToken(
            **mock_personal_access_token_data["data"]
        )

        result = await client.get_personal_access_token("1")

        assert isinstance(result, PCOResource)
        assert result.id == "1"
        assert result.get_name() == "Test Token"

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == "personal_access_tokens"
        assert call_args[1]["resource_id"] == "1"


class TestModelMethods:
    """Test model-specific methods."""

    def test_connected_application_person_connected_at_parsing(
        self, mock_connected_application_person_data
    ):
        """Test that connected_at is properly parsed as datetime."""
        person = PCOConnectedApplicationPerson(
            **mock_connected_application_person_data["data"]
        )
        connected_at = person.get_connected_at()
        assert isinstance(connected_at, datetime)
        assert connected_at.year == 2024
        assert connected_at.month == 1
        assert connected_at.day == 1

    def test_connected_application_person_full_name(
        self, mock_connected_application_person_data
    ):
        """Test full name generation."""
        person = PCOConnectedApplicationPerson(
            **mock_connected_application_person_data["data"]
        )
        assert person.get_full_name() == "John Doe"

    def test_connected_application_person_full_name_empty(self):
        """Test full name generation with empty names."""
        person = PCOConnectedApplicationPerson(
            id="1",
            type="ConnectedApplicationPerson",
            attributes={},
        )
        assert person.get_full_name() == ""

    def test_oauth_application_mau_relationship_access(
        self, mock_oauth_application_mau_data
    ):
        """Test OAuth application relationship access."""
        mau = PCOOauthApplicationMau(**mock_oauth_application_mau_data["data"])
        oauth_app_id = mau.get_oauth_application_id()
        assert oauth_app_id == "1"

    def test_organization_relationship_access(self, mock_organization_data):
        """Test organization relationship data access."""
        org = PCOOrganization(**mock_organization_data["data"])

        connected_apps = org.get_connected_applications()
        assert connected_apps is not None
        assert len(connected_apps) == 2

        oauth_apps = org.get_oauth_applications()
        assert oauth_apps is not None
        assert len(oauth_apps) == 1

        tokens = org.get_personal_access_tokens()
        assert tokens is not None
        assert len(tokens) == 1

    def test_person_full_name(self, mock_person_data):
        """Test person full name generation."""
        person = PCOOrganizationPerson(**mock_person_data["data"])
        assert person.get_full_name() == "Jane Smith"

    def test_personal_access_token_name(self, mock_personal_access_token_data):
        """Test personal access token name access."""
        token = PCOPersonalAccessToken(**mock_personal_access_token_data["data"])
        assert token.get_name() == "Test Token"


class TestPaginationAndFiltering:
    """Test pagination and filtering parameters."""

    async def test_get_connected_applications_with_pagination(
        self, client, mock_connected_application_data
    ):
        """Test getting connected applications with pagination."""
        collection_data = {
            "data": [
                PCOConnectedApplication(**mock_connected_application_data["data"])
            ],
            "included": None,
            "links": None,
            "meta": None,
        }
        client._http_client.get.return_value = PCOCollection(**collection_data)

        await client.get_connected_applications(per_page=10, offset=20)

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == "connected_applications"
        assert call_args[1]["per_page"] == 10
        assert call_args[1]["offset"] == 20

    async def test_get_oauth_applications_with_include(
        self, client, mock_oauth_application_data
    ):
        """Test getting OAuth applications with include parameter."""
        collection_data = {
            "data": [PCOOauthApplication(**mock_oauth_application_data["data"])],
            "included": None,
            "links": None,
            "meta": None,
        }
        client._http_client.get.return_value = PCOCollection(**collection_data)

        await client.get_oauth_applications(include=["mau"])

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == "oauth_applications"
        assert call_args[1]["include"] == ["mau"]

    async def test_get_personal_access_tokens_with_all_params(
        self, client, mock_personal_access_token_data
    ):
        """Test getting personal access tokens with all parameters."""
        collection_data = {
            "data": [PCOPersonalAccessToken(**mock_personal_access_token_data["data"])],
            "included": None,
            "links": None,
            "meta": None,
        }
        client._http_client.get.return_value = PCOCollection(**collection_data)

        await client.get_personal_access_tokens(
            per_page=50, offset=100, include=["organization"]
        )

        client._http_client.get.assert_called_once()
        call_args = client._http_client.get.call_args
        assert call_args[1]["product"] == "api/v2"
        assert call_args[1]["endpoint"] == "personal_access_tokens"
        assert call_args[1]["per_page"] == 50
        assert call_args[1]["offset"] == 100
        assert call_args[1]["include"] == ["organization"]
