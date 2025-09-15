"""Planning Center API client for MCP server - using the existing planning-center-api package."""

from planning_center_api import PCOClient as BasePCOClient

from .config import PCOConfig


class PCOClient(BasePCOClient):
    """Planning Center API client - extends the base client with MCP-specific methods."""

    def __init__(self, config: PCOConfig):
        super().__init__(
            app_id=config.app_id,
            secret=config.secret,
            access_token=config.access_token,
            webhook_secret=config.webhook_secret,
            config=config,
        )
