"""Additional People product models for Planning Center API."""

from datetime import datetime
from typing import Any

from ..models.base import PCOResource


class PCOHousehold(PCOResource):
    """Represents a household in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the household name."""
        return self.get_attribute("name")

    def get_member_count(self) -> int | None:
        """Get the member count."""
        return self.get_attribute("member_count")

    def get_primary_contact_name(self) -> str | None:
        """Get the primary contact name."""
        return self.get_attribute("primary_contact_name")

    def get_avatar(self) -> str | None:
        """Get the avatar."""
        return self.get_attribute("avatar")

    def get_primary_contact_id(self) -> str | None:
        """Get the primary contact ID."""
        return self.get_attribute("primary_contact_id")

    def get_primary_contact_id_from_relationship(self) -> str | None:
        """Get the primary contact ID from relationship."""
        primary_contact_data = self.get_relationship_data("primary_contact")
        if primary_contact_data and isinstance(primary_contact_data, dict):
            return primary_contact_data.get("id")
        return None

    def get_people_ids(self) -> list[str]:
        """Get all person IDs in this household."""
        people_data = self.get_relationship_data("people")
        if people_data and isinstance(people_data, list):
            return [person.get("id") for person in people_data if person.get("id")]
        return []


class PCOHouseholdMembership(PCOResource):
    """Represents a household membership in Planning Center People."""

    def get_person_name(self) -> str | None:
        """Get the person name."""
        return self.get_attribute("person_name")

    def is_pending(self) -> bool:
        """Check if the membership is pending."""
        return self.get_attribute("pending", False)

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCOInactiveReason(PCOResource):
    """Represents an inactive reason in Planning Center People."""

    def get_value(self) -> str | None:
        """Get the inactive reason value."""
        return self.get_attribute("value")


class PCOList(PCOResource):
    """Represents a list in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the list name."""
        return self.get_attribute("name")

    def is_auto_refresh(self) -> bool:
        """Check if auto refresh is enabled."""
        return self.get_attribute("auto_refresh", False)

    def get_status(self) -> str | None:
        """Get the list status."""
        return self.get_attribute("status")

    def is_has_inactive_results(self) -> bool:
        """Check if the list has inactive results."""
        return self.get_attribute("has_inactive_results", False)

    def is_include_inactive(self) -> bool:
        """Check if inactive people are included."""
        return self.get_attribute("include_inactive", False)

    def get_returns(self) -> str | None:
        """Get what the list returns."""
        return self.get_attribute("returns")

    def is_return_original_if_none(self) -> bool:
        """Check if original is returned if none."""
        return self.get_attribute("return_original_if_none", False)

    def get_subset(self) -> str | None:
        """Get the subset."""
        return self.get_attribute("subset")

    def is_automations_active(self) -> bool:
        """Check if automations are active."""
        return self.get_attribute("automations_active", False)

    def is_auto_generated_name(self) -> bool:
        """Check if the name is auto generated."""
        return self.get_attribute("auto_generated_name", False)

    def get_automations_count(self) -> int | None:
        """Get the automations count."""
        return self.get_attribute("automations_count")

    def get_paused_automations_count(self) -> int | None:
        """Get the paused automations count."""
        return self.get_attribute("paused_automations_count")

    def get_description(self) -> str | None:
        """Get the list description."""
        return self.get_attribute("description")

    def is_invalid(self) -> bool:
        """Check if the list is invalid."""
        return self.get_attribute("invalid", False)

    def get_auto_refresh_frequency(self) -> str | None:
        """Get the auto refresh frequency."""
        return self.get_attribute("auto_refresh_frequency")

    def get_name_or_description(self) -> str | None:
        """Get the name or description."""
        return self.get_attribute("name_or_description")

    def is_recently_viewed(self) -> bool:
        """Check if the list was recently viewed."""
        return self.get_attribute("recently_viewed", False)

    def get_refreshed_at(self) -> datetime | None:
        """Get the refreshed date."""
        refreshed_at = self.get_attribute("refreshed_at")
        if refreshed_at:
            return datetime.fromisoformat(refreshed_at.replace("Z", "+00:00"))
        return None

    def is_starred(self) -> bool:
        """Check if the list is starred."""
        return self.get_attribute("starred", False)

    def get_total_people(self) -> int | None:
        """Get the total people count."""
        return self.get_attribute("total_people")

    def get_batch_completed_at(self) -> datetime | None:
        """Get the batch completed date."""
        batch_completed_at = self.get_attribute("batch_completed_at")
        if batch_completed_at:
            return datetime.fromisoformat(batch_completed_at.replace("Z", "+00:00"))
        return None


class PCOListCategory(PCOResource):
    """Represents a list category in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the list category name."""
        return self.get_attribute("name")

    def get_organization_id(self) -> str | None:
        """Get the organization ID."""
        return self.get_attribute("organization_id")

    def get_organization_id_from_relationship(self) -> str | None:
        """Get the organization ID from relationship."""
        organization_data = self.get_relationship_data("organization")
        if organization_data and isinstance(organization_data, dict):
            return organization_data.get("id")
        return None


class PCOListResult(PCOResource):
    """Represents a list result in Planning Center People."""

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_list_id(self) -> str | None:
        """Get the list ID."""
        list_data = self.get_relationship_data("list")
        if list_data and isinstance(list_data, dict):
            return list_data.get("id")
        return None


class PCOListShare(PCOResource):
    """Represents a list share in Planning Center People."""

    def get_permission(self) -> str | None:
        """Get the permission."""
        return self.get_attribute("permission")

    def get_group(self) -> str | None:
        """Get the group."""
        return self.get_attribute("group")

    def get_name(self) -> str | None:
        """Get the name."""
        return self.get_attribute("name")

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCOListStar(PCOResource):
    """Represents a list star in Planning Center People."""

    pass  # This is a simple resource with only created_at


class PCOMailchimpSyncStatus(PCOResource):
    """Represents a Mailchimp sync status in Planning Center People."""

    def get_status(self) -> str | None:
        """Get the sync status."""
        return self.get_attribute("status")

    def get_error(self) -> str | None:
        """Get the error message."""
        return self.get_attribute("error")

    def get_progress(self) -> int | None:
        """Get the progress percentage."""
        return self.get_attribute("progress")

    def get_completed_at(self) -> datetime | None:
        """Get the completed date."""
        completed_at = self.get_attribute("completed_at")
        if completed_at:
            return datetime.fromisoformat(completed_at.replace("Z", "+00:00"))
        return None

    def get_segment_id(self) -> int | None:
        """Get the segment ID."""
        return self.get_attribute("segment_id")


class PCOMaritalStatus(PCOResource):
    """Represents a marital status in Planning Center People."""

    def get_value(self) -> str | None:
        """Get the marital status value."""
        return self.get_attribute("value")


class PCOMessage(PCOResource):
    """Represents a message in Planning Center People."""

    def get_kind(self) -> str | None:
        """Get the message kind."""
        return self.get_attribute("kind")

    def get_to_addresses(self) -> str | None:
        """Get the to addresses."""
        return self.get_attribute("to_addresses")

    def get_subject(self) -> str | None:
        """Get the subject."""
        return self.get_attribute("subject")

    def get_delivery_status(self) -> str | None:
        """Get the delivery status."""
        return self.get_attribute("delivery_status")

    def get_reject_reason(self) -> str | None:
        """Get the reject reason."""
        return self.get_attribute("reject_reason")

    def get_sent_at(self) -> datetime | None:
        """Get the sent date."""
        sent_at = self.get_attribute("sent_at")
        if sent_at:
            return datetime.fromisoformat(sent_at.replace("Z", "+00:00"))
        return None

    def get_bounced_at(self) -> datetime | None:
        """Get the bounced date."""
        bounced_at = self.get_attribute("bounced_at")
        if bounced_at:
            return datetime.fromisoformat(bounced_at.replace("Z", "+00:00"))
        return None

    def get_rejection_notification_sent_at(self) -> datetime | None:
        """Get the rejection notification sent date."""
        rejection_notification_sent_at = self.get_attribute("rejection_notification_sent_at")
        if rejection_notification_sent_at:
            return datetime.fromisoformat(rejection_notification_sent_at.replace("Z", "+00:00"))
        return None

    def get_from_name(self) -> str | None:
        """Get the from name."""
        return self.get_attribute("from_name")

    def get_from_address(self) -> str | None:
        """Get the from address."""
        return self.get_attribute("from_address")

    def get_read_at(self) -> datetime | None:
        """Get the read date."""
        read_at = self.get_attribute("read_at")
        if read_at:
            return datetime.fromisoformat(read_at.replace("Z", "+00:00"))
        return None

    def get_app_name(self) -> str | None:
        """Get the app name."""
        return self.get_attribute("app_name")

    def get_message_type(self) -> str | None:
        """Get the message type."""
        return self.get_attribute("message_type")

    def get_file(self) -> str | None:
        """Get the file."""
        return self.get_attribute("file")

    def get_from_id(self) -> str | None:
        """Get the from person ID."""
        from_data = self.get_relationship_data("from")
        if from_data and isinstance(from_data, dict):
            return from_data.get("id")
        return None

    def get_to_id(self) -> str | None:
        """Get the to person ID."""
        to_data = self.get_relationship_data("to")
        if to_data and isinstance(to_data, dict):
            return to_data.get("id")
        return None

    def get_message_group_id(self) -> str | None:
        """Get the message group ID."""
        message_group_data = self.get_relationship_data("message_group")
        if message_group_data and isinstance(message_group_data, dict):
            return message_group_data.get("id")
        return None


class PCOMessageGroup(PCOResource):
    """Represents a message group in Planning Center People."""

    def get_uuid(self) -> str | None:
        """Get the UUID."""
        return self.get_attribute("uuid")

    def get_message_type(self) -> str | None:
        """Get the message type."""
        return self.get_attribute("message_type")

    def get_from_address(self) -> str | None:
        """Get the from address."""
        return self.get_attribute("from_address")

    def get_subject(self) -> str | None:
        """Get the subject."""
        return self.get_attribute("subject")

    def get_message_count(self) -> int | None:
        """Get the message count."""
        return self.get_attribute("message_count")

    def is_system_message(self) -> bool:
        """Check if this is a system message."""
        return self.get_attribute("system_message", False)

    def is_transactional_message(self) -> bool:
        """Check if this is a transactional message."""
        return self.get_attribute("transactional_message", False)

    def is_contains_user_generated_content(self) -> bool:
        """Check if this contains user generated content."""
        return self.get_attribute("contains_user_generated_content", False)

    def get_reply_to_name(self) -> str | None:
        """Get the reply to name."""
        return self.get_attribute("reply_to_name")

    def get_reply_to_address(self) -> str | None:
        """Get the reply to address."""
        return self.get_attribute("reply_to_address")

    def get_app_id(self) -> str | None:
        """Get the app ID."""
        app_data = self.get_relationship_data("app")
        if app_data and isinstance(app_data, dict):
            return app_data.get("id")
        return None

    def get_from_id(self) -> str | None:
        """Get the from person ID."""
        from_data = self.get_relationship_data("from")
        if from_data and isinstance(from_data, dict):
            return from_data.get("id")
        return None


class PCONameSuffix(PCOResource):
    """Represents a name suffix in Planning Center People."""

    def get_value(self) -> str | None:
        """Get the name suffix value."""
        return self.get_attribute("value")


class PCOPeopleNote(PCOResource):
    """Represents a note in Planning Center People."""

    def get_note(self) -> str | None:
        """Get the note content."""
        return self.get_attribute("note")

    def get_display_date(self) -> datetime | None:
        """Get the display date."""
        display_date = self.get_attribute("display_date")
        if display_date:
            return datetime.fromisoformat(display_date.replace("Z", "+00:00"))
        return None

    def get_note_category_id(self) -> str | None:
        """Get the note category ID."""
        return self.get_attribute("note_category_id")

    def get_organization_id(self) -> str | None:
        """Get the organization ID."""
        return self.get_attribute("organization_id")

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        return self.get_attribute("person_id")

    def get_created_by_id(self) -> str | None:
        """Get the created by ID."""
        return self.get_attribute("created_by_id")

    def get_note_category_id_from_relationship(self) -> str | None:
        """Get the note category ID from relationship."""
        note_category_data = self.get_relationship_data("note_category")
        if note_category_data and isinstance(note_category_data, dict):
            return note_category_data.get("id")
        return None

    def get_organization_id_from_relationship(self) -> str | None:
        """Get the organization ID from relationship."""
        organization_data = self.get_relationship_data("organization")
        if organization_data and isinstance(organization_data, dict):
            return organization_data.get("id")
        return None

    def get_person_id_from_relationship(self) -> str | None:
        """Get the person ID from relationship."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_created_by_id_from_relationship(self) -> str | None:
        """Get the created by ID from relationship."""
        created_by_data = self.get_relationship_data("created_by")
        if created_by_data and isinstance(created_by_data, dict):
            return created_by_data.get("id")
        return None


class PCONoteCategory(PCOResource):
    """Represents a note category in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the note category name."""
        return self.get_attribute("name")

    def is_locked(self) -> bool:
        """Check if the note category is locked."""
        return self.get_attribute("locked", False)

    def get_organization_id(self) -> str | None:
        """Get the organization ID."""
        return self.get_attribute("organization_id")

    def get_organization_id_from_relationship(self) -> str | None:
        """Get the organization ID from relationship."""
        organization_data = self.get_relationship_data("organization")
        if organization_data and isinstance(organization_data, dict):
            return organization_data.get("id")
        return None


class PCONoteCategoryShare(PCOResource):
    """Represents a note category share in Planning Center People."""

    def get_group(self) -> str | None:
        """Get the group."""
        return self.get_attribute("group")

    def get_permission(self) -> str | None:
        """Get the permission."""
        return self.get_attribute("permission")

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        return self.get_attribute("person_id")

    def get_person_id_from_relationship(self) -> str | None:
        """Get the person ID from relationship."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_note_category_id_from_relationship(self) -> str | None:
        """Get the note category ID from relationship."""
        note_category_data = self.get_relationship_data("note_category")
        if note_category_data and isinstance(note_category_data, dict):
            return note_category_data.get("id")
        return None


class PCONoteCategorySubscription(PCOResource):
    """Represents a note category subscription in Planning Center People."""

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_note_category_id(self) -> str | None:
        """Get the note category ID."""
        note_category_data = self.get_relationship_data("note_category")
        if note_category_data and isinstance(note_category_data, dict):
            return note_category_data.get("id")
        return None


class PCOOrganizationStatistics(PCOResource):
    """Represents organization statistics in Planning Center People."""

    pass  # This is a simple resource with only ID


class PCOPeopleImport(PCOResource):
    """Represents a people import in Planning Center People."""

    def get_attribs(self) -> str | None:
        """Get the attributes."""
        return self.get_attribute("attribs")

    def get_status(self) -> str | None:
        """Get the import status."""
        return self.get_attribute("status")

    def get_processed_at(self) -> datetime | None:
        """Get the processed date."""
        processed_at = self.get_attribute("processed_at")
        if processed_at:
            return datetime.fromisoformat(processed_at.replace("Z", "+00:00"))
        return None

    def get_undone_at(self) -> datetime | None:
        """Get the undone date."""
        undone_at = self.get_attribute("undone_at")
        if undone_at:
            return datetime.fromisoformat(undone_at.replace("Z", "+00:00"))
        return None

    def get_created_by_id(self) -> str | None:
        """Get the created by ID."""
        created_by_data = self.get_relationship_data("created_by")
        if created_by_data and isinstance(created_by_data, dict):
            return created_by_data.get("id")
        return None

    def get_undone_by_id(self) -> str | None:
        """Get the undone by ID."""
        undone_by_data = self.get_relationship_data("undone_by")
        if undone_by_data and isinstance(undone_by_data, dict):
            return undone_by_data.get("id")
        return None


class PCOPeopleImportConflict(PCOResource):
    """Represents a people import conflict in Planning Center People."""

    def get_kind(self) -> str | None:
        """Get the conflict kind."""
        return self.get_attribute("kind")

    def get_name(self) -> str | None:
        """Get the conflict name."""
        return self.get_attribute("name")

    def get_message(self) -> str | None:
        """Get the conflict message."""
        return self.get_attribute("message")

    def get_data(self) -> str | None:
        """Get the conflict data."""
        return self.get_attribute("data")

    def get_conflicting_changes(self) -> str | None:
        """Get the conflicting changes."""
        return self.get_attribute("conflicting_changes")

    def is_ignore(self) -> bool:
        """Check if the conflict should be ignored."""
        return self.get_attribute("ignore", False)


class PCOPeopleImportHistory(PCOResource):
    """Represents a people import history in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the history name."""
        return self.get_attribute("name")

    def get_conflicting_changes(self) -> dict[str, Any] | None:
        """Get the conflicting changes."""
        return self.get_attribute("conflicting_changes")

    def get_kind(self) -> str | None:
        """Get the history kind."""
        return self.get_attribute("kind")

    def get_household_id(self) -> str | None:
        """Get the household ID."""
        household_data = self.get_relationship_data("household")
        if household_data and isinstance(household_data, dict):
            return household_data.get("id")
        return None

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCOPersonApp(PCOResource):
    """Represents a person app in Planning Center People."""

    def is_allow_pco_login(self) -> bool:
        """Check if PCO login is allowed."""
        return self.get_attribute("allow_pco_login", False)

    def get_people_permissions(self) -> str | None:
        """Get the people permissions."""
        return self.get_attribute("people_permissions")

    def get_app_id(self) -> str | None:
        """Get the app ID."""
        app_data = self.get_relationship_data("app")
        if app_data and isinstance(app_data, dict):
            return app_data.get("id")
        return None

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCOPlatformNotification(PCOResource):
    """Represents a platform notification in Planning Center People."""

    def get_html(self) -> str | None:
        """Get the HTML content."""
        return self.get_attribute("html")


class PCOReport(PCOResource):
    """Represents a report in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the report name."""
        return self.get_attribute("name")

    def get_body(self) -> str | None:
        """Get the report body."""
        return self.get_attribute("body")

    def get_created_by_id(self) -> str | None:
        """Get the created by ID."""
        created_by_data = self.get_relationship_data("created_by")
        if created_by_data and isinstance(created_by_data, dict):
            return created_by_data.get("id")
        return None

    def get_updated_by_id(self) -> str | None:
        """Get the updated by ID."""
        updated_by_data = self.get_relationship_data("updated_by")
        if updated_by_data and isinstance(updated_by_data, dict):
            return updated_by_data.get("id")
        return None


class PCORule(PCOResource):
    """Represents a rule in Planning Center People."""

    def get_subset(self) -> str | None:
        """Get the subset."""
        return self.get_attribute("subset")


class PCOSchoolOption(PCOResource):
    """Represents a school option in Planning Center People."""

    def get_value(self) -> str | None:
        """Get the school option value."""
        return self.get_attribute("value")

    def get_sequence(self) -> int | None:
        """Get the sequence."""
        return self.get_attribute("sequence")

    def get_beginning_grade(self) -> str | None:
        """Get the beginning grade."""
        return self.get_attribute("beginning_grade")

    def get_ending_grade(self) -> str | None:
        """Get the ending grade."""
        return self.get_attribute("ending_grade")

    def get_school_types(self) -> list[str]:
        """Get the school types."""
        return self.get_attribute("school_types", [])

    def get_promotes_to_school_id(self) -> str | None:
        """Get the promotes to school ID."""
        promotes_to_school_data = self.get_relationship_data("promotes_to_school")
        if promotes_to_school_data and isinstance(promotes_to_school_data, dict):
            return promotes_to_school_data.get("id")
        return None


class PCOServiceTime(PCOResource):
    """Represents a service time in Planning Center People."""

    def get_start_time(self) -> int | None:
        """Get the start time."""
        return self.get_attribute("start_time")

    def get_day(self) -> str | None:
        """Get the day."""
        return self.get_attribute("day")

    def get_description(self) -> str | None:
        """Get the description."""
        return self.get_attribute("description")

    def get_organization_id(self) -> str | None:
        """Get the organization ID."""
        organization_data = self.get_relationship_data("organization")
        if organization_data and isinstance(organization_data, dict):
            return organization_data.get("id")
        return None

    def get_campus_id(self) -> str | None:
        """Get the campus ID."""
        campus_data = self.get_relationship_data("campus")
        if campus_data and isinstance(campus_data, dict):
            return campus_data.get("id")
        return None


class PCOSocialProfile(PCOResource):
    """Represents a social profile in Planning Center People."""

    def get_site(self) -> str | None:
        """Get the social site."""
        return self.get_attribute("site")

    def get_url(self) -> str | None:
        """Get the social profile URL."""
        return self.get_attribute("url")

    def is_verified(self) -> bool:
        """Check if the social profile is verified."""
        return self.get_attribute("verified", False)

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCOSpamEmailAddress(PCOResource):
    """Represents a spam email address in Planning Center People."""

    def get_address(self) -> str | None:
        """Get the email address."""
        return self.get_attribute("address")


class PCOTab(PCOResource):
    """Represents a tab in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the tab name."""
        return self.get_attribute("name")

    def get_sequence(self) -> int | None:
        """Get the sequence."""
        return self.get_attribute("sequence")

    def get_slug(self) -> str | None:
        """Get the slug."""
        return self.get_attribute("slug")


class PCOWorkflow(PCOResource):
    """Represents a workflow in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the workflow name."""
        return self.get_attribute("name")

    def get_my_ready_card_count(self) -> int | None:
        """Get the my ready card count."""
        return self.get_attribute("my_ready_card_count")

    def get_total_ready_card_count(self) -> int | None:
        """Get the total ready card count."""
        return self.get_attribute("total_ready_card_count")

    def get_completed_card_count(self) -> int | None:
        """Get the completed card count."""
        return self.get_attribute("completed_card_count")

    def get_total_cards_count(self) -> int | None:
        """Get the total cards count."""
        return self.get_attribute("total_cards_count")

    def get_total_ready_and_snoozed_card_count(self) -> int | None:
        """Get the total ready and snoozed card count."""
        return self.get_attribute("total_ready_and_snoozed_card_count")

    def get_total_steps_count(self) -> int | None:
        """Get the total steps count."""
        return self.get_attribute("total_steps_count")

    def get_total_unassigned_steps_count(self) -> int | None:
        """Get the total unassigned steps count."""
        return self.get_attribute("total_unassigned_steps_count")

    def get_total_unassigned_card_count(self) -> int | None:
        """Get the total unassigned card count."""
        return self.get_attribute("total_unassigned_card_count")

    def get_total_overdue_card_count(self) -> int | None:
        """Get the total overdue card count."""
        return self.get_attribute("total_overdue_card_count")

    def get_deleted_at(self) -> datetime | None:
        """Get the deleted date."""
        deleted_at = self.get_attribute("deleted_at")
        if deleted_at:
            return datetime.fromisoformat(deleted_at.replace("Z", "+00:00"))
        return None

    def get_archived_at(self) -> datetime | None:
        """Get the archived date."""
        archived_at = self.get_attribute("archived_at")
        if archived_at:
            return datetime.fromisoformat(archived_at.replace("Z", "+00:00"))
        return None

    def get_campus_id(self) -> str | None:
        """Get the campus ID."""
        return self.get_attribute("campus_id")

    def get_workflow_category_id(self) -> str | None:
        """Get the workflow category ID."""
        return self.get_attribute("workflow_category_id")

    def get_my_overdue_card_count(self) -> int | None:
        """Get the my overdue card count."""
        return self.get_attribute("my_overdue_card_count")

    def get_my_due_soon_card_count(self) -> int | None:
        """Get the my due soon card count."""
        return self.get_attribute("my_due_soon_card_count")

    def is_recently_viewed(self) -> bool:
        """Check if the workflow was recently viewed."""
        return self.get_attribute("recently_viewed", False)

    def get_workflow_category_id_from_relationship(self) -> str | None:
        """Get the workflow category ID from relationship."""
        workflow_category_data = self.get_relationship_data("workflow_category")
        if workflow_category_data and isinstance(workflow_category_data, dict):
            return workflow_category_data.get("id")
        return None

    def get_campus_id_from_relationship(self) -> str | None:
        """Get the campus ID from relationship."""
        campus_data = self.get_relationship_data("campus")
        if campus_data and isinstance(campus_data, dict):
            return campus_data.get("id")
        return None


class PCOWorkflowCard(PCOResource):
    """Represents a workflow card in Planning Center People."""

    def get_snooze_until(self) -> datetime | None:
        """Get the snooze until date."""
        snooze_until = self.get_attribute("snooze_until")
        if snooze_until:
            return datetime.fromisoformat(snooze_until.replace("Z", "+00:00"))
        return None

    def is_overdue(self) -> bool:
        """Check if the card is overdue."""
        return self.get_attribute("overdue", False)

    def get_stage(self) -> str | None:
        """Get the card stage."""
        return self.get_attribute("stage")

    def get_calculated_due_at_in_days_ago(self) -> int | None:
        """Get the calculated due at in days ago."""
        return self.get_attribute("calculated_due_at_in_days_ago")

    def is_sticky_assignment(self) -> bool:
        """Check if the assignment is sticky."""
        return self.get_attribute("sticky_assignment", False)

    def get_completed_at(self) -> datetime | None:
        """Get the completed date."""
        completed_at = self.get_attribute("completed_at")
        if completed_at:
            return datetime.fromisoformat(completed_at.replace("Z", "+00:00"))
        return None

    def get_flagged_for_notification_at(self) -> datetime | None:
        """Get the flagged for notification date."""
        flagged_for_notification_at = self.get_attribute("flagged_for_notification_at")
        if flagged_for_notification_at:
            return datetime.fromisoformat(flagged_for_notification_at.replace("Z", "+00:00"))
        return None

    def get_removed_at(self) -> datetime | None:
        """Get the removed date."""
        removed_at = self.get_attribute("removed_at")
        if removed_at:
            return datetime.fromisoformat(removed_at.replace("Z", "+00:00"))
        return None

    def get_moved_to_step_at(self) -> datetime | None:
        """Get the moved to step date."""
        moved_to_step_at = self.get_attribute("moved_to_step_at")
        if moved_to_step_at:
            return datetime.fromisoformat(moved_to_step_at.replace("Z", "+00:00"))
        return None

    def get_assignee_id(self) -> str | None:
        """Get the assignee ID."""
        assignee_data = self.get_relationship_data("assignee")
        if assignee_data and isinstance(assignee_data, dict):
            return assignee_data.get("id")
        return None

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_workflow_id(self) -> str | None:
        """Get the workflow ID."""
        workflow_data = self.get_relationship_data("workflow")
        if workflow_data and isinstance(workflow_data, dict):
            return workflow_data.get("id")
        return None

    def get_current_step_id(self) -> str | None:
        """Get the current step ID."""
        current_step_data = self.get_relationship_data("current_step")
        if current_step_data and isinstance(current_step_data, dict):
            return current_step_data.get("id")
        return None


class PCOWorkflowCardActivity(PCOResource):
    """Represents a workflow card activity in Planning Center People."""

    def get_comment(self) -> str | None:
        """Get the comment."""
        return self.get_attribute("comment")

    def get_content(self) -> str | None:
        """Get the content."""
        return self.get_attribute("content")

    def get_form_submission_url(self) -> str | None:
        """Get the form submission URL."""
        return self.get_attribute("form_submission_url")

    def get_automation_url(self) -> str | None:
        """Get the automation URL."""
        return self.get_attribute("automation_url")

    def get_person_avatar_url(self) -> str | None:
        """Get the person avatar URL."""
        return self.get_attribute("person_avatar_url")

    def get_person_name(self) -> str | None:
        """Get the person name."""
        return self.get_attribute("person_name")

    def get_reassigned_to_avatar_url(self) -> str | None:
        """Get the reassigned to avatar URL."""
        return self.get_attribute("reassigned_to_avatar_url")

    def get_reassigned_to_name(self) -> str | None:
        """Get the reassigned to name."""
        return self.get_attribute("reassigned_to_name")

    def get_subject(self) -> str | None:
        """Get the subject."""
        return self.get_attribute("subject")

    def get_type(self) -> str | None:
        """Get the activity type."""
        return self.get_attribute("type")

    def is_content_is_html(self) -> bool:
        """Check if the content is HTML."""
        return self.get_attribute("content_is_html", False)

    def get_workflow_card_id(self) -> str | None:
        """Get the workflow card ID."""
        workflow_card_data = self.get_relationship_data("workflow_card")
        if workflow_card_data and isinstance(workflow_card_data, dict):
            return workflow_card_data.get("id")
        return None

    def get_workflow_step_id(self) -> str | None:
        """Get the workflow step ID."""
        workflow_step_data = self.get_relationship_data("workflow_step")
        if workflow_step_data and isinstance(workflow_step_data, dict):
            return workflow_step_data.get("id")
        return None


class PCOWorkflowCardNote(PCOResource):
    """Represents a workflow card note in Planning Center People."""

    def get_note(self) -> str | None:
        """Get the note content."""
        return self.get_attribute("note")


class PCOWorkflowCategory(PCOResource):
    """Represents a workflow category in Planning Center People."""

    def get_name(self) -> str | None:
        """Get the workflow category name."""
        return self.get_attribute("name")


class PCOWorkflowShare(PCOResource):
    """Represents a workflow share in Planning Center People."""

    def get_group(self) -> str | None:
        """Get the group."""
        return self.get_attribute("group")

    def get_permission(self) -> str | None:
        """Get the permission."""
        return self.get_attribute("permission")

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        return self.get_attribute("person_id")

    def get_person_id_from_relationship(self) -> str | None:
        """Get the person ID from relationship."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_workflow_id_from_relationship(self) -> str | None:
        """Get the workflow ID from relationship."""
        workflow_data = self.get_relationship_data("workflow")
        if workflow_data and isinstance(workflow_data, dict):
            return workflow_data.get("id")
        return None


class PCOWorkflowStep(PCOResource):
    """Represents a workflow step in Planning Center People."""

    def get_sequence(self) -> int | None:
        """Get the sequence."""
        return self.get_attribute("sequence")

    def get_name(self) -> str | None:
        """Get the step name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the step description."""
        return self.get_attribute("description")

    def get_expected_response_time_in_days(self) -> int | None:
        """Get the expected response time in days."""
        return self.get_attribute("expected_response_time_in_days")

    def get_auto_snooze_value(self) -> int | None:
        """Get the auto snooze value."""
        return self.get_attribute("auto_snooze_value")

    def get_auto_snooze_interval(self) -> str | None:
        """Get the auto snooze interval."""
        return self.get_attribute("auto_snooze_interval")

    def get_auto_snooze_days(self) -> int | None:
        """Get the auto snooze days."""
        return self.get_attribute("auto_snooze_days")

    def get_my_ready_card_count(self) -> int | None:
        """Get the my ready card count."""
        return self.get_attribute("my_ready_card_count")

    def get_total_ready_card_count(self) -> int | None:
        """Get the total ready card count."""
        return self.get_attribute("total_ready_card_count")

    def get_default_assignee_id(self) -> str | None:
        """Get the default assignee ID."""
        return self.get_attribute("default_assignee_id")

    def get_default_assignee_id_from_relationship(self) -> str | None:
        """Get the default assignee ID from relationship."""
        default_assignee_data = self.get_relationship_data("default_assignee")
        if default_assignee_data and isinstance(default_assignee_data, dict):
            return default_assignee_data.get("id")
        return None

    def get_workflow_id_from_relationship(self) -> str | None:
        """Get the workflow ID from relationship."""
        workflow_data = self.get_relationship_data("workflow")
        if workflow_data and isinstance(workflow_data, dict):
            return workflow_data.get("id")
        return None


class PCOWorkflowStepAssigneeSummary(PCOResource):
    """Represents a workflow step assignee summary in Planning Center People."""

    def get_ready_count(self) -> int | None:
        """Get the ready count."""
        return self.get_attribute("ready_count")

    def get_snoozed_count(self) -> int | None:
        """Get the snoozed count."""
        return self.get_attribute("snoozed_count")

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_step_id(self) -> str | None:
        """Get the step ID."""
        step_data = self.get_relationship_data("step")
        if step_data and isinstance(step_data, dict):
            return step_data.get("id")
        return None
