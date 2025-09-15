"""Groups product models for Planning Center API."""

from datetime import datetime

from ..models.base import PCOResource


class PCOAttendance(PCOResource):
    """Represents attendance in Planning Center Groups."""

    def get_attended(self) -> bool | None:
        """Get whether the person attended the event."""
        return self.get_attribute("attended")

    def get_role(self) -> str | None:
        """Get the role of the person at the time of event (member, leader, visitor, or applicant)."""
        return self.get_attribute("role")

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_event_id(self) -> str | None:
        """Get the event ID."""
        event_data = self.get_relationship_data("event")
        if event_data and isinstance(event_data, dict):
            return event_data.get("id")
        return None


class PCOGroupCampus(PCOResource):
    """Represents a campus in Planning Center Groups."""

    def get_name(self) -> str | None:
        """Get the campus name."""
        return self.get_attribute("name")


class PCOEnrollment(PCOResource):
    """Represents enrollment details for a group in Planning Center Groups."""

    def get_auto_closed(self) -> bool | None:
        """Get whether enrollment has been closed automatically due to set limits."""
        return self.get_attribute("auto_closed")

    def get_auto_closed_reason(self) -> str | None:
        """Get the reason enrollment was automatically closed."""
        return self.get_attribute("auto_closed_reason")

    def get_date_limit(self) -> str | None:
        """Get the date when enrollment should automatically close."""
        return self.get_attribute("date_limit")

    def get_date_limit_reached(self) -> bool | None:
        """Get whether the date limit has been reached."""
        return self.get_attribute("date_limit_reached")

    def get_member_limit(self) -> int | None:
        """Get the total number of members allowed before enrollment should automatically close."""
        return self.get_attribute("member_limit")

    def get_member_limit_reached(self) -> bool | None:
        """Get whether the member limit has been reached."""
        return self.get_attribute("member_limit_reached")

    def get_status(self) -> str | None:
        """Get the current enrollment status (open, closed, full, or private)."""
        return self.get_attribute("status")

    def get_strategy(self) -> str | None:
        """Get the sign up strategy (request_to_join, open_signup, or closed)."""
        return self.get_attribute("strategy")

    def get_group_id(self) -> str | None:
        """Get the group ID."""
        group_data = self.get_relationship_data("group")
        if group_data and isinstance(group_data, dict):
            return group_data.get("id")
        return None


class PCOGroupEvent(PCOResource):
    """Represents an event in Planning Center Groups."""

    def get_attendance_requests_enabled(self) -> bool | None:
        """Get whether attendance requests are enabled."""
        return self.get_attribute("attendance_requests_enabled")

    def get_automated_reminder_enabled(self) -> bool | None:
        """Get whether automated reminders are enabled."""
        return self.get_attribute("automated_reminder_enabled")

    def get_canceled(self) -> bool | None:
        """Get whether the event has been canceled."""
        return self.get_attribute("canceled")

    def get_canceled_at(self) -> datetime | None:
        """Get when the event was canceled."""
        canceled_at = self.get_attribute("canceled_at")
        if canceled_at:
            return datetime.fromisoformat(canceled_at.replace("Z", "+00:00"))
        return None

    def get_description(self) -> str | None:
        """Get the event description."""
        return self.get_attribute("description")

    def get_ends_at(self) -> datetime | None:
        """Get when the event ends."""
        ends_at = self.get_attribute("ends_at")
        if ends_at:
            return datetime.fromisoformat(ends_at.replace("Z", "+00:00"))
        return None

    def get_location_type_preference(self) -> str | None:
        """Get the location type preference (physical or virtual)."""
        return self.get_attribute("location_type_preference")

    def get_multi_day(self) -> bool | None:
        """Get whether the event spans multiple days."""
        return self.get_attribute("multi_day")

    def get_name(self) -> str | None:
        """Get the event name."""
        return self.get_attribute("name")

    def get_reminders_sent(self) -> bool | None:
        """Get whether reminders have been sent for this event."""
        return self.get_attribute("reminders_sent")

    def get_reminders_sent_at(self) -> datetime | None:
        """Get when reminders were sent for this event."""
        reminders_sent_at = self.get_attribute("reminders_sent_at")
        if reminders_sent_at:
            return datetime.fromisoformat(reminders_sent_at.replace("Z", "+00:00"))
        return None

    def get_repeating(self) -> bool | None:
        """Get whether the event is a repeating event."""
        return self.get_attribute("repeating")

    def get_starts_at(self) -> datetime | None:
        """Get when the event starts."""
        starts_at = self.get_attribute("starts_at")
        if starts_at:
            return datetime.fromisoformat(starts_at.replace("Z", "+00:00"))
        return None

    def get_virtual_location_url(self) -> str | None:
        """Get the URL for the virtual location."""
        return self.get_attribute("virtual_location_url")

    def get_visitors_count(self) -> int | None:
        """Get the number of visitors who attended the event."""
        return self.get_attribute("visitors_count")

    def get_attendance_submitter_id(self) -> str | None:
        """Get the attendance submitter person ID."""
        attendance_submitter_data = self.get_relationship_data("attendance_submitter")
        if attendance_submitter_data and isinstance(attendance_submitter_data, dict):
            return attendance_submitter_data.get("id")
        return None

    def get_group_id(self) -> str | None:
        """Get the group ID."""
        group_data = self.get_relationship_data("group")
        if group_data and isinstance(group_data, dict):
            return group_data.get("id")
        return None

    def get_location_id(self) -> str | None:
        """Get the location ID."""
        location_data = self.get_relationship_data("location")
        if location_data and isinstance(location_data, dict):
            return location_data.get("id")
        return None

    def get_repeating_event_id(self) -> str | None:
        """Get the repeating event ID."""
        repeating_event_data = self.get_relationship_data("repeating_event")
        if repeating_event_data and isinstance(repeating_event_data, dict):
            return repeating_event_data.get("id")
        return None


class PCOEventNote(PCOResource):
    """Represents an event note in Planning Center Groups."""

    def get_body(self) -> str | None:
        """Get the note body text."""
        return self.get_attribute("body")

    def get_annotatable_id(self) -> str | None:
        """Get the annotatable ID."""
        annotatable_data = self.get_relationship_data("annotatable")
        if annotatable_data and isinstance(annotatable_data, dict):
            return annotatable_data.get("id")
        return None

    def get_owner_id(self) -> str | None:
        """Get the owner ID."""
        owner_data = self.get_relationship_data("owner")
        if owner_data and isinstance(owner_data, dict):
            return owner_data.get("id")
        return None


class PCOGroup(PCOResource):
    """Represents a group in Planning Center Groups."""

    def get_archived_at(self) -> datetime | None:
        """Get when the group was archived."""
        archived_at = self.get_attribute("archived_at")
        if archived_at:
            return datetime.fromisoformat(archived_at.replace("Z", "+00:00"))
        return None

    def get_can_create_conversation(self) -> bool | None:
        """Get whether the current user can create a conversation in the group."""
        return self.get_attribute("can_create_conversation")

    def get_chat_enabled(self) -> bool | None:
        """Get whether the group has Chat enabled."""
        return self.get_attribute("chat_enabled")

    def get_contact_email(self) -> str | None:
        """Get the contact email for the group."""
        return self.get_attribute("contact_email")

    def get_created_at(self) -> datetime | None:
        """Get when the group was created."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_description(self) -> str | None:
        """Get the group description."""
        return self.get_attribute("description")

    def get_events_visibility(self) -> str | None:
        """Get the visibility of events for the group (public or members)."""
        return self.get_attribute("events_visibility")

    def get_header_image(self) -> dict | None:
        """Get the header image hash with thumbnail, medium, and original URLs."""
        return self.get_attribute("header_image")

    def get_leaders_can_search_people_database(self) -> bool | None:
        """Get whether group leaders can search the entire church database."""
        return self.get_attribute("leaders_can_search_people_database")

    def get_location_type_preference(self) -> str | None:
        """Get the location type preference (physical or virtual)."""
        return self.get_attribute("location_type_preference")

    def get_members_are_confidential(self) -> bool | None:
        """Get whether group members can see other members' info."""
        return self.get_attribute("members_are_confidential")

    def get_memberships_count(self) -> int | None:
        """Get the number of members in the group."""
        return self.get_attribute("memberships_count")

    def get_name(self) -> str | None:
        """Get the group name."""
        return self.get_attribute("name")

    def get_public_church_center_web_url(self) -> str | None:
        """Get the public URL for the group on Church Center."""
        return self.get_attribute("public_church_center_web_url")

    def get_schedule(self) -> str | None:
        """Get the group's typical meeting schedule."""
        return self.get_attribute("schedule")

    def get_tag_ids(self) -> int | None:
        """Get the IDs of the tags associated with the group."""
        return self.get_attribute("tag_ids")

    def get_virtual_location_url(self) -> str | None:
        """Get the URL for the group's virtual location."""
        return self.get_attribute("virtual_location_url")

    def get_widget_status(self) -> dict | None:
        """Get the widget status (deprecated)."""
        return self.get_attribute("widget_status")

    def get_group_type_id(self) -> str | None:
        """Get the group type ID."""
        group_type_data = self.get_relationship_data("group_type")
        if group_type_data and isinstance(group_type_data, dict):
            return group_type_data.get("id")
        return None

    def get_location_id(self) -> str | None:
        """Get the location ID."""
        location_data = self.get_relationship_data("location")
        if location_data and isinstance(location_data, dict):
            return location_data.get("id")
        return None


class PCOGroupApplication(PCOResource):
    """Represents a group application in Planning Center Groups."""

    def get_applied_at(self) -> datetime | None:
        """Get when this person applied."""
        applied_at = self.get_attribute("applied_at")
        if applied_at:
            return datetime.fromisoformat(applied_at.replace("Z", "+00:00"))
        return None

    def get_message(self) -> str | None:
        """Get the optional personal message from the applicant."""
        return self.get_attribute("message")

    def get_status(self) -> str | None:
        """Get the approval status (pending, approved, or rejected)."""
        return self.get_attribute("status")

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


class PCOGroupType(PCOResource):
    """Represents a group type in Planning Center Groups."""

    def get_church_center_visible(self) -> bool | None:
        """Get whether the group type contains any published groups."""
        return self.get_attribute("church_center_visible")

    def get_church_center_map_visible(self) -> bool | None:
        """Get whether the map view is visible on the public groups list page."""
        return self.get_attribute("church_center_map_visible")

    def get_color(self) -> str | None:
        """Get the hex color value."""
        return self.get_attribute("color")

    def get_default_group_settings(self) -> str | None:
        """Get the JSON object of default settings for groups of this type."""
        return self.get_attribute("default_group_settings")

    def get_description(self) -> str | None:
        """Get the group type description."""
        return self.get_attribute("description")

    def get_name(self) -> str | None:
        """Get the group type name."""
        return self.get_attribute("name")

    def get_position(self) -> int | None:
        """Get the position of the group type in relation to other group types."""
        return self.get_attribute("position")

    def get_public_church_center_web_url(self) -> str | None:
        """Get the public URL for the group on Church Center."""
        return self.get_attribute("public_church_center_web_url")


class PCOGroupLocation(PCOResource):
    """Represents a physical event location in Planning Center Groups."""

    def get_display_preference(self) -> str | None:
        """Get the display preference (hidden, approximate, or exact)."""
        return self.get_attribute("display_preference")

    def get_full_formatted_address(self) -> str | None:
        """Get the full formatted address."""
        return self.get_attribute("full_formatted_address")

    def get_latitude(self) -> float | None:
        """Get the latitude coordinate."""
        return self.get_attribute("latitude")

    def get_longitude(self) -> float | None:
        """Get the longitude coordinate."""
        return self.get_attribute("longitude")

    def get_name(self) -> str | None:
        """Get the location name."""
        return self.get_attribute("name")

    def get_radius(self) -> str | None:
        """Get the number of miles in a location's approximate address."""
        return self.get_attribute("radius")

    def get_strategy(self) -> str | None:
        """Get the display preference strategy (hidden, approximate, or exact)."""
        return self.get_attribute("strategy")

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


class PCOMembership(PCOResource):
    """Represents a membership in Planning Center Groups."""

    def get_joined_at(self) -> datetime | None:
        """Get when the person joined the group."""
        joined_at = self.get_attribute("joined_at")
        if joined_at:
            return datetime.fromisoformat(joined_at.replace("Z", "+00:00"))
        return None

    def get_role(self) -> str | None:
        """Get the role of the person in the group (member or leader)."""
        return self.get_attribute("role")

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


class PCOGroupOrganization(PCOResource):
    """Represents an organization in Planning Center Groups."""

    def get_name(self) -> str | None:
        """Get the organization name."""
        return self.get_attribute("name")

    def get_time_zone(self) -> str | None:
        """Get the organization time zone."""
        return self.get_attribute("time_zone")


class PCOOwner(PCOResource):
    """Represents the owner/creator of an event note in Planning Center Groups."""

    def get_avatar_url(self) -> str | None:
        """Get the URL of the person's avatar."""
        return self.get_attribute("avatar_url")

    def get_first_name(self) -> str | None:
        """Get the person's first name."""
        return self.get_attribute("first_name")

    def get_last_name(self) -> str | None:
        """Get the person's last name."""
        return self.get_attribute("last_name")


class PCOGroupPerson(PCOResource):
    """Represents a person in Planning Center Groups."""

    def get_addresses(self) -> list[dict] | None:
        """Get all the addresses associated with this person."""
        return self.get_attribute("addresses")

    def get_avatar_url(self) -> str | None:
        """Get the URL of the person's avatar."""
        return self.get_attribute("avatar_url")

    def get_child(self) -> bool | None:
        """Get whether the person is under 13 years old."""
        return self.get_attribute("child")

    def get_created_at(self) -> datetime | None:
        """Get when this person was first created in Planning Center."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_email_addresses(self) -> list[dict] | None:
        """Get all the email addresses associated with this person."""
        return self.get_attribute("email_addresses")

    def get_first_name(self) -> str | None:
        """Get the person's first name."""
        return self.get_attribute("first_name")

    def get_last_name(self) -> str | None:
        """Get the person's last name."""
        return self.get_attribute("last_name")

    def get_permissions(self) -> str | None:
        """Get the person's permissions (administrator, group_type_manager, leader, member, or no access)."""
        return self.get_attribute("permissions")

    def get_phone_numbers(self) -> list[dict] | None:
        """Get all the phone numbers associated with this person."""
        return self.get_attribute("phone_numbers")


class PCOGroupResource(PCOResource):
    """Represents a file or link resource in Planning Center Groups."""

    def get_description(self) -> str | None:
        """Get the description of the resource."""
        return self.get_attribute("description")

    def get_last_updated(self) -> datetime | None:
        """Get when the resource was last updated."""
        last_updated = self.get_attribute("last_updated")
        if last_updated:
            return datetime.fromisoformat(last_updated.replace("Z", "+00:00"))
        return None

    def get_name(self) -> str | None:
        """Get the name/title of the resource."""
        return self.get_attribute("name")

    def get_type(self) -> str | None:
        """Get the resource type (FileResource or LinkResource)."""
        return self.get_attribute("type")

    def get_visibility(self) -> str | None:
        """Get the visibility (leaders or members)."""
        return self.get_attribute("visibility")

    def get_created_by_id(self) -> str | None:
        """Get the ID of the person who created this resource."""
        created_by_data = self.get_relationship_data("created_by")
        if created_by_data and isinstance(created_by_data, dict):
            return created_by_data.get("id")
        return None


class PCOGroupTag(PCOResource):
    """Represents a tag in Planning Center Groups."""

    def get_name(self) -> str | None:
        """Get the tag name."""
        return self.get_attribute("name")

    def get_position(self) -> int | None:
        """Get the position of the tag in relation to other tags."""
        return self.get_attribute("position")

    def get_tag_group_id(self) -> str | None:
        """Get the tag group ID."""
        tag_group_data = self.get_relationship_data("tag_group")
        if tag_group_data and isinstance(tag_group_data, dict):
            return tag_group_data.get("id")
        return None


class PCOGroupTagGroup(PCOResource):
    """Represents a tag group in Planning Center Groups."""

    def get_display_publicly(self) -> bool | None:
        """Get whether this tag group is visible to the public on Church Center."""
        return self.get_attribute("display_publicly")

    def get_multiple_options_enabled(self) -> bool | None:
        """Get whether a group can belong to many tags within this tag group."""
        return self.get_attribute("multiple_options_enabled")

    def get_name(self) -> str | None:
        """Get the tag group name."""
        return self.get_attribute("name")

    def get_position(self) -> int | None:
        """Get the position of the tag group in relation to other tag groups."""
        return self.get_attribute("position")


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
