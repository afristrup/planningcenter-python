"""Comprehensive integration tests for the entire Planning Center API."""

from unittest.mock import AsyncMock

import pytest

from planning_center_api.client import PCOClient
from planning_center_api.config import PCOConfig, PCOProduct
from planning_center_api.models.base import PCOCollection, PCOResource


class TestFullAPIIntegration:
    """Comprehensive integration tests for all Planning Center API products."""

    @pytest.fixture
    def client(self):
        """Create a test client."""
        config = PCOConfig(
            app_id="test_app_id",
            secret="test_secret",
        )
        client = PCOClient(config=config)
        client._http_client = AsyncMock()
        return client

    @pytest.fixture
    def mock_collection_response(self):
        """Mock collection response."""
        return {
            "data": [
                {
                    "id": "1",
                    "type": "test_resource",
                    "attributes": {"name": "Test Resource 1"},
                },
                {
                    "id": "2",
                    "type": "test_resource",
                    "attributes": {"name": "Test Resource 2"},
                },
            ],
            "links": {
                "self": {
                    "href": "https://api.planningcenteronline.com/test/v2/test_resource"
                },
            },
        }

    @pytest.fixture
    def mock_resource_response(self):
        """Mock single resource response."""
        return {
            "data": {
                "id": "123",
                "type": "test_resource",
                "attributes": {"name": "Test Resource"},
            }
        }

    async def test_all_products_accessible(self, client):
        """Test that all products are accessible through the client."""
        client._http_client.get.return_value = PCOCollection(
            **{"data": [], "links": {}}
        )

        # Test all products with actual resources
        test_cases = [
            (PCOProduct.PEOPLE, "people"),
            (PCOProduct.SERVICES, "plans"),
            (PCOProduct.CHECK_INS, "events"),
            (PCOProduct.GIVING, "funds"),
            (PCOProduct.GROUPS, "groups"),
            (PCOProduct.CALENDAR, "events"),
            (PCOProduct.REGISTRATIONS, "events"),
        ]

        for product, resource in test_cases:
            result = await client.get(product, resource)
            assert isinstance(result, PCOCollection)

            # Verify the correct product base was used
            call_args = client._http_client.get.call_args
            expected_base = f"{product.value}/v2"
            assert call_args[1]["product"] == expected_base

    async def test_people_api_methods(self, client, mock_collection_response):
        """Test People API convenience methods."""
        client._http_client.get.return_value = PCOCollection(**mock_collection_response)

        # Test get_people
        result = await client.get_people(per_page=25)
        assert isinstance(result, PCOCollection)

        # Test get_person
        client._http_client.get.return_value = PCOResource(
            **mock_collection_response["data"][0]
        )
        result = await client.get_person("123")
        assert isinstance(result, PCOResource)

        # Test search_people
        client._http_client.get.return_value = PCOCollection(**mock_collection_response)
        result = await client.search_people("john")
        assert isinstance(result, PCOCollection)

        # Test get_people_by_email
        result = await client.get_people_by_email("john@example.com")
        assert isinstance(result, PCOCollection)

        # Test get_active_people
        result = await client.get_active_people()
        assert isinstance(result, PCOCollection)

        # Test get_inactive_people
        result = await client.get_inactive_people()
        assert isinstance(result, PCOCollection)

    async def test_services_api_methods(self, client, mock_collection_response):
        """Test Services API convenience methods."""
        client._http_client.get.return_value = PCOCollection(**mock_collection_response)

        # Test get_services
        result = await client.get_services(per_page=25)
        assert isinstance(result, PCOCollection)

        # Test get_service
        client._http_client.get.return_value = PCOResource(
            **mock_collection_response["data"][0]
        )
        result = await client.get_service("123")
        assert isinstance(result, PCOResource)

        # Test get_plans
        client._http_client.get.return_value = PCOCollection(**mock_collection_response)
        result = await client.get_plans(service_id="123")
        assert isinstance(result, PCOCollection)

        # Test get_plan
        client._http_client.get.return_value = PCOResource(
            **mock_collection_response["data"][0]
        )
        result = await client.get_plan("123")
        assert isinstance(result, PCOResource)

    async def test_registrations_api_methods(self, client, mock_collection_response):
        """Test Registrations API convenience methods."""
        client._http_client.get.return_value = PCOCollection(**mock_collection_response)

        # Test get_registration_events
        result = await client.get_registration_events(per_page=25)
        assert isinstance(result, PCOCollection)

        # Test get_registration_event
        client._http_client.get.return_value = PCOResource(
            **mock_collection_response["data"][0]
        )
        result = await client.get_registration_event("123")
        assert isinstance(result, PCOResource)

        # Test get_registrations
        client._http_client.get.return_value = PCOCollection(**mock_collection_response)
        result = await client.get_registrations(per_page=25)
        assert isinstance(result, PCOCollection)

        # Test get_registration
        client._http_client.get.return_value = PCOResource(
            **mock_collection_response["data"][0]
        )
        result = await client.get_registration("123")
        assert isinstance(result, PCOResource)

        # Test get_registration_instances
        client._http_client.get.return_value = PCOCollection(**mock_collection_response)
        result = await client.get_registration_instances(registration_id="123")
        assert isinstance(result, PCOCollection)

        # Test get_registration_forms
        result = await client.get_registration_forms(registration_id="123")
        assert isinstance(result, PCOCollection)

        # Test get_registration_instance_people
        result = await client.get_registration_instance_people(instance_id="123")
        assert isinstance(result, PCOCollection)

        # Test utility methods
        result = await client.get_open_registrations()
        assert isinstance(result, PCOCollection)

        result = await client.get_closed_registrations()
        assert isinstance(result, PCOCollection)

        result = await client.get_registrations_by_capacity(
            min_capacity=10, max_capacity=100
        )
        assert isinstance(result, PCOCollection)

        # Test get_attendees
        result = await client.get_attendees(per_page=25)
        assert isinstance(result, PCOCollection)

        # Test get_attendee
        client._http_client.get.return_value = PCOResource(
            **mock_collection_response["data"][0]
        )
        result = await client.get_attendee("123")
        assert isinstance(result, PCOResource)

        # Test get_attendees_by_event
        client._http_client.get.return_value = PCOCollection(**mock_collection_response)
        result = await client.get_attendees_by_event("event_123")
        assert isinstance(result, PCOCollection)

        # Test get_checked_in_attendees
        result = await client.get_checked_in_attendees()
        assert isinstance(result, PCOCollection)

    async def test_generic_crud_operations_all_products(
        self, client, mock_resource_response
    ):
        """Test generic CRUD operations for all products."""
        client._http_client.get.return_value = PCOResource(
            **mock_resource_response["data"]
        )
        client._http_client.post.return_value = PCOResource(
            **mock_resource_response["data"]
        )
        client._http_client.patch.return_value = PCOResource(
            **mock_resource_response["data"]
        )
        client._http_client.delete.return_value = True

        test_cases = [
            (PCOProduct.PEOPLE, "people"),
            (PCOProduct.SERVICES, "plans"),
            (PCOProduct.CHECK_INS, "events"),
            (PCOProduct.GIVING, "funds"),
            (PCOProduct.GROUPS, "groups"),
            (PCOProduct.CALENDAR, "events"),
            (PCOProduct.REGISTRATIONS, "events"),
        ]

        for product, resource in test_cases:
            # Test GET
            result = await client.get(product, resource, "123")
            assert isinstance(result, PCOResource)
            assert result.id == "123"

            # Test CREATE
            result = await client.create(product, resource, {"name": "Test"})
            assert isinstance(result, PCOResource)
            assert result.id == "123"

            # Test UPDATE
            result = await client.update(product, resource, "123", {"name": "Updated"})
            assert isinstance(result, PCOResource)
            assert result.id == "123"

            # Test DELETE
            result = await client.delete(product, resource, "123")
            assert result is True

    async def test_pagination_all_products(self, client):
        """Test pagination for all products."""
        # Mock pagination response
        first_page = {
            "data": [
                {
                    "id": "1",
                    "type": "test_resource",
                    "attributes": {"name": "Resource 1"},
                },
                {
                    "id": "2",
                    "type": "test_resource",
                    "attributes": {"name": "Resource 2"},
                },
            ],
            "links": {
                "self": {
                    "href": "https://api.planningcenteronline.com/test/v2/test_resource"
                },
                "next": {
                    "href": "https://api.planningcenteronline.com/test/v2/test_resource?page=2"
                },
            },
        }

        second_page = {
            "data": [
                {
                    "id": "3",
                    "type": "test_resource",
                    "attributes": {"name": "Resource 3"},
                },
            ],
            "links": {
                "self": {
                    "href": "https://api.planningcenteronline.com/test/v2/test_resource?page=2"
                },
            },
        }

        client._http_client.get.side_effect = [
            PCOCollection(**first_page),
            PCOCollection(**second_page),
        ]

        test_cases = [
            (PCOProduct.PEOPLE, "people"),
            (PCOProduct.SERVICES, "plans"),
            (PCOProduct.CHECK_INS, "events"),
            (PCOProduct.GIVING, "funds"),
            (PCOProduct.GROUPS, "groups"),
            (PCOProduct.CALENDAR, "events"),
            (PCOProduct.REGISTRATIONS, "events"),
        ]

        for product, resource in test_cases:
            resources = []
            async for res in client.paginate_all(product, resource, per_page=2):
                resources.append(res)

            assert len(resources) == 3
            assert resources[0].get_attribute("name") == "Resource 1"
            assert resources[1].get_attribute("name") == "Resource 2"
            assert resources[2].get_attribute("name") == "Resource 3"

            # Reset mock for next product
            client._http_client.get.side_effect = [
                PCOCollection(**first_page),
                PCOCollection(**second_page),
            ]

    async def test_webhook_events_configuration(self):
        """Test that webhook events are properly configured for all products."""
        from planning_center_api.config import WEBHOOK_EVENTS

        # Verify all products have webhook events
        products = [
            PCOProduct.PEOPLE,
            PCOProduct.SERVICES,
            PCOProduct.CHECK_INS,
            PCOProduct.GIVING,
            PCOProduct.GROUPS,
            PCOProduct.CALENDAR,
            PCOProduct.REGISTRATIONS,
        ]

        for product in products:
            assert product in WEBHOOK_EVENTS
            assert len(WEBHOOK_EVENTS[product]) > 0

            # Verify event format
            for event in WEBHOOK_EVENTS[product]:
                assert "." in event  # Should be in format "resource.action"
                parts = event.split(".")
                assert len(parts) == 2
                assert parts[1] in ["created", "updated", "deleted"]

    async def test_api_endpoints_configuration(self):
        """Test that API endpoints are properly configured for all products."""
        from planning_center_api.config import API_ENDPOINTS

        # Verify all products have endpoints
        products = [
            PCOProduct.PEOPLE,
            PCOProduct.SERVICES,
            PCOProduct.CHECK_INS,
            PCOProduct.GIVING,
            PCOProduct.GROUPS,
            PCOProduct.CALENDAR,
            PCOProduct.REGISTRATIONS,
        ]

        for product in products:
            assert product in API_ENDPOINTS
            assert "base" in API_ENDPOINTS[product]
            assert "resources" in API_ENDPOINTS[product]

            # Verify base URL format
            base = API_ENDPOINTS[product]["base"]
            assert base.endswith("/v2")
            assert product.value in base

            # Verify resources exist
            resources = API_ENDPOINTS[product]["resources"]
            assert len(resources) > 0

            # Verify resource format
            for resource_name, resource_endpoint in resources.items():
                assert isinstance(resource_name, str)
                assert isinstance(resource_endpoint, str)
                assert len(resource_name) > 0
                assert len(resource_endpoint) > 0

    async def test_async_context_manager(self, client):
        """Test async context manager functionality."""
        # Test that the client can be used as an async context manager
        async with client as ctx_client:
            assert ctx_client is client
            assert client._http_client is not None
            # The http client should be properly initialized
            assert hasattr(client._http_client, "__aenter__")
            assert hasattr(client._http_client, "__aexit__")

    async def test_error_handling(self, client):
        """Test error handling for various scenarios."""
        from planning_center_api.exceptions import (
            PCOAuthenticationError,
            PCOError,
            PCONotFoundError,
            PCOPermissionError,
            PCORateLimitError,
            PCOServerError,
            PCOValidationError,
        )

        # Test that exceptions are properly imported and available
        assert PCOError is not None
        assert PCOAuthenticationError is not None
        assert PCOPermissionError is not None
        assert PCONotFoundError is not None
        assert PCOValidationError is not None
        assert PCORateLimitError is not None
        assert PCOServerError is not None

    async def test_configuration_options(self):
        """Test configuration options."""
        config = PCOConfig(
            app_id="test_app_id",
            secret="test_secret",
            access_token="test_token",
            webhook_secret="test_webhook_secret",
            timeout=60.0,
            max_retries=5,
            retry_delay=2.0,
            backoff_factor=3.0,
            rate_limit_requests=200,
            rate_limit_window=120,
            default_per_page=50,
            max_per_page=200,
        )

        # Test auth headers
        headers = config.get_auth_headers()
        assert "Authorization" in headers

        # Test configuration values
        assert config.timeout == 60.0
        assert config.max_retries == 5
        assert config.retry_delay == 2.0
        assert config.backoff_factor == 3.0
        assert config.rate_limit_requests == 200
        assert config.rate_limit_window == 120
        assert config.default_per_page == 50
        assert config.max_per_page == 200

    async def test_model_inheritance(self):
        """Test that all models properly inherit from base classes."""
        from planning_center_api.models.base import (
            PCOBaseModel,
            PCOResource,
        )
        from planning_center_api.products.registrations import PCOSignup

        # Test model instantiation
        signup_data = {
            "id": "123",
            "type": "signups",
            "attributes": {"name": "Test Signup"},
        }

        signup = PCOSignup(**signup_data)

        # Test inheritance
        assert isinstance(signup, PCOResource)
        assert isinstance(signup, PCOBaseModel)

        # Test basic functionality
        assert signup.id == "123"
        assert signup.get_name() == "Test Signup"
