"""Calendar product models for Planning Center API."""

from datetime import datetime

from ..models.base import PCOResource


class PCOEvent(PCOResource):
    """Represents an event in Planning Center Calendar."""

    def get_name(self) -> str | None:
        """Get the event name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the event description."""
        return self.get_attribute("description")

    def get_summary(self) -> str | None:
        """Get the event summary."""
        return self.get_attribute("summary")

    def get_approval_status(self) -> str | None:
        """Get the approval status (A: approved, P: pending, R: rejected)."""
        return self.get_attribute("approval_status")

    def get_featured(self) -> bool | None:
        """Get whether the event is featured on Church Center."""
        return self.get_attribute("featured")

    def get_image_url(self) -> str | None:
        """Get the event image URL."""
        return self.get_attribute("image_url")

    def get_percent_approved(self) -> int | None:
        """Get the percent approved."""
        return self.get_attribute("percent_approved")

    def get_percent_rejected(self) -> int | None:
        """Get the percent rejected."""
        return self.get_attribute("percent_rejected")

    def get_registration_url(self) -> str | None:
        """Get the registration URL."""
        return self.get_attribute("registration_url")

    def get_visible_in_church_center(self) -> bool | None:
        """Get whether the event is visible in Church Center."""
        return self.get_attribute("visible_in_church_center")

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

    def get_owner_id(self) -> str | None:
        """Get the owner person ID."""
        owner_data = self.get_relationship_data("owner")
        if owner_data and isinstance(owner_data, dict):
            return owner_data.get("id")
        return None


class PCOEventInstance(PCOResource):
    """Represents an event instance in Planning Center Calendar."""

    def get_name(self) -> str | None:
        """Get the event instance name."""
        return self.get_attribute("name")

    def get_all_day_event(self) -> bool | None:
        """Get whether the event instance lasts all day."""
        return self.get_attribute("all_day_event")

    def get_compact_recurrence_description(self) -> str | None:
        """Get the compact recurrence description."""
        return self.get_attribute("compact_recurrence_description")

    def get_ends_at(self) -> datetime | None:
        """Get the event instance end time."""
        ends_at = self.get_attribute("ends_at")
        if ends_at:
            return datetime.fromisoformat(ends_at.replace("Z", "+00:00"))
        return None

    def get_location(self) -> str | None:
        """Get the event instance location."""
        return self.get_attribute("location")

    def get_recurrence(self) -> str | None:
        """Get the recurrence pattern."""
        return self.get_attribute("recurrence")

    def get_recurrence_description(self) -> str | None:
        """Get the recurrence description."""
        return self.get_attribute("recurrence_description")

    def get_starts_at(self) -> datetime | None:
        """Get the event instance start time."""
        starts_at = self.get_attribute("starts_at")
        if starts_at:
            return datetime.fromisoformat(starts_at.replace("Z", "+00:00"))
        return None

    def get_church_center_url(self) -> str | None:
        """Get the Church Center URL."""
        return self.get_attribute("church_center_url")

    def get_published_starts_at(self) -> str | None:
        """Get the published start time."""
        return self.get_attribute("published_starts_at")

    def get_published_ends_at(self) -> str | None:
        """Get the published end time."""
        return self.get_attribute("published_ends_at")

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

    def get_name(self) -> str | None:
        """Get the event time name."""
        return self.get_attribute("name")

    def get_ends_at(self) -> datetime | None:
        """Get the event time end."""
        ends_at = self.get_attribute("ends_at")
        if ends_at:
            return datetime.fromisoformat(ends_at.replace("Z", "+00:00"))
        return None

    def get_starts_at(self) -> datetime | None:
        """Get the event time start."""
        starts_at = self.get_attribute("starts_at")
        if starts_at:
            return datetime.fromisoformat(starts_at.replace("Z", "+00:00"))
        return None

    def get_visible_on_kiosks(self) -> bool | None:
        """Get whether the time is visible on kiosks."""
        return self.get_attribute("visible_on_kiosks")

    def get_visible_on_widget_and_ical(self) -> bool | None:
        """Get whether the time is visible on widget or iCal."""
        return self.get_attribute("visible_on_widget_and_ical")

    def get_event_id(self) -> str | None:
        """Get the event ID."""
        event_data = self.get_relationship_data("event")
        if event_data and isinstance(event_data, dict):
            return event_data.get("id")
        return None


class PCOAttachment(PCOResource):
    """Represents an attachment in Planning Center Calendar."""

    def get_content_type(self) -> str | None:
        """Get the attachment content type."""
        return self.get_attribute("content_type")

    def get_description(self) -> str | None:
        """Get the attachment description."""
        return self.get_attribute("description")

    def get_file_size(self) -> int | None:
        """Get the attachment file size in bytes."""
        return self.get_attribute("file_size")

    def get_name(self) -> str | None:
        """Get the attachment name."""
        return self.get_attribute("name")

    def get_url(self) -> str | None:
        """Get the attachment URL."""
        return self.get_attribute("url")

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


class PCOConflict(PCOResource):
    """Represents a conflict between two events in Planning Center Calendar."""

    def get_note(self) -> str | None:
        """Get the conflict note."""
        return self.get_attribute("note")

    def get_resolved_at(self) -> datetime | None:
        """Get when the conflict was resolved."""
        resolved_at = self.get_attribute("resolved_at")
        if resolved_at:
            return datetime.fromisoformat(resolved_at.replace("Z", "+00:00"))
        return None

    def get_created_at(self) -> datetime | None:
        """Get the conflict creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the conflict last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_resource_id(self) -> str | None:
        """Get the resource ID."""
        resource_data = self.get_relationship_data("resource")
        if resource_data and isinstance(resource_data, dict):
            return resource_data.get("id")
        return None

    def get_resolved_by_id(self) -> str | None:
        """Get the resolved by person ID."""
        resolved_by_data = self.get_relationship_data("resolved_by")
        if resolved_by_data and isinstance(resolved_by_data, dict):
            return resolved_by_data.get("id")
        return None

    def get_winner_id(self) -> str | None:
        """Get the winner event ID."""
        winner_data = self.get_relationship_data("winner")
        if winner_data and isinstance(winner_data, dict):
            return winner_data.get("id")
        return None


class PCOEventConnection(PCOResource):
    """Represents a connection between a Calendar event and a record in another product."""

    def get_connected_to_id(self) -> str | None:
        """Get the connected record ID."""
        return self.get_attribute("connected_to_id")

    def get_connected_to_name(self) -> str | None:
        """Get the connected record name."""
        return self.get_attribute("connected_to_name")

    def get_connected_to_type(self) -> str | None:
        """Get the connected record type."""
        return self.get_attribute("connected_to_type")

    def get_product_name(self) -> str | None:
        """Get the product name."""
        return self.get_attribute("product_name")

    def get_connected_to_url(self) -> str | None:
        """Get the connected record URL."""
        return self.get_attribute("connected_to_url")

    def get_promoted(self) -> bool | None:
        """Get whether this connection is promoted for display."""
        return self.get_attribute("promoted")

    def get_event_id(self) -> str | None:
        """Get the event ID."""
        event_data = self.get_relationship_data("event")
        if event_data and isinstance(event_data, dict):
            return event_data.get("id")
        return None


class PCOEventResourceAnswer(PCOResource):
    """Represents an answer to a question in a room or resource request."""

    def get_answer(self) -> dict | None:
        """Get the answer formatted for display."""
        return self.get_attribute("answer")

    def get_db_answer(self) -> str | None:
        """Get the database answer."""
        return self.get_attribute("db_answer")

    def get_question(self) -> dict | None:
        """Get the question details."""
        return self.get_attribute("question")

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

    def get_created_by_id(self) -> str | None:
        """Get the created by person ID."""
        created_by_data = self.get_relationship_data("created_by")
        if created_by_data and isinstance(created_by_data, dict):
            return created_by_data.get("id")
        return None

    def get_updated_by_id(self) -> str | None:
        """Get the updated by person ID."""
        updated_by_data = self.get_relationship_data("updated_by")
        if updated_by_data and isinstance(updated_by_data, dict):
            return updated_by_data.get("id")
        return None

    def get_resource_question_id(self) -> str | None:
        """Get the resource question ID."""
        resource_question_data = self.get_relationship_data("resource_question")
        if resource_question_data and isinstance(resource_question_data, dict):
            return resource_question_data.get("id")
        return None

    def get_event_resource_request_id(self) -> str | None:
        """Get the event resource request ID."""
        event_resource_request_data = self.get_relationship_data(
            "event_resource_request"
        )
        if event_resource_request_data and isinstance(
            event_resource_request_data, dict
        ):
            return event_resource_request_data.get("id")
        return None


class PCOEventResourceRequest(PCOResource):
    """Represents a room or resource request for a specific event."""

    def get_approval_sent(self) -> bool | None:
        """Get whether approval email has been sent."""
        return self.get_attribute("approval_sent")

    def get_approval_status(self) -> str | None:
        """Get the approval status (A: approved, P: pending, R: rejected)."""
        return self.get_attribute("approval_status")

    def get_notes(self) -> str | None:
        """Get the request notes."""
        return self.get_attribute("notes")

    def get_quantity(self) -> int | None:
        """Get the quantity requested."""
        return self.get_attribute("quantity")

    def get_visible_on_kiosks(self) -> bool | None:
        """Get whether visible on kiosks."""
        return self.get_attribute("visible_on_kiosks")

    def get_created_at(self) -> datetime | None:
        """Get the request creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the request last update time."""
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

    def get_resource_id(self) -> str | None:
        """Get the resource ID."""
        resource_data = self.get_relationship_data("resource")
        if resource_data and isinstance(resource_data, dict):
            return resource_data.get("id")
        return None

    def get_created_by_id(self) -> str | None:
        """Get the created by person ID."""
        created_by_data = self.get_relationship_data("created_by")
        if created_by_data and isinstance(created_by_data, dict):
            return created_by_data.get("id")
        return None

    def get_updated_by_id(self) -> str | None:
        """Get the updated by person ID."""
        updated_by_data = self.get_relationship_data("updated_by")
        if updated_by_data and isinstance(updated_by_data, dict):
            return updated_by_data.get("id")
        return None

    def get_room_setup_id(self) -> str | None:
        """Get the room setup ID."""
        room_setup_data = self.get_relationship_data("room_setup")
        if room_setup_data and isinstance(room_setup_data, dict):
            return room_setup_data.get("id")
        return None


class PCOFeed(PCOResource):
    """Represents a feed belonging to an organization."""

    def get_can_delete(self) -> bool | None:
        """Get whether the feed can be deleted."""
        return self.get_attribute("can_delete")

    def get_default_church_center_visibility(self) -> str | None:
        """Get the default Church Center visibility."""
        return self.get_attribute("default_church_center_visibility")

    def get_feed_type(self) -> str | None:
        """Get the feed type."""
        return self.get_attribute("feed_type")

    def get_imported_at(self) -> datetime | None:
        """Get when the feed was imported."""
        imported_at = self.get_attribute("imported_at")
        if imported_at:
            return datetime.fromisoformat(imported_at.replace("Z", "+00:00"))
        return None

    def get_name(self) -> str | None:
        """Get the feed name."""
        return self.get_attribute("name")

    def get_deleting(self) -> bool | None:
        """Get whether the feed is being deleted."""
        return self.get_attribute("deleting")

    def get_sync_campus_tags(self) -> bool | None:
        """Get whether to sync campus tags."""
        return self.get_attribute("sync_campus_tags")

    def get_source_id(self) -> str | None:
        """Get the source ID."""
        return self.get_attribute("source_id")

    def get_event_owner_id(self) -> str | None:
        """Get the event owner person ID."""
        event_owner_data = self.get_relationship_data("event_owner")
        if event_owner_data and isinstance(event_owner_data, dict):
            return event_owner_data.get("id")
        return None


class PCOJobStatus(PCOResource):
    """Represents a job status."""

    def get_retries(self) -> int | None:
        """Get the number of retries."""
        return self.get_attribute("retries")

    def get_errors(self) -> dict | None:
        """Get the errors."""
        return self.get_attribute("errors")

    def get_message(self) -> str | None:
        """Get the status message."""
        return self.get_attribute("message")

    def get_started_at(self) -> datetime | None:
        """Get when the job started."""
        started_at = self.get_attribute("started_at")
        if started_at:
            return datetime.fromisoformat(started_at.replace("Z", "+00:00"))
        return None

    def get_status(self) -> str | None:
        """Get the job status."""
        return self.get_attribute("status")


class PCOOrganization(PCOResource):
    """Represents an organization in Planning Center Calendar."""

    def get_name(self) -> str | None:
        """Get the organization name."""
        return self.get_attribute("name")

    def get_time_zone(self) -> str | None:
        """Get the organization time zone."""
        return self.get_attribute("time_zone")

    def get_twenty_four_hour_time(self) -> bool | None:
        """Get whether to use 24-hour time format."""
        return self.get_attribute("twenty_four_hour_time")

    def get_date_format(self) -> str | None:
        """Get the date format."""
        return self.get_attribute("date_format")

    def get_onboarding(self) -> bool | None:
        """Get whether onboarding is active."""
        return self.get_attribute("onboarding")

    def get_calendar_starts_on(self) -> str | None:
        """Get the day of the week the calendar starts on."""
        return self.get_attribute("calendar_starts_on")


class PCOPerson(PCOResource):
    """Represents a person in Planning Center Calendar."""

    def get_first_name(self) -> str | None:
        """Get the person's first name."""
        return self.get_attribute("first_name")

    def get_last_name(self) -> str | None:
        """Get the person's last name."""
        return self.get_attribute("last_name")

    def get_middle_name(self) -> str | None:
        """Get the person's middle name."""
        return self.get_attribute("middle_name")

    def get_avatar_url(self) -> str | None:
        """Get the person's avatar URL."""
        return self.get_attribute("avatar_url")

    def get_child(self) -> bool | None:
        """Get whether the person is a child."""
        return self.get_attribute("child")

    def get_contact_data(self) -> str | None:
        """Get the person's contact data."""
        return self.get_attribute("contact_data")

    def get_gender(self) -> str | None:
        """Get the person's gender."""
        return self.get_attribute("gender")

    def get_has_access(self) -> bool | None:
        """Get whether the person has access to Calendar."""
        return self.get_attribute("has_access")

    def get_name_prefix(self) -> str | None:
        """Get the person's name prefix."""
        return self.get_attribute("name_prefix")

    def get_name_suffix(self) -> str | None:
        """Get the person's name suffix."""
        return self.get_attribute("name_suffix")

    def get_pending_request_count(self) -> int | None:
        """Get the number of pending requests."""
        return self.get_attribute("pending_request_count")

    def get_permissions(self) -> int | None:
        """Get the person's permissions."""
        return self.get_attribute("permissions")

    def get_resolves_conflicts(self) -> bool | None:
        """Get whether the person can resolve conflicts."""
        return self.get_attribute("resolves_conflicts")

    def get_site_administrator(self) -> bool | None:
        """Get whether the person is a site administrator."""
        return self.get_attribute("site_administrator")

    def get_status(self) -> str | None:
        """Get the person's status."""
        return self.get_attribute("status")

    def get_can_edit_people(self) -> bool | None:
        """Get whether the person can edit other people."""
        return self.get_attribute("can_edit_people")

    def get_can_edit_resources(self) -> bool | None:
        """Get whether the person can edit resources."""
        return self.get_attribute("can_edit_resources")

    def get_can_edit_rooms(self) -> bool | None:
        """Get whether the person can edit rooms."""
        return self.get_attribute("can_edit_rooms")

    def get_event_permissions_type(self) -> str | None:
        """Get the person's event permissions type."""
        return self.get_attribute("event_permissions_type")

    def get_member_of_approval_groups(self) -> bool | None:
        """Get whether the person is a member of approval groups."""
        return self.get_attribute("member_of_approval_groups")

    def get_name(self) -> str | None:
        """Get the person's full name."""
        return self.get_attribute("name")

    def get_people_permissions_type(self) -> str | None:
        """Get the person's people permissions type."""
        return self.get_attribute("people_permissions_type")

    def get_room_permissions_type(self) -> str | None:
        """Get the person's room permissions type."""
        return self.get_attribute("room_permissions_type")

    def get_resources_permissions_type(self) -> str | None:
        """Get the person's resources permissions type."""
        return self.get_attribute("resources_permissions_type")

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


class PCOReportTemplate(PCOResource):
    """Represents a report template."""

    def get_body(self) -> str | None:
        """Get the report template body."""
        return self.get_attribute("body")

    def get_description(self) -> str | None:
        """Get the report template description."""
        return self.get_attribute("description")

    def get_title(self) -> str | None:
        """Get the report template title."""
        return self.get_attribute("title")

    def get_created_at(self) -> str | None:
        """Get the report template creation time."""
        return self.get_attribute("created_at")

    def get_updated_at(self) -> str | None:
        """Get the report template last update time."""
        return self.get_attribute("updated_at")


class PCORequiredApproval(PCOResource):
    """Represents the relationship between a Resource and a Resource Approval Group."""

    def get_resource_id(self) -> str | None:
        """Get the resource ID."""
        resource_data = self.get_relationship_data("resource")
        if resource_data and isinstance(resource_data, dict):
            return resource_data.get("id")
        return None


class PCOResource(PCOResource):
    """Represents a room or resource that can be requested for use as part of an event."""

    def get_kind(self) -> str | None:
        """Get the resource kind (Room or Resource)."""
        return self.get_attribute("kind")

    def get_name(self) -> str | None:
        """Get the resource name."""
        return self.get_attribute("name")

    def get_serial_number(self) -> str | None:
        """Get the resource serial number."""
        return self.get_attribute("serial_number")

    def get_description(self) -> str | None:
        """Get the resource description."""
        return self.get_attribute("description")

    def get_expires_at(self) -> datetime | None:
        """Get when the resource expires."""
        expires_at = self.get_attribute("expires_at")
        if expires_at:
            return datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        return None

    def get_home_location(self) -> str | None:
        """Get the resource home location."""
        return self.get_attribute("home_location")

    def get_image(self) -> str | None:
        """Get the resource image."""
        return self.get_attribute("image")

    def get_quantity(self) -> int | None:
        """Get the resource quantity."""
        return self.get_attribute("quantity")

    def get_path_name(self) -> str | None:
        """Get the resource path name."""
        return self.get_attribute("path_name")

    def get_created_at(self) -> datetime | None:
        """Get the resource creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the resource last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOResourceApprovalGroup(PCOResource):
    """Represents a group of people that can be attached to a room or resource for approval."""

    def get_name(self) -> str | None:
        """Get the approval group name."""
        return self.get_attribute("name")

    def get_form_count(self) -> int | None:
        """Get the number of forms in the approval group."""
        return self.get_attribute("form_count")

    def get_resource_count(self) -> int | None:
        """Get the number of resources in the approval group."""
        return self.get_attribute("resource_count")

    def get_room_count(self) -> int | None:
        """Get the number of rooms in the approval group."""
        return self.get_attribute("room_count")

    def get_created_at(self) -> datetime | None:
        """Get the approval group creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the approval group last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOResourceBooking(PCOResource):
    """Represents a specific booking of a room or resource for an event instance."""

    def get_ends_at(self) -> datetime | None:
        """Get when the booking ends."""
        ends_at = self.get_attribute("ends_at")
        if ends_at:
            return datetime.fromisoformat(ends_at.replace("Z", "+00:00"))
        return None

    def get_starts_at(self) -> datetime | None:
        """Get when the booking starts."""
        starts_at = self.get_attribute("starts_at")
        if starts_at:
            return datetime.fromisoformat(starts_at.replace("Z", "+00:00"))
        return None

    def get_quantity(self) -> int | None:
        """Get the quantity booked."""
        return self.get_attribute("quantity")

    def get_created_at(self) -> datetime | None:
        """Get the booking creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the booking last update time."""
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

    def get_event_instance_id(self) -> str | None:
        """Get the event instance ID."""
        event_instance_data = self.get_relationship_data("event_instance")
        if event_instance_data and isinstance(event_instance_data, dict):
            return event_instance_data.get("id")
        return None

    def get_resource_id(self) -> str | None:
        """Get the resource ID."""
        resource_data = self.get_relationship_data("resource")
        if resource_data and isinstance(resource_data, dict):
            return resource_data.get("id")
        return None


class PCOResourceFolder(PCOResource):
    """Represents an organizational folder containing rooms or resources."""

    def get_name(self) -> str | None:
        """Get the folder name."""
        return self.get_attribute("name")

    def get_ancestry(self) -> str | None:
        """Get the folder ancestry."""
        return self.get_attribute("ancestry")

    def get_kind(self) -> str | None:
        """Get the folder kind (Room or Resource)."""
        return self.get_attribute("kind")

    def get_path_name(self) -> str | None:
        """Get the folder path name."""
        return self.get_attribute("path_name")

    def get_created_at(self) -> datetime | None:
        """Get the folder creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the folder last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOResourceQuestion(PCOResource):
    """Represents a question to answer when requesting to book a room or resource."""

    def get_kind(self) -> str | None:
        """Get the question kind."""
        return self.get_attribute("kind")

    def get_choices(self) -> str | None:
        """Get the question choices."""
        return self.get_attribute("choices")

    def get_description(self) -> str | None:
        """Get the question description."""
        return self.get_attribute("description")

    def get_multiple_select(self) -> bool | None:
        """Get whether multiple selections are permitted."""
        return self.get_attribute("multiple_select")

    def get_optional(self) -> bool | None:
        """Get whether the question is optional."""
        return self.get_attribute("optional")

    def get_position(self) -> int | None:
        """Get the question position."""
        return self.get_attribute("position")

    def get_question(self) -> str | None:
        """Get the question text."""
        return self.get_attribute("question")

    def get_created_at(self) -> datetime | None:
        """Get the question creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the question last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_resource_id(self) -> str | None:
        """Get the resource ID."""
        resource_data = self.get_relationship_data("resource")
        if resource_data and isinstance(resource_data, dict):
            return resource_data.get("id")
        return None


class PCOResourceSuggestion(PCOResource):
    """Represents a resource and quantity suggested by a room setup."""

    def get_quantity(self) -> int | None:
        """Get the suggested quantity."""
        return self.get_attribute("quantity")

    def get_created_at(self) -> datetime | None:
        """Get the suggestion creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the suggestion last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_resource_id(self) -> str | None:
        """Get the resource ID."""
        resource_data = self.get_relationship_data("resource")
        if resource_data and isinstance(resource_data, dict):
            return resource_data.get("id")
        return None

    def get_room_setup_id(self) -> str | None:
        """Get the room setup ID."""
        room_setup_data = self.get_relationship_data("room_setup")
        if room_setup_data and isinstance(room_setup_data, dict):
            return room_setup_data.get("id")
        return None


class PCORoomSetup(PCOResource):
    """Represents a diagram and list of suggested resources for predefined room setups."""

    def get_name(self) -> str | None:
        """Get the room setup name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the room setup description."""
        return self.get_attribute("description")

    def get_diagram(self) -> str | None:
        """Get the room setup diagram."""
        return self.get_attribute("diagram")

    def get_diagram_url(self) -> str | None:
        """Get the room setup diagram URL."""
        return self.get_attribute("diagram_url")

    def get_diagram_thumbnail_url(self) -> str | None:
        """Get the room setup diagram thumbnail URL."""
        return self.get_attribute("diagram_thumbnail_url")

    def get_created_at(self) -> datetime | None:
        """Get the room setup creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the room setup last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_room_setup_id(self) -> str | None:
        """Get the shared room setup ID."""
        room_setup_data = self.get_relationship_data("room_setup")
        if room_setup_data and isinstance(room_setup_data, dict):
            return room_setup_data.get("id")
        return None

    def get_containing_resource_id(self) -> str | None:
        """Get the containing resource ID."""
        containing_resource_data = self.get_relationship_data("containing_resource")
        if containing_resource_data and isinstance(containing_resource_data, dict):
            return containing_resource_data.get("id")
        return None


class PCOTag(PCOResource):
    """Represents an organizational tag that can be applied to events."""

    def get_name(self) -> str | None:
        """Get the tag name."""
        return self.get_attribute("name")

    def get_church_center_category(self) -> bool | None:
        """Get whether this tag is used as a category on Church Center."""
        return self.get_attribute("church_center_category")

    def get_color(self) -> str | None:
        """Get the tag color."""
        return self.get_attribute("color")

    def get_position(self) -> float | None:
        """Get the tag position."""
        return self.get_attribute("position")

    def get_created_at(self) -> datetime | None:
        """Get the tag creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the tag last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_tag_group_id(self) -> str | None:
        """Get the tag group ID."""
        tag_group_data = self.get_relationship_data("tag_group")
        if tag_group_data and isinstance(tag_group_data, dict):
            return tag_group_data.get("id")
        return None


class PCOTagGroup(PCOResource):
    """Represents a grouping of tags for organizational purposes."""

    def get_name(self) -> str | None:
        """Get the tag group name."""
        return self.get_attribute("name")

    def get_required(self) -> bool | None:
        """Get whether a tag from this group must be applied when creating an event."""
        return self.get_attribute("required")

    def get_created_at(self) -> datetime | None:
        """Get the tag group creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the tag group last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None
