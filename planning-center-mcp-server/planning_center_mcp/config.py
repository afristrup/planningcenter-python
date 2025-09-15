"""Configuration for Planning Center MCP Server."""

import os

from planning_center_api import PCOConfig as BasePCOConfig


class PCOConfig(BasePCOConfig):
    """Configuration for Planning Center API - extends the base config."""

    @classmethod
    def from_env(cls) -> "PCOConfig":
        """Create configuration from environment variables."""
        return cls(
            app_id=os.getenv("PCO_APP_ID"),
            secret=os.getenv("PCO_SECRET"),
            access_token=os.getenv("PCO_ACCESS_TOKEN"),
            base_url=os.getenv("PCO_BASE_URL", "https://api.planningcenteronline.com"),
        )
