"""Check-Ins product models for Planning Center API."""

from datetime import datetime

from ..models.base import PCOResource


class PCOEvent(PCOResource):
    """Represents an event in Planning Center Check-Ins."""

    def get_name(self) -> str | None:
        """Get the event name."""
        return self.get_attribute("name")

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


class PCOLocation(PCOResource):
    """Represents a location in Planning Center Check-Ins."""

    def get_name(self) -> str | None:
        """Get the location name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the location description."""
        return self.get_attribute("description")

    def get_address(self) -> str | None:
        """Get the location address."""
        return self.get_attribute("address")

    def get_city(self) -> str | None:
        """Get the location city."""
        return self.get_attribute("city")

    def get_state(self) -> str | None:
        """Get the location state."""
        return self.get_attribute("state")

    def get_zip(self) -> str | None:
        """Get the location ZIP code."""
        return self.get_attribute("zip")

    def get_country(self) -> str | None:
        """Get the location country."""
        return self.get_attribute("country")

    def get_created_at(self) -> datetime | None:
        """Get the location creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the location last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOStation(PCOResource):
    """Represents a station in Planning Center Check-Ins."""

    def get_name(self) -> str | None:
        """Get the station name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the station description."""
        return self.get_attribute("description")

    def get_created_at(self) -> datetime | None:
        """Get the station creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the station last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_location_id(self) -> str | None:
        """Get the location ID."""
        location_data = self.get_relationship_data("location")
        if location_data and isinstance(location_data, dict):
            return location_data.get("id")
        return None


class PCOCheckIn(PCOResource):
    """Represents a check-in in Planning Center Check-Ins."""

    def get_created_at(self) -> datetime | None:
        """Get the check-in creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the check-in last update time."""
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

    def get_location_id(self) -> str | None:
        """Get the location ID."""
        location_data = self.get_relationship_data("location")
        if location_data and isinstance(location_data, dict):
            return location_data.get("id")
        return None

    def get_station_id(self) -> str | None:
        """Get the station ID."""
        station_data = self.get_relationship_data("station")
        if station_data and isinstance(station_data, dict):
            return station_data.get("id")
        return None


class PCOCheckInPerson(PCOResource):
    """Represents a check-in person in Planning Center Check-Ins."""

    def get_first_name(self) -> str | None:
        """Get the person's first name."""
        return self.get_attribute("first_name")

    def get_last_name(self) -> str | None:
        """Get the person's last name."""
        return self.get_attribute("last_name")

    def get_full_name(self) -> str:
        """Get the person's full name."""
        first = self.get_first_name() or ""
        last = self.get_last_name() or ""
        return f"{first} {last}".strip()

    def get_birthdate(self) -> datetime | None:
        """Get the person's birthdate."""
        birthdate = self.get_attribute("birthdate")
        if birthdate:
            return datetime.fromisoformat(birthdate.replace("Z", "+00:00"))
        return None

    def get_created_at(self) -> datetime | None:
        """Get the person creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the person last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOCheckInHousehold(PCOResource):
    """Represents a check-in household in Planning Center Check-Ins."""

    def get_name(self) -> str | None:
        """Get the household name."""
        return self.get_attribute("name")

    def get_created_at(self) -> datetime | None:
        """Get the household creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the household last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None
