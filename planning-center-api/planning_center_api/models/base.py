"""Base Pydantic models for Planning Center API."""

from datetime import datetime
from typing import TYPE_CHECKING, Any, Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .links import PCOLinks
    from .relationships import PCORelationships

T = TypeVar("T")


class PCOBaseModel(BaseModel):
    """Base model for all Planning Center API models."""

    model_config = ConfigDict(
        extra="allow",
        validate_assignment=True,
        use_enum_values=True,
        str_strip_whitespace=True,
    )


class PCOLink(PCOBaseModel):
    """Represents a link in JSON API format."""

    href: str
    meta: dict[str, Any] | None = None


class PCOMeta(PCOBaseModel):
    """Represents meta information in JSON API format."""

    count: int | None = None
    total_count: int | None = None
    total_pages: int | None = None
    current_page: int | None = None
    per_page: int | None = None
    offset: int | None = None
    limit: int | None = None


class PCORelationship(PCOBaseModel):
    """Represents a relationship in JSON API format."""

    links: "PCOLinks | None" = None
    data: dict[str, Any] | list[dict[str, Any]] | None = None
    meta: dict[str, Any] | None = None


class PCOResource(PCOBaseModel, Generic[T]):
    """Represents a resource in JSON API format."""

    id: str
    type: str
    attributes: dict[str, Any] = Field(default_factory=dict)
    relationships: "PCORelationships | None" = None
    links: "PCOLinks | None" = None
    meta: dict[str, Any] | None = None

    def get_attribute(self, key: str, default: Any = None) -> Any:
        """Get an attribute value with optional default."""
        return self.attributes.get(key, default)

    def set_attribute(self, key: str, value: Any) -> None:
        """Set an attribute value."""
        self.attributes[key] = value

    def get_relationship_data(
        self, relationship_name: str
    ) -> dict[str, Any] | list[dict[str, Any]] | None:
        """Get relationship data for a specific relationship."""
        if not self.relationships:
            return None
        relationship = getattr(self.relationships, relationship_name, None)
        return relationship.data if relationship else None


class PCOCollection(PCOBaseModel, Generic[T]):
    """Represents a collection of resources in JSON API format."""

    data: list[PCOResource[T]] = Field(default_factory=list)
    included: list[PCOResource[T]] | None = None
    links: "PCOLinks | None" = None
    meta: PCOMeta | None = None

    def __len__(self) -> int:
        """Return the number of resources in the collection."""
        return len(self.data)

    def __iter__(self):
        """Allow iteration over the resources."""
        return iter(self.data)

    def __getitem__(self, index: int) -> PCOResource[T]:
        """Allow indexing into the collection."""
        return self.data[index]

    def get_included_resource(
        self, resource_type: str, resource_id: str
    ) -> PCOResource[T] | None:
        """Get an included resource by type and ID."""
        if not self.included:
            return None

        for resource in self.included:
            if resource.type == resource_type and resource.id == resource_id:
                return resource
        return None

    def get_included_resources(self, resource_type: str) -> list[PCOResource[T]]:
        """Get all included resources of a specific type."""
        if not self.included:
            return []

        return [
            resource for resource in self.included if resource.type == resource_type
        ]


class PCOErrorDetail(PCOBaseModel):
    """Represents an error detail in JSON API format."""

    id: str | None = None
    status: str | None = None
    code: str | None = None
    title: str | None = None
    detail: str | None = None
    source: dict[str, Any] | None = None
    meta: dict[str, Any] | None = None


class PCOErrorResponse(PCOBaseModel):
    """Represents an error response in JSON API format."""

    errors: list[PCOErrorDetail] = Field(default_factory=list)
    meta: dict[str, Any] | None = None
    links: "PCOLinks | None" = None

    def get_error_messages(self) -> list[str]:
        """Get all error messages from the response."""
        messages = []
        for error in self.errors:
            if error.detail:
                messages.append(error.detail)
            elif error.title:
                messages.append(error.title)
        return messages

    def get_first_error_message(self) -> str | None:
        """Get the first error message from the response."""
        messages = self.get_error_messages()
        return messages[0] if messages else None


class PCOWebhookPayload(PCOBaseModel):
    """Represents a webhook payload from Planning Center."""

    id: str
    type: str
    attributes: dict[str, Any] = Field(default_factory=dict)
    relationships: "PCORelationships | None" = None
    links: "PCOLinks | None" = None
    meta: dict[str, Any] | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def get_attribute(self, key: str, default: Any = None) -> Any:
        """Get an attribute value with optional default."""
        return self.attributes.get(key, default)


class PCOWebhookEvent(PCOBaseModel):
    """Represents a webhook event from Planning Center."""

    event_type: str
    resource: PCOWebhookPayload
    timestamp: datetime
    webhook_id: str | None = None
    organization_id: str | None = None
