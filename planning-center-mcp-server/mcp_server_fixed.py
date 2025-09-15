#!/usr/bin/env python3
"""Fixed MCP server entry point for Planning Center API."""

import asyncio
import logging
import sys
from typing import Any, Dict, List, Optional

from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from planning_center_api.config import PCOConfig, PCOProduct
from planning_center_api.client import PCOClient


# Set up logging to stderr so it appears in Claude Desktop logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

# Global variables
config: Optional[PCOConfig] = None
client: Optional[PCOClient] = None

# Create MCP server
server = Server("planning-center-api")


def get_pco_client() -> PCOClient:
    """Get or create PCO client."""
    global client
    if client is None:
        if config is None:
            raise ValueError("Configuration not initialized")
        client = PCOClient(config)
    return client


@server.list_tools()
async def list_tools() -> List[Tool]:
    """List available tools."""
    logger.info("Listing tools")
    return [
        Tool(
            name="get_people",
            description="Get people from Planning Center People with optional filtering",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {
                        "type": "integer",
                        "description": "Number of people per page (max 100)",
                        "default": 25,
                    },
                    "offset": {
                        "type": "integer",
                        "description": "Offset for pagination",
                        "default": 0,
                    },
                    "include": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Related resources to include",
                    },
                    "search": {
                        "type": "string",
                        "description": "Search query for people",
                    },
                    "status": {
                        "type": "string",
                        "description": "Filter by status (active, inactive)",
                    },
                    "email": {
                        "type": "string",
                        "description": "Filter by email address",
                    },
                    "phone": {
                        "type": "string",
                        "description": "Filter by phone number",
                    },
                },
            },
        ),
        Tool(
            name="get_person",
            description="Get a specific person by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "person_id": {
                        "type": "string",
                        "description": "ID of the person to retrieve",
                    },
                    "include": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Related resources to include",
                    },
                },
                "required": ["person_id"],
            },
        ),
        Tool(
            name="get_services",
            description="Get services from Planning Center Services",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {
                        "type": "integer",
                        "description": "Number of services per page (max 100)",
                        "default": 25,
                    },
                    "offset": {
                        "type": "integer",
                        "description": "Offset for pagination",
                        "default": 0,
                    },
                    "include": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Related resources to include",
                    },
                },
            },
        ),
        Tool(
            name="get_service",
            description="Get a specific service by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "service_id": {
                        "type": "string",
                        "description": "ID of the service to retrieve",
                    },
                    "include": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Related resources to include",
                    },
                },
                "required": ["service_id"],
            },
        ),
        Tool(
            name="get_plans",
            description="Get plans from Planning Center Services",
            inputSchema={
                "type": "object",
                "properties": {
                    "service_id": {
                        "type": "string",
                        "description": "Filter plans by service ID",
                    },
                    "per_page": {
                        "type": "integer",
                        "description": "Number of plans per page (max 100)",
                        "default": 25,
                    },
                    "offset": {
                        "type": "integer",
                        "description": "Offset for pagination",
                        "default": 0,
                    },
                    "include": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Related resources to include",
                    },
                },
            },
        ),
        Tool(
            name="get_plan",
            description="Get a specific plan by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "plan_id": {
                        "type": "string",
                        "description": "ID of the plan to retrieve",
                    },
                    "include": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Related resources to include",
                    },
                },
                "required": ["plan_id"],
            },
        ),
        Tool(
            name="get_registrations",
            description="Get registrations from Planning Center Registrations",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {
                        "type": "integer",
                        "description": "Number of registrations per page (max 100)",
                        "default": 25,
                    },
                    "offset": {
                        "type": "integer",
                        "description": "Offset for pagination",
                        "default": 0,
                    },
                    "include": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Related resources to include",
                    },
                    "status": {
                        "type": "string",
                        "description": "Filter by status (open, closed)",
                    },
                },
            },
        ),
        Tool(
            name="get_registration",
            description="Get a specific registration by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "registration_id": {
                        "type": "string",
                        "description": "ID of the registration to retrieve",
                    },
                    "include": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Related resources to include",
                    },
                },
                "required": ["registration_id"],
            },
        ),
        Tool(
            name="get_attendees",
            description="Get attendees from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {
                        "type": "integer",
                        "description": "Number of attendees per page (max 100)",
                        "default": 25,
                    },
                    "offset": {
                        "type": "integer",
                        "description": "Offset for pagination",
                        "default": 0,
                    },
                    "include": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Related resources to include",
                    },
                    "event_id": {"type": "string", "description": "Filter by event ID"},
                    "registration_instance_id": {
                        "type": "string",
                        "description": "Filter by registration instance ID",
                    },
                    "attendance_status": {
                        "type": "string",
                        "description": "Filter by attendance status (checked_in, checked_out)",
                    },
                },
            },
        ),
        Tool(
            name="get_attendee",
            description="Get a specific attendee by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "attendee_id": {
                        "type": "string",
                        "description": "ID of the attendee to retrieve",
                    },
                    "include": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Related resources to include",
                    },
                },
                "required": ["attendee_id"],
            },
        ),
        Tool(
            name="get_event_attendees",
            description="Get all attendees for a specific event/registration (convenience tool)",
            inputSchema={
                "type": "object",
                "properties": {
                    "event_id": {
                        "type": "string",
                        "description": "Event ID to get attendees for",
                    },
                    "registration_instance_id": {
                        "type": "string",
                        "description": "Registration instance ID to get attendees for",
                    },
                    "per_page": {
                        "type": "integer",
                        "description": "Number of attendees per page (max 100)",
                        "default": 25,
                    },
                    "offset": {
                        "type": "integer",
                        "description": "Offset for pagination",
                        "default": 0,
                    },
                    "include": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Related resources to include",
                    },
                    "attendance_status": {
                        "type": "string",
                        "description": "Filter by attendance status (checked_in, checked_out)",
                    },
                },
                "anyOf": [
                    {"required": ["event_id"]},
                    {"required": ["registration_instance_id"]}
                ],
            },
        ),
        # People API - Additional endpoints
        Tool(
            name="get_person_addresses",
            description="Get addresses for a specific person",
            inputSchema={
                "type": "object",
                "properties": {
                    "person_id": {"type": "string", "description": "Person ID"},
                    "per_page": {"type": "integer", "description": "Number of addresses per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["person_id"],
            },
        ),
        Tool(
            name="get_person_emails",
            description="Get email addresses for a specific person",
            inputSchema={
                "type": "object",
                "properties": {
                    "person_id": {"type": "string", "description": "Person ID"},
                    "per_page": {"type": "integer", "description": "Number of emails per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["person_id"],
            },
        ),
        Tool(
            name="get_person_phones",
            description="Get phone numbers for a specific person",
            inputSchema={
                "type": "object",
                "properties": {
                    "person_id": {"type": "string", "description": "Person ID"},
                    "per_page": {"type": "integer", "description": "Number of phones per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["person_id"],
            },
        ),
        Tool(
            name="get_person_background_checks",
            description="Get background checks for a specific person",
            inputSchema={
                "type": "object",
                "properties": {
                    "person_id": {"type": "string", "description": "Person ID"},
                    "per_page": {"type": "integer", "description": "Number of background checks per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["person_id"],
            },
        ),
        Tool(
            name="get_field_definitions",
            description="Get field definitions from Planning Center People",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of field definitions per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_forms",
            description="Get forms from Planning Center People",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of forms per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                    "active": {"type": "boolean", "description": "Filter by active status"},
                },
            },
        ),
        Tool(
            name="get_form",
            description="Get a specific form from Planning Center People",
            inputSchema={
                "type": "object",
                "properties": {
                    "form_id": {"type": "string", "description": "Form ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["form_id"],
            },
        ),
        Tool(
            name="get_campuses",
            description="Get campuses from Planning Center People",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of campuses per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_campus",
            description="Get a specific campus from Planning Center People",
            inputSchema={
                "type": "object",
                "properties": {
                    "campus_id": {"type": "string", "description": "Campus ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["campus_id"],
            },
        ),
        # Services API - Additional endpoints
        Tool(
            name="get_songs",
            description="Get songs from Planning Center Services",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of songs per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_song",
            description="Get a specific song from Planning Center Services",
            inputSchema={
                "type": "object",
                "properties": {
                    "song_id": {"type": "string", "description": "Song ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["song_id"],
            },
        ),
        Tool(
            name="get_arrangements",
            description="Get arrangements for a specific song",
            inputSchema={
                "type": "object",
                "properties": {
                    "song_id": {"type": "string", "description": "Song ID"},
                    "per_page": {"type": "integer", "description": "Number of arrangements per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["song_id"],
            },
        ),
        Tool(
            name="get_arrangement",
            description="Get a specific arrangement",
            inputSchema={
                "type": "object",
                "properties": {
                    "song_id": {"type": "string", "description": "Song ID"},
                    "arrangement_id": {"type": "string", "description": "Arrangement ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["song_id", "arrangement_id"],
            },
        ),
        Tool(
            name="get_keys",
            description="Get keys from Planning Center Services",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of keys per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_key",
            description="Get a specific key from Planning Center Services",
            inputSchema={
                "type": "object",
                "properties": {
                    "key_id": {"type": "string", "description": "Key ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["key_id"],
            },
        ),
        Tool(
            name="get_teams",
            description="Get teams from Planning Center Services",
            inputSchema={
                "type": "object",
                "properties": {
                    "service_type_id": {"type": "string", "description": "Filter by service type ID"},
                    "per_page": {"type": "integer", "description": "Number of teams per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_team",
            description="Get a specific team from Planning Center Services",
            inputSchema={
                "type": "object",
                "properties": {
                    "team_id": {"type": "string", "description": "Team ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["team_id"],
            },
        ),
        Tool(
            name="get_team_positions",
            description="Get team positions for a specific team",
            inputSchema={
                "type": "object",
                "properties": {
                    "team_id": {"type": "string", "description": "Team ID"},
                    "per_page": {"type": "integer", "description": "Number of team positions per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["team_id"],
            },
        ),
        Tool(
            name="get_team_position",
            description="Get a specific team position",
            inputSchema={
                "type": "object",
                "properties": {
                    "team_id": {"type": "string", "description": "Team ID"},
                    "team_position_id": {"type": "string", "description": "Team position ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["team_id", "team_position_id"],
            },
        ),
        # Giving API endpoints
        Tool(
            name="get_donations",
            description="Get donations from Planning Center Giving",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of donations per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                    "person_id": {"type": "string", "description": "Filter by person ID"},
                    "fund_id": {"type": "string", "description": "Filter by fund ID"},
                    "payment_method": {"type": "string", "description": "Filter by payment method"},
                    "payment_status": {"type": "string", "description": "Filter by payment status"},
                },
            },
        ),
        Tool(
            name="get_donation",
            description="Get a specific donation from Planning Center Giving",
            inputSchema={
                "type": "object",
                "properties": {
                    "donation_id": {"type": "string", "description": "Donation ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["donation_id"],
            },
        ),
        Tool(
            name="get_funds",
            description="Get funds from Planning Center Giving",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of funds per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_fund",
            description="Get a specific fund from Planning Center Giving",
            inputSchema={
                "type": "object",
                "properties": {
                    "fund_id": {"type": "string", "description": "Fund ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["fund_id"],
            },
        ),
        Tool(
            name="get_batches",
            description="Get batches from Planning Center Giving",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of batches per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                    "status": {"type": "string", "description": "Filter by batch status"},
                },
            },
        ),
        Tool(
            name="get_batch",
            description="Get a specific batch from Planning Center Giving",
            inputSchema={
                "type": "object",
                "properties": {
                    "batch_id": {"type": "string", "description": "Batch ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["batch_id"],
            },
        ),
        Tool(
            name="get_pledges",
            description="Get pledges from Planning Center Giving",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of pledges per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                    "person_id": {"type": "string", "description": "Filter by person ID"},
                    "pledge_campaign_id": {"type": "string", "description": "Filter by pledge campaign ID"},
                },
            },
        ),
        Tool(
            name="get_pledge",
            description="Get a specific pledge from Planning Center Giving",
            inputSchema={
                "type": "object",
                "properties": {
                    "pledge_id": {"type": "string", "description": "Pledge ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["pledge_id"],
            },
        ),
        Tool(
            name="get_pledge_campaigns",
            description="Get pledge campaigns from Planning Center Giving",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of pledge campaigns per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_pledge_campaign",
            description="Get a specific pledge campaign from Planning Center Giving",
            inputSchema={
                "type": "object",
                "properties": {
                    "pledge_campaign_id": {"type": "string", "description": "Pledge campaign ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["pledge_campaign_id"],
            },
        ),
        Tool(
            name="get_recurring_donations",
            description="Get recurring donations from Planning Center Giving",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of recurring donations per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                    "person_id": {"type": "string", "description": "Filter by person ID"},
                    "status": {"type": "string", "description": "Filter by status"},
                },
            },
        ),
        Tool(
            name="get_recurring_donation",
            description="Get a specific recurring donation from Planning Center Giving",
            inputSchema={
                "type": "object",
                "properties": {
                    "recurring_donation_id": {"type": "string", "description": "Recurring donation ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["recurring_donation_id"],
            },
        ),
        # Groups API endpoints
        Tool(
            name="get_groups",
            description="Get groups from Planning Center Groups",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of groups per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                    "group_type_id": {"type": "string", "description": "Filter by group type ID"},
                    "campus_id": {"type": "string", "description": "Filter by campus ID"},
                },
            },
        ),
        Tool(
            name="get_group",
            description="Get a specific group from Planning Center Groups",
            inputSchema={
                "type": "object",
                "properties": {
                    "group_id": {"type": "string", "description": "Group ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["group_id"],
            },
        ),
        Tool(
            name="get_group_events",
            description="Get events for a specific group",
            inputSchema={
                "type": "object",
                "properties": {
                    "group_id": {"type": "string", "description": "Group ID"},
                    "per_page": {"type": "integer", "description": "Number of events per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["group_id"],
            },
        ),
        Tool(
            name="get_group_event",
            description="Get a specific group event",
            inputSchema={
                "type": "object",
                "properties": {
                    "group_id": {"type": "string", "description": "Group ID"},
                    "event_id": {"type": "string", "description": "Event ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["group_id", "event_id"],
            },
        ),
        Tool(
            name="get_group_memberships",
            description="Get memberships for a specific group",
            inputSchema={
                "type": "object",
                "properties": {
                    "group_id": {"type": "string", "description": "Group ID"},
                    "per_page": {"type": "integer", "description": "Number of memberships per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                    "role": {"type": "string", "description": "Filter by role (member, leader)"},
                },
                "required": ["group_id"],
            },
        ),
        Tool(
            name="get_group_membership",
            description="Get a specific group membership",
            inputSchema={
                "type": "object",
                "properties": {
                    "group_id": {"type": "string", "description": "Group ID"},
                    "membership_id": {"type": "string", "description": "Membership ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["group_id", "membership_id"],
            },
        ),
        Tool(
            name="get_group_types",
            description="Get group types from Planning Center Groups",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of group types per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_group_type",
            description="Get a specific group type from Planning Center Groups",
            inputSchema={
                "type": "object",
                "properties": {
                    "group_type_id": {"type": "string", "description": "Group type ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["group_type_id"],
            },
        ),
        # Calendar API endpoints
        Tool(
            name="get_calendar_events",
            description="Get events from Planning Center Calendar",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of events per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                    "start_date": {"type": "string", "description": "Filter events starting from this date"},
                    "end_date": {"type": "string", "description": "Filter events ending before this date"},
                    "approval_status": {"type": "string", "description": "Filter by approval status"},
                },
            },
        ),
        Tool(
            name="get_calendar_event",
            description="Get a specific event from Planning Center Calendar",
            inputSchema={
                "type": "object",
                "properties": {
                    "event_id": {"type": "string", "description": "Event ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["event_id"],
            },
        ),
        # Check-ins API endpoints
        Tool(
            name="get_check_in_events",
            description="Get events from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of events per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_check_in_event",
            description="Get a specific event from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "event_id": {"type": "string", "description": "Event ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["event_id"],
            },
        ),
        Tool(
            name="get_locations",
            description="Get locations from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of locations per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_location",
            description="Get a specific location from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "location_id": {"type": "string", "description": "Location ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["location_id"],
            },
        ),
        # Webhooks API endpoints
        Tool(
            name="get_webhook_subscriptions",
            description="Get webhook subscriptions from Planning Center",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of webhook subscriptions per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                    "active": {"type": "boolean", "description": "Filter by active status"},
                },
            },
        ),
        Tool(
            name="get_webhook_subscription",
            description="Get a specific webhook subscription from Planning Center",
            inputSchema={
                "type": "object",
                "properties": {
                    "webhook_subscription_id": {"type": "string", "description": "Webhook subscription ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["webhook_subscription_id"],
            },
        ),
        # Publishing API endpoints
        Tool(
            name="get_channels",
            description="Get channels from Planning Center Publishing",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of channels per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_channel",
            description="Get a specific channel from Planning Center Publishing",
            inputSchema={
                "type": "object",
                "properties": {
                    "channel_id": {"type": "string", "description": "Channel ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["channel_id"],
            },
        ),
        Tool(
            name="get_episodes",
            description="Get episodes from Planning Center Publishing",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of episodes per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                    "channel_id": {"type": "string", "description": "Filter by channel ID"},
                },
            },
        ),
        Tool(
            name="get_episode",
            description="Get a specific episode from Planning Center Publishing",
            inputSchema={
                "type": "object",
                "properties": {
                    "episode_id": {"type": "string", "description": "Episode ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["episode_id"],
            },
        ),
        # Organization API endpoints
        Tool(
            name="get_connected_applications",
            description="Get connected applications from Planning Center",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of connected applications per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_connected_application",
            description="Get a specific connected application from Planning Center",
            inputSchema={
                "type": "object",
                "properties": {
                    "connected_application_id": {"type": "string", "description": "Connected application ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["connected_application_id"],
            },
        ),
        Tool(
            name="get_oauth_applications",
            description="Get OAuth applications from Planning Center",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of OAuth applications per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_oauth_application",
            description="Get a specific OAuth application from Planning Center",
            inputSchema={
                "type": "object",
                "properties": {
                    "oauth_application_id": {"type": "string", "description": "OAuth application ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["oauth_application_id"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Handle tool calls."""
    logger.info(f"Calling tool: {name} with arguments: {arguments}")

    try:
        pco_client = get_pco_client()

        if name == "get_people":
            async with pco_client:
                result = await pco_client.get_people(
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params={
                        k: v
                        for k, v in arguments.items()
                        if k in ["search", "status", "email", "phone"] and v is not None
                    }
                    or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_person":
            async with pco_client:
                result = await pco_client.get_person(
                    person_id=arguments["person_id"], include=arguments.get("include")
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_services":
            async with pco_client:
                result = await pco_client.get_services(
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_service":
            async with pco_client:
                result = await pco_client.get_service(
                    service_id=arguments["service_id"], include=arguments.get("include")
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_plans":
            async with pco_client:
                result = await pco_client.get_plans(
                    service_id=arguments.get("service_id"),
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_plan":
            async with pco_client:
                result = await pco_client.get_plan(
                    plan_id=arguments["plan_id"], include=arguments.get("include")
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_registrations":
            async with pco_client:
                result = await pco_client.get_registrations(
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params={
                        k: v
                        for k, v in arguments.items()
                        if k in ["status"] and v is not None
                    }
                    or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_registration":
            async with pco_client:
                result = await pco_client.get_registration(
                    registration_id=arguments["registration_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_attendees":
            async with pco_client:
                result = await pco_client.get_attendees(
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params={
                        k: v
                        for k, v in arguments.items()
                        if k
                        in ["event_id", "registration_instance_id", "attendance_status"]
                        and v is not None
                    }
                    or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_event_attendees":
            async with pco_client:
                # This is a convenience tool that calls get_attendees with the appropriate filters
                filter_params = {}
                if arguments.get("event_id"):
                    filter_params["event_id"] = arguments["event_id"]
                if arguments.get("registration_instance_id"):
                    filter_params["registration_instance_id"] = arguments["registration_instance_id"]
                if arguments.get("attendance_status"):
                    filter_params["attendance_status"] = arguments["attendance_status"]
                
                result = await pco_client.get_attendees(
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params=filter_params or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_attendee":
            async with pco_client:
                result = await pco_client.get_attendee(
                    attendee_id=arguments["attendee_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        # People API - Additional endpoints
        elif name == "get_person_addresses":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.PEOPLE,
                    "addresses",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params={"person_id": arguments["person_id"]} if arguments.get("person_id") else None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_person_emails":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.PEOPLE,
                    "emails",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params={"person_id": arguments["person_id"]} if arguments.get("person_id") else None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_person_phones":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.PEOPLE,
                    "phone_numbers",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params={"person_id": arguments["person_id"]} if arguments.get("person_id") else None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_person_background_checks":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.PEOPLE,
                    "background_checks",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params={"person_id": arguments["person_id"]} if arguments.get("person_id") else None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_field_definitions":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.PEOPLE,
                    "field_definitions",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_forms":
            async with pco_client:
                filter_params = {}
                if arguments.get("active") is not None:
                    filter_params["active"] = arguments["active"]
                result = await pco_client.get(
                    PCOProduct.PEOPLE,
                    "forms",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params=filter_params or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_form":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.PEOPLE,
                    "forms",
                    resource_id=arguments["form_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_campuses":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.PEOPLE,
                    "campuses",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_campus":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.PEOPLE,
                    "campuses",
                    resource_id=arguments["campus_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        # Services API - Additional endpoints
        elif name == "get_songs":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.SERVICES,
                    "songs",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_song":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.SERVICES,
                    "songs",
                    resource_id=arguments["song_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_arrangements":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.SERVICES,
                    "arrangements",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params={"song_id": arguments["song_id"]},
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_arrangement":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.SERVICES,
                    "arrangements",
                    resource_id=arguments["arrangement_id"],
                    include=arguments.get("include"),
                    filter_params={"song_id": arguments["song_id"]},
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_keys":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.SERVICES,
                    "keys",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_key":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.SERVICES,
                    "keys",
                    resource_id=arguments["key_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_teams":
            async with pco_client:
                filter_params = {}
                if arguments.get("service_type_id"):
                    filter_params["service_type_id"] = arguments["service_type_id"]
                result = await pco_client.get(
                    PCOProduct.SERVICES,
                    "teams",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params=filter_params or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_team":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.SERVICES,
                    "teams",
                    resource_id=arguments["team_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_team_positions":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.SERVICES,
                    "team_positions",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params={"team_id": arguments["team_id"]},
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_team_position":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.SERVICES,
                    "team_positions",
                    resource_id=arguments["team_position_id"],
                    include=arguments.get("include"),
                    filter_params={"team_id": arguments["team_id"]},
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        # Giving API endpoints
        elif name == "get_donations":
            async with pco_client:
                filter_params = {}
                for key in ["person_id", "fund_id", "payment_method", "payment_status"]:
                    if arguments.get(key):
                        filter_params[key] = arguments[key]
                result = await pco_client.get(
                    PCOProduct.GIVING,
                    "donations",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params=filter_params or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_donation":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.GIVING,
                    "donations",
                    resource_id=arguments["donation_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_funds":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.GIVING,
                    "funds",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_fund":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.GIVING,
                    "funds",
                    resource_id=arguments["fund_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_batches":
            async with pco_client:
                filter_params = {}
                if arguments.get("status"):
                    filter_params["status"] = arguments["status"]
                result = await pco_client.get(
                    PCOProduct.GIVING,
                    "batches",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params=filter_params or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_batch":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.GIVING,
                    "batches",
                    resource_id=arguments["batch_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_pledges":
            async with pco_client:
                filter_params = {}
                for key in ["person_id", "pledge_campaign_id"]:
                    if arguments.get(key):
                        filter_params[key] = arguments[key]
                result = await pco_client.get(
                    PCOProduct.GIVING,
                    "pledges",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params=filter_params or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_pledge":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.GIVING,
                    "pledges",
                    resource_id=arguments["pledge_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_pledge_campaigns":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.GIVING,
                    "pledge_campaigns",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_pledge_campaign":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.GIVING,
                    "pledge_campaigns",
                    resource_id=arguments["pledge_campaign_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_recurring_donations":
            async with pco_client:
                filter_params = {}
                for key in ["person_id", "status"]:
                    if arguments.get(key):
                        filter_params[key] = arguments[key]
                result = await pco_client.get(
                    PCOProduct.GIVING,
                    "recurring_donations",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params=filter_params or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_recurring_donation":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.GIVING,
                    "recurring_donations",
                    resource_id=arguments["recurring_donation_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        # Groups API endpoints
        elif name == "get_groups":
            async with pco_client:
                filter_params = {}
                for key in ["group_type_id", "campus_id"]:
                    if arguments.get(key):
                        filter_params[key] = arguments[key]
                result = await pco_client.get(
                    PCOProduct.GROUPS,
                    "groups",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params=filter_params or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_group":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.GROUPS,
                    "groups",
                    resource_id=arguments["group_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_group_events":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.GROUPS,
                    "events",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params={"group_id": arguments["group_id"]},
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_group_event":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.GROUPS,
                    "events",
                    resource_id=arguments["event_id"],
                    include=arguments.get("include"),
                    filter_params={"group_id": arguments["group_id"]},
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_group_memberships":
            async with pco_client:
                filter_params = {"group_id": arguments["group_id"]}
                if arguments.get("role"):
                    filter_params["role"] = arguments["role"]
                result = await pco_client.get(
                    PCOProduct.GROUPS,
                    "memberships",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params=filter_params,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_group_membership":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.GROUPS,
                    "memberships",
                    resource_id=arguments["membership_id"],
                    include=arguments.get("include"),
                    filter_params={"group_id": arguments["group_id"]},
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_group_types":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.GROUPS,
                    "group_types",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_group_type":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.GROUPS,
                    "group_types",
                    resource_id=arguments["group_type_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        # Calendar API endpoints
        elif name == "get_calendar_events":
            async with pco_client:
                filter_params = {}
                for key in ["start_date", "end_date", "approval_status"]:
                    if arguments.get(key):
                        filter_params[key] = arguments[key]
                result = await pco_client.get(
                    PCOProduct.CALENDAR,
                    "events",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params=filter_params or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_calendar_event":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CALENDAR,
                    "events",
                    resource_id=arguments["event_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        # Check-ins API endpoints
        elif name == "get_check_in_events":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "events",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_check_in_event":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "events",
                    resource_id=arguments["event_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_locations":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "locations",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_location":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "locations",
                    resource_id=arguments["location_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        # Webhooks API endpoints
        elif name == "get_webhook_subscriptions":
            async with pco_client:
                filter_params = {}
                if arguments.get("active") is not None:
                    filter_params["active"] = arguments["active"]
                result = await pco_client.get(
                    PCOProduct.WEBHOOKS,
                    "webhook_subscriptions",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params=filter_params or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_webhook_subscription":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.WEBHOOKS,
                    "webhook_subscriptions",
                    resource_id=arguments["webhook_subscription_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        # Publishing API endpoints
        elif name == "get_channels":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.PUBLISHING,
                    "channels",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_channel":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.PUBLISHING,
                    "channels",
                    resource_id=arguments["channel_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_episodes":
            async with pco_client:
                filter_params = {}
                if arguments.get("channel_id"):
                    filter_params["channel_id"] = arguments["channel_id"]
                result = await pco_client.get(
                    PCOProduct.PUBLISHING,
                    "episodes",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params=filter_params or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_episode":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.PUBLISHING,
                    "episodes",
                    resource_id=arguments["episode_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        # Organization API endpoints
        elif name == "get_connected_applications":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.ORGANIZATION,
                    "connected_applications",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_connected_application":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.ORGANIZATION,
                    "connected_applications",
                    resource_id=arguments["connected_application_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_oauth_applications":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.ORGANIZATION,
                    "oauth_applications",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_oauth_application":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.ORGANIZATION,
                    "oauth_applications",
                    resource_id=arguments["oauth_application_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]

    except Exception as e:
        logger.error(f"Error calling tool {name}: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


async def main():
    """Main entry point."""
    global config

    logger.info("Starting Planning Center MCP Server...")

    # Initialize configuration
    try:
        config = PCOConfig.from_env()
        # Test configuration
        config.get_auth_headers()
        logger.info("✓ Configuration loaded successfully")
    except ValueError as e:
        logger.error(f"✗ Configuration error: {e}")
        logger.error(
            "Please set PCO_ACCESS_TOKEN or both PCO_APP_ID and PCO_SECRET environment variables"
        )
        sys.exit(1)
    except Exception as e:
        logger.error(f"✗ Unexpected error during configuration: {e}")
        sys.exit(1)

    logger.info("Starting MCP server with stdio transport...")

    # Run the MCP server
    try:
        async with stdio_server() as (read_stream, write_stream):
            logger.info("MCP server transport established")
            await server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="planning-center-api",
                    server_version="0.1.0",
                    capabilities=server.get_capabilities(
                        notification_options=None,
                        experimental_capabilities=None,
                    ),
                ),
            )
    except Exception as e:
        logger.error(f"Error running MCP server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)
