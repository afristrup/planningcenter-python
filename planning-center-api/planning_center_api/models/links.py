"""Link models for Planning Center API."""

from typing import Any

from pydantic import Field

from .base import PCOBaseModel


class PCOLink(PCOBaseModel):
    """Represents a link in JSON API format."""

    href: str
    meta: dict[str, Any] | None = Field(
        default=None, description="Additional metadata for the link"
    )


class PCOLinks(PCOBaseModel):
    """Represents links object in JSON API format."""

    self: PCOLink | None = Field(
        default=None, description="Link to the resource itself"
    )
    related: PCOLink | None = Field(
        default=None, description="Link to related resources"
    )
    first: PCOLink | None = Field(default=None, description="Link to the first page")
    last: PCOLink | None = Field(default=None, description="Link to the last page")
    prev: PCOLink | None = Field(default=None, description="Link to the previous page")
    next: PCOLink | None = Field(default=None, description="Link to the next page")

    def get_pagination_links(self) -> dict[str, str | None]:
        """Get pagination links as a dictionary of URLs."""
        return {
            "first": self.first.href if self.first else None,
            "last": self.last.href if self.last else None,
            "prev": self.prev.href if self.prev else None,
            "next": self.next.href if self.next else None,
        }

    def has_next_page(self) -> bool:
        """Check if there is a next page available."""
        return self.next is not None

    def has_prev_page(self) -> bool:
        """Check if there is a previous page available."""
        return self.prev is not None
