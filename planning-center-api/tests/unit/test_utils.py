"""Unit tests for utility functions."""

from datetime import datetime, timedelta
from decimal import Decimal
from unittest.mock import Mock

import pytest

from planning_center_api.models.base import PCOResource
from planning_center_api.utils import (
    PCOBatchProcessor,
    PCODataAnalyzer,
    PCODataExporter,
    PCODataTransformer,
    PCODataValidator,
    chunk_list,
    deep_merge_dicts,
    format_currency,
    format_date,
    format_relative_date,
    merge_dicts,
    safe_get,
)


class TestPCOBatchProcessor:
    """Test PCOBatchProcessor class."""

    @pytest.fixture
    def mock_client(self):
        """Create mock client."""
        client = Mock()
        return client

    @pytest.fixture
    def processor(self, mock_client):
        """Create batch processor."""
        return PCOBatchProcessor(mock_client, batch_size=10)

    def test_init(self, processor, mock_client):
        """Test processor initialization."""
        assert processor.client == mock_client
        assert processor.batch_size == 10

    @pytest.mark.asyncio
    async def test_process_people_batch(self, processor):
        """Test processing people in batches."""
        # Mock paginate_all method
        mock_people = [
            PCOResource(id="1", type="people", attributes={"name": "John"}),
            PCOResource(id="2", type="people", attributes={"name": "Jane"}),
        ]

        async def mock_paginate_all(*args, **kwargs):
            for person in mock_people:
                yield person

        processor.client.paginate_all = mock_paginate_all

        # Test without processor function
        results = await processor.process_people_batch()

        assert len(results) == 2
        assert results[0].id == "1"
        assert results[1].id == "2"

    @pytest.mark.asyncio
    async def test_process_people_batch_with_processor(self, processor):
        """Test processing people with processor function."""
        mock_people = [
            PCOResource(id="1", type="people", attributes={"name": "John"}),
            PCOResource(id="2", type="people", attributes={"name": "Jane"}),
        ]

        async def mock_paginate_all(*args, **kwargs):
            for person in mock_people:
                yield person

        processor.client.paginate_all = mock_paginate_all

        # Test with processor function
        def process_person(person):
            return {"id": person.id, "name": person.get_attribute("name")}

        results = await processor.process_people_batch(processor=process_person)

        assert len(results) == 2
        assert results[0] == {"id": "1", "name": "John"}
        assert results[1] == {"id": "2", "name": "Jane"}

    @pytest.mark.asyncio
    async def test_process_people_batch_with_async_processor(self, processor):
        """Test processing people with async processor function."""
        mock_people = [
            PCOResource(id="1", type="people", attributes={"name": "John"}),
        ]

        async def mock_paginate_all(*args, **kwargs):
            for person in mock_people:
                yield person

        processor.client.paginate_all = mock_paginate_all

        # Test with async processor function
        async def async_process_person(person):
            return {"id": person.id, "name": person.get_attribute("name")}

        results = await processor.process_people_batch(processor=async_process_person)

        assert len(results) == 1
        assert results[0] == {"id": "1", "name": "John"}

    @pytest.mark.asyncio
    async def test_process_services_batch(self, processor):
        """Test processing services in batches."""
        mock_services = [
            PCOResource(id="1", type="services", attributes={"name": "Service 1"}),
            PCOResource(id="2", type="services", attributes={"name": "Service 2"}),
        ]

        async def mock_paginate_all(*args, **kwargs):
            for service in mock_services:
                yield service

        processor.client.paginate_all = mock_paginate_all

        results = await processor.process_services_batch()

        assert len(results) == 2
        assert results[0].id == "1"
        assert results[1].id == "2"


class TestPCODataExporter:
    """Test PCODataExporter class."""

    @pytest.fixture
    def mock_client(self):
        """Create mock client."""
        client = Mock()
        return client

    @pytest.fixture
    def exporter(self, mock_client):
        """Create data exporter."""
        return PCODataExporter(mock_client)

    @pytest.mark.asyncio
    async def test_export_people_to_dict(self, exporter):
        """Test exporting people to dictionary."""
        mock_people = [
            PCOResource(id="1", type="people", attributes={"name": "John"}),
            PCOResource(id="2", type="people", attributes={"name": "Jane"}),
        ]

        async def mock_paginate_all(*args, **kwargs):
            for person in mock_people:
                yield person

        exporter.client.paginate_all = mock_paginate_all

        results = await exporter.export_people_to_dict()

        assert len(results) == 2
        assert results[0]["id"] == "1"
        assert results[0]["type"] == "people"
        assert results[0]["attributes"]["name"] == "John"

    @pytest.mark.asyncio
    async def test_export_services_to_dict(self, exporter):
        """Test exporting services to dictionary."""
        mock_services = [
            PCOResource(id="1", type="services", attributes={"name": "Service 1"}),
        ]

        async def mock_paginate_all(*args, **kwargs):
            for service in mock_services:
                yield service

        exporter.client.paginate_all = mock_paginate_all

        results = await exporter.export_services_to_dict()

        assert len(results) == 1
        assert results[0]["id"] == "1"
        assert results[0]["type"] == "services"
        assert results[0]["attributes"]["name"] == "Service 1"


class TestPCODataAnalyzer:
    """Test PCODataAnalyzer class."""

    @pytest.fixture
    def mock_client(self):
        """Create mock client."""
        client = Mock()
        return client

    @pytest.fixture
    def analyzer(self, mock_client):
        """Create data analyzer."""
        return PCODataAnalyzer(mock_client)

    @pytest.mark.asyncio
    async def test_get_people_stats(self, analyzer):
        """Test getting people statistics."""
        mock_people = [
            PCOResource(id="1", type="people", attributes={"status": "active"}),
            PCOResource(id="2", type="people", attributes={"status": "active"}),
            PCOResource(id="3", type="people", attributes={"status": "inactive"}),
        ]

        async def mock_paginate_all(*args, **kwargs):
            for person in mock_people:
                yield person

        analyzer.client.paginate_all = mock_paginate_all

        stats = await analyzer.get_people_stats()

        assert stats["total_people"] == 3
        assert stats["active_people"] == 2
        assert stats["inactive_people"] == 1
        assert abs(stats["active_percentage"] - 66.66666666666667) < 0.0001

    @pytest.mark.asyncio
    async def test_get_services_stats(self, analyzer):
        """Test getting services statistics."""
        mock_services = [
            PCOResource(id="1", type="services", attributes={"name": "Service 1"}),
            PCOResource(id="2", type="services", attributes={"name": "Service 2"}),
        ]

        mock_plans = [
            PCOResource(id="1", type="plans", attributes={"title": "Plan 1"}),
            PCOResource(id="2", type="plans", attributes={"title": "Plan 2"}),
            PCOResource(id="3", type="plans", attributes={"title": "Plan 3"}),
        ]

        async def mock_paginate_all(*args, **kwargs):
            if kwargs.get("resource") == "services":
                for service in mock_services:
                    yield service
            elif kwargs.get("resource") == "plans":
                for plan in mock_plans:
                    yield plan

        analyzer.client.paginate_all = mock_paginate_all

        stats = await analyzer.get_services_stats()

        assert stats["total_services"] == 2
        assert stats["total_plans"] == 3
        assert stats["plans_per_service"] == 1.5


class TestPCODataValidator:
    """Test PCODataValidator class."""

    def test_validate_person_data_valid(self):
        """Test validating valid person data."""
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "phone": "555-123-4567",
        }

        errors = PCODataValidator.validate_person_data(data)

        assert len(errors) == 0

    def test_validate_person_data_missing_names(self):
        """Test validating person data with missing names."""
        data = {"email": "john@example.com"}

        errors = PCODataValidator.validate_person_data(data)

        assert len(errors) == 1
        assert "Either first_name or last_name is required" in errors

    def test_validate_person_data_invalid_email(self):
        """Test validating person data with invalid email."""
        data = {"first_name": "John", "email": "invalid-email"}

        errors = PCODataValidator.validate_person_data(data)

        assert len(errors) == 1
        assert "Invalid email format" in errors

    def test_validate_person_data_invalid_phone(self):
        """Test validating person data with invalid phone."""
        data = {
            "first_name": "John",
            "phone": "123",  # Too short
        }

        errors = PCODataValidator.validate_person_data(data)

        assert len(errors) == 1
        assert "Invalid phone format" in errors

    def test_validate_service_data_valid(self):
        """Test validating valid service data."""
        data = {"name": "Sunday Service"}

        errors = PCODataValidator.validate_service_data(data)

        assert len(errors) == 0

    def test_validate_service_data_missing_name(self):
        """Test validating service data with missing name."""
        data = {"description": "A service"}

        errors = PCODataValidator.validate_service_data(data)

        assert len(errors) == 1
        assert "Service name is required" in errors


class TestPCODataTransformer:
    """Test PCODataTransformer class."""

    def test_person_to_contact_dict(self):
        """Test converting person to contact dictionary."""
        person = PCOResource(
            id="123",
            type="people",
            attributes={
                "first_name": "John",
                "last_name": "Doe",
                "email": "john@example.com",
                "phone": "555-123-4567",
                "created_at": "2023-01-01T00:00:00Z",
                "updated_at": "2023-01-02T00:00:00Z",
            },
        )

        contact = PCODataTransformer.person_to_contact_dict(person)

        assert contact["id"] == "123"
        assert contact["name"] == "John Doe"
        assert contact["email"] == "john@example.com"
        assert contact["phone"] == "555-123-4567"
        assert contact["created_at"] == "2023-01-01T00:00:00Z"
        assert contact["updated_at"] == "2023-01-02T00:00:00Z"

    def test_service_to_event_dict(self):
        """Test converting service to event dictionary."""
        service = PCOResource(
            id="456",
            type="services",
            attributes={
                "name": "Sunday Service",
                "description": "Weekly service",
                "start_time": "2023-01-01T10:00:00Z",
                "end_time": "2023-01-01T11:00:00Z",
                "created_at": "2023-01-01T00:00:00Z",
                "updated_at": "2023-01-02T00:00:00Z",
            },
        )

        event = PCODataTransformer.service_to_event_dict(service)

        assert event["id"] == "456"
        assert event["title"] == "Sunday Service"
        assert event["description"] == "Weekly service"
        assert event["start_time"] == "2023-01-01T10:00:00Z"
        assert event["end_time"] == "2023-01-01T11:00:00Z"
        assert event["created_at"] == "2023-01-01T00:00:00Z"
        assert event["updated_at"] == "2023-01-02T00:00:00Z"


class TestUtilityFunctions:
    """Test utility functions."""

    def test_format_currency_decimal(self):
        """Test formatting currency with Decimal."""
        amount = Decimal("1234.56")
        result = format_currency(amount)
        assert result == "$1,234.56"

    def test_format_currency_float(self):
        """Test formatting currency with float."""
        amount = 1234.56
        result = format_currency(amount)
        assert result == "$1,234.56"

    def test_format_currency_int(self):
        """Test formatting currency with int."""
        amount = 1234
        result = format_currency(amount)
        assert result == "$1,234.00"

    def test_format_currency_string(self):
        """Test formatting currency with string."""
        amount = "1234.56"
        result = format_currency(amount)
        assert result == "$1,234.56"

    def test_format_date_datetime(self):
        """Test formatting date with datetime object."""
        date = datetime(2023, 1, 1, 12, 30, 45)
        result = format_date(date)
        assert result == "2023-01-01 12:30:45"

    def test_format_date_string(self):
        """Test formatting date with string."""
        date = "2023-01-01T12:30:45Z"
        result = format_date(date)
        assert result == "2023-01-01 12:30:45"

    def test_format_relative_date_recent(self):
        """Test formatting relative date for recent time."""
        now = datetime.utcnow()
        recent = now - timedelta(minutes=5)
        result = format_relative_date(recent)
        assert result == "5 minutes ago"

    def test_format_relative_date_hours(self):
        """Test formatting relative date for hours ago."""
        now = datetime.utcnow()
        hours_ago = now - timedelta(hours=2)
        result = format_relative_date(hours_ago)
        assert result == "2 hours ago"

    def test_format_relative_date_days(self):
        """Test formatting relative date for days ago."""
        now = datetime.utcnow()
        days_ago = now - timedelta(days=3)
        result = format_relative_date(days_ago)
        assert result == "3 days ago"

    def test_format_relative_date_just_now(self):
        """Test formatting relative date for just now."""
        now = datetime.utcnow()
        just_now = now - timedelta(seconds=30)
        result = format_relative_date(just_now)
        assert result == "Just now"

    def test_format_relative_date_string(self):
        """Test formatting relative date with string."""
        date = "2023-01-01T12:30:45Z"
        result = format_relative_date(date)
        # Should return a relative time string
        assert isinstance(result, str)
        assert "ago" in result or "Just now" in result

    def test_chunk_list(self):
        """Test chunking a list."""
        items = list(range(10))
        chunks = chunk_list(items, 3)

        assert len(chunks) == 4
        assert chunks[0] == [0, 1, 2]
        assert chunks[1] == [3, 4, 5]
        assert chunks[2] == [6, 7, 8]
        assert chunks[3] == [9]

    def test_chunk_list_empty(self):
        """Test chunking an empty list."""
        chunks = chunk_list([], 3)
        assert chunks == []

    def test_merge_dicts(self):
        """Test merging dictionaries."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        dict3 = {"e": 5}

        result = merge_dicts(dict1, dict2, dict3)

        assert result == {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

    def test_merge_dicts_overlap(self):
        """Test merging dictionaries with overlapping keys."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"b": 3, "c": 4}  # b overlaps

        result = merge_dicts(dict1, dict2)

        assert result == {"a": 1, "b": 3, "c": 4}  # Later dict wins

    def test_safe_get_simple_key(self):
        """Test safe_get with simple key."""
        data = {"name": "John", "age": 30}

        assert safe_get(data, "name") == "John"
        assert safe_get(data, "age") == 30
        assert safe_get(data, "email") is None
        assert safe_get(data, "email", "default") == "default"

    def test_safe_get_nested_key(self):
        """Test safe_get with nested key."""
        data = {"person": {"name": "John", "address": {"city": "New York"}}}

        assert safe_get(data, "person.name") == "John"
        assert safe_get(data, "person.address.city") == "New York"
        assert safe_get(data, "person.address.zip") is None
        assert safe_get(data, "person.address.zip", "12345") == "12345"

    def test_safe_get_missing_intermediate(self):
        """Test safe_get with missing intermediate key."""
        data = {"person": {"name": "John"}}

        assert safe_get(data, "person.address.city") is None
        assert safe_get(data, "person.address.city", "default") == "default"

    def test_deep_merge_dicts(self):
        """Test deep merging dictionaries."""
        dict1 = {"person": {"name": "John", "age": 30}, "settings": {"theme": "dark"}}

        dict2 = {
            "person": {"age": 31, "email": "john@example.com"},
            "settings": {"language": "en"},
        }

        result = deep_merge_dicts(dict1, dict2)

        expected = {
            "person": {"name": "John", "age": 31, "email": "john@example.com"},
            "settings": {"theme": "dark", "language": "en"},
        }

        assert result == expected

    def test_deep_merge_dicts_non_dict_values(self):
        """Test deep merging with non-dict values."""
        dict1 = {"a": 1, "b": {"c": 2}}
        dict2 = {"a": 3, "b": {"d": 4}}

        result = deep_merge_dicts(dict1, dict2)

        assert result == {"a": 3, "b": {"c": 2, "d": 4}}
