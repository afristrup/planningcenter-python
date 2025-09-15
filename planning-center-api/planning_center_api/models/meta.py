"""Meta information models for Planning Center API."""

from pydantic import Field

from .base import PCOBaseModel


class PCOMeta(PCOBaseModel):
    """Represents meta information in JSON API format."""

    count: int | None = Field(
        default=None, description="Number of items in current page"
    )
    total_count: int | None = Field(
        default=None, description="Total number of items across all pages"
    )
    total_pages: int | None = Field(default=None, description="Total number of pages")
    current_page: int | None = Field(default=None, description="Current page number")
    per_page: int | None = Field(default=None, description="Number of items per page")
    offset: int | None = Field(default=None, description="Offset for pagination")
    limit: int | None = Field(default=None, description="Limit for pagination")

    def get_pagination_info(self) -> dict[str, int | None]:
        """Get pagination information as a dictionary."""
        return {
            "count": self.count,
            "total_count": self.total_count,
            "total_pages": self.total_pages,
            "current_page": self.current_page,
            "per_page": self.per_page,
            "offset": self.offset,
            "limit": self.limit,
        }

    def has_more_pages(self) -> bool:
        """Check if there are more pages available."""
        if self.current_page is None or self.total_pages is None:
            return False
        return self.current_page < self.total_pages

    def get_remaining_items(self) -> int | None:
        """Get the number of remaining items across all pages."""
        if self.total_count is None or self.count is None:
            return None
        return max(0, self.total_count - self.count)
