"""Organization-related models for Planning Center API."""

from datetime import datetime
from typing import Any

from ..models.base import PCOResource


class PCOConnectedApplication(PCOResource):
    """Represents a connected application in Planning Center."""

    def get_name(self) -> str | None:
        """Get the application name."""
        return self.get_attribute("name")

    def get_url(self) -> str | None:
        """Get the application URL."""
        return self.get_attribute("url")

    def get_description(self) -> str | None:
        """Get the application description."""
        return self.get_attribute("description")


class PCOConnectedApplicationPerson(PCOResource):
    """Represents a person connected to an application."""

    def get_first_name(self) -> str | None:
        """Get the person's first name."""
        return self.get_attribute("first_name")

    def get_last_name(self) -> str | None:
        """Get the person's last name."""
        return self.get_attribute("last_name")

    def get_full_name(self) -> str:
        """Get the person's full name."""
        first_name = self.get_first_name() or ""
        last_name = self.get_last_name() or ""
        return f"{first_name} {last_name}".strip()

    def get_avatar_url(self) -> str | None:
        """Get the person's avatar URL."""
        return self.get_attribute("avatar_url")

    def get_connected_at(self) -> datetime | None:
        """Get when the person connected to the application."""
        connected_at = self.get_attribute("connected_at")
        if connected_at and isinstance(connected_at, str):
            try:
                return datetime.fromisoformat(connected_at.replace("Z", "+00:00"))
            except ValueError:
                return None
        return connected_at


class PCOOauthApplication(PCOResource):
    """Represents an OAuth application in Planning Center."""

    def get_name(self) -> str | None:
        """Get the application name."""
        return self.get_attribute("name")

    def get_url(self) -> str | None:
        """Get the application URL."""
        return self.get_attribute("url")

    def get_description(self) -> str | None:
        """Get the application description."""
        return self.get_attribute("description")


class PCOOauthApplicationMau(PCOResource):
    """Represents monthly active users for an OAuth application."""

    def get_count(self) -> int | None:
        """Get the total number of unique active users."""
        return self.get_attribute("count")

    def get_month(self) -> int | None:
        """Get the month the stat was recorded for (1-12)."""
        return self.get_attribute("month")

    def get_year(self) -> int | None:
        """Get the year the stat was recorded for."""
        return self.get_attribute("year")

    def get_oauth_application_id(self) -> str | None:
        """Get the OAuth application ID from relationships."""
        if not self.relationships:
            return None
        relationship = getattr(self.relationships, "oauth_application", None)
        if relationship and isinstance(relationship, dict) and "data" in relationship:
            return relationship["data"].get("id")
        return None


class PCOOrganization(PCOResource):
    """Represents an organization in Planning Center."""

    def get_connected_applications(self) -> list[dict[str, Any]] | None:
        """Get connected applications relationship data."""
        if not self.relationships:
            return None
        relationship = getattr(self.relationships, "connected_applications", None)
        if relationship and isinstance(relationship, dict) and "data" in relationship:
            return relationship["data"]
        return None

    def get_oauth_applications(self) -> list[dict[str, Any]] | None:
        """Get OAuth applications relationship data."""
        if not self.relationships:
            return None
        relationship = getattr(self.relationships, "oauth_applications", None)
        if relationship and isinstance(relationship, dict) and "data" in relationship:
            return relationship["data"]
        return None

    def get_personal_access_tokens(self) -> list[dict[str, Any]] | None:
        """Get personal access tokens relationship data."""
        if not self.relationships:
            return None
        relationship = getattr(self.relationships, "personal_access_tokens", None)
        if relationship and isinstance(relationship, dict) and "data" in relationship:
            return relationship["data"]
        return None


class PCOOrganizationPerson(PCOResource):
    """Represents a person in Planning Center (organization context)."""

    def get_first_name(self) -> str | None:
        """Get the person's first name."""
        return self.get_attribute("first_name")

    def get_last_name(self) -> str | None:
        """Get the person's last name."""
        return self.get_attribute("last_name")

    def get_full_name(self) -> str:
        """Get the person's full name."""
        first_name = self.get_first_name() or ""
        last_name = self.get_last_name() or ""
        return f"{first_name} {last_name}".strip()


class PCOPersonalAccessToken(PCOResource):
    """Represents a personal access token in Planning Center."""

    def get_name(self) -> str | None:
        """Get the token name."""
        return self.get_attribute("name")
