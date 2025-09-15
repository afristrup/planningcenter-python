"""Services API models and services for Planning Center API."""

from datetime import datetime
from typing import Any

from ..models.base import PCOBaseModel
from ..models.links import PCOLinks
from ..models.relationships import PCORelationships


# Core Service Models
class PCOService(PCOBaseModel):
    """Represents a service in Planning Center Services."""

    id: str
    type: str = "Service"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def name(self) -> str | None:
        """Get the service name."""
        return self.attributes.get("name")

    @property
    def description(self) -> str | None:
        """Get the service description."""
        return self.attributes.get("description")

    @property
    def start_time(self) -> datetime | None:
        """Get the service start time."""
        start_time = self.attributes.get("start_time")
        if start_time and isinstance(start_time, str):
            return datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        return start_time

    @property
    def end_time(self) -> datetime | None:
        """Get the service end time."""
        end_time = self.attributes.get("end_time")
        if end_time and isinstance(end_time, str):
            return datetime.fromisoformat(end_time.replace("Z", "+00:00"))
        return end_time

    @property
    def created_at(self) -> datetime | None:
        """Get the service creation time."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the service last update time."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at


class PCOServiceType(PCOBaseModel):
    """Represents a service type in Planning Center Services."""

    id: str
    type: str = "ServiceType"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def name(self) -> str | None:
        """Get the service type name."""
        return self.attributes.get("name")

    @property
    def description(self) -> str | None:
        """Get the service type description."""
        return self.attributes.get("description")

    @property
    def created_at(self) -> datetime | None:
        """Get the service type creation time."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the service type last update time."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at


# Plan Models
class PCOPlan(PCOBaseModel):
    """Represents a plan in Planning Center Services."""

    id: str
    type: str = "Plan"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def title(self) -> str | None:
        """Get the plan title."""
        return self.attributes.get("title")

    @property
    def series_title(self) -> str | None:
        """Get the series title."""
        return self.attributes.get("series_title")

    @property
    def plan_notes_count(self) -> int | None:
        """Get the plan notes count."""
        return self.attributes.get("plan_notes_count")

    @property
    def other_time_count(self) -> int | None:
        """Get the other time count."""
        return self.attributes.get("other_time_count")

    @property
    def service_time_count(self) -> int | None:
        """Get the service time count."""
        return self.attributes.get("service_time_count")

    @property
    def sort_date(self) -> datetime | None:
        """Get the sort date."""
        sort_date = self.attributes.get("sort_date")
        if sort_date and isinstance(sort_date, str):
            return datetime.fromisoformat(sort_date.replace("Z", "+00:00"))
        return sort_date

    @property
    def created_at(self) -> datetime | None:
        """Get the plan creation time."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the plan last update time."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at


class PCOPlanTime(PCOBaseModel):
    """Represents a plan time in Planning Center Services."""

    id: str
    type: str = "PlanTime"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def name(self) -> str | None:
        """Get the plan time name."""
        return self.attributes.get("name")

    @property
    def starts_at(self) -> datetime | None:
        """Get the start time."""
        starts_at = self.attributes.get("starts_at")
        if starts_at and isinstance(starts_at, str):
            return datetime.fromisoformat(starts_at.replace("Z", "+00:00"))
        return starts_at

    @property
    def ends_at(self) -> datetime | None:
        """Get the end time."""
        ends_at = self.attributes.get("ends_at")
        if ends_at and isinstance(ends_at, str):
            return datetime.fromisoformat(ends_at.replace("Z", "+00:00"))
        return ends_at

    @property
    def live(self) -> bool | None:
        """Get whether this is a live service."""
        return self.attributes.get("live")

    @property
    def created_at(self) -> datetime | None:
        """Get the plan time creation time."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the plan time last update time."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at


class PCOPlanPerson(PCOBaseModel):
    """Represents a plan person in Planning Center Services."""

    id: str
    type: str = "PlanPerson"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def status(self) -> str | None:
        """Get the plan person status."""
        return self.attributes.get("status")

    @property
    def team_position_name(self) -> str | None:
        """Get the team position name."""
        return self.attributes.get("team_position_name")

    @property
    def created_at(self) -> datetime | None:
        """Get the plan person creation time."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the plan person last update time."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at


class PCOPlanNote(PCOBaseModel):
    """Represents a plan note in Planning Center Services."""

    id: str
    type: str = "PlanNote"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def content(self) -> str | None:
        """Get the note content."""
        return self.attributes.get("content")

    @property
    def created_at(self) -> datetime | None:
        """Get the plan note creation time."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the plan note last update time."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at


# Media Models
class PCOSong(PCOBaseModel):
    """Represents a song in Planning Center Services."""

    id: str
    type: str = "Song"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def title(self) -> str | None:
        """Get the song title."""
        return self.attributes.get("title")

    @property
    def author(self) -> str | None:
        """Get the song author."""
        return self.attributes.get("author")

    @property
    def ccli_number(self) -> str | None:
        """Get the CCLI number."""
        return self.attributes.get("ccli_number")

    @property
    def created_at(self) -> datetime | None:
        """Get the song creation time."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the song last update time."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at


class PCOArrangement(PCOBaseModel):
    """Represents an arrangement in Planning Center Services."""

    id: str
    type: str = "Arrangement"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def name(self) -> str | None:
        """Get the arrangement name."""
        return self.attributes.get("name")

    @property
    def bpm(self) -> float | None:
        """Get the beats per minute."""
        return self.attributes.get("bpm")

    @property
    def length(self) -> int | None:
        """Get the length in seconds."""
        return self.attributes.get("length")

    @property
    def meter(self) -> str | None:
        """Get the meter."""
        return self.attributes.get("meter")

    @property
    def has_chords(self) -> bool | None:
        """Get whether the arrangement has chords."""
        return self.attributes.get("has_chords")

    @property
    def notes(self) -> str | None:
        """Get the arrangement notes."""
        return self.attributes.get("notes")

    @property
    def lyrics(self) -> str | None:
        """Get the lyrics."""
        return self.attributes.get("lyrics")

    @property
    def created_at(self) -> datetime | None:
        """Get the arrangement creation time."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the arrangement last update time."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at


class PCOKey(PCOBaseModel):
    """Represents a key in Planning Center Services."""

    id: str
    type: str = "Key"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def name(self) -> str | None:
        """Get the key name."""
        return self.attributes.get("name")

    @property
    def created_at(self) -> datetime | None:
        """Get the key creation time."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the key last update time."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at


class PCOAttachment(PCOBaseModel):
    """Represents an attachment in Planning Center Services."""

    id: str
    type: str = "Attachment"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def filename(self) -> str | None:
        """Get the attachment filename."""
        return self.attributes.get("filename")

    @property
    def content_type(self) -> str | None:
        """Get the content type."""
        return self.attributes.get("content_type")

    @property
    def file_size(self) -> int | None:
        """Get the file size in bytes."""
        return self.attributes.get("file_size")

    @property
    def created_at(self) -> datetime | None:
        """Get the attachment creation time."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the attachment last update time."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at


class PCOMedia(PCOBaseModel):
    """Represents media in Planning Center Services."""

    id: str
    type: str = "Media"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def filename(self) -> str | None:
        """Get the media filename."""
        return self.attributes.get("filename")

    @property
    def content_type(self) -> str | None:
        """Get the content type."""
        return self.attributes.get("content_type")

    @property
    def file_size(self) -> int | None:
        """Get the file size in bytes."""
        return self.attributes.get("file_size")

    @property
    def created_at(self) -> datetime | None:
        """Get the media creation time."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the media last update time."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at


class PCOFolder(PCOBaseModel):
    """Represents a folder in Planning Center Services."""

    id: str
    type: str = "Folder"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def name(self) -> str | None:
        """Get the folder name."""
        return self.attributes.get("name")

    @property
    def created_at(self) -> datetime | None:
        """Get the folder creation time."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the folder last update time."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at


class PCOTemplate(PCOBaseModel):
    """Represents a template in Planning Center Services."""

    id: str
    type: str = "Template"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def name(self) -> str | None:
        """Get the template name."""
        return self.attributes.get("name")

    @property
    def created_at(self) -> datetime | None:
        """Get the template creation time."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the template last update time."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at


class PCOItem(PCOBaseModel):
    """Represents an item in Planning Center Services."""

    id: str
    type: str = "Item"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def title(self) -> str | None:
        """Get the item title."""
        return self.attributes.get("title")

    @property
    def length(self) -> int | None:
        """Get the item length in seconds."""
        return self.attributes.get("length")

    @property
    def created_at(self) -> datetime | None:
        """Get the item creation time."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the item last update time."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at


class PCOTeam(PCOBaseModel):
    """Represents a team in Planning Center Services."""

    id: str
    type: str = "Team"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def name(self) -> str | None:
        """Get the team name."""
        return self.attributes.get("name")

    @property
    def created_at(self) -> datetime | None:
        """Get the team creation time."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the team last update time."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at


class PCOTeamPosition(PCOBaseModel):
    """Represents a team position in Planning Center Services."""

    id: str
    type: str = "TeamPosition"
    attributes: dict[str, Any] = {}
    relationships: PCORelationships | None = None
    links: PCOLinks | None = None
    meta: dict[str, Any] | None = None

    @property
    def name(self) -> str | None:
        """Get the team position name."""
        return self.attributes.get("name")

    @property
    def created_at(self) -> datetime | None:
        """Get the team position creation time."""
        created_at = self.attributes.get("created_at")
        if created_at and isinstance(created_at, str):
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return created_at

    @property
    def updated_at(self) -> datetime | None:
        """Get the team position last update time."""
        updated_at = self.attributes.get("updated_at")
        if updated_at and isinstance(updated_at, str):
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return updated_at


class PCOServiceService:
    """Service for managing Planning Center Services API."""

    def __init__(self, client):
        """Initialize the services service.

        Args:
            client: Planning Center API client
        """
        self.client = client
        self.base_url = "/services/v2"

    # Service Type Methods
    async def get_service_types(
        self,
        per_page: int | None = None,
        offset: int | None = None,
    ) -> list[PCOServiceType]:
        """Get all service types.

        Args:
            per_page: Number of records per page (1-100, default 25)
            offset: Offset for pagination

        Returns:
            List of service types
        """
        params = {}
        if per_page is not None:
            params["per_page"] = per_page
        if offset is not None:
            params["offset"] = offset

        response = await self.client.get(f"{self.base_url}/service_types", params=params)
        return [PCOServiceType(**item) for item in response.get("data", [])]

    async def get_service_type(self, service_type_id: str) -> PCOServiceType:
        """Get a specific service type.

        Args:
            service_type_id: The service type ID

        Returns:
            The service type
        """
        response = await self.client.get(f"{self.base_url}/service_types/{service_type_id}")
        return PCOServiceType(**response["data"])

    # Plan Methods
    async def get_plans(
        self,
        service_type_id: str | None = None,
        per_page: int | None = None,
        offset: int | None = None,
    ) -> list[PCOPlan]:
        """Get all plans.

        Args:
            service_type_id: Filter by service type ID
            per_page: Number of records per page (1-100, default 25)
            offset: Offset for pagination

        Returns:
            List of plans
        """
        params = {}
        if service_type_id:
            params["service_type_id"] = service_type_id
        if per_page is not None:
            params["per_page"] = per_page
        if offset is not None:
            params["offset"] = offset

        response = await self.client.get(f"{self.base_url}/plans", params=params)
        return [PCOPlan(**item) for item in response.get("data", [])]

    async def get_plan(self, plan_id: str) -> PCOPlan:
        """Get a specific plan.

        Args:
            plan_id: The plan ID

        Returns:
            The plan
        """
        response = await self.client.get(f"{self.base_url}/plans/{plan_id}")
        return PCOPlan(**response["data"])

    async def create_plan(
        self,
        service_type_id: str,
        title: str,
        series_title: str | None = None,
    ) -> PCOPlan:
        """Create a new plan.

        Args:
            service_type_id: The service type ID
            title: The plan title
            series_title: The series title (optional)

        Returns:
            The created plan
        """
        data = {
            "data": {
                "type": "Plan",
                "attributes": {
                    "title": title,
                },
                "relationships": {
                    "service_type": {
                        "data": {
                            "type": "ServiceType",
                            "id": service_type_id,
                        }
                    }
                },
            }
        }
        if series_title:
            data["data"]["attributes"]["series_title"] = series_title

        response = await self.client.post(f"{self.base_url}/plans", json=data)
        return PCOPlan(**response["data"])

    async def update_plan(
        self,
        plan_id: str,
        title: str | None = None,
        series_title: str | None = None,
    ) -> PCOPlan:
        """Update a plan.

        Args:
            plan_id: The plan ID
            title: The plan title (optional)
            series_title: The series title (optional)

        Returns:
            The updated plan
        """
        attributes = {}
        if title is not None:
            attributes["title"] = title
        if series_title is not None:
            attributes["series_title"] = series_title

        data = {
            "data": {
                "type": "Plan",
                "id": plan_id,
                "attributes": attributes,
            }
        }
        response = await self.client.patch(f"{self.base_url}/plans/{plan_id}", json=data)
        return PCOPlan(**response["data"])

    async def delete_plan(self, plan_id: str) -> None:
        """Delete a plan.

        Args:
            plan_id: The plan ID
        """
        await self.client.delete(f"{self.base_url}/plans/{plan_id}")

    # Song Methods
    async def get_songs(
        self,
        per_page: int | None = None,
        offset: int | None = None,
    ) -> list[PCOSong]:
        """Get all songs.

        Args:
            per_page: Number of records per page (1-100, default 25)
            offset: Offset for pagination

        Returns:
            List of songs
        """
        params = {}
        if per_page is not None:
            params["per_page"] = per_page
        if offset is not None:
            params["offset"] = offset

        response = await self.client.get(f"{self.base_url}/songs", params=params)
        return [PCOSong(**item) for item in response.get("data", [])]

    async def get_song(self, song_id: str) -> PCOSong:
        """Get a specific song.

        Args:
            song_id: The song ID

        Returns:
            The song
        """
        response = await self.client.get(f"{self.base_url}/songs/{song_id}")
        return PCOSong(**response["data"])

    async def create_song(
        self,
        title: str,
        author: str | None = None,
        ccli_number: str | None = None,
    ) -> PCOSong:
        """Create a new song.

        Args:
            title: The song title
            author: The song author (optional)
            ccli_number: The CCLI number (optional)

        Returns:
            The created song
        """
        attributes = {"title": title}
        if author:
            attributes["author"] = author
        if ccli_number:
            attributes["ccli_number"] = ccli_number

        data = {
            "data": {
                "type": "Song",
                "attributes": attributes,
            }
        }
        response = await self.client.post(f"{self.base_url}/songs", json=data)
        return PCOSong(**response["data"])

    # Arrangement Methods
    async def get_arrangements(
        self,
        song_id: str,
        per_page: int | None = None,
        offset: int | None = None,
    ) -> list[PCOArrangement]:
        """Get arrangements for a song.

        Args:
            song_id: The song ID
            per_page: Number of records per page (1-100, default 25)
            offset: Offset for pagination

        Returns:
            List of arrangements
        """
        params = {}
        if per_page is not None:
            params["per_page"] = per_page
        if offset is not None:
            params["offset"] = offset

        response = await self.client.get(f"{self.base_url}/songs/{song_id}/arrangements", params=params)
        return [PCOArrangement(**item) for item in response.get("data", [])]

    async def get_arrangement(self, song_id: str, arrangement_id: str) -> PCOArrangement:
        """Get a specific arrangement.

        Args:
            song_id: The song ID
            arrangement_id: The arrangement ID

        Returns:
            The arrangement
        """
        response = await self.client.get(f"{self.base_url}/songs/{song_id}/arrangements/{arrangement_id}")
        return PCOArrangement(**response["data"])

    # Key Methods
    async def get_keys(
        self,
        per_page: int | None = None,
        offset: int | None = None,
    ) -> list[PCOKey]:
        """Get all keys.

        Args:
            per_page: Number of records per page (1-100, default 25)
            offset: Offset for pagination

        Returns:
            List of keys
        """
        params = {}
        if per_page is not None:
            params["per_page"] = per_page
        if offset is not None:
            params["offset"] = offset

        response = await self.client.get(f"{self.base_url}/keys", params=params)
        return [PCOKey(**item) for item in response.get("data", [])]

    async def get_key(self, key_id: str) -> PCOKey:
        """Get a specific key.

        Args:
            key_id: The key ID

        Returns:
            The key
        """
        response = await self.client.get(f"{self.base_url}/keys/{key_id}")
        return PCOKey(**response["data"])

    # Team Methods
    async def get_teams(
        self,
        service_type_id: str | None = None,
        per_page: int | None = None,
        offset: int | None = None,
    ) -> list[PCOTeam]:
        """Get all teams.

        Args:
            service_type_id: Filter by service type ID
            per_page: Number of records per page (1-100, default 25)
            offset: Offset for pagination

        Returns:
            List of teams
        """
        params = {}
        if service_type_id:
            params["service_type_id"] = service_type_id
        if per_page is not None:
            params["per_page"] = per_page
        if offset is not None:
            params["offset"] = offset

        response = await self.client.get(f"{self.base_url}/teams", params=params)
        return [PCOTeam(**item) for item in response.get("data", [])]

    async def get_team(self, team_id: str) -> PCOTeam:
        """Get a specific team.

        Args:
            team_id: The team ID

        Returns:
            The team
        """
        response = await self.client.get(f"{self.base_url}/teams/{team_id}")
        return PCOTeam(**response["data"])
