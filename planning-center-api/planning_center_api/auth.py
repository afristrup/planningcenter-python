"""Authentication handling for Planning Center API."""

import base64

from .config import PCOConfig


class PCOAuth:
    """Handles authentication for Planning Center API."""

    def __init__(self, config: PCOConfig):
        self.config = config

    def get_headers(self) -> dict[str, str]:
        """Get authentication headers for API requests."""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        if self.config.access_token:
            headers["Authorization"] = f"Bearer {self.config.access_token}"
        elif self.config.app_id and self.config.secret:
            headers["Authorization"] = f"Basic {self._encode_basic_auth()}"
        else:
            raise ValueError(
                "Either access_token or (app_id and secret) must be provided"
            )

        return headers

    def _encode_basic_auth(self) -> str:
        """Encode app_id and secret for basic authentication."""
        credentials = f"{self.config.app_id}:{self.config.secret}"
        return base64.b64encode(credentials.encode()).decode()

    def is_authenticated(self) -> bool:
        """Check if authentication credentials are available."""
        return bool(
            self.config.access_token or (self.config.app_id and self.config.secret)
        )

    def get_auth_type(self) -> str:
        """Get the type of authentication being used."""
        if self.config.access_token:
            return "bearer"
        elif self.config.app_id and self.config.secret:
            return "basic"
        else:
            return "none"
