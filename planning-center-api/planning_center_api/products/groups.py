"""Groups product models for Planning Center API."""

from datetime import datetime

from ..models.base import PCOResource


class PCOGroup(PCOResource):
    """Represents a group in Planning Center Groups."""

    def get_name(self) -> str | None:
        """Get the group name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the group description."""
        return self.get_attribute("description")

    def get_created_at(self) -> datetime | None:
        """Get the group creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the group last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_group_type_id(self) -> str | None:
        """Get the group type ID."""
        group_type_data = self.get_relationship_data("group_type")
        if group_type_data and isinstance(group_type_data, dict):
            return group_type_data.get("id")
        return None


class PCOGroupType(PCOResource):
    """Represents a group type in Planning Center Groups."""

    def get_name(self) -> str | None:
        """Get the group type name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the group type description."""
        return self.get_attribute("description")

    def get_created_at(self) -> datetime | None:
        """Get the group type creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the group type last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOGroupTime(PCOResource):
    """Represents a group time in Planning Center Groups."""

    def get_starts_at(self) -> datetime | None:
        """Get the group time start."""
        starts_at = self.get_attribute("starts_at")
        if starts_at:
            return datetime.fromisoformat(starts_at.replace("Z", "+00:00"))
        return None

    def get_ends_at(self) -> datetime | None:
        """Get the group time end."""
        ends_at = self.get_attribute("ends_at")
        if ends_at:
            return datetime.fromisoformat(ends_at.replace("Z", "+00:00"))
        return None

    def get_created_at(self) -> datetime | None:
        """Get the group time creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the group time last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_group_id(self) -> str | None:
        """Get the group ID."""
        group_data = self.get_relationship_data("group")
        if group_data and isinstance(group_data, dict):
            return group_data.get("id")
        return None


class PCOGroupMembership(PCOResource):
    """Represents a group membership in Planning Center Groups."""

    def get_role(self) -> str | None:
        """Get the membership role."""
        return self.get_attribute("role")

    def get_created_at(self) -> datetime | None:
        """Get the membership creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the membership last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_group_id(self) -> str | None:
        """Get the group ID."""
        group_data = self.get_relationship_data("group")
        if group_data and isinstance(group_data, dict):
            return group_data.get("id")
        return None

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCOGroupNote(PCOResource):
    """Represents a group note in Planning Center Groups."""

    def get_content(self) -> str | None:
        """Get the group note content."""
        return self.get_attribute("content")

    def get_created_at(self) -> datetime | None:
        """Get the group note creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the group note last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_group_id(self) -> str | None:
        """Get the group ID."""
        group_data = self.get_relationship_data("group")
        if group_data and isinstance(group_data, dict):
            return group_data.get("id")
        return None
