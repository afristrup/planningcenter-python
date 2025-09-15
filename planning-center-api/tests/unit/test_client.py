"""Unit tests for PCOClient."""

from unittest.mock import AsyncMock, patch

import pytest

from planning_center_api import PCOClient, PCOProduct
from planning_center_api.config import PCOConfig
from planning_center_api.models.base import PCOCollection, PCOResource


class TestPCOClient:
    """Test PCOClient class."""

    @pytest.fixture
    def config(self):
        """Create test configuration."""
        return PCOConfig(
            app_id="test_app_id", secret="test_secret", access_token="test_token"
        )

    @pytest.fixture
    def client(self, config):
        """Create test client."""
        return PCOClient(config=config)

    def test_init_with_credentials(self):
        """Test client initialization with credentials."""
        client = PCOClient(app_id="test_app_id", secret="test_secret")

        assert client.config.app_id == "test_app_id"
        assert client.config.secret == "test_secret"

    def test_init_with_access_token(self):
        """Test client initialization with access token."""
        client = PCOClient(access_token="test_token")

        assert client.config.access_token == "test_token"

    def test_init_with_config(self):
        """Test client initialization with config object."""
        config = PCOConfig(app_id="test_app_id", secret="test_secret")
        client = PCOClient(config=config)

        assert client.config == config

    def test_get_product_base(self, client):
        """Test getting product base path."""
        base = client._get_product_base(PCOProduct.PEOPLE)
        assert base == "people/v2"

        base = client._get_product_base(PCOProduct.SERVICES)
        assert base == "services/v2"

    def test_get_resource_endpoint(self, client):
        """Test getting resource endpoint."""
        endpoint = client._get_resource_endpoint(PCOProduct.PEOPLE, "people")
        assert endpoint == "people"

        endpoint = client._get_resource_endpoint(PCOProduct.PEOPLE, "emails")
        assert endpoint == "emails"

    def test_get_resource_endpoint_invalid(self, client):
        """Test getting invalid resource endpoint."""
        with pytest.raises(ValueError, match="Unknown resource"):
            client._get_resource_endpoint(PCOProduct.PEOPLE, "invalid_resource")

    @pytest.mark.asyncio
    async def test_context_manager(self, client):
        """Test async context manager."""
        with patch("planning_center_api.client.PCOHttpClient") as mock_http_client:
            mock_client_instance = AsyncMock()
            mock_http_client.return_value = mock_client_instance

            async with client:
                assert client._http_client == mock_client_instance
                mock_client_instance.__aenter__.assert_called_once()

            mock_client_instance.__aexit__.assert_called_once()

    @pytest.mark.asyncio
    async def test_ensure_client_not_initialized(self, client):
        """Test ensure_client when not initialized."""
        with pytest.raises(RuntimeError, match="Client not initialized"):
            client._ensure_client()

    @pytest.mark.asyncio
    async def test_get_single_resource(self, client):
        """Test getting a single resource."""
        mock_resource = PCOResource(
            id="123", type="people", attributes={"first_name": "John"}
        )

        with patch.object(client, "_ensure_client") as mock_ensure_client:
            mock_http_client = AsyncMock()
            mock_http_client.get = AsyncMock(return_value=mock_resource)
            mock_ensure_client.return_value = mock_http_client

            result = await client.get(
                product=PCOProduct.PEOPLE, resource="people", resource_id="123"
            )

            assert result == mock_resource
            mock_http_client.get.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_collection(self, client):
        """Test getting a collection."""
        mock_collection = PCOCollection(
            data=[
                PCOResource(id="1", type="people", attributes={"name": "John"}),
                PCOResource(id="2", type="people", attributes={"name": "Jane"}),
            ]
        )

        with patch.object(client, "_ensure_client") as mock_ensure_client:
            mock_http_client = AsyncMock()
            mock_http_client.get = AsyncMock(return_value=mock_collection)
            mock_ensure_client.return_value = mock_http_client

            result = await client.get(product=PCOProduct.PEOPLE, resource="people")

            assert result == mock_collection
            mock_http_client.get.assert_called_once()

    @pytest.mark.asyncio
    async def test_create_resource(self, client):
        """Test creating a resource."""
        mock_resource = PCOResource(
            id="123", type="people", attributes={"first_name": "John"}
        )

        with patch.object(client, "_ensure_client") as mock_ensure_client:
            mock_http_client = AsyncMock()
            mock_http_client.post = AsyncMock(return_value=mock_resource)
            mock_ensure_client.return_value = mock_http_client

            result = await client.create(
                product=PCOProduct.PEOPLE,
                resource="people",
                data={"first_name": "John"},
            )

            assert result == mock_resource
            mock_http_client.post.assert_called_once()

    @pytest.mark.asyncio
    async def test_update_resource(self, client):
        """Test updating a resource."""
        mock_resource = PCOResource(
            id="123",
            type="people",
            attributes={"first_name": "John", "last_name": "Doe"},
        )

        with patch.object(client, "_ensure_client") as mock_ensure_client:
            mock_http_client = AsyncMock()
            mock_http_client.patch = AsyncMock(return_value=mock_resource)
            mock_ensure_client.return_value = mock_http_client

            result = await client.update(
                product=PCOProduct.PEOPLE,
                resource="people",
                resource_id="123",
                data={"last_name": "Doe"},
            )

            assert result == mock_resource
            mock_http_client.patch.assert_called_once()

    @pytest.mark.asyncio
    async def test_delete_resource(self, client):
        """Test deleting a resource."""
        with patch.object(client, "_ensure_client") as mock_ensure_client:
            mock_http_client = AsyncMock()
            mock_http_client.delete = AsyncMock(return_value=True)
            mock_ensure_client.return_value = mock_http_client

            result = await client.delete(
                product=PCOProduct.PEOPLE, resource="people", resource_id="123"
            )

            assert result is True
            mock_http_client.delete.assert_called_once()

    @pytest.mark.asyncio
    async def test_paginate_all(self, client):
        """Test paginating through all resources."""
        from planning_center_api.models.links import PCOLink, PCOLinks

        mock_collection1 = PCOCollection(
            data=[
                PCOResource(id="1", type="people", attributes={"name": "John"}),
                PCOResource(id="2", type="people", attributes={"name": "Jane"}),
            ],
            links=PCOLinks(next=PCOLink(href="https://api.planningcenteronline.com/people/v2/people?page=2")),
        )

        mock_collection2 = PCOCollection(
            data=[PCOResource(id="3", type="people", attributes={"name": "Bob"})],
            links=PCOLinks(),
        )

        with patch.object(client, "_ensure_client") as mock_ensure_client:
            mock_http_client = AsyncMock()
            mock_http_client.get = AsyncMock(side_effect=[mock_collection1, mock_collection2])
            mock_ensure_client.return_value = mock_http_client

            results = []
            async for resource in client.paginate_all(
                product=PCOProduct.PEOPLE, resource="people", per_page=2
            ):
                results.append(resource)

            assert len(results) == 3
            assert results[0].id == "1"
            assert results[1].id == "2"
            assert results[2].id == "3"

    @pytest.mark.asyncio
    async def test_get_people(self, client):
        """Test getting people."""
        mock_collection = PCOCollection(
            data=[PCOResource(id="1", type="people", attributes={"name": "John"})]
        )

        with patch.object(client, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_collection

            result = await client.get_people(per_page=10)

            assert result == mock_collection
            mock_get.assert_called_once_with(
                product=PCOProduct.PEOPLE,
                resource="people",
                per_page=10,
                offset=None,
                include=None,
                filter_params=None,
                sort=None,
            )

    @pytest.mark.asyncio
    async def test_get_person(self, client):
        """Test getting a specific person."""
        mock_resource = PCOResource(
            id="123", type="people", attributes={"first_name": "John"}
        )

        with patch.object(client, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_resource

            result = await client.get_person("123", include=["emails"])

            assert result == mock_resource
            mock_get.assert_called_once_with(
                product=PCOProduct.PEOPLE,
                resource="people",
                resource_id="123",
                include=["emails"],
            )

    @pytest.mark.asyncio
    async def test_create_person(self, client):
        """Test creating a person."""
        mock_resource = PCOResource(
            id="123", type="people", attributes={"first_name": "John"}
        )

        with patch.object(client, "create") as mock_create:
            mock_create.return_value = mock_resource

            result = await client.create_person(
                {"first_name": "John"}, include=["emails"]
            )

            assert result == mock_resource
            mock_create.assert_called_once_with(
                product=PCOProduct.PEOPLE,
                resource="people",
                data={"first_name": "John"},
                include=["emails"],
            )

    @pytest.mark.asyncio
    async def test_update_person(self, client):
        """Test updating a person."""
        mock_resource = PCOResource(
            id="123",
            type="people",
            attributes={"first_name": "John", "last_name": "Doe"},
        )

        with patch.object(client, "update") as mock_update:
            mock_update.return_value = mock_resource

            result = await client.update_person(
                "123", {"last_name": "Doe"}, include=["emails"]
            )

            assert result == mock_resource
            mock_update.assert_called_once_with(
                product=PCOProduct.PEOPLE,
                resource="people",
                resource_id="123",
                data={"last_name": "Doe"},
                include=["emails"],
            )

    @pytest.mark.asyncio
    async def test_delete_person(self, client):
        """Test deleting a person."""
        with patch.object(client, "delete") as mock_delete:
            mock_delete.return_value = True

            result = await client.delete_person("123")

            assert result is True
            mock_delete.assert_called_once_with(
                product=PCOProduct.PEOPLE, resource="people", resource_id="123"
            )

    @pytest.mark.asyncio
    async def test_search_people(self, client):
        """Test searching for people."""
        mock_collection = PCOCollection(
            data=[PCOResource(id="1", type="people", attributes={"name": "John"})]
        )

        with patch.object(client, "get_people") as mock_get_people:
            mock_get_people.return_value = mock_collection

            result = await client.search_people("john", per_page=10)

            assert result == mock_collection
            mock_get_people.assert_called_once_with(
                per_page=10,
                include=None,
                filter_params={"search": "john"},
            )

    @pytest.mark.asyncio
    async def test_get_people_by_email(self, client):
        """Test getting people by email."""
        mock_collection = PCOCollection(
            data=[PCOResource(id="1", type="people", attributes={"name": "John"})]
        )

        with patch.object(client, "get_people") as mock_get_people:
            mock_get_people.return_value = mock_collection

            result = await client.get_people_by_email("john@example.com")

            assert result == mock_collection
            mock_get_people.assert_called_once_with(
                include=None,
                filter_params={"email": "john@example.com"},
            )

    @pytest.mark.asyncio
    async def test_get_people_by_phone(self, client):
        """Test getting people by phone."""
        mock_collection = PCOCollection(
            data=[PCOResource(id="1", type="people", attributes={"name": "John"})]
        )

        with patch.object(client, "get_people") as mock_get_people:
            mock_get_people.return_value = mock_collection

            result = await client.get_people_by_phone("555-123-4567")

            assert result == mock_collection
            mock_get_people.assert_called_once_with(
                include=None,
                filter_params={"phone": "555-123-4567"},
            )

    @pytest.mark.asyncio
    async def test_get_active_people(self, client):
        """Test getting active people."""
        mock_collection = PCOCollection(
            data=[PCOResource(id="1", type="people", attributes={"name": "John"})]
        )

        with patch.object(client, "get_people") as mock_get_people:
            mock_get_people.return_value = mock_collection

            result = await client.get_active_people(per_page=10)

            assert result == mock_collection
            mock_get_people.assert_called_once_with(
                per_page=10,
                include=None,
                filter_params={"status": "active"},
            )

    @pytest.mark.asyncio
    async def test_get_inactive_people(self, client):
        """Test getting inactive people."""
        mock_collection = PCOCollection(
            data=[PCOResource(id="1", type="people", attributes={"name": "John"})]
        )

        with patch.object(client, "get_people") as mock_get_people:
            mock_get_people.return_value = mock_collection

            result = await client.get_inactive_people(per_page=10)

            assert result == mock_collection
            mock_get_people.assert_called_once_with(
                per_page=10,
                include=None,
                filter_params={"status": "inactive"},
            )

    @pytest.mark.asyncio
    async def test_get_services(self, client):
        """Test getting services."""
        mock_collection = PCOCollection(
            data=[
                PCOResource(
                    id="1", type="services", attributes={"name": "Sunday Service"}
                )
            ]
        )

        with patch.object(client, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_collection

            result = await client.get_services(per_page=10)

            assert result == mock_collection
            mock_get.assert_called_once_with(
                product=PCOProduct.SERVICES,
                resource="services",
                per_page=10,
                offset=None,
                include=None,
                filter_params=None,
                sort=None,
            )

    @pytest.mark.asyncio
    async def test_get_service(self, client):
        """Test getting a specific service."""
        mock_resource = PCOResource(
            id="123", type="services", attributes={"name": "Sunday Service"}
        )

        with patch.object(client, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_resource

            result = await client.get_service("123", include=["plans"])

            assert result == mock_resource
            mock_get.assert_called_once_with(
                product=PCOProduct.SERVICES,
                resource="services",
                resource_id="123",
                include=["plans"],
            )

    @pytest.mark.asyncio
    async def test_get_plans_with_service_id(self, client):
        """Test getting plans for a specific service."""
        mock_collection = PCOCollection(
            data=[PCOResource(id="1", type="plans", attributes={"title": "Plan 1"})]
        )

        with patch.object(client, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_collection

            result = await client.get_plans(service_id="123", per_page=10)

            assert result == mock_collection
            mock_get.assert_called_once_with(
                product=PCOProduct.SERVICES,
                resource="plans",
                per_page=10,
                offset=None,
                include=None,
                filter_params={"service": "123"},
                sort=None,
            )

    @pytest.mark.asyncio
    async def test_get_plans_without_service_id(self, client):
        """Test getting all plans."""
        mock_collection = PCOCollection(
            data=[PCOResource(id="1", type="plans", attributes={"title": "Plan 1"})]
        )

        with patch.object(client, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_collection

            result = await client.get_plans(per_page=10)

            assert result == mock_collection
            mock_get.assert_called_once_with(
                product=PCOProduct.SERVICES,
                resource="plans",
                per_page=10,
                offset=None,
                include=None,
                filter_params=None,
                sort=None,
            )

    @pytest.mark.asyncio
    async def test_get_plan(self, client):
        """Test getting a specific plan."""
        mock_resource = PCOResource(
            id="123", type="plans", attributes={"title": "Plan 1"}
        )

        with patch.object(client, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_resource

            result = await client.get_plan("123", include=["songs"])

            assert result == mock_resource
            mock_get.assert_called_once_with(
                product=PCOProduct.SERVICES,
                resource="plans",
                resource_id="123",
                include=["songs"],
            )
