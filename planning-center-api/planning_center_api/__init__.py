"""Planning Center API Wrapper - A comprehensive Python client for Planning Center APIs."""

from .client import PCOClient
from .config import PCOConfig, PCOProduct
from .exceptions import (
    PCOAuthenticationError,
    PCOError,
    PCONotFoundError,
    PCOPermissionError,
    PCORateLimitError,
    PCOServerError,
    PCOValidationError,
)
from .models.base import PCOBaseModel, PCOCollection, PCOResource
from .webhooks import PCOWebhookHandler, handle_webhook_event

__version__ = "0.1.0"
__all__ = [
    "PCOClient",
    "PCOProduct",
    "PCOConfig",
    "PCOError",
    "PCOAuthenticationError",
    "PCOPermissionError",
    "PCORateLimitError",
    "PCOValidationError",
    "PCONotFoundError",
    "PCOServerError",
    "PCOBaseModel",
    "PCOResource",
    "PCOCollection",
    "PCOWebhookHandler",
    "handle_webhook_event",
]
