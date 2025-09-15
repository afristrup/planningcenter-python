"""People product models for Planning Center API."""

from datetime import datetime
from typing import Any

from ..models.base import PCOResource


class PCOPerson(PCOResource):
    """Represents a person in Planning Center People."""

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
        """Get the person's primary email address."""
        return self.get_attribute("email")

    def get_phone(self) -> str | None:
        """Get the person's primary phone number."""
        return self.get_attribute("phone")

    def get_birthdate(self) -> datetime | None:
        """Get the person's birthdate."""
        birthdate = self.get_attribute("birthdate")
        if birthdate:
            return datetime.fromisoformat(birthdate.replace("Z", "+00:00"))
        return None

    def get_anniversary(self) -> datetime | None:
        """Get the person's anniversary date."""
        anniversary = self.get_attribute("anniversary")
        if anniversary:
            return datetime.fromisoformat(anniversary.replace("Z", "+00:00"))
        return None

    def is_active(self) -> bool:
        """Check if the person is active."""
        return self.get_attribute("status") == "active"

    def get_household_id(self) -> str | None:
        """Get the person's household ID."""
        household_data = self.get_relationship_data("household")
        if household_data and isinstance(household_data, dict):
            return household_data.get("id")
        return None


class PCOEmail(PCOResource):
    """Represents an email address in Planning Center People."""

    def get_address(self) -> str | None:
        """Get the email address."""
        return self.get_attribute("address")

    def get_location(self) -> str | None:
        """Get the email location (e.g., 'Home', 'Work')."""
        return self.get_attribute("location")

    def is_primary(self) -> bool:
        """Check if this is the primary email address."""
        return self.get_attribute("primary", False)

    def get_person_id(self) -> str | None:
        """Get the person ID this email belongs to."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCOPhoneNumber(PCOResource):
    """Represents a phone number in Planning Center People."""

    def get_number(self) -> str | None:
        """Get the phone number."""
        return self.get_attribute("number")

    def get_location(self) -> str | None:
        """Get the phone location (e.g., 'Home', 'Work', 'Mobile')."""
        return self.get_attribute("location")

    def is_primary(self) -> bool:
        """Check if this is the primary phone number."""
        return self.get_attribute("primary", False)

    def get_person_id(self) -> str | None:
        """Get the person ID this phone number belongs to."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCOAddress(PCOResource):
    """Represents an address in Planning Center People."""

    def get_street(self) -> str | None:
        """Get the street address."""
        return self.get_attribute("street")

    def get_city(self) -> str | None:
        """Get the city."""
        return self.get_attribute("city")

    def get_state(self) -> str | None:
        """Get the state."""
        return self.get_attribute("state")

    def get_zip(self) -> str | None:
        """Get the ZIP code."""
        return self.get_attribute("zip")

    def get_country(self) -> str | None:
        """Get the country."""
        return self.get_attribute("country")

    def get_location(self) -> str | None:
        """Get the address location (e.g., 'Home', 'Work')."""
        return self.get_attribute("location")

    def is_primary(self) -> bool:
        """Check if this is the primary address."""
        return self.get_attribute("primary", False)

    def get_full_address(self) -> str:
        """Get the full formatted address."""
        parts = []
        if self.get_street():
            parts.append(self.get_street())
        if self.get_city():
            parts.append(self.get_city())
        if self.get_state():
            parts.append(self.get_state())
        if self.get_zip():
            parts.append(self.get_zip())
        if self.get_country():
            parts.append(self.get_country())
        return ", ".join(parts)

    def get_person_id(self) -> str | None:
        """Get the person ID this address belongs to."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCOFieldData(PCOResource):
    """Represents field data in Planning Center People."""

    def get_value(self) -> Any:
        """Get the field value."""
        return self.get_attribute("value")

    def get_field_definition_id(self) -> str | None:
        """Get the field definition ID."""
        return self.get_attribute("field_definition_id")

    def get_person_id(self) -> str | None:
        """Get the person ID this field data belongs to."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCOCustomField(PCOResource):
    """Represents a custom field definition in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the custom field name."""
        return self.get_attribute("name")

    def get_field_type(self) -> str | None:
        """Get the custom field type."""
        return self.get_attribute("field_type")

    def get_required(self) -> bool:
        """Check if the custom field is required."""
        return self.get_attribute("required", False)

    def get_options(self) -> list[str]:
        """Get the custom field options (for select fields)."""
        return self.get_attribute("options", [])


class PCOHousehold(PCOResource):
    """Represents a household in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the household name."""
        return self.get_attribute("name")

    def get_primary_contact_id(self) -> str | None:
        """Get the primary contact person ID."""
        return self.get_attribute("primary_contact_id")

    def get_member_count(self) -> int:
        """Get the number of household members."""
        return self.get_attribute("member_count", 0)

    def get_people_ids(self) -> list[str]:
        """Get all person IDs in this household."""
        people_data = self.get_relationship_data("people")
        if people_data and isinstance(people_data, list):
            return [person.get("id") for person in people_data if person.get("id")]
        return []


class PCOInactiveReason(PCOResource):
    """Represents an inactive reason in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the inactive reason name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the inactive reason description."""
        return self.get_attribute("description")


class PCOMaritalStatus(PCOResource):
    """Represents a marital status in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the marital status name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the marital status description."""
        return self.get_attribute("description")


class PCONameSuffix(PCOResource):
    """Represents a name suffix in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the name suffix."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the name suffix description."""
        return self.get_attribute("description")


class PCONameTitle(PCOResource):
    """Represents a name title in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the name title."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the name title description."""
        return self.get_attribute("description")


class PCOWorkflow(PCOResource):
    """Represents a workflow in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the workflow name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the workflow description."""
        return self.get_attribute("description")

    def is_active(self) -> bool:
        """Check if the workflow is active."""
        return self.get_attribute("active", True)

    def get_step_count(self) -> int:
        """Get the number of steps in the workflow."""
        return self.get_attribute("step_count", 0)


class PCOWorkflowStep(PCOResource):
    """Represents a workflow step in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the workflow step name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the workflow step description."""
        return self.get_attribute("description")

    def get_order(self) -> int:
        """Get the step order."""
        return self.get_attribute("order", 0)

    def get_workflow_id(self) -> str | None:
        """Get the workflow ID this step belongs to."""
        workflow_data = self.get_relationship_data("workflow")
        if workflow_data and isinstance(workflow_data, dict):
            return workflow_data.get("id")
        return None
