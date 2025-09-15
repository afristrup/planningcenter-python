"""Registrations product models for Planning Center API."""

from datetime import UTC, datetime
from typing import Any

from ..models.base import PCOResource


class PCORegistrationEvent(PCOResource):
    """Represents a registration event in Planning Center Registrations."""

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

    def get_registration_start_time(self) -> datetime | None:
        """Get the registration start time."""
        reg_start = self.get_attribute("registration_start_time")
        if reg_start:
            return datetime.fromisoformat(reg_start.replace("Z", "+00:00"))
        return None

    def get_registration_end_time(self) -> datetime | None:
        """Get the registration end time."""
        reg_end = self.get_attribute("registration_end_time")
        if reg_end:
            return datetime.fromisoformat(reg_end.replace("Z", "+00:00"))
        return None

    def get_capacity(self) -> int | None:
        """Get the event capacity."""
        return self.get_attribute("capacity")

    def get_registered_count(self) -> int:
        """Get the number of registered people."""
        return self.get_attribute("registered_count", 0)

    def get_available_spots(self) -> int | None:
        """Get the number of available spots."""
        capacity = self.get_capacity()
        if capacity is not None:
            return capacity - self.get_registered_count()
        return None

    def is_registration_open(self) -> bool:
        """Check if registration is currently open."""
        now = datetime.now(UTC)
        reg_start = self.get_registration_start_time()
        reg_end = self.get_registration_end_time()

        if reg_start and now < reg_start:
            return False
        if reg_end and now > reg_end:
            return False
        return True

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


class PCORegistrationEventInstance(PCOResource):
    """Represents a registration event instance in Planning Center Registrations."""

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

    def get_capacity(self) -> int | None:
        """Get the event instance capacity."""
        return self.get_attribute("capacity")

    def get_registered_count(self) -> int:
        """Get the number of registered people for this instance."""
        return self.get_attribute("registered_count", 0)

    def get_available_spots(self) -> int | None:
        """Get the number of available spots for this instance."""
        capacity = self.get_capacity()
        if capacity is not None:
            return capacity - self.get_registered_count()
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


class PCORegistrationEventTime(PCOResource):
    """Represents a registration event time in Planning Center Registrations."""

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


class PCORegistration(PCOResource):
    """Represents a registration in Planning Center Registrations."""

    def get_name(self) -> str | None:
        """Get the registration name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the registration description."""
        return self.get_attribute("description")

    def get_registration_start_time(self) -> datetime | None:
        """Get the registration start time."""
        reg_start = self.get_attribute("registration_start_time")
        if reg_start:
            return datetime.fromisoformat(reg_start.replace("Z", "+00:00"))
        return None

    def get_registration_end_time(self) -> datetime | None:
        """Get the registration end time."""
        reg_end = self.get_attribute("registration_end_time")
        if reg_end:
            return datetime.fromisoformat(reg_end.replace("Z", "+00:00"))
        return None

    def get_capacity(self) -> int | None:
        """Get the registration capacity."""
        return self.get_attribute("capacity")

    def get_registered_count(self) -> int:
        """Get the number of registered people."""
        return self.get_attribute("registered_count", 0)

    def get_available_spots(self) -> int | None:
        """Get the number of available spots."""
        capacity = self.get_capacity()
        if capacity is not None:
            return capacity - self.get_registered_count()
        return None

    def is_registration_open(self) -> bool:
        """Check if registration is currently open."""
        now = datetime.now(UTC)
        reg_start = self.get_registration_start_time()
        reg_end = self.get_registration_end_time()

        if reg_start and now < reg_start:
            return False
        if reg_end and now > reg_end:
            return False
        return True

    def get_created_at(self) -> datetime | None:
        """Get the registration creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the registration last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCORegistrationForm(PCOResource):
    """Represents a registration form in Planning Center Registrations."""

    def get_name(self) -> str | None:
        """Get the form name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the form description."""
        return self.get_attribute("description")

    def get_created_at(self) -> datetime | None:
        """Get the form creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the form last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_registration_id(self) -> str | None:
        """Get the registration ID."""
        registration_data = self.get_relationship_data("registration")
        if registration_data and isinstance(registration_data, dict):
            return registration_data.get("id")
        return None


class PCORegistrationFormField(PCOResource):
    """Represents a registration form field in Planning Center Registrations."""

    def get_name(self) -> str | None:
        """Get the field name."""
        return self.get_attribute("name")

    def get_field_type(self) -> str | None:
        """Get the field type."""
        return self.get_attribute("field_type")

    def get_required(self) -> bool:
        """Check if the field is required."""
        return self.get_attribute("required", False)

    def get_order(self) -> int:
        """Get the field order."""
        return self.get_attribute("order", 0)

    def get_created_at(self) -> datetime | None:
        """Get the field creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the field last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_form_id(self) -> str | None:
        """Get the form ID."""
        form_data = self.get_relationship_data("form")
        if form_data and isinstance(form_data, dict):
            return form_data.get("id")
        return None


class PCORegistrationFormFieldOption(PCOResource):
    """Represents a registration form field option in Planning Center Registrations."""

    def get_name(self) -> str | None:
        """Get the option name."""
        return self.get_attribute("name")

    def get_value(self) -> str | None:
        """Get the option value."""
        return self.get_attribute("value")

    def get_order(self) -> int:
        """Get the option order."""
        return self.get_attribute("order", 0)

    def get_created_at(self) -> datetime | None:
        """Get the option creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the option last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_field_id(self) -> str | None:
        """Get the field ID."""
        field_data = self.get_relationship_data("field")
        if field_data and isinstance(field_data, dict):
            return field_data.get("id")
        return None


class PCORegistrationInstance(PCOResource):
    """Represents a registration instance in Planning Center Registrations."""

    def get_starts_at(self) -> datetime | None:
        """Get the registration instance start time."""
        starts_at = self.get_attribute("starts_at")
        if starts_at:
            return datetime.fromisoformat(starts_at.replace("Z", "+00:00"))
        return None

    def get_ends_at(self) -> datetime | None:
        """Get the registration instance end time."""
        ends_at = self.get_attribute("ends_at")
        if ends_at:
            return datetime.fromisoformat(ends_at.replace("Z", "+00:00"))
        return None

    def get_capacity(self) -> int | None:
        """Get the registration instance capacity."""
        return self.get_attribute("capacity")

    def get_registered_count(self) -> int:
        """Get the number of registered people for this instance."""
        return self.get_attribute("registered_count", 0)

    def get_available_spots(self) -> int | None:
        """Get the number of available spots for this instance."""
        capacity = self.get_capacity()
        if capacity is not None:
            return capacity - self.get_registered_count()
        return None

    def get_created_at(self) -> datetime | None:
        """Get the registration instance creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the registration instance last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_registration_id(self) -> str | None:
        """Get the registration ID."""
        registration_data = self.get_relationship_data("registration")
        if registration_data and isinstance(registration_data, dict):
            return registration_data.get("id")
        return None


class PCORegistrationInstancePerson(PCOResource):
    """Represents a person registered for a registration instance."""

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

    def get_email(self) -> str | None:
        """Get the person's email."""
        return self.get_attribute("email")

    def get_phone(self) -> str | None:
        """Get the person's phone."""
        return self.get_attribute("phone")

    def get_registration_date(self) -> datetime | None:
        """Get the registration date."""
        reg_date = self.get_attribute("registration_date")
        if reg_date:
            return datetime.fromisoformat(reg_date.replace("Z", "+00:00"))
        return None

    def get_created_at(self) -> datetime | None:
        """Get the registration creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the registration last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_registration_instance_id(self) -> str | None:
        """Get the registration instance ID."""
        instance_data = self.get_relationship_data("registration_instance")
        if instance_data and isinstance(instance_data, dict):
            return instance_data.get("id")
        return None

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCORegistrationInstancePersonAnswer(PCOResource):
    """Represents an answer to a registration form field."""

    def get_value(self) -> Any:
        """Get the answer value."""
        return self.get_attribute("value")

    def get_created_at(self) -> datetime | None:
        """Get the answer creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the answer last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_registration_instance_person_id(self) -> str | None:
        """Get the registration instance person ID."""
        person_data = self.get_relationship_data("registration_instance_person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_field_id(self) -> str | None:
        """Get the field ID."""
        field_data = self.get_relationship_data("field")
        if field_data and isinstance(field_data, dict):
            return field_data.get("id")
        return None
