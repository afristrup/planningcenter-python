"""Relationship models for Planning Center API."""

from typing import Any

from pydantic import Field

from .base import PCOBaseModel
from .links import PCOLinks


class PCORelationship(PCOBaseModel):
    """Represents a relationship in JSON API format."""

    links: PCOLinks | None = Field(
        default=None, description="Links related to the relationship"
    )
    data: dict[str, Any] | list[dict[str, Any]] | None = Field(
        default=None, description="Resource identifier(s) for the relationship"
    )
    meta: dict[str, Any] | None = Field(
        default=None, description="Additional metadata for the relationship"
    )

    def is_single_resource(self) -> bool:
        """Check if this relationship represents a single resource."""
        return isinstance(self.data, dict)

    def is_collection(self) -> bool:
        """Check if this relationship represents a collection of resources."""
        return isinstance(self.data, list)

    def get_resource_ids(self) -> list[str]:
        """Get all resource IDs from the relationship data."""
        if not self.data:
            return []

        if isinstance(self.data, dict):
            return [self.data.get("id")] if self.data.get("id") else []
        elif isinstance(self.data, list):
            return [item.get("id") for item in self.data if item.get("id")]

        return []

    def get_resource_types(self) -> list[str]:
        """Get all resource types from the relationship data."""
        if not self.data:
            return []

        if isinstance(self.data, dict):
            return [self.data.get("type")] if self.data.get("type") else []
        elif isinstance(self.data, list):
            return [item.get("type") for item in self.data if item.get("type")]

        return []


class PCORelationships(PCOBaseModel):
    """Represents relationships object in JSON API format."""

    def __getitem__(self, key: str) -> PCORelationship:
        """Allow dictionary-style access to relationships."""
        return getattr(self, key)

    def __setitem__(self, key: str, value: PCORelationship) -> None:
        """Allow dictionary-style setting of relationships."""
        setattr(self, key, value)

    def get_relationship(self, name: str) -> PCORelationship | None:
        """Get a specific relationship by name."""
        return getattr(self, name, None)

    def has_relationship(self, name: str) -> bool:
        """Check if a relationship exists."""
        return hasattr(self, name) and getattr(self, name) is not None

    def get_relationship_names(self) -> list[str]:
        """Get all relationship names."""
        return [name for name in self.model_fields if hasattr(self, name)]

    def get_relationship_data(
        self, name: str
    ) -> dict[str, Any] | list[dict[str, Any]] | None:
        """Get relationship data for a specific relationship."""
        relationship = self.get_relationship(name)
        return relationship.data if relationship else None
