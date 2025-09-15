"""Registrations API models for Planning Center Online."""

from typing import Any

from ..models.base import PCOResource


class PCOAttendee(PCOResource):
    """Represents an attendee in Planning Center Registrations."""

    def get_complete(self) -> bool | None:
        """Get whether attendee has completed all necessary items."""
        return self.get_attribute("complete")

    def get_active(self) -> bool | None:
        """Get whether the attendee is active."""
        return self.get_attribute("active")

    def get_canceled(self) -> bool | None:
        """Get whether the attendee is canceled."""
        return self.get_attribute("canceled")

    def get_waitlisted(self) -> bool | None:
        """Get whether the attendee is waitlisted."""
        return self.get_attribute("waitlisted")

    def get_waitlisted_at(self) -> str | None:
        """Get UTC time at which the attendee was waitlisted."""
        return self.get_attribute("waitlisted_at")

    def get_created_at(self) -> str | None:
        """Get the creation timestamp."""
        return self.get_attribute("created_at")

    def get_updated_at(self) -> str | None:
        """Get the last update timestamp."""
        return self.get_attribute("updated_at")

    def get_emergency_contact(self) -> dict[str, Any] | None:
        """Get the associated emergency contact."""
        return self.get_relationship("emergency_contact")

    def get_person(self) -> dict[str, Any] | None:
        """Get the associated person."""
        return self.get_relationship("person")

    def get_registration(self) -> dict[str, Any] | None:
        """Get the associated registration."""
        return self.get_relationship("registration")

    def get_selection_type(self) -> dict[str, Any] | None:
        """Get the associated selection type."""
        return self.get_relationship("selection_type")

    def get_signup(self) -> dict[str, Any] | None:
        """Get the associated signup."""
        return self.get_relationship("signup")


class PCORegistrationsCampus(PCOResource):
    """Represents a campus in Planning Center Registrations."""

    def get_name(self) -> str | None:
        """Get the campus name."""
        return self.get_attribute("name")

    def get_street(self) -> str | None:
        """Get the street address of the campus."""
        return self.get_attribute("street")

    def get_city(self) -> str | None:
        """Get the city where the campus is located."""
        return self.get_attribute("city")

    def get_state(self) -> str | None:
        """Get the state or province where the campus is located."""
        return self.get_attribute("state")

    def get_zip(self) -> str | None:
        """Get the zip code of the campus."""
        return self.get_attribute("zip")

    def get_country(self) -> str | None:
        """Get the country where the campus is located."""
        return self.get_attribute("country")

    def get_full_formatted_address(self) -> str | None:
        """Get the full formatted address."""
        return self.get_attribute("full_formatted_address")

    def get_created_at(self) -> str | None:
        """Get the creation timestamp."""
        return self.get_attribute("created_at")

    def get_updated_at(self) -> str | None:
        """Get the last update timestamp."""
        return self.get_attribute("updated_at")

    def get_organization(self) -> dict[str, Any] | None:
        """Get the associated organization."""
        return self.get_relationship("organization")

    def get_signup(self) -> dict[str, Any] | None:
        """Get the associated signup."""
        return self.get_relationship("signup")


class PCORegistrationsCategory(PCOResource):
    """Represents a category in Planning Center Registrations."""

    def get_name(self) -> str | None:
        """Get the category name."""
        return self.get_attribute("name")

    def get_created_at(self) -> str | None:
        """Get the creation timestamp."""
        return self.get_attribute("created_at")

    def get_updated_at(self) -> str | None:
        """Get the last update timestamp."""
        return self.get_attribute("updated_at")

    def get_organization(self) -> dict[str, Any] | None:
        """Get the associated organization."""
        return self.get_relationship("organization")

    def get_signup(self) -> dict[str, Any] | None:
        """Get the associated signup."""
        return self.get_relationship("signup")


class PCOEmergencyContact(PCOResource):
    """Represents an emergency contact in Planning Center Registrations."""

    def get_name(self) -> str | None:
        """Get the emergency contact name."""
        return self.get_attribute("name")

    def get_phone_number(self) -> str | None:
        """Get the phone number of the emergency contact person."""
        return self.get_attribute("phone_number")

    def get_attendee(self) -> dict[str, Any] | None:
        """Get the associated attendee."""
        return self.get_relationship("attendee")


class PCORegistrationsOrganization(PCOResource):
    """Represents an organization in Planning Center Registrations."""

    def get_name(self) -> str | None:
        """Get the organization name."""
        return self.get_attribute("name")

    def get_created_at(self) -> str | None:
        """Get the creation timestamp."""
        return self.get_attribute("created_at")

    def get_updated_at(self) -> str | None:
        """Get the last update timestamp."""
        return self.get_attribute("updated_at")

    def get_campuses(self) -> list[dict[str, Any]] | None:
        """Get associated campuses."""
        return self.get_relationship("campuses")

    def get_categories(self) -> list[dict[str, Any]] | None:
        """Get associated categories."""
        return self.get_relationship("categories")

    def get_signups(self) -> list[dict[str, Any]] | None:
        """Get associated signups."""
        return self.get_relationship("signups")


class PCORegistrationsPerson(PCOResource):
    """Represents a person in Planning Center Registrations."""

    def get_first_name(self) -> str | None:
        """Get the first name."""
        return self.get_attribute("first_name")

    def get_last_name(self) -> str | None:
        """Get the last name."""
        return self.get_attribute("last_name")

    def get_name(self) -> str | None:
        """Get the full name."""
        return self.get_attribute("name")

    def get_attendee(self) -> dict[str, Any] | None:
        """Get the associated attendee."""
        return self.get_relationship("attendee")

    def get_registration(self) -> dict[str, Any] | None:
        """Get the associated registration."""
        return self.get_relationship("registration")


class PCORegistration(PCOResource):
    """Represents a registration in Planning Center Registrations."""

    def get_created_at(self) -> str | None:
        """Get the creation timestamp."""
        return self.get_attribute("created_at")

    def get_updated_at(self) -> str | None:
        """Get the last update timestamp."""
        return self.get_attribute("updated_at")

    def get_created_by(self) -> dict[str, Any] | None:
        """Get the associated created by person."""
        return self.get_relationship("created_by")

    def get_registrant_contact(self) -> dict[str, Any] | None:
        """Get the associated registrant contact."""
        return self.get_relationship("registrant_contact")

    def get_attendee(self) -> dict[str, Any] | None:
        """Get the associated attendee."""
        return self.get_relationship("attendee")

    def get_signup(self) -> dict[str, Any] | None:
        """Get the associated signup."""
        return self.get_relationship("signup")


class PCOSelectionType(PCOResource):
    """Represents a selection type in Planning Center Registrations."""

    def get_name(self) -> str | None:
        """Get the selection type name."""
        return self.get_attribute("name")

    def get_publicly_available(self) -> bool | None:
        """Get whether the selection type is available to the public."""
        return self.get_attribute("publicly_available")

    def get_price_cents(self) -> int | None:
        """Get the price of selection type in cents."""
        return self.get_attribute("price_cents")

    def get_price_currency(self) -> str | None:
        """Get the signup currency code."""
        return self.get_attribute("price_currency")

    def get_price_currency_symbol(self) -> str | None:
        """Get the signup currency symbol."""
        return self.get_attribute("price_currency_symbol")

    def get_price_formatted(self) -> str | None:
        """Get the price with currency formatting."""
        return self.get_attribute("price_formatted")

    def get_created_at(self) -> str | None:
        """Get the creation timestamp."""
        return self.get_attribute("created_at")

    def get_updated_at(self) -> str | None:
        """Get the last update timestamp."""
        return self.get_attribute("updated_at")

    def get_attendee(self) -> dict[str, Any] | None:
        """Get the associated attendee."""
        return self.get_relationship("attendee")


class PCOSignup(PCOResource):
    """Represents a signup in Planning Center Registrations."""

    def get_archived(self) -> bool | None:
        """Get whether the signup is archived or not."""
        return self.get_attribute("archived")

    def get_close_at(self) -> str | None:
        """Get UTC time at which registration closes."""
        return self.get_attribute("close_at")

    def get_description(self) -> str | None:
        """Get the description of the signup."""
        return self.get_attribute("description")

    def get_logo_url(self) -> str | None:
        """Get URL for the image used for the signup."""
        return self.get_attribute("logo_url")

    def get_name(self) -> str | None:
        """Get the name of the signup."""
        return self.get_attribute("name")

    def get_new_registration_url(self) -> str | None:
        """Get URL to allow people to register for signup."""
        return self.get_attribute("new_registration_url")

    def get_open_at(self) -> str | None:
        """Get UTC time at which registration opens."""
        return self.get_attribute("open_at")

    def get_created_at(self) -> str | None:
        """Get the creation timestamp."""
        return self.get_attribute("created_at")

    def get_updated_at(self) -> str | None:
        """Get the last update timestamp."""
        return self.get_attribute("updated_at")

    def get_attendees(self) -> list[dict[str, Any]] | None:
        """Get associated attendees."""
        return self.get_relationship("attendees")

    def get_campuses(self) -> list[dict[str, Any]] | None:
        """Get associated campuses."""
        return self.get_relationship("campuses")

    def get_categories(self) -> list[dict[str, Any]] | None:
        """Get associated categories."""
        return self.get_relationship("categories")

    def get_next_signup_time(self) -> dict[str, Any] | None:
        """Get the associated next signup time."""
        return self.get_relationship("next_signup_time")

    def get_signup_location(self) -> dict[str, Any] | None:
        """Get the associated signup location."""
        return self.get_relationship("signup_location")

    def get_signup_times(self) -> list[dict[str, Any]] | None:
        """Get associated signup times."""
        return self.get_relationship("signup_times")

    def get_registrations(self) -> list[dict[str, Any]] | None:
        """Get associated registrations."""
        return self.get_relationship("registrations")

    def get_selection_types(self) -> list[dict[str, Any]] | None:
        """Get associated selection types."""
        return self.get_relationship("selection_types")

    def get_organization(self) -> dict[str, Any] | None:
        """Get the associated organization."""
        return self.get_relationship("organization")


class PCOSignupLocation(PCOResource):
    """Represents a signup location in Planning Center Registrations."""

    def get_name(self) -> str | None:
        """Get the name of the signup location."""
        return self.get_attribute("name")

    def get_address_data(self) -> dict[str, Any] | None:
        """Get the address data of the signup location."""
        return self.get_attribute("address_data")

    def get_subpremise(self) -> str | None:
        """Get the subpremise of the signup location."""
        return self.get_attribute("subpremise")

    def get_latitude(self) -> str | None:
        """Get the latitude of the signup location."""
        return self.get_attribute("latitude")

    def get_longitude(self) -> str | None:
        """Get the longitude of the signup location."""
        return self.get_attribute("longitude")

    def get_location_type(self) -> str | None:
        """Get the type of location."""
        return self.get_attribute("location_type")

    def get_url(self) -> str | None:
        """Get the URL for the signup location."""
        return self.get_attribute("url")

    def get_formatted_address(self) -> str | None:
        """Get the formatted address of the signup location."""
        return self.get_attribute("formatted_address")

    def get_full_formatted_address(self) -> str | None:
        """Get the fully formatted address of the signup location."""
        return self.get_attribute("full_formatted_address")

    def get_created_at(self) -> str | None:
        """Get the creation timestamp."""
        return self.get_attribute("created_at")

    def get_updated_at(self) -> str | None:
        """Get the last update timestamp."""
        return self.get_attribute("updated_at")

    def get_signup(self) -> dict[str, Any] | None:
        """Get the associated signup."""
        return self.get_relationship("signup")


class PCOSignupTime(PCOResource):
    """Represents a signup time in Planning Center Registrations."""

    def get_starts_at(self) -> str | None:
        """Get the start date and time of signup time."""
        return self.get_attribute("starts_at")

    def get_ends_at(self) -> str | None:
        """Get the end date and time of signup time."""
        return self.get_attribute("ends_at")

    def get_all_day(self) -> bool | None:
        """Get whether the signup time is all day."""
        return self.get_attribute("all_day")

    def get_created_at(self) -> str | None:
        """Get the creation timestamp."""
        return self.get_attribute("created_at")

    def get_updated_at(self) -> str | None:
        """Get the last update timestamp."""
        return self.get_attribute("updated_at")

    def get_signup(self) -> dict[str, Any] | None:
        """Get the associated signup."""
        return self.get_relationship("signup")
