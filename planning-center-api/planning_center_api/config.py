"""Configuration and constants for Planning Center API."""

from dataclasses import dataclass
from enum import Enum


class PCOProduct(Enum):
    """Planning Center product identifiers."""

    PEOPLE = "people"
    SERVICES = "services"
    CHECK_INS = "check_ins"
    GIVING = "giving"
    GROUPS = "groups"
    CALENDAR = "calendar"
    REGISTRATIONS = "registrations"
    ORGANIZATION = "organization"
    WEBHOOKS = "webhooks"


@dataclass
class PCOConfig:
    """Configuration for Planning Center API client."""

    # API Configuration
    base_url: str = "https://api.planningcenteronline.com"
    api_version: str = "v2"

    # Authentication
    app_id: str | None = None
    secret: str | None = None
    access_token: str | None = None

    # Webhook Configuration
    webhook_secret: str | None = None

    # Request Configuration
    timeout: float = 30.0
    max_retries: int = 3
    retry_delay: float = 1.0
    backoff_factor: float = 2.0

    # Rate Limiting
    rate_limit_requests: int = 100
    rate_limit_window: int = 60  # seconds

    # Pagination
    default_per_page: int = 25
    max_per_page: int = 100

    def get_auth_headers(self) -> dict[str, str]:
        """Get authentication headers for API requests."""
        if self.access_token:
            return {"Authorization": f"Bearer {self.access_token}"}
        elif self.app_id and self.secret:
            return {"Authorization": f"Basic {self._encode_basic_auth()}"}
        else:
            raise ValueError(
                "Either access_token or (app_id and secret) must be provided"
            )

    def _encode_basic_auth(self) -> str:
        """Encode app_id and secret for basic authentication."""
        import base64

        credentials = f"{self.app_id}:{self.secret}"
        return base64.b64encode(credentials.encode()).decode()


# API Endpoints Configuration
API_ENDPOINTS = {
    PCOProduct.PEOPLE: {
        "base": "people/v2",
        "resources": {
            "people": "people",
            "emails": "emails",
            "phone_numbers": "phone_numbers",
            "addresses": "addresses",
            "field_data": "field_data",
            "custom_fields": "custom_fields",
            "households": "households",
            "inactive_reasons": "inactive_reasons",
            "marital_statuses": "marital_statuses",
            "name_suffixes": "name_suffixes",
            "name_titles": "name_titles",
            "workflows": "workflows",
            "workflow_steps": "workflow_steps",
        },
    },
    PCOProduct.SERVICES: {
        "base": "services/v2",
        "resources": {
            "services": "services",
            "service_types": "service_types",
            "plans": "plans",
            "plan_times": "plan_times",
            "plan_people": "plan_people",
            "plan_notes": "plan_notes",
            "songs": "songs",
            "arrangements": "arrangements",
            "keys": "keys",
            "attachments": "attachments",
            "media": "media",
            "folders": "folders",
            "templates": "templates",
        },
    },
    PCOProduct.CHECK_INS: {
        "base": "check_ins/v2",
        "resources": {
            "events": "events",
            "locations": "locations",
            "stations": "stations",
            "check_ins": "check_ins",
            "people": "people",
            "households": "households",
        },
    },
    PCOProduct.GIVING: {
        "base": "giving/v2",
        "resources": {
            "donations": "donations",
            "funds": "funds",
            "batches": "batches",
            "designations": "designations",
            "pledges": "pledges",
            "recurring_donations": "recurring_donations",
        },
    },
    PCOProduct.GROUPS: {
        "base": "groups/v2",
        "resources": {
            "groups": "groups",
            "group_types": "group_types",
            "group_times": "group_times",
            "group_memberships": "group_memberships",
            "group_notes": "group_notes",
        },
    },
    PCOProduct.CALENDAR: {
        "base": "calendar/v2",
        "resources": {
            "attachments": "attachments",
            "conflicts": "conflicts",
            "events": "events",
            "event_connections": "event_connections",
            "event_instances": "event_instances",
            "event_resource_answers": "answers",
            "event_resource_requests": "event_resource_requests",
            "event_times": "event_times",
            "feeds": "feeds",
            "job_statuses": "job_statuses",
            "organization": "organization",
            "people": "people",
            "report_templates": "report_templates",
            "required_approvals": "required_approvals",
            "resources": "resources",
            "resource_approval_groups": "resource_approval_groups",
            "resource_bookings": "resource_bookings",
            "resource_folders": "resource_folders",
            "resource_questions": "resource_questions",
            "resource_suggestions": "resource_suggestions",
            "room_setups": "room_setups",
            "tags": "tags",
            "tag_groups": "tag_groups",
        },
    },
    PCOProduct.REGISTRATIONS: {
        "base": "registrations/v2",
        "resources": {
            "events": "events",
            "event_instances": "event_instances",
            "event_times": "event_times",
            "registrations": "registrations",
            "registration_forms": "registration_forms",
            "registration_form_fields": "registration_form_fields",
            "registration_form_field_options": "registration_form_field_options",
            "registration_instances": "registration_instances",
            "registration_instances_people": "registration_instances_people",
            "registration_instances_people_answers": "registration_instances_people_answers",
            "attendee": "attendee",
        },
    },
    PCOProduct.ORGANIZATION: {
        "base": "api/v2",
        "resources": {
            "connected_applications": "connected_applications",
            "connected_application_people": "people",
            "oauth_applications": "oauth_applications",
            "oauth_application_mau": "mau",
            "organization": "",
            "person": "",
            "personal_access_tokens": "personal_access_tokens",
        },
    },
    PCOProduct.WEBHOOKS: {
        "base": "webhooks/v2",
        "resources": {
            "webhook_subscriptions": "webhook_subscriptions",
            "events": "events",
            "deliveries": "deliveries",
            "available_events": "available_events",
            "organization": "",
        },
    },
}

# HTTP Status Codes
HTTP_STATUS = {
    200: "OK",
    201: "Created",
    204: "No Content",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    422: "Unprocessable Entity",
    429: "Too Many Requests",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
}

# Webhook Event Types
WEBHOOK_EVENTS = {
    PCOProduct.PEOPLE: [
        "people.created",
        "people.updated",
        "people.deleted",
        "emails.created",
        "emails.updated",
        "emails.deleted",
        "phone_numbers.created",
        "phone_numbers.updated",
        "phone_numbers.deleted",
    ],
    PCOProduct.SERVICES: [
        "services.created",
        "services.updated",
        "services.deleted",
        "plans.created",
        "plans.updated",
        "plans.deleted",
        "songs.created",
        "songs.updated",
        "songs.deleted",
    ],
    PCOProduct.CHECK_INS: [
        "check_ins.created",
        "check_ins.updated",
        "check_ins.deleted",
        "events.created",
        "events.updated",
        "events.deleted",
    ],
    PCOProduct.GIVING: [
        "donations.created",
        "donations.updated",
        "donations.deleted",
        "funds.created",
        "funds.updated",
        "funds.deleted",
    ],
    PCOProduct.GROUPS: [
        "groups.created",
        "groups.updated",
        "groups.deleted",
        "group_memberships.created",
        "group_memberships.updated",
        "group_memberships.deleted",
    ],
    PCOProduct.CALENDAR: [
        "events.created",
        "events.updated",
        "events.deleted",
        "event_instances.created",
        "event_instances.updated",
        "event_instances.deleted",
    ],
    PCOProduct.REGISTRATIONS: [
        "events.created",
        "events.updated",
        "events.deleted",
        "registrations.created",
        "registrations.updated",
        "registrations.deleted",
        "registration_instances.created",
        "registration_instances.updated",
        "registration_instances.deleted",
        "registration_instances_people.created",
        "registration_instances_people.updated",
        "registration_instances_people.deleted",
        "attendee.created",
        "attendee.updated",
        "attendee.deleted",
    ],
    PCOProduct.ORGANIZATION: [
        "connected_applications.created",
        "connected_applications.updated",
        "connected_applications.deleted",
        "oauth_applications.created",
        "oauth_applications.updated",
        "oauth_applications.deleted",
        "personal_access_tokens.created",
        "personal_access_tokens.updated",
        "personal_access_tokens.deleted",
    ],
    PCOProduct.WEBHOOKS: [
        "webhook_subscriptions.created",
        "webhook_subscriptions.updated",
        "webhook_subscriptions.deleted",
        "events.created",
        "events.updated",
        "events.deleted",
        "deliveries.created",
        "deliveries.updated",
        "deliveries.deleted",
    ],
}
