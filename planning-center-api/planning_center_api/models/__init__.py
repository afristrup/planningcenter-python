"""Pydantic models for Planning Center API."""

from .base import (
    PCOBaseModel,
    PCOCollection,
    PCOErrorResponse,
    PCOResource,
    PCOWebhookPayload,
)
from .links import PCOLink, PCOLinks
from .meta import PCOMeta
from .relationships import PCORelationship, PCORelationships

# Rebuild models to resolve forward references
PCOResource.model_rebuild()
PCOWebhookPayload.model_rebuild()
PCOCollection.model_rebuild()
PCOErrorResponse.model_rebuild()

__all__ = [
    "PCOBaseModel",
    "PCOResource",
    "PCOCollection",
    "PCOErrorResponse",
    "PCOLinks",
    "PCOLink",
    "PCOMeta",
    "PCORelationship",
    "PCORelationships",
]
