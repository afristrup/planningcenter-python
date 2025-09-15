"""Calendar product models for Planning Center API."""

from datetime import datetime

from ..models.base import PCOResource


class PCOCalendarEvent(PCOResource):
    """Represents a calendar event in Planning Center Calendar."""

    def get_title(self) -> str | None:
        """Get the event title."""
        return self.get_attribute("title")

    def get_description(self) -> str | None:
        """Get the event description."""
        return self.get_attribute("description")

    def get_start_time(self) -> datetime | None:
        """Get the event start time."""
        start_time = self.get_attribute("start_time")
        if start_time:
            return datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        return None

    def get_end_time(self) -> datetime | None:
        """Get the event end time."""
        end_time = self.get_attribute("end_time")
        if end_time:
            return datetime.fromisoformat(end_time.replace("Z", "+00:00"))
        return None

    def get_created_at(self) -> datetime | None:
        """Get the event creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the event last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOEventInstance(PCOResource):
    """Represents an event instance in Planning Center Calendar."""

    def get_starts_at(self) -> datetime | None:
        """Get the event instance start time."""
        starts_at = self.get_attribute("starts_at")
        if starts_at:
            return datetime.fromisoformat(starts_at.replace("Z", "+00:00"))
        return None

    def get_ends_at(self) -> datetime | None:
        """Get the event instance end time."""
        ends_at = self.get_attribute("ends_at")
        if ends_at:
            return datetime.fromisoformat(ends_at.replace("Z", "+00:00"))
        return None

    def get_created_at(self) -> datetime | None:
        """Get the event instance creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the event instance last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_event_id(self) -> str | None:
        """Get the event ID."""
        event_data = self.get_relationship_data("event")
        if event_data and isinstance(event_data, dict):
            return event_data.get("id")
        return None


class PCOEventTime(PCOResource):
    """Represents an event time in Planning Center Calendar."""

    def get_starts_at(self) -> datetime | None:
        """Get the event time start."""
        starts_at = self.get_attribute("starts_at")
        if starts_at:
            return datetime.fromisoformat(starts_at.replace("Z", "+00:00"))
        return None

    def get_ends_at(self) -> datetime | None:
        """Get the event time end."""
        ends_at = self.get_attribute("ends_at")
        if ends_at:
            return datetime.fromisoformat(ends_at.replace("Z", "+00:00"))
        return None

    def get_created_at(self) -> datetime | None:
        """Get the event time creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the event time last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_event_id(self) -> str | None:
        """Get the event ID."""
        event_data = self.get_relationship_data("event")
        if event_data and isinstance(event_data, dict):
            return event_data.get("id")
        return None


class PCOEventRsvp(PCOResource):
    """Represents an event RSVP in Planning Center Calendar."""

    def get_response(self) -> str | None:
        """Get the RSVP response."""
        return self.get_attribute("response")

    def get_created_at(self) -> datetime | None:
        """Get the RSVP creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the RSVP last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_event_id(self) -> str | None:
        """Get the event ID."""
        event_data = self.get_relationship_data("event")
        if event_data and isinstance(event_data, dict):
            return event_data.get("id")
        return None

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCOEventNote(PCOResource):
    """Represents an event note in Planning Center Calendar."""

    def get_content(self) -> str | None:
        """Get the event note content."""
        return self.get_attribute("content")

    def get_created_at(self) -> datetime | None:
        """Get the event note creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the event note last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_event_id(self) -> str | None:
        """Get the event ID."""
        event_data = self.get_relationship_data("event")
        if event_data and isinstance(event_data, dict):
            return event_data.get("id")
        return None


class PCOEventLabel(PCOResource):
    """Represents an event label in Planning Center Calendar."""

    def get_name(self) -> str | None:
        """Get the event label name."""
        return self.get_attribute("name")

    def get_color(self) -> str | None:
        """Get the event label color."""
        return self.get_attribute("color")

    def get_created_at(self) -> datetime | None:
        """Get the event label creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the event label last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOEventAttachment(PCOResource):
    """Represents an event attachment in Planning Center Calendar."""

    def get_filename(self) -> str | None:
        """Get the attachment filename."""
        return self.get_attribute("filename")

    def get_content_type(self) -> str | None:
        """Get the attachment content type."""
        return self.get_attribute("content_type")

    def get_file_size(self) -> int | None:
        """Get the attachment file size in bytes."""
        return self.get_attribute("file_size")

    def get_created_at(self) -> datetime | None:
        """Get the attachment creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the attachment last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_event_id(self) -> str | None:
        """Get the event ID."""
        event_data = self.get_relationship_data("event")
        if event_data and isinstance(event_data, dict):
            return event_data.get("id")
        return None
