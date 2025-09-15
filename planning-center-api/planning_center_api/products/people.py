"""People product models for Planning Center API."""

from datetime import datetime
from typing import Any

from ..models.base import PCOResource


class PCOPeoplePerson(PCOResource):
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


class PCOAddress(PCOResource):
    """Represents an address in Planning Center People."""

    def get_city(self) -> str | None:
        """Get the city."""
        return self.get_attribute("city")

    def get_state(self) -> str | None:
        """Get the state."""
        return self.get_attribute("state")

    def get_zip(self) -> str | None:
        """Get the ZIP code."""
        return self.get_attribute("zip")

    def get_country_code(self) -> str | None:
        """Get the country code."""
        return self.get_attribute("country_code")

    def get_country_name(self) -> str | None:
        """Get the country name."""
        return self.get_attribute("country_name")

    def get_location(self) -> str | None:
        """Get the address location (e.g., 'Home', 'Work')."""
        return self.get_attribute("location")

    def is_primary(self) -> bool:
        """Check if this is the primary address."""
        return self.get_attribute("primary", False)

    def get_street_line_1(self) -> str | None:
        """Get the first street line."""
        return self.get_attribute("street_line_1")

    def get_street_line_2(self) -> str | None:
        """Get the second street line."""
        return self.get_attribute("street_line_2")

    def get_full_address(self) -> str:
        """Get the full formatted address."""
        parts = []
        if self.get_street_line_1():
            parts.append(self.get_street_line_1())
        if self.get_street_line_2():
            parts.append(self.get_street_line_2())
        if self.get_city():
            parts.append(self.get_city())
        if self.get_state():
            parts.append(self.get_state())
        if self.get_zip():
            parts.append(self.get_zip())
        if self.get_country_name():
            parts.append(self.get_country_name())
        return ", ".join(parts)

    def get_person_id(self) -> str | None:
        """Get the person ID this address belongs to."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCOApp(PCOResource):
    """Represents an app in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the app name."""
        return self.get_attribute("name")

    def get_url(self) -> str | None:
        """Get the app URL."""
        return self.get_attribute("url")


class PCOBackgroundCheck(PCOResource):
    """Represents a background check in Planning Center People."""

    def is_current(self) -> bool:
        """Check if this is the current background check."""
        return self.get_attribute("current", False)

    def get_note(self) -> str | None:
        """Get the background check note."""
        return self.get_attribute("note")

    def get_status(self) -> str | None:
        """Get the background check status."""
        return self.get_attribute("status")

    def get_report_url(self) -> str | None:
        """Get the background check report URL."""
        return self.get_attribute("report_url")

    def get_expires_on(self) -> datetime | None:
        """Get the expiration date."""
        expires_on = self.get_attribute("expires_on")
        if expires_on:
            return datetime.fromisoformat(expires_on.replace("Z", "+00:00"))
        return None

    def get_completed_at(self) -> datetime | None:
        """Get the completion date."""
        completed_at = self.get_attribute("completed_at")
        if completed_at:
            return datetime.fromisoformat(completed_at.replace("Z", "+00:00"))
        return None

    def get_person_id(self) -> str | None:
        """Get the person ID this background check belongs to."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_created_by_id(self) -> str | None:
        """Get the ID of the person who created this background check."""
        created_by_data = self.get_relationship_data("created_by")
        if created_by_data and isinstance(created_by_data, dict):
            return created_by_data.get("id")
        return None


class PCOBirthdayPeople(PCOResource):
    """Represents birthday people collection in Planning Center People."""

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        return self.get_id()


class PCOPeopleCampus(PCOResource):
    """Represents a campus in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the campus name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the campus description."""
        return self.get_attribute("description")

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

    def get_phone_number(self) -> str | None:
        """Get the phone number."""
        return self.get_attribute("phone_number")

    def get_website(self) -> str | None:
        """Get the website URL."""
        return self.get_attribute("website")

    def get_contact_email_address(self) -> str | None:
        """Get the contact email address."""
        return self.get_attribute("contact_email_address")

    def get_time_zone(self) -> str | None:
        """Get the time zone."""
        return self.get_attribute("time_zone")

    def get_latitude(self) -> float | None:
        """Get the latitude."""
        return self.get_attribute("latitude")

    def get_longitude(self) -> float | None:
        """Get the longitude."""
        return self.get_attribute("longitude")

    def is_church_center_enabled(self) -> bool:
        """Check if Church Center is enabled."""
        return self.get_attribute("church_center_enabled", False)

    def get_organization_id(self) -> str | None:
        """Get the organization ID."""
        organization_data = self.get_relationship_data("organization")
        if organization_data and isinstance(organization_data, dict):
            return organization_data.get("id")
        return None


class PCOCarrier(PCOResource):
    """Represents a carrier in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the carrier name."""
        return self.get_attribute("name")

    def get_value(self) -> str | None:
        """Get the carrier value."""
        return self.get_attribute("value")

    def is_international(self) -> bool:
        """Check if this is an international carrier."""
        return self.get_attribute("international", False)


class PCOCondition(PCOResource):
    """Represents a condition in Planning Center People."""

    def get_application(self) -> str | None:
        """Get the application."""
        return self.get_attribute("application")

    def get_definition_class(self) -> str | None:
        """Get the definition class."""
        return self.get_attribute("definition_class")

    def get_comparison(self) -> str | None:
        """Get the comparison."""
        return self.get_attribute("comparison")

    def get_settings(self) -> str | None:
        """Get the settings."""
        return self.get_attribute("settings")

    def get_definition_identifier(self) -> str | None:
        """Get the definition identifier."""
        return self.get_attribute("definition_identifier")

    def get_description(self) -> str | None:
        """Get the description."""
        return self.get_attribute("description")

    def get_created_by_id(self) -> str | None:
        """Get the ID of the person who created this condition."""
        created_by_data = self.get_relationship_data("created_by")
        if created_by_data and isinstance(created_by_data, dict):
            return created_by_data.get("id")
        return None


class PCOConnectedPerson(PCOResource):
    """Represents a connected person in Planning Center People."""

    def get_given_name(self) -> str | None:
        """Get the given name."""
        return self.get_attribute("given_name")

    def get_first_name(self) -> str | None:
        """Get the first name."""
        return self.get_attribute("first_name")

    def get_nickname(self) -> str | None:
        """Get the nickname."""
        return self.get_attribute("nickname")

    def get_middle_name(self) -> str | None:
        """Get the middle name."""
        return self.get_attribute("middle_name")

    def get_last_name(self) -> str | None:
        """Get the last name."""
        return self.get_attribute("last_name")

    def get_gender(self) -> str | None:
        """Get the gender."""
        return self.get_attribute("gender")

    def get_organization_name(self) -> str | None:
        """Get the organization name."""
        return self.get_attribute("organization_name")

    def get_organization_id(self) -> str | None:
        """Get the organization ID."""
        return self.get_attribute("organization_id")

    def get_organization_id_from_relationship(self) -> str | None:
        """Get the organization ID from relationship."""
        organization_data = self.get_relationship_data("organization")
        if organization_data and isinstance(organization_data, dict):
            return organization_data.get("id")
        return None


class PCOCustomSender(PCOResource):
    """Represents a custom sender in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the custom sender name."""
        return self.get_attribute("name")

    def get_email_address(self) -> str | None:
        """Get the email address."""
        return self.get_attribute("email_address")

    def get_verified_at(self) -> datetime | None:
        """Get the verification date."""
        verified_at = self.get_attribute("verified_at")
        if verified_at:
            return datetime.fromisoformat(verified_at.replace("Z", "+00:00"))
        return None

    def get_verification_requested_at(self) -> datetime | None:
        """Get the verification requested date."""
        verification_requested_at = self.get_attribute("verification_requested_at")
        if verification_requested_at:
            return datetime.fromisoformat(verification_requested_at.replace("Z", "+00:00"))
        return None

    def is_verified(self) -> bool:
        """Check if the custom sender is verified."""
        return self.get_attribute("verified", False)

    def is_expired(self) -> bool:
        """Check if the custom sender is expired."""
        return self.get_attribute("expired", False)

    def get_verification_status(self) -> str | None:
        """Get the verification status."""
        return self.get_attribute("verification_status")


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

    def is_blocked(self) -> bool:
        """Check if this email address is blocked."""
        return self.get_attribute("blocked", False)

    def get_person_id(self) -> str | None:
        """Get the person ID this email belongs to."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCOFieldDatum(PCOResource):
    """Represents field data in Planning Center People."""

    def get_value(self) -> Any:
        """Get the field value."""
        return self.get_attribute("value")

    def get_file(self) -> str | None:
        """Get the file."""
        return self.get_attribute("file")

    def get_file_size(self) -> int | None:
        """Get the file size."""
        return self.get_attribute("file_size")

    def get_file_content_type(self) -> str | None:
        """Get the file content type."""
        return self.get_attribute("file_content_type")

    def get_file_name(self) -> str | None:
        """Get the file name."""
        return self.get_attribute("file_name")

    def get_field_definition_id(self) -> str | None:
        """Get the field definition ID."""
        field_definition_data = self.get_relationship_data("field_definition")
        if field_definition_data and isinstance(field_definition_data, dict):
            return field_definition_data.get("id")
        return None

    def get_customizable_id(self) -> str | None:
        """Get the customizable ID."""
        customizable_data = self.get_relationship_data("customizable")
        if customizable_data and isinstance(customizable_data, dict):
            return customizable_data.get("id")
        return None


class PCOFieldDefinition(PCOResource):
    """Represents a field definition in Planning Center People."""

    def get_data_type(self) -> str | None:
        """Get the data type."""
        return self.get_attribute("data_type")

    def get_name(self) -> str | None:
        """Get the field name."""
        return self.get_attribute("name")

    def get_sequence(self) -> int | None:
        """Get the sequence."""
        return self.get_attribute("sequence")

    def get_slug(self) -> str | None:
        """Get the slug."""
        return self.get_attribute("slug")

    def get_config(self) -> str | None:
        """Get the config."""
        return self.get_attribute("config")

    def get_deleted_at(self) -> datetime | None:
        """Get the deleted date."""
        deleted_at = self.get_attribute("deleted_at")
        if deleted_at:
            return datetime.fromisoformat(deleted_at.replace("Z", "+00:00"))
        return None

    def get_tab_id(self) -> str | None:
        """Get the tab ID."""
        return self.get_attribute("tab_id")

    def get_tab_id_from_relationship(self) -> str | None:
        """Get the tab ID from relationship."""
        tab_data = self.get_relationship_data("tab")
        if tab_data and isinstance(tab_data, dict):
            return tab_data.get("id")
        return None


class PCOFieldOption(PCOResource):
    """Represents a field option in Planning Center People."""

    def get_value(self) -> str | None:
        """Get the option value."""
        return self.get_attribute("value")

    def get_sequence(self) -> int | None:
        """Get the sequence."""
        return self.get_attribute("sequence")

    def get_field_definition_id(self) -> str | None:
        """Get the field definition ID."""
        field_definition_data = self.get_relationship_data("field_definition")
        if field_definition_data and isinstance(field_definition_data, dict):
            return field_definition_data.get("id")
        return None


class PCOForm(PCOResource):
    """Represents a form in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the form name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the form description."""
        return self.get_attribute("description")

    def is_active(self) -> bool:
        """Check if the form is active."""
        return self.get_attribute("active", False)

    def get_archived_at(self) -> datetime | None:
        """Get the archived date."""
        archived_at = self.get_attribute("archived_at")
        if archived_at:
            return datetime.fromisoformat(archived_at.replace("Z", "+00:00"))
        return None

    def get_deleted_at(self) -> datetime | None:
        """Get the deleted date."""
        deleted_at = self.get_attribute("deleted_at")
        if deleted_at:
            return datetime.fromisoformat(deleted_at.replace("Z", "+00:00"))
        return None

    def get_submission_count(self) -> int | None:
        """Get the submission count."""
        return self.get_attribute("submission_count")

    def get_public_url(self) -> str | None:
        """Get the public URL."""
        return self.get_attribute("public_url")

    def is_recently_viewed(self) -> bool:
        """Check if the form was recently viewed."""
        return self.get_attribute("recently_viewed", False)

    def is_archived(self) -> bool:
        """Check if the form is archived."""
        return self.get_attribute("archived", False)

    def is_send_submission_notification_to_submitter(self) -> bool:
        """Check if submission notifications are sent to submitter."""
        return self.get_attribute("send_submission_notification_to_submitter", False)

    def is_login_required(self) -> bool:
        """Check if login is required."""
        return self.get_attribute("login_required", False)

    def get_campus_id(self) -> str | None:
        """Get the campus ID."""
        campus_data = self.get_relationship_data("campus")
        if campus_data and isinstance(campus_data, dict):
            return campus_data.get("id")
        return None

    def get_form_category_id(self) -> str | None:
        """Get the form category ID."""
        form_category_data = self.get_relationship_data("form_category")
        if form_category_data and isinstance(form_category_data, dict):
            return form_category_data.get("id")
        return None


class PCOFormCategory(PCOResource):
    """Represents a form category in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the form category name."""
        return self.get_attribute("name")


class PCOFormField(PCOResource):
    """Represents a form field in Planning Center People."""

    def get_label(self) -> str | None:
        """Get the field label."""
        return self.get_attribute("label")

    def get_description(self) -> str | None:
        """Get the field description."""
        return self.get_attribute("description")

    def is_required(self) -> bool:
        """Check if the field is required."""
        return self.get_attribute("required", False)

    def get_settings(self) -> str | None:
        """Get the field settings."""
        return self.get_attribute("settings")

    def get_field_type(self) -> str | None:
        """Get the field type."""
        return self.get_attribute("field_type")

    def get_sequence(self) -> int | None:
        """Get the sequence."""
        return self.get_attribute("sequence")

    def get_form_id(self) -> str | None:
        """Get the form ID."""
        form_data = self.get_relationship_data("form")
        if form_data and isinstance(form_data, dict):
            return form_data.get("id")
        return None


class PCOFormFieldOption(PCOResource):
    """Represents a form field option in Planning Center People."""

    def get_label(self) -> str | None:
        """Get the option label."""
        return self.get_attribute("label")

    def get_sequence(self) -> int | None:
        """Get the sequence."""
        return self.get_attribute("sequence")

    def get_form_field_id(self) -> str | None:
        """Get the form field ID."""
        form_field_data = self.get_relationship_data("form_field")
        if form_field_data and isinstance(form_field_data, dict):
            return form_field_data.get("id")
        return None


class PCOFormSubmission(PCOResource):
    """Represents a form submission in Planning Center People."""

    def is_verified(self) -> bool:
        """Check if the submission is verified."""
        return self.get_attribute("verified", False)

    def is_requires_verification(self) -> bool:
        """Check if verification is required."""
        return self.get_attribute("requires_verification", False)

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_form_id(self) -> str | None:
        """Get the form ID."""
        form_data = self.get_relationship_data("form")
        if form_data and isinstance(form_data, dict):
            return form_data.get("id")
        return None


class PCOFormSubmissionValue(PCOResource):
    """Represents a form submission value in Planning Center People."""

    def get_display_value(self) -> str | None:
        """Get the display value."""
        return self.get_attribute("display_value")

    def get_attachments(self) -> list[Any]:
        """Get the attachments."""
        return self.get_attribute("attachments", [])

    def get_form_field_id(self) -> str | None:
        """Get the form field ID."""
        form_field_data = self.get_relationship_data("form_field")
        if form_field_data and isinstance(form_field_data, dict):
            return form_field_data.get("id")
        return None

    def get_form_field_option_id(self) -> str | None:
        """Get the form field option ID."""
        form_field_option_data = self.get_relationship_data("form_field_option")
        if form_field_option_data and isinstance(form_field_option_data, dict):
            return form_field_option_data.get("id")
        return None

    def get_form_submission_id(self) -> str | None:
        """Get the form submission ID."""
        form_submission_data = self.get_relationship_data("form_submission")
        if form_submission_data and isinstance(form_submission_data, dict):
            return form_submission_data.get("id")
        return None


class PCOPhoneNumber(PCOResource):
    """Represents a phone number in Planning Center People."""

    def get_number(self) -> str | None:
        """Get the phone number."""
        return self.get_attribute("number")

    def get_carrier(self) -> str | None:
        """Get the carrier."""
        return self.get_attribute("carrier")

    def get_location(self) -> str | None:
        """Get the phone location (e.g., 'Home', 'Work', 'Mobile')."""
        return self.get_attribute("location")

    def is_primary(self) -> bool:
        """Check if this is the primary phone number."""
        return self.get_attribute("primary", False)

    def get_e164(self) -> str | None:
        """Get the E164 formatted number."""
        return self.get_attribute("e164")

    def get_international(self) -> str | None:
        """Get the international format."""
        return self.get_attribute("international")

    def get_national(self) -> str | None:
        """Get the national format."""
        return self.get_attribute("national")

    def get_country_code(self) -> str | None:
        """Get the country code."""
        return self.get_attribute("country_code")

    def get_formatted_number(self) -> str | None:
        """Get the formatted number."""
        return self.get_attribute("formatted_number")

    def get_person_id(self) -> str | None:
        """Get the person ID this phone number belongs to."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


# Import additional classes from the separate file
