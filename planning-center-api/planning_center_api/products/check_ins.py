"""Check-Ins product models for Planning Center API."""

from datetime import datetime

from ..models.base import PCOResource


class PCOAttendanceType(PCOResource):
    """Represents an attendance type in Planning Center Check-Ins."""

    def get_name(self) -> str | None:
        """Get the attendance type name."""
        return self.get_attribute("name")

    def get_color(self) -> str | None:
        """Get the attendance type color."""
        return self.get_attribute("color")

    def get_limit(self) -> int | None:
        """Get the attendance type limit."""
        return self.get_attribute("limit")

    def get_created_at(self) -> datetime | None:
        """Get the attendance type creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the attendance type last update time."""
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


class PCOCheckIn(PCOResource):
    """Represents a check-in in Planning Center Check-Ins."""

    def get_first_name(self) -> str | None:
        """Get the first name."""
        return self.get_attribute("first_name")

    def get_last_name(self) -> str | None:
        """Get the last name."""
        return self.get_attribute("last_name")

    def get_medical_notes(self) -> str | None:
        """Get the medical notes."""
        return self.get_attribute("medical_notes")

    def get_number(self) -> int | None:
        """Get the check-in number."""
        return self.get_attribute("number")

    def get_security_code(self) -> str | None:
        """Get the security code."""
        return self.get_attribute("security_code")

    def get_checked_out_at(self) -> datetime | None:
        """Get the checked out time."""
        checked_out_at = self.get_attribute("checked_out_at")
        if checked_out_at:
            return datetime.fromisoformat(checked_out_at.replace("Z", "+00:00"))
        return None

    def get_confirmed_at(self) -> datetime | None:
        """Get the confirmed time."""
        confirmed_at = self.get_attribute("confirmed_at")
        if confirmed_at:
            return datetime.fromisoformat(confirmed_at.replace("Z", "+00:00"))
        return None

    def get_emergency_contact_name(self) -> str | None:
        """Get the emergency contact name."""
        return self.get_attribute("emergency_contact_name")

    def get_emergency_contact_phone_number(self) -> str | None:
        """Get the emergency contact phone number."""
        return self.get_attribute("emergency_contact_phone_number")

    def get_one_time_guest(self) -> bool | None:
        """Get whether this is a one-time guest."""
        return self.get_attribute("one_time_guest")

    def get_kind(self) -> str | None:
        """Get the check-in kind."""
        return self.get_attribute("kind")

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

    def get_event_period_id(self) -> str | None:
        """Get the event period ID."""
        event_period_data = self.get_relationship_data("event_period")
        if event_period_data and isinstance(event_period_data, dict):
            return event_period_data.get("id")
        return None

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCOCheckInGroup(PCOResource):
    """Represents a check-in group in Planning Center Check-Ins."""

    def get_name_labels_count(self) -> int | None:
        """Get the name labels count."""
        return self.get_attribute("name_labels_count")

    def get_security_labels_count(self) -> int | None:
        """Get the security labels count."""
        return self.get_attribute("security_labels_count")

    def get_check_ins_count(self) -> int | None:
        """Get the check-ins count."""
        return self.get_attribute("check_ins_count")

    def get_print_status(self) -> str | None:
        """Get the print status."""
        return self.get_attribute("print_status")

    def get_created_at(self) -> datetime | None:
        """Get the check-in group creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the check-in group last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOCheckInTime(PCOResource):
    """Represents a check-in time in Planning Center Check-Ins."""

    def get_kind(self) -> str | None:
        """Get the check-in time kind."""
        return self.get_attribute("kind")

    def get_has_validated(self) -> bool | None:
        """Get whether it has been validated."""
        return self.get_attribute("has_validated")

    def get_services_integrated(self) -> bool | None:
        """Get whether services are integrated."""
        return self.get_attribute("services_integrated")

    def get_alerts(self) -> list | None:
        """Get the alerts."""
        return self.get_attribute("alerts")

    def get_event_time_id(self) -> str | None:
        """Get the event time ID."""
        event_time_data = self.get_relationship_data("event_time")
        if event_time_data and isinstance(event_time_data, dict):
            return event_time_data.get("id")
        return None

    def get_location_id(self) -> str | None:
        """Get the location ID."""
        location_data = self.get_relationship_data("location")
        if location_data and isinstance(location_data, dict):
            return location_data.get("id")
        return None

    def get_check_in_id(self) -> str | None:
        """Get the check-in ID."""
        check_in_data = self.get_relationship_data("check_in")
        if check_in_data and isinstance(check_in_data, dict):
            return check_in_data.get("id")
        return None

    def get_pre_check_id(self) -> str | None:
        """Get the pre-check ID."""
        pre_check_data = self.get_relationship_data("pre_check")
        if pre_check_data and isinstance(pre_check_data, dict):
            return pre_check_data.get("id")
        return None


class PCOCheckInsEvent(PCOResource):
    """Represents an event in Planning Center Check-Ins."""

    def get_name(self) -> str | None:
        """Get the event name."""
        return self.get_attribute("name")

    def get_frequency(self) -> str | None:
        """Get the event frequency."""
        return self.get_attribute("frequency")

    def get_enable_services_integration(self) -> bool | None:
        """Get whether services integration is enabled."""
        return self.get_attribute("enable_services_integration")

    def get_archived_at(self) -> datetime | None:
        """Get the archived time."""
        archived_at = self.get_attribute("archived_at")
        if archived_at:
            return datetime.fromisoformat(archived_at.replace("Z", "+00:00"))
        return None

    def get_integration_key(self) -> str | None:
        """Get the integration key."""
        return self.get_attribute("integration_key")

    def get_location_times_enabled(self) -> bool | None:
        """Get whether location times are enabled."""
        return self.get_attribute("location_times_enabled")

    def get_pre_select_enabled(self) -> bool | None:
        """Get whether pre-select is enabled."""
        return self.get_attribute("pre_select_enabled")

    def get_app_source(self) -> str | None:
        """Get the app source."""
        return self.get_attribute("app_source")

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


class PCOCheckInsEventLabel(PCOResource):
    """Represents an event label in Planning Center Check-Ins."""

    def get_quantity(self) -> int | None:
        """Get the quantity."""
        return self.get_attribute("quantity")

    def get_for_regular(self) -> bool | None:
        """Get whether it's for regular attendees."""
        return self.get_attribute("for_regular")

    def get_for_guest(self) -> bool | None:
        """Get whether it's for guests."""
        return self.get_attribute("for_guest")

    def get_for_volunteer(self) -> bool | None:
        """Get whether it's for volunteers."""
        return self.get_attribute("for_volunteer")

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


class PCOCheckInsEventPeriod(PCOResource):
    """Represents an event period in Planning Center Check-Ins."""

    def get_starts_at(self) -> datetime | None:
        """Get the start time."""
        starts_at = self.get_attribute("starts_at")
        if starts_at:
            return datetime.fromisoformat(starts_at.replace("Z", "+00:00"))
        return None

    def get_ends_at(self) -> datetime | None:
        """Get the end time."""
        ends_at = self.get_attribute("ends_at")
        if ends_at:
            return datetime.fromisoformat(ends_at.replace("Z", "+00:00"))
        return None

    def get_regular_count(self) -> int | None:
        """Get the regular count."""
        return self.get_attribute("regular_count")

    def get_guest_count(self) -> int | None:
        """Get the guest count."""
        return self.get_attribute("guest_count")

    def get_volunteer_count(self) -> int | None:
        """Get the volunteer count."""
        return self.get_attribute("volunteer_count")

    def get_note(self) -> str | None:
        """Get the note."""
        return self.get_attribute("note")

    def get_created_at(self) -> datetime | None:
        """Get the event period creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the event period last update time."""
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


class PCOCheckInsEventTime(PCOResource):
    """Represents an event time in Planning Center Check-Ins."""

    def get_total_count(self) -> int | None:
        """Get the total count."""
        return self.get_attribute("total_count")

    def get_starts_at(self) -> datetime | None:
        """Get the start time."""
        starts_at = self.get_attribute("starts_at")
        if starts_at:
            return datetime.fromisoformat(starts_at.replace("Z", "+00:00"))
        return None

    def get_shows_at(self) -> datetime | None:
        """Get the shows at time."""
        shows_at = self.get_attribute("shows_at")
        if shows_at:
            return datetime.fromisoformat(shows_at.replace("Z", "+00:00"))
        return None

    def get_hides_at(self) -> datetime | None:
        """Get the hides at time."""
        hides_at = self.get_attribute("hides_at")
        if hides_at:
            return datetime.fromisoformat(hides_at.replace("Z", "+00:00"))
        return None

    def get_regular_count(self) -> int | None:
        """Get the regular count."""
        return self.get_attribute("regular_count")

    def get_guest_count(self) -> int | None:
        """Get the guest count."""
        return self.get_attribute("guest_count")

    def get_volunteer_count(self) -> int | None:
        """Get the volunteer count."""
        return self.get_attribute("volunteer_count")

    def get_name(self) -> str | None:
        """Get the event time name."""
        return self.get_attribute("name")

    def get_hour(self) -> int | None:
        """Get the hour."""
        return self.get_attribute("hour")

    def get_minute(self) -> int | None:
        """Get the minute."""
        return self.get_attribute("minute")

    def get_day_of_week(self) -> int | None:
        """Get the day of week."""
        return self.get_attribute("day_of_week")

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

    def get_event_period_id(self) -> str | None:
        """Get the event period ID."""
        event_period_data = self.get_relationship_data("event_period")
        if event_period_data and isinstance(event_period_data, dict):
            return event_period_data.get("id")
        return None


class PCOHeadcount(PCOResource):
    """Represents a headcount in Planning Center Check-Ins."""

    def get_total(self) -> int | None:
        """Get the total count."""
        return self.get_attribute("total")

    def get_created_at(self) -> datetime | None:
        """Get the headcount creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the headcount last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_event_time_id(self) -> str | None:
        """Get the event time ID."""
        event_time_data = self.get_relationship_data("event_time")
        if event_time_data and isinstance(event_time_data, dict):
            return event_time_data.get("id")
        return None

    def get_attendance_type_id(self) -> str | None:
        """Get the attendance type ID."""
        attendance_type_data = self.get_relationship_data("attendance_type")
        if attendance_type_data and isinstance(attendance_type_data, dict):
            return attendance_type_data.get("id")
        return None


class PCOIntegrationLink(PCOResource):
    """Represents an integration link in Planning Center Check-Ins."""

    def get_remote_gid(self) -> str | None:
        """Get the remote global ID."""
        return self.get_attribute("remote_gid")

    def get_remote_app(self) -> str | None:
        """Get the remote app."""
        return self.get_attribute("remote_app")

    def get_remote_type(self) -> str | None:
        """Get the remote type."""
        return self.get_attribute("remote_type")

    def get_remote_id(self) -> str | None:
        """Get the remote ID."""
        return self.get_attribute("remote_id")

    def get_sync_future_assignment_types(self) -> bool | None:
        """Get whether to sync future assignment types."""
        return self.get_attribute("sync_future_assignment_types")


class PCOCheckInsLabel(PCOResource):
    """Represents a label in Planning Center Check-Ins."""

    def get_name(self) -> str | None:
        """Get the label name."""
        return self.get_attribute("name")

    def get_xml(self) -> str | None:
        """Get the XML content."""
        return self.get_attribute("xml")

    def get_prints_for(self) -> str | None:
        """Get what the label prints for."""
        return self.get_attribute("prints_for")

    def get_roll(self) -> str | None:
        """Get the roll."""
        return self.get_attribute("roll")

    def get_created_at(self) -> datetime | None:
        """Get the label creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the label last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOLocation(PCOResource):
    """Represents a location in Planning Center Check-Ins."""

    def get_name(self) -> str | None:
        """Get the location name."""
        return self.get_attribute("name")

    def get_kind(self) -> str | None:
        """Get the location kind."""
        return self.get_attribute("kind")

    def get_opened(self) -> bool | None:
        """Get whether the location is opened."""
        return self.get_attribute("opened")

    def get_questions(self) -> str | None:
        """Get the questions."""
        return self.get_attribute("questions")

    def get_age_min_in_months(self) -> int | None:
        """Get the minimum age in months."""
        return self.get_attribute("age_min_in_months")

    def get_age_max_in_months(self) -> int | None:
        """Get the maximum age in months."""
        return self.get_attribute("age_max_in_months")

    def get_age_range_by(self) -> str | None:
        """Get the age range by."""
        return self.get_attribute("age_range_by")

    def get_age_on(self) -> datetime | None:
        """Get the age on date."""
        age_on = self.get_attribute("age_on")
        if age_on:
            return datetime.fromisoformat(age_on.replace("Z", "+00:00"))
        return None

    def get_child_or_adult(self) -> str | None:
        """Get whether it's child or adult."""
        return self.get_attribute("child_or_adult")

    def get_effective_date(self) -> datetime | None:
        """Get the effective date."""
        effective_date = self.get_attribute("effective_date")
        if effective_date:
            return datetime.fromisoformat(effective_date.replace("Z", "+00:00"))
        return None

    def get_gender(self) -> str | None:
        """Get the gender."""
        return self.get_attribute("gender")

    def get_grade_min(self) -> int | None:
        """Get the minimum grade."""
        return self.get_attribute("grade_min")

    def get_grade_max(self) -> int | None:
        """Get the maximum grade."""
        return self.get_attribute("grade_max")

    def get_max_occupancy(self) -> int | None:
        """Get the maximum occupancy."""
        return self.get_attribute("max_occupancy")

    def get_min_volunteers(self) -> int | None:
        """Get the minimum volunteers."""
        return self.get_attribute("min_volunteers")

    def get_attendees_per_volunteer(self) -> int | None:
        """Get the attendees per volunteer."""
        return self.get_attribute("attendees_per_volunteer")

    def get_position(self) -> int | None:
        """Get the position."""
        return self.get_attribute("position")

    def get_milestone(self) -> str | None:
        """Get the milestone."""
        return self.get_attribute("milestone")

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

    def get_parent_id(self) -> str | None:
        """Get the parent ID."""
        parent_data = self.get_relationship_data("parent")
        if parent_data and isinstance(parent_data, dict):
            return parent_data.get("id")
        return None


class PCOLocationEventPeriod(PCOResource):
    """Represents a location event period in Planning Center Check-Ins."""

    def get_regular_count(self) -> int | None:
        """Get the regular count."""
        return self.get_attribute("regular_count")

    def get_guest_count(self) -> int | None:
        """Get the guest count."""
        return self.get_attribute("guest_count")

    def get_volunteer_count(self) -> int | None:
        """Get the volunteer count."""
        return self.get_attribute("volunteer_count")

    def get_created_at(self) -> datetime | None:
        """Get the location event period creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the location event period last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOLocationEventTime(PCOResource):
    """Represents a location event time in Planning Center Check-Ins."""

    def get_regular_count(self) -> int | None:
        """Get the regular count."""
        return self.get_attribute("regular_count")

    def get_guest_count(self) -> int | None:
        """Get the guest count."""
        return self.get_attribute("guest_count")

    def get_volunteer_count(self) -> int | None:
        """Get the volunteer count."""
        return self.get_attribute("volunteer_count")

    def get_created_at(self) -> datetime | None:
        """Get the location event time creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the location event time last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOLocationLabel(PCOResource):
    """Represents a location label in Planning Center Check-Ins."""

    def get_quantity(self) -> int | None:
        """Get the quantity."""
        return self.get_attribute("quantity")

    def get_for_regular(self) -> bool | None:
        """Get whether it's for regular attendees."""
        return self.get_attribute("for_regular")

    def get_for_guest(self) -> bool | None:
        """Get whether it's for guests."""
        return self.get_attribute("for_guest")

    def get_for_volunteer(self) -> bool | None:
        """Get whether it's for volunteers."""
        return self.get_attribute("for_volunteer")

    def get_created_at(self) -> datetime | None:
        """Get the location label creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the location label last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOOption(PCOResource):
    """Represents an option in Planning Center Check-Ins."""

    def get_body(self) -> str | None:
        """Get the option body."""
        return self.get_attribute("body")

    def get_quantity(self) -> int | None:
        """Get the quantity."""
        return self.get_attribute("quantity")

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


class PCOCheckInsOrganization(PCOResource):
    """Represents an organization in Planning Center Check-Ins."""

    def get_date_format_pattern(self) -> str | None:
        """Get the date format pattern."""
        return self.get_attribute("date_format_pattern")

    def get_time_zone(self) -> str | None:
        """Get the time zone."""
        return self.get_attribute("time_zone")

    def get_name(self) -> str | None:
        """Get the organization name."""
        return self.get_attribute("name")

    def get_daily_check_ins(self) -> int | None:
        """Get the daily check-ins count."""
        return self.get_attribute("daily_check_ins")

    def get_avatar_url(self) -> str | None:
        """Get the avatar URL."""
        return self.get_attribute("avatar_url")

    def get_created_at(self) -> datetime | None:
        """Get the organization creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the organization last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOPass(PCOResource):
    """Represents a pass in Planning Center Check-Ins."""

    def get_code(self) -> str | None:
        """Get the pass code."""
        return self.get_attribute("code")

    def get_kind(self) -> str | None:
        """Get the pass kind."""
        return self.get_attribute("kind")

    def get_created_at(self) -> datetime | None:
        """Get the pass creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the pass last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCOCheckInsPerson(PCOResource):
    """Represents a person in Planning Center Check-Ins."""

    def get_addresses(self) -> list | None:
        """Get the addresses."""
        return self.get_attribute("addresses")

    def get_email_addresses(self) -> list | None:
        """Get the email addresses."""
        return self.get_attribute("email_addresses")

    def get_phone_numbers(self) -> list | None:
        """Get the phone numbers."""
        return self.get_attribute("phone_numbers")

    def get_avatar_url(self) -> str | None:
        """Get the avatar URL."""
        return self.get_attribute("avatar_url")

    def get_name_prefix(self) -> str | None:
        """Get the name prefix."""
        return self.get_attribute("name_prefix")

    def get_first_name(self) -> str | None:
        """Get the first name."""
        return self.get_attribute("first_name")

    def get_middle_name(self) -> str | None:
        """Get the middle name."""
        return self.get_attribute("middle_name")

    def get_last_name(self) -> str | None:
        """Get the last name."""
        return self.get_attribute("last_name")

    def get_name_suffix(self) -> str | None:
        """Get the name suffix."""
        return self.get_attribute("name_suffix")

    def get_birthdate(self) -> datetime | None:
        """Get the birthdate."""
        birthdate = self.get_attribute("birthdate")
        if birthdate:
            return datetime.fromisoformat(birthdate.replace("Z", "+00:00"))
        return None

    def get_grade(self) -> int | None:
        """Get the grade."""
        return self.get_attribute("grade")

    def get_gender(self) -> str | None:
        """Get the gender."""
        return self.get_attribute("gender")

    def get_medical_notes(self) -> str | None:
        """Get the medical notes."""
        return self.get_attribute("medical_notes")

    def get_child(self) -> bool | None:
        """Get whether it's a child."""
        return self.get_attribute("child")

    def get_permission(self) -> str | None:
        """Get the permission."""
        return self.get_attribute("permission")

    def get_headcounter(self) -> bool | None:
        """Get whether it's a headcounter."""
        return self.get_attribute("headcounter")

    def get_last_checked_in_at(self) -> datetime | None:
        """Get the last checked in time."""
        last_checked_in_at = self.get_attribute("last_checked_in_at")
        if last_checked_in_at:
            return datetime.fromisoformat(last_checked_in_at.replace("Z", "+00:00"))
        return None

    def get_check_in_count(self) -> int | None:
        """Get the check-in count."""
        return self.get_attribute("check_in_count")

    def get_passed_background_check(self) -> bool | None:
        """Get whether background check was passed."""
        return self.get_attribute("passed_background_check")

    def get_demographic_avatar_url(self) -> str | None:
        """Get the demographic avatar URL."""
        return self.get_attribute("demographic_avatar_url")

    def get_name(self) -> str | None:
        """Get the full name."""
        return self.get_attribute("name")

    def get_top_permission(self) -> str | None:
        """Get the top permission."""
        return self.get_attribute("top_permission")

    def get_ignore_filters(self) -> bool | None:
        """Get whether to ignore filters."""
        return self.get_attribute("ignore_filters")

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


class PCOPersonEvent(PCOResource):
    """Represents a person event in Planning Center Check-Ins."""

    def get_check_in_count(self) -> int | None:
        """Get the check-in count."""
        return self.get_attribute("check_in_count")

    def get_created_at(self) -> datetime | None:
        """Get the person event creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the person event last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOPreCheck(PCOResource):
    """Represents a pre-check in Planning Center Check-Ins."""

    pass  # No specific attributes defined in the API


class PCORosterListPerson(PCOResource):
    """Represents a roster list person in Planning Center Check-Ins."""

    def get_first_name(self) -> str | None:
        """Get the first name."""
        return self.get_attribute("first_name")

    def get_last_name(self) -> str | None:
        """Get the last name."""
        return self.get_attribute("last_name")

    def get_name(self) -> str | None:
        """Get the full name."""
        return self.get_attribute("name")

    def get_demographic_avatar_url(self) -> str | None:
        """Get the demographic avatar URL."""
        return self.get_attribute("demographic_avatar_url")

    def get_grade(self) -> str | None:
        """Get the grade."""
        return self.get_attribute("grade")

    def get_gender(self) -> str | None:
        """Get the gender."""
        return self.get_attribute("gender")

    def get_medical_notes(self) -> str | None:
        """Get the medical notes."""
        return self.get_attribute("medical_notes")

    def get_birthdate(self) -> datetime | None:
        """Get the birthdate."""
        birthdate = self.get_attribute("birthdate")
        if birthdate:
            return datetime.fromisoformat(birthdate.replace("Z", "+00:00"))
        return None


class PCOStation(PCOResource):
    """Represents a station in Planning Center Check-Ins."""

    def get_online(self) -> bool | None:
        """Get whether the station is online."""
        return self.get_attribute("online")

    def get_mode(self) -> int | None:
        """Get the station mode."""
        return self.get_attribute("mode")

    def get_name(self) -> str | None:
        """Get the station name."""
        return self.get_attribute("name")

    def get_timeout_seconds(self) -> int | None:
        """Get the timeout seconds."""
        return self.get_attribute("timeout_seconds")

    def get_input_type(self) -> str | None:
        """Get the input type."""
        return self.get_attribute("input_type")

    def get_input_type_options(self) -> str | None:
        """Get the input type options."""
        return self.get_attribute("input_type_options")

    def get_next_shows_at(self) -> datetime | None:
        """Get the next shows at time."""
        next_shows_at = self.get_attribute("next_shows_at")
        if next_shows_at:
            return datetime.fromisoformat(next_shows_at.replace("Z", "+00:00"))
        return None

    def get_open_for_check_in(self) -> bool | None:
        """Get whether it's open for check-in."""
        return self.get_attribute("open_for_check_in")

    def get_closes_at(self) -> datetime | None:
        """Get the closes at time."""
        closes_at = self.get_attribute("closes_at")
        if closes_at:
            return datetime.fromisoformat(closes_at.replace("Z", "+00:00"))
        return None

    def get_check_in_count(self) -> int | None:
        """Get the check-in count."""
        return self.get_attribute("check_in_count")

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

    def get_print_station_id(self) -> str | None:
        """Get the print station ID."""
        print_station_data = self.get_relationship_data("print_station")
        if print_station_data and isinstance(print_station_data, dict):
            return print_station_data.get("id")
        return None

    def get_theme_id(self) -> str | None:
        """Get the theme ID."""
        theme_data = self.get_relationship_data("theme")
        if theme_data and isinstance(theme_data, dict):
            return theme_data.get("id")
        return None


class PCOTheme(PCOResource):
    """Represents a theme in Planning Center Check-Ins."""

    def get_image_thumbnail(self) -> str | None:
        """Get the image thumbnail."""
        return self.get_attribute("image_thumbnail")

    def get_name(self) -> str | None:
        """Get the theme name."""
        return self.get_attribute("name")

    def get_color(self) -> str | None:
        """Get the theme color."""
        return self.get_attribute("color")

    def get_text_color(self) -> str | None:
        """Get the text color."""
        return self.get_attribute("text_color")

    def get_image(self) -> str | None:
        """Get the image."""
        return self.get_attribute("image")

    def get_background_color(self) -> str | None:
        """Get the background color."""
        return self.get_attribute("background_color")

    def get_mode(self) -> str | None:
        """Get the theme mode."""
        return self.get_attribute("mode")

    def get_created_at(self) -> datetime | None:
        """Get the theme creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the theme last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


