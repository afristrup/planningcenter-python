"""Services product models for Planning Center API."""

from datetime import datetime

from ..models.base import PCOResource


class PCOService(PCOResource):
    """Represents a service in Planning Center Services."""

    def get_name(self) -> str | None:
        """Get the service name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the service description."""
        return self.get_attribute("description")

    def get_start_time(self) -> datetime | None:
        """Get the service start time."""
        start_time = self.get_attribute("start_time")
        if start_time:
            return datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        return None

    def get_end_time(self) -> datetime | None:
        """Get the service end time."""
        end_time = self.get_attribute("end_time")
        if end_time:
            return datetime.fromisoformat(end_time.replace("Z", "+00:00"))
        return None

    def get_created_at(self) -> datetime | None:
        """Get the service creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the service last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOServiceType(PCOResource):
    """Represents a service type in Planning Center Services."""

    def get_name(self) -> str | None:
        """Get the service type name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the service type description."""
        return self.get_attribute("description")

    def get_sequence(self) -> int:
        """Get the service type sequence."""
        return self.get_attribute("sequence", 0)

    def is_active(self) -> bool:
        """Check if the service type is active."""
        return self.get_attribute("active", True)


class PCOPlan(PCOResource):
    """Represents a plan in Planning Center Services."""

    def get_title(self) -> str | None:
        """Get the plan title."""
        return self.get_attribute("title")

    def get_series_title(self) -> str | None:
        """Get the plan series title."""
        return self.get_attribute("series_title")

    def get_plan_notes_count(self) -> int:
        """Get the number of plan notes."""
        return self.get_attribute("plan_notes_count", 0)

    def get_plan_people_count(self) -> int:
        """Get the number of plan people."""
        return self.get_attribute("plan_people_count", 0)

    def get_plan_times_count(self) -> int:
        """Get the number of plan times."""
        return self.get_attribute("plan_times_count", 0)

    def get_created_at(self) -> datetime | None:
        """Get the plan creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the plan last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_service_type_id(self) -> str | None:
        """Get the service type ID."""
        service_type_data = self.get_relationship_data("service_type")
        if service_type_data and isinstance(service_type_data, dict):
            return service_type_data.get("id")
        return None


class PCOPlanTime(PCOResource):
    """Represents a plan time in Planning Center Services."""

    def get_starts_at(self) -> datetime | None:
        """Get the plan time start."""
        starts_at = self.get_attribute("starts_at")
        if starts_at:
            return datetime.fromisoformat(starts_at.replace("Z", "+00:00"))
        return None

    def get_ends_at(self) -> datetime | None:
        """Get the plan time end."""
        ends_at = self.get_attribute("ends_at")
        if ends_at:
            return datetime.fromisoformat(ends_at.replace("Z", "+00:00"))
        return None

    def get_plan_id(self) -> str | None:
        """Get the plan ID."""
        plan_data = self.get_relationship_data("plan")
        if plan_data and isinstance(plan_data, dict):
            return plan_data.get("id")
        return None


class PCOPlanPerson(PCOResource):
    """Represents a plan person in Planning Center Services."""

    def get_name(self) -> str | None:
        """Get the plan person name."""
        return self.get_attribute("name")

    def get_first_name(self) -> str | None:
        """Get the plan person first name."""
        return self.get_attribute("first_name")

    def get_last_name(self) -> str | None:
        """Get the plan person last name."""
        return self.get_attribute("last_name")

    def get_email(self) -> str | None:
        """Get the plan person email."""
        return self.get_attribute("email")

    def get_phone(self) -> str | None:
        """Get the plan person phone."""
        return self.get_attribute("phone")

    def get_plan_id(self) -> str | None:
        """Get the plan ID."""
        plan_data = self.get_relationship_data("plan")
        if plan_data and isinstance(plan_data, dict):
            return plan_data.get("id")
        return None

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCOPlanNote(PCOResource):
    """Represents a plan note in Planning Center Services."""

    def get_content(self) -> str | None:
        """Get the plan note content."""
        return self.get_attribute("content")

    def get_created_at(self) -> datetime | None:
        """Get the plan note creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the plan note last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_plan_id(self) -> str | None:
        """Get the plan ID."""
        plan_data = self.get_relationship_data("plan")
        if plan_data and isinstance(plan_data, dict):
            return plan_data.get("id")
        return None


class PCOSong(PCOResource):
    """Represents a song in Planning Center Services."""

    def get_title(self) -> str | None:
        """Get the song title."""
        return self.get_attribute("title")

    def get_author(self) -> str | None:
        """Get the song author."""
        return self.get_attribute("author")

    def get_copyright(self) -> str | None:
        """Get the song copyright."""
        return self.get_attribute("copyright")

    def get_ccli_number(self) -> str | None:
        """Get the CCLI number."""
        return self.get_attribute("ccli_number")

    def get_created_at(self) -> datetime | None:
        """Get the song creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the song last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOArrangement(PCOResource):
    """Represents an arrangement in Planning Center Services."""

    def get_name(self) -> str | None:
        """Get the arrangement name."""
        return self.get_attribute("name")

    def get_length(self) -> int | None:
        """Get the arrangement length in seconds."""
        return self.get_attribute("length")

    def get_created_at(self) -> datetime | None:
        """Get the arrangement creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the arrangement last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_song_id(self) -> str | None:
        """Get the song ID."""
        song_data = self.get_relationship_data("song")
        if song_data and isinstance(song_data, dict):
            return song_data.get("id")
        return None


class PCOKey(PCOResource):
    """Represents a key in Planning Center Services."""

    def get_name(self) -> str | None:
        """Get the key name."""
        return self.get_attribute("name")

    def get_created_at(self) -> datetime | None:
        """Get the key creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the key last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOAttachment(PCOResource):
    """Represents an attachment in Planning Center Services."""

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


class PCOMedia(PCOResource):
    """Represents media in Planning Center Services."""

    def get_title(self) -> str | None:
        """Get the media title."""
        return self.get_attribute("title")

    def get_description(self) -> str | None:
        """Get the media description."""
        return self.get_attribute("description")

    def get_media_type(self) -> str | None:
        """Get the media type."""
        return self.get_attribute("media_type")

    def get_url(self) -> str | None:
        """Get the media URL."""
        return self.get_attribute("url")

    def get_created_at(self) -> datetime | None:
        """Get the media creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the media last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOFolder(PCOResource):
    """Represents a folder in Planning Center Services."""

    def get_name(self) -> str | None:
        """Get the folder name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the folder description."""
        return self.get_attribute("description")

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


class PCOTemplate(PCOResource):
    """Represents a template in Planning Center Services."""

    def get_name(self) -> str | None:
        """Get the template name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the template description."""
        return self.get_attribute("description")

    def get_created_at(self) -> datetime | None:
        """Get the template creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the template last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None
