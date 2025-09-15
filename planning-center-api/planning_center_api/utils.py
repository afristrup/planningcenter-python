"""Utility functions for Planning Center API."""

import asyncio
from collections.abc import Callable
from datetime import datetime
from decimal import Decimal
from typing import Any

from .client import PCOClient
from .config import PCOProduct
from .models.base import PCOResource


class PCOBatchProcessor:
    """Utility for processing large datasets in batches."""

    def __init__(self, client: PCOClient, batch_size: int = 100):
        """Initialize batch processor.

        Args:
            client: Planning Center client
            batch_size: Number of items to process per batch
        """
        self.client = client
        self.batch_size = batch_size

    async def process_people_batch(
        self,
        filter_params: dict[str, Any] | None = None,
        include: list[str] | None = None,
        processor: Callable | None = None,
    ) -> list[Any]:
        """Process people in batches.

        Args:
            filter_params: Filter parameters
            include: Related resources to include
            processor: Function to process each person

        Returns:
            List of processed results
        """
        results = []
        async for person in self.client.paginate_all(
            product=PCOProduct.PEOPLE,
            resource="people",
            per_page=self.batch_size,
            include=include,
            filter_params=filter_params,
        ):
            if processor:
                result = (
                    await processor(person)
                    if asyncio.iscoroutinefunction(processor)
                    else processor(person)
                )
                results.append(result)
            else:
                results.append(person)

        return results

    async def process_services_batch(
        self,
        filter_params: dict[str, Any] | None = None,
        include: list[str] | None = None,
        processor: Callable | None = None,
    ) -> list[Any]:
        """Process services in batches.

        Args:
            filter_params: Filter parameters
            include: Related resources to include
            processor: Function to process each service

        Returns:
            List of processed results
        """
        results = []
        async for service in self.client.paginate_all(
            product=PCOProduct.SERVICES,
            resource="services",
            per_page=self.batch_size,
            include=include,
            filter_params=filter_params,
        ):
            if processor:
                result = (
                    await processor(service)
                    if asyncio.iscoroutinefunction(processor)
                    else processor(service)
                )
                results.append(result)
            else:
                results.append(service)

        return results


class PCODataExporter:
    """Utility for exporting data from Planning Center."""

    def __init__(self, client: PCOClient):
        """Initialize data exporter.

        Args:
            client: Planning Center client
        """
        self.client = client

    async def export_people_to_dict(
        self,
        filter_params: dict[str, Any] | None = None,
        include: list[str] | None = None,
    ) -> list[dict[str, Any]]:
        """Export people data to list of dictionaries.

        Args:
            filter_params: Filter parameters
            include: Related resources to include

        Returns:
            List of people as dictionaries
        """
        people = []
        async for person in self.client.paginate_all(
            product=PCOProduct.PEOPLE,
            resource="people",
            include=include,
            filter_params=filter_params,
        ):
            people.append(person.model_dump())

        return people

    async def export_services_to_dict(
        self,
        filter_params: dict[str, Any] | None = None,
        include: list[str] | None = None,
    ) -> list[dict[str, Any]]:
        """Export services data to list of dictionaries.

        Args:
            filter_params: Filter parameters
            include: Related resources to include

        Returns:
            List of services as dictionaries
        """
        services = []
        async for service in self.client.paginate_all(
            product=PCOProduct.SERVICES,
            resource="services",
            include=include,
            filter_params=filter_params,
        ):
            services.append(service.model_dump())

        return services


class PCODataValidator:
    """Utility for validating data before sending to Planning Center."""

    @staticmethod
    def validate_person_data(data: dict[str, Any]) -> list[str]:
        """Validate person data.

        Args:
            data: Person data to validate

        Returns:
            List of validation errors
        """
        errors = []

        # Check required fields
        if not data.get("first_name") and not data.get("last_name"):
            errors.append("Either first_name or last_name is required")

        # Validate email if provided
        email = data.get("email")
        if email and not _is_valid_email(email):
            errors.append("Invalid email format")

        # Validate phone if provided
        phone = data.get("phone")
        if phone and not _is_valid_phone(phone):
            errors.append("Invalid phone format")

        return errors

    @staticmethod
    def validate_service_data(data: dict[str, Any]) -> list[str]:
        """Validate service data.

        Args:
            data: Service data to validate

        Returns:
            List of validation errors
        """
        errors = []

        # Check required fields
        if not data.get("name"):
            errors.append("Service name is required")

        return errors


class PCODataTransformer:
    """Utility for transforming data between formats."""

    @staticmethod
    def person_to_contact_dict(person: PCOResource) -> dict[str, Any]:
        """Convert person to contact dictionary format.

        Args:
            person: Person resource

        Returns:
            Contact dictionary
        """
        return {
            "id": person.id,
            "name": f"{person.get_attribute('first_name', '')} {person.get_attribute('last_name', '')}".strip(),
            "email": person.get_attribute("email"),
            "phone": person.get_attribute("phone"),
            "created_at": person.get_attribute("created_at"),
            "updated_at": person.get_attribute("updated_at"),
        }

    @staticmethod
    def service_to_event_dict(service: PCOResource) -> dict[str, Any]:
        """Convert service to event dictionary format.

        Args:
            service: Service resource

        Returns:
            Event dictionary
        """
        return {
            "id": service.id,
            "title": service.get_attribute("name"),
            "description": service.get_attribute("description"),
            "start_time": service.get_attribute("start_time"),
            "end_time": service.get_attribute("end_time"),
            "created_at": service.get_attribute("created_at"),
            "updated_at": service.get_attribute("updated_at"),
        }


class PCODataAnalyzer:
    """Utility for analyzing Planning Center data."""

    def __init__(self, client: PCOClient):
        """Initialize data analyzer.

        Args:
            client: Planning Center client
        """
        self.client = client

    async def get_people_stats(self) -> dict[str, Any]:
        """Get people statistics.

        Returns:
            Dictionary with people statistics
        """
        active_count = 0
        inactive_count = 0
        total_count = 0

        async for person in self.client.paginate_all(
            product=PCOProduct.PEOPLE,
            resource="people",
        ):
            total_count += 1
            if person.get_attribute("status") == "active":
                active_count += 1
            else:
                inactive_count += 1

        return {
            "total_people": total_count,
            "active_people": active_count,
            "inactive_people": inactive_count,
            "active_percentage": (active_count / total_count * 100)
            if total_count > 0
            else 0,
        }

    async def get_services_stats(self) -> dict[str, Any]:
        """Get services statistics.

        Returns:
            Dictionary with services statistics
        """
        total_services = 0
        total_plans = 0

        async for _service in self.client.paginate_all(
            product=PCOProduct.SERVICES,
            resource="services",
        ):
            total_services += 1

        async for _plan in self.client.paginate_all(
            product=PCOProduct.SERVICES,
            resource="plans",
        ):
            total_plans += 1

        return {
            "total_services": total_services,
            "total_plans": total_plans,
            "plans_per_service": total_plans / total_services
            if total_services > 0
            else 0,
        }


def _is_valid_email(email: str) -> bool:
    """Check if email is valid."""
    import re

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def _is_valid_phone(phone: str) -> bool:
    """Check if phone number is valid."""
    import re

    # Remove all non-digit characters
    digits = re.sub(r"\D", "", phone)
    # Check if it's a valid length (7-15 digits)
    return 7 <= len(digits) <= 15


def format_currency(amount: Decimal | float | int | str) -> str:
    """Format amount as currency.

    Args:
        amount: Amount to format

    Returns:
        Formatted currency string
    """
    if isinstance(amount, str):
        amount = Decimal(amount)
    elif isinstance(amount, (int, float)):
        amount = Decimal(str(amount))

    return f"${amount:,.2f}"


def format_date(date: datetime | str) -> str:
    """Format date for display.

    Args:
        date: Date to format

    Returns:
        Formatted date string
    """
    if isinstance(date, str):
        date = datetime.fromisoformat(date.replace("Z", "+00:00"))

    return date.strftime("%Y-%m-%d %H:%M:%S")


def format_relative_date(date: datetime | str) -> str:
    """Format date as relative time.

    Args:
        date: Date to format

    Returns:
        Relative date string (e.g., "2 days ago")
    """
    if isinstance(date, str):
        date = datetime.fromisoformat(date.replace("Z", "+00:00"))

    now = datetime.now(date.tzinfo) if date.tzinfo else datetime.utcnow()
    diff = now - date

    if diff.days > 0:
        return f"{diff.days} day{'s' if diff.days != 1 else ''} ago"
    elif diff.seconds > 3600:
        hours = diff.seconds // 3600
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    elif diff.seconds > 60:
        minutes = diff.seconds // 60
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    else:
        return "Just now"


def chunk_list(items: list[Any], chunk_size: int) -> list[list[Any]]:
    """Split a list into chunks of specified size.

    Args:
        items: List to chunk
        chunk_size: Size of each chunk

    Returns:
        List of chunks
    """
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def merge_dicts(*dicts: dict[str, Any]) -> dict[str, Any]:
    """Merge multiple dictionaries.

    Args:
        *dicts: Dictionaries to merge

    Returns:
        Merged dictionary
    """
    result = {}
    for d in dicts:
        result.update(d)
    return result


def safe_get(data: dict[str, Any], key: str, default: Any = None) -> Any:
    """Safely get a value from a dictionary.

    Args:
        data: Dictionary to get value from
        key: Key to get (supports dot notation)
        default: Default value if key not found

    Returns:
        Value or default
    """
    keys = key.split(".")
    value = data

    for k in keys:
        if isinstance(value, dict) and k in value:
            value = value[k]
        else:
            return default

    return value


def deep_merge_dicts(dict1: dict[str, Any], dict2: dict[str, Any]) -> dict[str, Any]:
    """Deep merge two dictionaries.

    Args:
        dict1: First dictionary
        dict2: Second dictionary

    Returns:
        Deep merged dictionary
    """
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value

    return result
