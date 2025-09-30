#!/usr/bin/env python3
"""Fixed MCP server entry point for Planning Center API."""

import asyncio
import json
import logging
import sys
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from planning_center_api.config import PCOConfig, PCOProduct
from planning_center_api.client import PCOClient


# Simple notification options class
class NotificationOptions:
    def __init__(self):
        self.tools_changed = False


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
    global client, config
    if client is None:
        if config is None:
            raise ValueError("Configuration not initialized")
        # Create client with explicit parameters to ensure proper configuration
        client = PCOClient(
            app_id=config.app_id,
            secret=config.secret,
            access_token=config.access_token,
            webhook_secret=config.webhook_secret
        )
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
            name="get_songs_for_service",
            description="Get songs for a specific service or plan from Planning Center Services",
            inputSchema={
                "type": "object",
                "properties": {
                    "service_id": {"type": "string", "description": "Service ID to get songs for"},
                    "plan_id": {"type": "string", "description": "Plan ID to get songs for (alternative to service_id)"},
                    "per_page": {"type": "integer", "description": "Number of songs per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Number of songs to skip", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include (e.g., 'arrangements', 'attachments')"},
                },
                "anyOf": [
                    {"required": ["service_id"]},
                    {"required": ["plan_id"]}
                ],
            },
        ),
        Tool(
            name="get_song_analytics",
            description="Get analytics and information about songs in Planning Center Services",
            inputSchema={
                "type": "object",
                "properties": {
                    "search": {"type": "string", "description": "Search for songs by title or artist"},
                    "per_page": {"type": "integer", "description": "Number of songs per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Number of songs to skip", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include (e.g., 'arrangements', 'attachments')"},
                },
            },
        ),
        Tool(
            name="get_song_names",
            description="Get a simple list of song names and artists from Planning Center Services",
            inputSchema={
                "type": "object",
                "properties": {
                    "search": {"type": "string", "description": "Search for songs by title or artist"},
                    "per_page": {"type": "integer", "description": "Number of songs per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Number of songs to skip", "default": 0},
                    "format": {"type": "string", "enum": ["simple", "detailed"], "description": "Output format - simple (just names) or detailed (with metadata)", "default": "simple"},
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
        # Additional Check-ins API endpoints
        Tool(
            name="get_attendance_types",
            description="Get attendance types from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of attendance types per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_attendance_type",
            description="Get a specific attendance type from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "attendance_type_id": {"type": "string", "description": "Attendance type ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["attendance_type_id"],
            },
        ),
        Tool(
            name="get_check_ins",
            description="Get check-ins from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of check-ins per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                    "order": {"type": "string", "description": "Order by field (e.g., 'created_at', '-created_at')"},
                },
            },
        ),
        Tool(
            name="get_check_in",
            description="Get a specific check-in from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "check_in_id": {"type": "string", "description": "Check-in ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["check_in_id"],
            },
        ),
        Tool(
            name="get_check_in_groups",
            description="Get check-in groups from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of check-in groups per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_check_in_group",
            description="Get a specific check-in group from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "check_in_group_id": {"type": "string", "description": "Check-in group ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["check_in_group_id"],
            },
        ),
        Tool(
            name="get_check_in_times",
            description="Get check-in times from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "check_in_id": {"type": "string", "description": "Check-in ID"},
                    "per_page": {"type": "integer", "description": "Number of check-in times per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                },
                "required": ["check_in_id"],
            },
        ),
        Tool(
            name="get_check_in_time",
            description="Get a specific check-in time from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "check_in_id": {"type": "string", "description": "Check-in ID"},
                    "check_in_time_id": {"type": "string", "description": "Check-in time ID"},
                },
                "required": ["check_in_id", "check_in_time_id"],
            },
        ),
        Tool(
            name="get_event_periods",
            description="Get event periods from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "event_id": {"type": "string", "description": "Event ID"},
                    "per_page": {"type": "integer", "description": "Number of event periods per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                    "order": {"type": "string", "description": "Order by field (e.g., 'starts_at', '-starts_at')"},
                },
                "required": ["event_id"],
            },
        ),
        Tool(
            name="get_event_period",
            description="Get a specific event period from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "event_period_id": {"type": "string", "description": "Event period ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["event_period_id"],
            },
        ),
        Tool(
            name="get_event_times",
            description="Get event times from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of event times per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                    "order": {"type": "string", "description": "Order by field (e.g., 'starts_at', '-starts_at')"},
                },
            },
        ),
        Tool(
            name="get_event_time",
            description="Get a specific event time from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "event_time_id": {"type": "string", "description": "Event time ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["event_time_id"],
            },
        ),
        Tool(
            name="get_headcounts",
            description="Get headcounts from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of headcounts per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                    "order": {"type": "string", "description": "Order by field (e.g., 'total', '-total')"},
                },
            },
        ),
        Tool(
            name="get_headcount",
            description="Get a specific headcount from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "headcount_id": {"type": "string", "description": "Headcount ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["headcount_id"],
            },
        ),
        Tool(
            name="get_integration_links",
            description="Get integration links from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of integration links per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "remote_gid": {"type": "string", "description": "Filter by remote global ID"},
                },
            },
        ),
        Tool(
            name="get_integration_link",
            description="Get a specific integration link from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "integration_link_id": {"type": "string", "description": "Integration link ID"},
                },
                "required": ["integration_link_id"],
            },
        ),
        Tool(
            name="get_labels",
            description="Get labels from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of labels per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                },
            },
        ),
        Tool(
            name="get_label",
            description="Get a specific label from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "label_id": {"type": "string", "description": "Label ID"},
                },
                "required": ["label_id"],
            },
        ),
        Tool(
            name="get_options",
            description="Get options from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of options per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_option",
            description="Get a specific option from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "option_id": {"type": "string", "description": "Option ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["option_id"],
            },
        ),
        Tool(
            name="get_check_ins_organization",
            description="Get organization from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {},
            },
        ),
        Tool(
            name="get_passes",
            description="Get passes from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of passes per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                    "code": {"type": "string", "description": "Filter by pass code"},
                },
            },
        ),
        Tool(
            name="get_pass",
            description="Get a specific pass from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "pass_id": {"type": "string", "description": "Pass ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["pass_id"],
            },
        ),
        Tool(
            name="get_check_ins_people",
            description="Get people from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of people per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                    "order": {"type": "string", "description": "Order by field (e.g., 'first_name', '-first_name')"},
                    "headcounter": {"type": "boolean", "description": "Filter by headcounter status"},
                    "ignore_filters": {"type": "boolean", "description": "Filter by ignore filters status"},
                    "permission": {"type": "string", "description": "Filter by permission"},
                    "search_name": {"type": "string", "description": "Search by person name"},
                },
            },
        ),
        Tool(
            name="get_check_ins_person",
            description="Get a specific person from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "person_id": {"type": "string", "description": "Person ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["person_id"],
            },
        ),
        Tool(
            name="get_person_events",
            description="Get person events from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "event_id": {"type": "string", "description": "Event ID"},
                    "per_page": {"type": "integer", "description": "Number of person events per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["event_id"],
            },
        ),
        Tool(
            name="get_person_event",
            description="Get a specific person event from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "event_id": {"type": "string", "description": "Event ID"},
                    "person_event_id": {"type": "string", "description": "Person event ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["event_id", "person_event_id"],
            },
        ),
        Tool(
            name="get_stations",
            description="Get stations from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of stations per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
            },
        ),
        Tool(
            name="get_station",
            description="Get a specific station from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "station_id": {"type": "string", "description": "Station ID"},
                    "include": {"type": "array", "items": {"type": "string"}, "description": "Related resources to include"},
                },
                "required": ["station_id"],
            },
        ),
        Tool(
            name="get_themes",
            description="Get themes from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {"type": "integer", "description": "Number of themes per page (max 100)", "default": 25},
                    "offset": {"type": "integer", "description": "Offset for pagination", "default": 0},
                },
            },
        ),
        Tool(
            name="get_theme",
            description="Get a specific theme from Planning Center Check-ins",
            inputSchema={
                "type": "object",
                "properties": {
                    "theme_id": {"type": "string", "description": "Theme ID"},
                },
                "required": ["theme_id"],
            },
        ),
        # Check-ins Analytics and Workflow Tools
        Tool(
            name="get_volunteer_count_for_date",
            description="Get the count of volunteers (people with headcounter permission) for a specific date or date range",
            inputSchema={
                "type": "object",
                "properties": {
                    "date": {"type": "string", "description": "Specific date in YYYY-MM-DD format"},
                    "start_date": {"type": "string", "description": "Start date for range in YYYY-MM-DD format"},
                    "end_date": {"type": "string", "description": "End date for range in YYYY-MM-DD format"},
                    "include_details": {"type": "boolean", "description": "Include detailed volunteer information", "default": False},
                },
            },
        ),
        Tool(
            name="get_attendance_summary_for_event",
            description="Get comprehensive attendance summary for a specific event including headcounts, check-ins, and volunteer counts",
            inputSchema={
                "type": "object",
                "properties": {
                    "event_id": {"type": "string", "description": "Event ID"},
                    "include_breakdown": {"type": "boolean", "description": "Include breakdown by location, station, etc.", "default": True},
                },
                "required": ["event_id"],
            },
        ),
        Tool(
            name="get_weekly_attendance_trends",
            description="Get attendance trends for a specific week or date range, useful for Sunday service analysis",
            inputSchema={
                "type": "object",
                "properties": {
                    "start_date": {"type": "string", "description": "Start date in YYYY-MM-DD format"},
                    "end_date": {"type": "string", "description": "End date in YYYY-MM-DD format"},
                    "group_by": {"type": "string", "enum": ["day", "week", "event"], "description": "Group results by day, week, or event", "default": "day"},
                    "include_volunteers": {"type": "boolean", "description": "Include volunteer counts in trends", "default": True},
                },
                "required": ["start_date", "end_date"],
            },
        ),
        Tool(
            name="get_station_utilization_report",
            description="Get utilization report for check-in stations showing usage patterns and efficiency",
            inputSchema={
                "type": "object",
                "properties": {
                    "start_date": {"type": "string", "description": "Start date in YYYY-MM-DD format"},
                    "end_date": {"type": "string", "description": "End date in YYYY-MM-DD format"},
                    "station_id": {"type": "string", "description": "Specific station ID (optional, if not provided returns all stations)"},
                    "include_peak_times": {"type": "boolean", "description": "Include peak usage times", "default": True},
                },
                "required": ["start_date", "end_date"],
            },
        ),
        Tool(
            name="get_family_check_in_patterns",
            description="Analyze family check-in patterns including household sizes, repeat attendance, and family dynamics",
            inputSchema={
                "type": "object",
                "properties": {
                    "start_date": {"type": "string", "description": "Start date in YYYY-MM-DD format"},
                    "end_date": {"type": "string", "description": "End date in YYYY-MM-DD format"},
                    "min_family_size": {"type": "integer", "description": "Minimum family size to include", "default": 2},
                    "include_attendance_frequency": {"type": "boolean", "description": "Include how often families attend", "default": True},
                },
                "required": ["start_date", "end_date"],
            },
        ),
        Tool(
            name="get_volunteer_availability_report",
            description="Get report on volunteer availability and scheduling patterns",
            inputSchema={
                "type": "object",
                "properties": {
                    "start_date": {"type": "string", "description": "Start date in YYYY-MM-DD format"},
                    "end_date": {"type": "string", "description": "End date in YYYY-MM-DD format"},
                    "volunteer_type": {"type": "string", "description": "Filter by volunteer type (headcounter, etc.)"},
                    "include_contact_info": {"type": "boolean", "description": "Include volunteer contact information", "default": False},
                },
                "required": ["start_date", "end_date"],
            },
        ),
        Tool(
            name="get_attendance_by_demographics",
            description="Get attendance breakdown by age groups, family status, and other demographic factors",
            inputSchema={
                "type": "object",
                "properties": {
                    "start_date": {"type": "string", "description": "Start date in YYYY-MM-DD format"},
                    "end_date": {"type": "string", "description": "End date in YYYY-MM-DD format"},
                    "group_by": {"type": "string", "enum": ["age", "family_status", "location"], "description": "Group by age, family status, or location", "default": "age"},
                    "include_percentages": {"type": "boolean", "description": "Include percentage breakdowns", "default": True},
                },
                "required": ["start_date", "end_date"],
            },
        ),
        Tool(
            name="get_event_capacity_analysis",
            description="Analyze event capacity utilization and identify potential overcrowding or underutilization",
            inputSchema={
                "type": "object",
                "properties": {
                    "event_id": {"type": "string", "description": "Event ID"},
                    "include_recommendations": {"type": "boolean", "description": "Include capacity recommendations", "default": True},
                    "compare_to_historical": {"type": "boolean", "description": "Compare to historical averages", "default": True},
                },
                "required": ["event_id"],
            },
        ),
        Tool(
            name="get_check_in_efficiency_metrics",
            description="Get metrics on check-in efficiency including average wait times, processing speed, and bottlenecks",
            inputSchema={
                "type": "object",
                "properties": {
                    "start_date": {"type": "string", "description": "Start date in YYYY-MM-DD format"},
                    "end_date": {"type": "string", "description": "End date in YYYY-MM-DD format"},
                    "location_id": {"type": "string", "description": "Filter by specific location"},
                    "include_peak_analysis": {"type": "boolean", "description": "Include peak time analysis", "default": True},
                },
                "required": ["start_date", "end_date"],
            },
        ),
        Tool(
            name="get_volunteer_roster_for_date",
            description="Get a complete volunteer roster for a specific date with contact information and roles",
            inputSchema={
                "type": "object",
                "properties": {
                    "date": {"type": "string", "description": "Date in YYYY-MM-DD format"},
                    "include_contact_info": {"type": "boolean", "description": "Include phone numbers and email addresses", "default": True},
                    "include_emergency_contacts": {"type": "boolean", "description": "Include emergency contact information", "default": False},
                    "format": {"type": "string", "enum": ["list", "detailed", "contact_sheet"], "description": "Output format", "default": "detailed"},
                },
                "required": ["date"],
            },
        ),
        Tool(
            name="get_attendance_anomalies",
            description="Identify unusual attendance patterns, spikes, or drops that might need attention",
            inputSchema={
                "type": "object",
                "properties": {
                    "start_date": {"type": "string", "description": "Start date in YYYY-MM-DD format"},
                    "end_date": {"type": "string", "description": "End date in YYYY-MM-DD format"},
                    "sensitivity": {"type": "string", "enum": ["low", "medium", "high"], "description": "Sensitivity level for anomaly detection", "default": "medium"},
                    "include_explanations": {"type": "boolean", "description": "Include possible explanations for anomalies", "default": True},
                },
                "required": ["start_date", "end_date"],
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


async def make_direct_api_call(endpoint: str, params: dict = None, follow_redirects: bool = True, return_html_on_redirect: bool = False) -> dict:
    """Make a direct HTTP API call to bypass Pydantic validation issues."""
    import httpx
    import base64
    
    app_id = config.app_id
    secret = config.secret
    credentials = f'{app_id}:{secret}'
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    auth_header = f'Basic {encoded_credentials}'
    
    async with httpx.AsyncClient(follow_redirects=follow_redirects) as http_client:
        url = f"https://api.planningcenteronline.com{endpoint}"
        headers = {
            'Authorization': auth_header,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        
        response = await http_client.get(url, headers=headers, params=params or {})
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 302 and return_html_on_redirect:
            # Handle redirect and get HTML content
            redirect_url = response.headers.get('location')
            if redirect_url:
                # Try to get the redirected content
                try:
                    redirect_response = await http_client.get(redirect_url, headers=headers)
                    if redirect_response.status_code == 200:
                        # Try to parse as JSON first
                        try:
                            return redirect_response.json()
                        except:
                            # If not JSON, return HTML content as structured data
                            return {
                                'data': [],
                                'meta': {
                                    'redirect_url': redirect_url,
                                    'content_type': 'html',
                                    'html_content': redirect_response.text[:1000] + '...' if len(redirect_response.text) > 1000 else redirect_response.text
                                }
                            }
                    else:
                        return {
                            'data': [],
                            'meta': {
                                'redirect_url': redirect_url,
                                'error': f'Redirect failed with status {redirect_response.status_code}'
                            }
                        }
                except Exception as e:
                    return {
                        'data': [],
                        'meta': {
                            'redirect_url': redirect_url,
                            'error': f'Failed to follow redirect: {str(e)}'
                        }
                    }
            else:
                return {
                    'data': [],
                    'meta': {
                        'error': '302 redirect but no location header found'
                    }
                }
        else:
            raise Exception(f"HTTP {response.status_code} - {response.text}")

@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Handle tool calls."""
    logger.info(f"Calling tool: {name} with arguments: {arguments}")

    try:
        # Ensure config is loaded
        global config, client
        if config is None:
            load_dotenv()
            config = PCOConfig.from_env()
            # Reset client when config is reloaded
            client = None
        
        pco_client = get_pco_client()

        if name == "get_people":
            try:
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
            except Exception as e:
                if "validation errors" in str(e):
                    # Fallback to direct API call
                    params = {
                        'per_page': arguments.get("per_page", 25),
                        'offset': arguments.get("offset", 0),
                    }
                    if arguments.get("search"):
                        params['where[search]'] = arguments["search"]
                    if arguments.get("status"):
                        params['where[status]'] = arguments["status"]
                    if arguments.get("email"):
                        params['where[email]'] = arguments["email"]
                    if arguments.get("phone"):
                        params['where[phone]'] = arguments["phone"]
                    
                    data = await make_direct_api_call("/people/v2/people", params)
                    return [TextContent(type="text", text=json.dumps(data, indent=2))]
                else:
                    raise e

        elif name == "get_person":
            async with pco_client:
                result = await pco_client.get_person(
                    person_id=arguments["person_id"], include=arguments.get("include")
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_services":
            # Use direct API call since services endpoint might not be available
            params = {
                'per_page': arguments.get("per_page", 25),
                'offset': arguments.get("offset", 0),
            }
            if arguments.get("include"):
                params['include'] = ','.join(arguments["include"]) if isinstance(arguments["include"], list) else arguments["include"]
            
            # Try different possible endpoints for services
            try:
                data = await make_direct_api_call("/services/v2/services", params)
                return [TextContent(type="text", text=json.dumps(data, indent=2))]
            except Exception as e:
                if "404" in str(e):
                    # Try alternative endpoint structure
                    try:
                        data = await make_direct_api_call("/services/v2/service_types", params)
                        return [TextContent(type="text", text=json.dumps(data, indent=2))]
                    except Exception as e2:
                        return [TextContent(type="text", text=f"Error: Services endpoint not available. Tried /services/v2/services and /services/v2/service_types. Error: {str(e2)}")]
                else:
                    raise e

        elif name == "get_service":
            async with pco_client:
                result = await pco_client.get_service(
                    service_id=arguments["service_id"], include=arguments.get("include")
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_plans":
            # Use direct API call since the plans endpoint structure might be different
            params = {
                'per_page': arguments.get("per_page", 25),
                'offset': arguments.get("offset", 0),
            }
            if arguments.get("service_id"):
                params['where[service_id]'] = arguments["service_id"]
            if arguments.get("include"):
                params['include'] = ','.join(arguments["include"]) if isinstance(arguments["include"], list) else arguments["include"]
            
            data = await make_direct_api_call("/services/v2/plans", params)
            return [TextContent(type="text", text=json.dumps(data, indent=2))]

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
            # Use direct API call since attendees endpoint might not be available
            params = {
                'per_page': arguments.get("per_page", 25),
                'offset': arguments.get("offset", 0),
            }
            if arguments.get("event_id"):
                params['where[event_id]'] = arguments["event_id"]
            if arguments.get("registration_instance_id"):
                params['where[registration_instance_id]'] = arguments["registration_instance_id"]
            if arguments.get("attendance_status"):
                params['where[attendance_status]'] = arguments["attendance_status"]
            
            data = await make_direct_api_call("/registrations/v2/attendee", params)
            return [TextContent(type="text", text=json.dumps(data, indent=2))]

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
            # Use direct API call since forms is not in the available resources
            params = {
                'per_page': arguments.get("per_page", 25),
                'offset': arguments.get("offset", 0),
            }
            if arguments.get("active") is not None:
                params['where[active]'] = str(arguments["active"]).lower()
            
            data = await make_direct_api_call("/people/v2/forms", params)
            return [TextContent(type="text", text=json.dumps(data, indent=2))]

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
            try:
                async with pco_client:
                    result = await pco_client.get(
                        PCOProduct.SERVICES,
                        "songs",
                        per_page=arguments.get("per_page", 25),
                        offset=arguments.get("offset", 0),
                        include=arguments.get("include"),
                    )
                    return [TextContent(type="text", text=result.model_dump_json(indent=2))]
            except Exception as e:
                if "validation errors" in str(e):
                    # Fallback to direct API call
                    params = {
                        'per_page': arguments.get("per_page", 25),
                        'offset': arguments.get("offset", 0),
                    }
                    if arguments.get("include"):
                        params['include'] = ','.join(arguments["include"]) if isinstance(arguments["include"], list) else arguments["include"]
                    
                    data = await make_direct_api_call("/services/v2/songs", params)
                    return [TextContent(type="text", text=json.dumps(data, indent=2))]
                else:
                    raise e

        elif name == "get_songs_for_service":
            # Get songs for a specific service or plan
            service_id = arguments.get("service_id")
            plan_id = arguments.get("plan_id")
            
            if not service_id and not plan_id:
                return [TextContent(type="text", text="Error: Either service_id or plan_id must be provided")]
            
            try:
                # First, try to get plan items if we have a plan_id
                if plan_id:
                    params = {
                        'per_page': arguments.get("per_page", 25),
                        'offset': arguments.get("offset", 0),
                    }
                    if arguments.get("include"):
                        params['include'] = ','.join(arguments["include"]) if isinstance(arguments["include"], list) else arguments["include"]
                    
                    # Get plan items (which include songs)
                    data = await make_direct_api_call(f"/services/v2/plans/{plan_id}/items", params, follow_redirects=False, return_html_on_redirect=True)
                    return [TextContent(type="text", text=json.dumps(data, indent=2))]
                
                # If we have service_id, try different approaches to get songs
                elif service_id:
                    # Approach 1: Try to get plans for the service
                    try:
                        plans_data = await make_direct_api_call(f"/services/v2/service_types/{service_id}/plans", {
                            'per_page': 10,
                            'offset': 0,
                        })
                        
                        if plans_data and plans_data.get('data'):
                            # Found plans, now get songs from the first few plans
                            all_songs = []
                            for plan in plans_data.get('data', [])[:3]:  # Limit to first 3 plans
                                plan_id = plan.get('id')
                                if plan_id:
                                    try:
                                        items_data = await make_direct_api_call(f"/services/v2/plans/{plan_id}/items", {
                                            'per_page': 50,
                                            'offset': 0,
                                        }, follow_redirects=False, return_html_on_redirect=True)
                                        
                                        # Check if we got redirected content
                                        if items_data.get('meta', {}).get('content_type') == 'html':
                                            # We got HTML content from redirect, try to extract useful info
                                            html_content = items_data.get('meta', {}).get('html_content', '')
                                            if 'song' in html_content.lower() or 'item' in html_content.lower():
                                                # Create a mock item to indicate we found content
                                                all_songs.append({
                                                    'type': 'Item',
                                                    'id': f'redirected_{plan_id}',
                                                    'attributes': {
                                                        'title': f'Plan {plan_id} Items (Redirected)',
                                                        'item_type': 'song',
                                                        'redirect_info': items_data.get('meta', {}).get('redirect_url', '')
                                                    }
                                                })
                                        else:
                                            # Filter for song items from JSON response
                                            for item in items_data.get('data', []):
                                                if item.get('type') == 'Item' and item.get('attributes', {}).get('item_type') == 'song':
                                                    all_songs.append(item)
                                    except Exception:
                                        continue
                            
                            if all_songs:
                                # Apply pagination
                                offset = arguments.get("offset", 0)
                                per_page = arguments.get("per_page", 25)
                                paginated_songs = all_songs[offset:offset + per_page]
                                
                                result = {
                                    'data': paginated_songs,
                                    'meta': {
                                        'total_count': len(all_songs),
                                        'count': len(paginated_songs),
                                        'can_order_by': [],
                                        'can_query_by': [],
                                        'can_include': ['arrangements', 'attachments'],
                                        'parent': {
                                            'id': service_id,
                                            'type': 'ServiceType'
                                        }
                                    }
                                }
                                return [TextContent(type="text", text=json.dumps(result, indent=2))]
                            else:
                                return [TextContent(type="text", text=f"Found {len(plans_data.get('data', []))} plans for service {service_id}, but no songs found in the first few plans")]
                        else:
                            return [TextContent(type="text", text=f"No plans found for service {service_id}")]
                            
                    except Exception as e:
                        # Approach 2: Try to get songs directly with service filter
                        try:
                            songs_data = await make_direct_api_call("/services/v2/songs", {
                                'per_page': arguments.get("per_page", 25),
                                'offset': arguments.get("offset", 0),
                                'where[service_type_id]': service_id,
                            })
                            return [TextContent(type="text", text=json.dumps(songs_data, indent=2))]
                        except Exception as e2:
                            return [TextContent(type="text", text=f"Could not get songs for service {service_id}. Tried plans approach (error: {str(e)}) and direct songs approach (error: {str(e2)})")]
                    
            except Exception as e:
                return [TextContent(type="text", text=f"Error getting songs for service: {str(e)}")]

        elif name == "get_song_analytics":
            # Get analytics and information about songs
            try:
                params = {
                    'per_page': arguments.get("per_page", 25),
                    'offset': arguments.get("offset", 0),
                }
                if arguments.get("search"):
                    params['where[search]'] = arguments["search"]
                if arguments.get("include"):
                    params['include'] = ','.join(arguments["include"]) if isinstance(arguments["include"], list) else arguments["include"]
                
                # Get songs data
                songs_data = await make_direct_api_call("/services/v2/songs", params)
                
                # Add analytics information
                if songs_data and songs_data.get('data'):
                    songs = songs_data['data']
                    
                    # Calculate analytics
                    total_songs = len(songs)
                    artists = {}
                    song_titles = []
                    
                    for song in songs:
                        attrs = song.get('attributes', {})
                        title = attrs.get('title', 'Unknown')
                        artist = attrs.get('author', 'Unknown')
                        
                        song_titles.append(title)
                        if artist in artists:
                            artists[artist] += 1
                        else:
                            artists[artist] = 1
                    
                    # Add analytics to the response
                    songs_data['analytics'] = {
                        'total_songs': total_songs,
                        'unique_artists': len(artists),
                        'top_artists': sorted(artists.items(), key=lambda x: x[1], reverse=True)[:5],
                        'recent_songs': song_titles[:10] if song_titles else []
                    }
                
                return [TextContent(type="text", text=json.dumps(songs_data, indent=2))]
                
            except Exception as e:
                return [TextContent(type="text", text=f"Error getting song analytics: {str(e)}")]

        elif name == "get_song_names":
            # Get a simple list of song names and artists
            try:
                params = {
                    'per_page': arguments.get("per_page", 25),
                    'offset': arguments.get("offset", 0),
                }
                if arguments.get("search"):
                    params['where[search]'] = arguments["search"]
                
                # Get songs data
                songs_data = await make_direct_api_call("/services/v2/songs", params)
                
                if songs_data and songs_data.get('data'):
                    songs = songs_data['data']
                    format_type = arguments.get("format", "simple")
                    
                    if format_type == "simple":
                        # Simple format - just names and artists
                        song_list = []
                        for song in songs:
                            attrs = song.get('attributes', {})
                            title = attrs.get('title', 'Unknown')
                            author = attrs.get('author', 'Unknown')
                            song_list.append(f'"{title}" by {author}')
                        
                        result = {
                            'songs': song_list,
                            'total_count': len(song_list),
                            'meta': {
                                'format': 'simple',
                                'total_available': songs_data.get('meta', {}).get('total_count', len(songs))
                            }
                        }
                    else:
                        # Detailed format - with metadata
                        detailed_songs = []
                        for song in songs:
                            attrs = song.get('attributes', {})
                            detailed_songs.append({
                                'id': song.get('id'),
                                'title': attrs.get('title', 'Unknown'),
                                'author': attrs.get('author', 'Unknown'),
                                'created_at': attrs.get('created_at'),
                                'updated_at': attrs.get('updated_at'),
                                'ccli_number': attrs.get('ccli_number'),
                                'themes': attrs.get('themes', []),
                                'last_scheduled': attrs.get('last_scheduled')
                            })
                        
                        result = {
                            'songs': detailed_songs,
                            'total_count': len(detailed_songs),
                            'meta': {
                                'format': 'detailed',
                                'total_available': songs_data.get('meta', {}).get('total_count', len(songs))
                            }
                        }
                    
                    return [TextContent(type="text", text=json.dumps(result, indent=2))]
                else:
                    return [TextContent(type="text", text=json.dumps({'songs': [], 'total_count': 0, 'message': 'No songs found'}, indent=2))]
                
            except Exception as e:
                return [TextContent(type="text", text=f"Error getting song names: {str(e)}")]

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
            try:
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
            except Exception as e:
                if "could not be authenticated" in str(e) or "401" in str(e) or "TRASH_PANDA" in str(e):
                    # Fallback to direct API call - Giving API might require different permissions
                    params = {
                        'per_page': arguments.get("per_page", 25),
                        'offset': arguments.get("offset", 0),
                    }
                    if arguments.get("person_id"):
                        params['where[person_id]'] = arguments["person_id"]
                    if arguments.get("fund_id"):
                        params['where[fund_id]'] = arguments["fund_id"]
                    if arguments.get("payment_method"):
                        params['where[payment_method]'] = arguments["payment_method"]
                    if arguments.get("payment_status"):
                        params['where[payment_status]'] = arguments["payment_status"]
                    
                    data = await make_direct_api_call("/giving/v2/donations", params)
                    return [TextContent(type="text", text=json.dumps(data, indent=2))]
                else:
                    raise e

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
            try:
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
            except Exception as e:
                if "validation errors" in str(e):
                    # Fallback to direct API call
                    params = {
                        'per_page': arguments.get("per_page", 25),
                        'offset': arguments.get("offset", 0),
                    }
                    if arguments.get("group_type_id"):
                        params['where[group_type_id]'] = arguments["group_type_id"]
                    if arguments.get("campus_id"):
                        params['where[campus_id]'] = arguments["campus_id"]
                    
                    data = await make_direct_api_call("/groups/v2/groups", params)
                    return [TextContent(type="text", text=json.dumps(data, indent=2))]
                else:
                    raise e

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
            try:
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
            except Exception as e:
                if "validation errors" in str(e):
                    # Fallback to direct API call
                    params = {
                        'per_page': arguments.get("per_page", 25),
                        'offset': arguments.get("offset", 0),
                    }
                    if arguments.get("start_date"):
                        params['where[start_date]'] = arguments["start_date"]
                    if arguments.get("end_date"):
                        params['where[end_date]'] = arguments["end_date"]
                    if arguments.get("approval_status"):
                        params['where[approval_status]'] = arguments["approval_status"]
                    
                    data = await make_direct_api_call("/calendar/v2/events", params)
                    return [TextContent(type="text", text=json.dumps(data, indent=2))]
                else:
                    raise e

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
            try:
                async with pco_client:
                    result = await pco_client.get(
                        PCOProduct.CHECK_INS,
                        "events",
                        per_page=arguments.get("per_page", 25),
                        offset=arguments.get("offset", 0),
                        include=arguments.get("include"),
                    )
                    return [TextContent(type="text", text=result.model_dump_json(indent=2))]
            except Exception as e:
                if "validation errors" in str(e):
                    # Fallback to direct API call
                    params = {
                        'per_page': arguments.get("per_page", 25),
                        'offset': arguments.get("offset", 0),
                    }
                    
                    data = await make_direct_api_call("/check_ins/v2/events", params)
                    return [TextContent(type="text", text=json.dumps(data, indent=2))]
                else:
                    raise e

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
            try:
                async with pco_client:
                    result = await pco_client.get(
                        PCOProduct.CHECK_INS,
                        "locations",
                        per_page=arguments.get("per_page", 25),
                        offset=arguments.get("offset", 0),
                        include=arguments.get("include"),
                    )
                    return [TextContent(type="text", text=result.model_dump_json(indent=2))]
            except Exception as e:
                if "validation errors" in str(e):
                    # Fallback to direct API call
                    params = {
                        'per_page': arguments.get("per_page", 25),
                        'offset': arguments.get("offset", 0),
                    }
                    
                    data = await make_direct_api_call("/check_ins/v2/locations", params)
                    return [TextContent(type="text", text=json.dumps(data, indent=2))]
                else:
                    raise e

        elif name == "get_location":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "locations",
                    resource_id=arguments["location_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        # Additional Check-ins API endpoints
        elif name == "get_attendance_types":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "attendance_types",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_attendance_type":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "attendance_types",
                    resource_id=arguments["attendance_type_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_check_ins":
            try:
                async with pco_client:
                    filter_params = {}
                    if arguments.get("order"):
                        filter_params["order"] = arguments["order"]
                    result = await pco_client.get(
                        PCOProduct.CHECK_INS,
                        "check_ins",
                        per_page=arguments.get("per_page", 25),
                        offset=arguments.get("offset", 0),
                        include=arguments.get("include"),
                        filter_params=filter_params or None,
                    )
                    return [TextContent(type="text", text=result.model_dump_json(indent=2))]
            except Exception as e:
                if "validation errors" in str(e):
                    # Fallback to direct API call
                    params = {
                        'per_page': arguments.get("per_page", 25),
                        'offset': arguments.get("offset", 0),
                    }
                    if arguments.get("order"):
                        params['where[order]'] = arguments["order"]
                    
                    data = await make_direct_api_call("/check_ins/v2/check_ins", params)
                    return [TextContent(type="text", text=json.dumps(data, indent=2))]
                else:
                    raise e

        elif name == "get_check_in":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "check_ins",
                    resource_id=arguments["check_in_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_check_in_groups":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "check_in_groups",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_check_in_group":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "check_in_groups",
                    resource_id=arguments["check_in_group_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_check_in_times":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "check_ins",
                    resource_id=arguments["check_in_id"],
                    sub_resource="check_in_times",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_check_in_time":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "check_ins",
                    resource_id=arguments["check_in_id"],
                    sub_resource="check_in_times",
                    sub_resource_id=arguments["check_in_time_id"],
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_event_periods":
            # Use direct API call since event_periods is not in the available resources
            event_id = arguments["event_id"]
            params = {
                'per_page': arguments.get("per_page", 25),
                'offset': arguments.get("offset", 0),
            }
            if arguments.get("order"):
                params['where[order]'] = arguments["order"]
            
            data = await make_direct_api_call(f"/check_ins/v2/events/{event_id}/event_periods", params)
            return [TextContent(type="text", text=json.dumps(data, indent=2))]

        elif name == "get_event_period":
            # Use direct API call since event_periods is not in the available resources
            event_period_id = arguments["event_period_id"]
            data = await make_direct_api_call(f"/check_ins/v2/event_periods/{event_period_id}")
            return [TextContent(type="text", text=json.dumps(data, indent=2))]

        elif name == "get_event_times":
            async with pco_client:
                filter_params = {}
                if arguments.get("order"):
                    filter_params["order"] = arguments["order"]
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "event_times",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params=filter_params or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_event_time":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "event_times",
                    resource_id=arguments["event_time_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_headcounts":
            # Use direct API call since headcounts is not in the available resources
            params = {
                'per_page': arguments.get("per_page", 25),
                'offset': arguments.get("offset", 0),
            }
            if arguments.get("order"):
                params['where[order]'] = arguments["order"]
            
            data = await make_direct_api_call("/check_ins/v2/headcounts", params)
            return [TextContent(type="text", text=json.dumps(data, indent=2))]

        elif name == "get_headcount":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "headcounts",
                    resource_id=arguments["headcount_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_integration_links":
            async with pco_client:
                filter_params = {}
                if arguments.get("remote_gid"):
                    filter_params["remote_gid"] = arguments["remote_gid"]
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "integration_links",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    filter_params=filter_params or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_integration_link":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "integration_links",
                    resource_id=arguments["integration_link_id"],
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_labels":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "labels",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_label":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "labels",
                    resource_id=arguments["label_id"],
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_options":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "options",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_option":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "options",
                    resource_id=arguments["option_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_check_ins_organization":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "",
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_passes":
            async with pco_client:
                filter_params = {}
                if arguments.get("code"):
                    filter_params["code"] = arguments["code"]
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "passes",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params=filter_params or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_pass":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "passes",
                    resource_id=arguments["pass_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_check_ins_people":
            async with pco_client:
                filter_params = {}
                if arguments.get("order"):
                    filter_params["order"] = arguments["order"]
                if arguments.get("headcounter") is not None:
                    filter_params["headcounter"] = arguments["headcounter"]
                if arguments.get("ignore_filters") is not None:
                    filter_params["ignore_filters"] = arguments["ignore_filters"]
                if arguments.get("permission"):
                    filter_params["permission"] = arguments["permission"]
                if arguments.get("search_name"):
                    filter_params["search_name"] = arguments["search_name"]
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "people",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                    filter_params=filter_params or None,
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_check_ins_person":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "people",
                    resource_id=arguments["person_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_person_events":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "events",
                    resource_id=arguments["event_id"],
                    sub_resource="person_events",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_person_event":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "events",
                    resource_id=arguments["event_id"],
                    sub_resource="person_events",
                    sub_resource_id=arguments["person_event_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_stations":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "stations",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_station":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "stations",
                    resource_id=arguments["station_id"],
                    include=arguments.get("include"),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_themes":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "themes",
                    per_page=arguments.get("per_page", 25),
                    offset=arguments.get("offset", 0),
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        elif name == "get_theme":
            async with pco_client:
                result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "themes",
                    resource_id=arguments["theme_id"],
                )
                return [TextContent(type="text", text=result.model_dump_json(indent=2))]

        # Check-ins Analytics and Workflow Tools
        elif name == "get_volunteer_count_for_date":
            async with pco_client:
                # Get people with headcounter permission
                filter_params = {"headcounter": True}
                if arguments.get("date"):
                    # For specific date, we'd need to check event attendance
                    # This is a simplified version - in practice you'd cross-reference with events
                    pass
                
                try:
                    people_result = await pco_client.get(
                        PCOProduct.CHECK_INS,
                        "people",
                        per_page=100,
                        filter_params=filter_params,
                    )
                    
                    volunteer_count = len(people_result.data) if hasattr(people_result, 'data') else 0
                    
                    result = {
                        "volunteer_count": volunteer_count,
                        "date": arguments.get("date"),
                        "start_date": arguments.get("start_date"),
                        "end_date": arguments.get("end_date"),
                        "details": people_result.model_dump() if arguments.get("include_details") else None
                    }
                    return [TextContent(type="text", text=json.dumps(result, indent=2))]
                    
                except Exception as e:
                    # Handle Pydantic validation errors by using raw HTTP response
                    if "validation errors" in str(e):
                        # Make direct HTTP call to get raw data
                        import httpx
                        import base64
                        import os
                        
                        app_id = config.app_id
                        secret = config.secret
                        credentials = f'{app_id}:{secret}'
                        encoded_credentials = base64.b64encode(credentials.encode()).decode()
                        auth_header = f'Basic {encoded_credentials}'
                        
                        async with httpx.AsyncClient() as http_client:
                            url = "https://api.planningcenteronline.com/check_ins/v2/people"
                            headers = {
                                'Authorization': auth_header,
                                'Accept': 'application/json',
                                'Content-Type': 'application/json'
                            }
                            params = {'per_page': 100, 'where[headcounter]': 'True'}
                            
                            response = await http_client.get(url, headers=headers, params=params)
                            if response.status_code == 200:
                                data = response.json()
                                volunteer_count = len(data.get('data', []))
                                
                                result = {
                                    "volunteer_count": volunteer_count,
                                    "date": arguments.get("date"),
                                    "start_date": arguments.get("start_date"),
                                    "end_date": arguments.get("end_date"),
                                    "message": f"Found {volunteer_count} volunteers with headcounter permission"
                                }
                                return [TextContent(type="text", text=json.dumps(result, indent=2))]
                            else:
                                return [TextContent(type="text", text=f"Error: HTTP {response.status_code} - {response.text}")]
                    else:
                        raise e

        elif name == "get_attendance_summary_for_event":
            async with pco_client:
                event_id = arguments["event_id"]
                
                # Get event details
                event_result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "events",
                    resource_id=event_id,
                )
                
                # Get headcounts for the event
                headcounts_result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "headcounts",
                    filter_params={"event_id": event_id},
                )
                
                # Get check-ins for the event
                check_ins_result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "check_ins",
                    filter_params={"event_id": event_id},
                )
                
                # Get volunteers (people with headcounter permission)
                volunteers_result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "people",
                    filter_params={"headcounter": True},
                )
                
                total_headcount = sum(hc.get("total", 0) for hc in headcounts_result.data) if hasattr(headcounts_result, 'data') else 0
                total_check_ins = len(check_ins_result.data) if hasattr(check_ins_result, 'data') else 0
                volunteer_count = len(volunteers_result.data) if hasattr(volunteers_result, 'data') else 0
                
                result = {
                    "event_id": event_id,
                    "event_name": event_result.data.get("name") if hasattr(event_result, 'data') else "Unknown",
                    "total_headcount": total_headcount,
                    "total_check_ins": total_check_ins,
                    "volunteer_count": volunteer_count,
                    "breakdown": {
                        "headcounts": headcounts_result.model_dump() if arguments.get("include_breakdown") else None,
                        "check_ins": check_ins_result.model_dump() if arguments.get("include_breakdown") else None,
                    }
                }
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_weekly_attendance_trends":
            try:
                async with pco_client:
                    start_date = arguments["start_date"]
                    end_date = arguments["end_date"]
                    group_by = arguments.get("group_by", "day")
                    
                    # Get events in date range
                    events_result = await pco_client.get(
                        PCOProduct.CHECK_INS,
                        "events",
                        filter_params={
                            "start_date": start_date,
                            "end_date": end_date
                        },
                    )
                    
                    trends = []
                    if hasattr(events_result, 'data'):
                        for event in events_result.data:
                            # Get headcounts for each event
                            headcounts_result = await pco_client.get(
                                PCOProduct.CHECK_INS,
                                "headcounts",
                                filter_params={"event_id": event.get("id")},
                            )
                            
                            total_attendance = sum(hc.get("total", 0) for hc in headcounts_result.data) if hasattr(headcounts_result, 'data') else 0
                            
                            event_data = {
                                "date": event.get("starts_at", "").split("T")[0] if event.get("starts_at") else "",
                                "event_name": event.get("name", ""),
                                "attendance": total_attendance,
                            }
                            
                            if arguments.get("include_volunteers"):
                                # Get volunteer count for this event
                                volunteers_result = await pco_client.get(
                                    PCOProduct.CHECK_INS,
                                    "people",
                                    filter_params={"headcounter": True},
                                )
                                event_data["volunteer_count"] = len(volunteers_result.data) if hasattr(volunteers_result, 'data') else 0
                            
                            trends.append(event_data)
                    
                    result = {
                        "start_date": start_date,
                        "end_date": end_date,
                        "group_by": group_by,
                        "trends": trends,
                        "summary": {
                            "total_events": len(trends),
                            "average_attendance": sum(t["attendance"] for t in trends) / len(trends) if trends else 0,
                            "total_attendance": sum(t["attendance"] for t in trends)
                        }
                    }
                    return [TextContent(type="text", text=json.dumps(result, indent=2))]
            except Exception as e:
                if "validation errors" in str(e):
                    # Fallback to direct API call
                    start_date = arguments["start_date"]
                    end_date = arguments["end_date"]
                    
                    # Get events using direct API call
                    events_params = {
                        'where[start_date]': start_date,
                        'where[end_date]': end_date
                    }
                    events_data = await make_direct_api_call("/check_ins/v2/events", events_params)
                    
                    trends = []
                    for event in events_data.get('data', []):
                        event_data = {
                            "date": event.get("attributes", {}).get("starts_at", "").split("T")[0] if event.get("attributes", {}).get("starts_at") else "",
                            "event_name": event.get("attributes", {}).get("name", ""),
                            "attendance": 0,  # Would need additional API call for headcounts
                        }
                        
                        if arguments.get("include_volunteers"):
                            # Get volunteer count using direct API call
                            volunteers_data = await make_direct_api_call("/check_ins/v2/people", {'where[headcounter]': 'True'})
                            event_data["volunteer_count"] = len(volunteers_data.get('data', []))
                        
                        trends.append(event_data)
                    
                    result = {
                        "start_date": start_date,
                        "end_date": end_date,
                        "group_by": arguments.get("group_by", "day"),
                        "trends": trends,
                        "summary": {
                            "total_events": len(trends),
                            "average_attendance": sum(t["attendance"] for t in trends) / len(trends) if trends else 0,
                            "total_attendance": sum(t["attendance"] for t in trends)
                        }
                    }
                    return [TextContent(type="text", text=json.dumps(result, indent=2))]
                else:
                    raise e

        elif name == "get_station_utilization_report":
            async with pco_client:
                start_date = arguments["start_date"]
                end_date = arguments["end_date"]
                station_id = arguments.get("station_id")
                
                # Get stations
                if station_id:
                    stations_result = await pco_client.get(
                        PCOProduct.CHECK_INS,
                        "stations",
                        resource_id=station_id,
                    )
                    stations = [stations_result.data] if hasattr(stations_result, 'data') else []
                else:
                    stations_result = await pco_client.get(
                        PCOProduct.CHECK_INS,
                        "stations",
                    )
                    stations = stations_result.data if hasattr(stations_result, 'data') else []
                
                utilization_data = []
                for station in stations:
                    # Get check-ins for this station in date range
                    check_ins_result = await pco_client.get(
                        PCOProduct.CHECK_INS,
                        "check_ins",
                        filter_params={
                            "station_id": station.get("id"),
                            "start_date": start_date,
                            "end_date": end_date
                        },
                    )
                    
                    check_in_count = len(check_ins_result.data) if hasattr(check_ins_result, 'data') else 0
                    
                    station_data = {
                        "station_id": station.get("id"),
                        "station_name": station.get("name", ""),
                        "check_in_count": check_in_count,
                        "utilization_rate": "N/A",  # Would need capacity data to calculate
                    }
                    
                    if arguments.get("include_peak_times"):
                        # Analyze peak times (simplified)
                        station_data["peak_analysis"] = "Peak times would be calculated from check-in timestamps"
                    
                    utilization_data.append(station_data)
                
                result = {
                    "start_date": start_date,
                    "end_date": end_date,
                    "stations": utilization_data,
                    "summary": {
                        "total_stations": len(utilization_data),
                        "total_check_ins": sum(s["check_in_count"] for s in utilization_data),
                        "average_utilization": sum(s["check_in_count"] for s in utilization_data) / len(utilization_data) if utilization_data else 0
                    }
                }
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_family_check_in_patterns":
            async with pco_client:
                start_date = arguments["start_date"]
                end_date = arguments["end_date"]
                min_family_size = arguments.get("min_family_size", 2)
                
                # Get check-ins in date range
                check_ins_result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "check_ins",
                    filter_params={
                        "start_date": start_date,
                        "end_date": end_date
                    },
                )
                
                # Group by household/family
                family_patterns = {}
                if hasattr(check_ins_result, 'data'):
                    for check_in in check_ins_result.data:
                        household_id = check_in.get("household_id")
                        if household_id:
                            if household_id not in family_patterns:
                                family_patterns[household_id] = {
                                    "household_id": household_id,
                                    "check_ins": [],
                                    "family_size": 0,
                                    "attendance_dates": set()
                                }
                            
                            family_patterns[household_id]["check_ins"].append(check_in)
                            family_patterns[household_id]["attendance_dates"].add(
                                check_in.get("created_at", "").split("T")[0] if check_in.get("created_at") else ""
                            )
                
                # Filter by minimum family size and calculate patterns
                filtered_families = []
                for household_id, data in family_patterns.items():
                    family_size = len(data["check_ins"])
                    if family_size >= min_family_size:
                        family_data = {
                            "household_id": household_id,
                            "family_size": family_size,
                            "attendance_frequency": len(data["attendance_dates"]),
                            "total_check_ins": len(data["check_ins"]),
                        }
                        
                        if arguments.get("include_attendance_frequency"):
                            family_data["attendance_dates"] = list(data["attendance_dates"])
                        
                        filtered_families.append(family_data)
                
                result = {
                    "start_date": start_date,
                    "end_date": end_date,
                    "min_family_size": min_family_size,
                    "family_patterns": filtered_families,
                    "summary": {
                        "total_families": len(filtered_families),
                        "average_family_size": sum(f["family_size"] for f in filtered_families) / len(filtered_families) if filtered_families else 0,
                        "average_attendance_frequency": sum(f["attendance_frequency"] for f in filtered_families) / len(filtered_families) if filtered_families else 0
                    }
                }
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_volunteer_availability_report":
            async with pco_client:
                start_date = arguments["start_date"]
                end_date = arguments["end_date"]
                volunteer_type = arguments.get("volunteer_type")
                
                # Get volunteers
                filter_params = {"headcounter": True}
                if volunteer_type:
                    filter_params["permission"] = volunteer_type
                
                volunteers_result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "people",
                    filter_params=filter_params,
                )
                
                volunteers = []
                if hasattr(volunteers_result, 'data'):
                    for volunteer in volunteers_result.data:
                        volunteer_data = {
                            "person_id": volunteer.get("id"),
                            "name": f"{volunteer.get('first_name', '')} {volunteer.get('last_name', '')}".strip(),
                            "permissions": volunteer.get("permissions", []),
                        }
                        
                        if arguments.get("include_contact_info"):
                            volunteer_data.update({
                                "email": volunteer.get("email", ""),
                                "phone": volunteer.get("phone", ""),
                            })
                        
                        volunteers.append(volunteer_data)
                
                result = {
                    "start_date": start_date,
                    "end_date": end_date,
                    "volunteer_type": volunteer_type,
                    "volunteers": volunteers,
                    "summary": {
                        "total_volunteers": len(volunteers),
                        "available_volunteers": len(volunteers),  # Simplified - would need scheduling data
                    }
                }
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_attendance_by_demographics":
            async with pco_client:
                start_date = arguments["start_date"]
                end_date = arguments["end_date"]
                group_by = arguments.get("group_by", "age")
                
                # Get check-ins in date range
                check_ins_result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "check_ins",
                    filter_params={
                        "start_date": start_date,
                        "end_date": end_date
                    },
                )
                
                # Get people data for demographics
                people_result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "people",
                )
                
                # Create people lookup
                people_lookup = {}
                if hasattr(people_result, 'data'):
                    for person in people_result.data:
                        people_lookup[person.get("id")] = person
                
                # Group attendance by demographics
                demographic_groups = {}
                total_attendance = 0
                
                if hasattr(check_ins_result, 'data'):
                    for check_in in check_ins_result.data:
                        person_id = check_in.get("person_id")
                        person = people_lookup.get(person_id, {})
                        
                        if group_by == "age":
                            # Calculate age from birthdate
                            birthdate = person.get("birthdate")
                            if birthdate:
                                # Simplified age calculation
                                age_group = "Unknown"
                                # In practice, you'd calculate actual age and group
                                demographic_key = age_group
                            else:
                                demographic_key = "Unknown Age"
                        elif group_by == "family_status":
                            demographic_key = "Family" if person.get("household_id") else "Individual"
                        elif group_by == "location":
                            demographic_key = check_in.get("location_id", "Unknown Location")
                        else:
                            demographic_key = "Other"
                        
                        if demographic_key not in demographic_groups:
                            demographic_groups[demographic_key] = 0
                        
                        demographic_groups[demographic_key] += 1
                        total_attendance += 1
                
                # Calculate percentages
                demographic_breakdown = []
                for group, count in demographic_groups.items():
                    percentage = (count / total_attendance * 100) if total_attendance > 0 else 0
                    group_data = {
                        "group": group,
                        "count": count,
                    }
                    
                    if arguments.get("include_percentages"):
                        group_data["percentage"] = round(percentage, 2)
                    
                    demographic_breakdown.append(group_data)
                
                result = {
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "demographic_breakdown": demographic_breakdown,
                    "summary": {
                        "total_attendance": total_attendance,
                        "total_groups": len(demographic_breakdown)
                    }
                }
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_event_capacity_analysis":
            async with pco_client:
                event_id = arguments["event_id"]
                
                # Get event details
                event_result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "events",
                    resource_id=event_id,
                )
                
                # Get headcounts for the event
                headcounts_result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "headcounts",
                    filter_params={"event_id": event_id},
                )
                
                total_attendance = sum(hc.get("total", 0) for hc in headcounts_result.data) if hasattr(headcounts_result, 'data') else 0
                event_capacity = event_result.data.get("capacity") if hasattr(event_result, 'data') else None
                
                capacity_utilization = "N/A"
                if event_capacity and event_capacity > 0:
                    capacity_utilization = round((total_attendance / event_capacity) * 100, 2)
                
                result = {
                    "event_id": event_id,
                    "event_name": event_result.data.get("name") if hasattr(event_result, 'data') else "Unknown",
                    "total_attendance": total_attendance,
                    "event_capacity": event_capacity,
                    "capacity_utilization": capacity_utilization,
                }
                
                if arguments.get("include_recommendations"):
                    recommendations = []
                    if capacity_utilization != "N/A":
                        if capacity_utilization > 90:
                            recommendations.append("Event is near capacity - consider additional seating or overflow areas")
                        elif capacity_utilization < 50:
                            recommendations.append("Event has low attendance - consider promotion or scheduling adjustments")
                    
                    result["recommendations"] = recommendations
                
                if arguments.get("compare_to_historical"):
                    result["historical_comparison"] = "Historical data comparison would require additional analysis"
                
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_check_in_efficiency_metrics":
            async with pco_client:
                start_date = arguments["start_date"]
                end_date = arguments["end_date"]
                location_id = arguments.get("location_id")
                
                # Get check-ins in date range
                filter_params = {
                    "start_date": start_date,
                    "end_date": end_date
                }
                if location_id:
                    filter_params["location_id"] = location_id
                
                check_ins_result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "check_ins",
                    filter_params=filter_params,
                )
                
                check_ins = check_ins_result.data if hasattr(check_ins_result, 'data') else []
                
                # Calculate efficiency metrics
                total_check_ins = len(check_ins)
                stations_used = set()
                peak_hours = {}
                
                for check_in in check_ins:
                    station_id = check_in.get("station_id")
                    if station_id:
                        stations_used.add(station_id)
                    
                    # Analyze peak times
                    created_at = check_in.get("created_at")
                    if created_at:
                        hour = created_at.split("T")[1].split(":")[0] if "T" in created_at else "00"
                        peak_hours[hour] = peak_hours.get(hour, 0) + 1
                
                result = {
                    "start_date": start_date,
                    "end_date": end_date,
                    "location_id": location_id,
                    "efficiency_metrics": {
                        "total_check_ins": total_check_ins,
                        "stations_utilized": len(stations_used),
                        "average_check_ins_per_station": total_check_ins / len(stations_used) if stations_used else 0,
                    }
                }
                
                if arguments.get("include_peak_analysis"):
                    peak_hour = max(peak_hours.items(), key=lambda x: x[1]) if peak_hours else ("N/A", 0)
                    result["peak_analysis"] = {
                        "peak_hour": peak_hour[0],
                        "peak_hour_count": peak_hour[1],
                        "hourly_distribution": peak_hours
                    }
                
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_volunteer_roster_for_date":
            try:
                async with pco_client:
                    date = arguments["date"]
                    
                    # Get volunteers
                    volunteers_result = await pco_client.get(
                        PCOProduct.CHECK_INS,
                        "people",
                        filter_params={"headcounter": True},
                    )
                    
                    volunteers = []
                    if hasattr(volunteers_result, 'data'):
                        for volunteer in volunteers_result.data:
                            volunteer_data = {
                                "person_id": volunteer.get("id"),
                                "name": f"{volunteer.get('first_name', '')} {volunteer.get('last_name', '')}".strip(),
                                "role": "Headcounter",  # Simplified
                            }
                            
                            if arguments.get("include_contact_info"):
                                volunteer_data.update({
                                    "email": volunteer.get("email", ""),
                                    "phone": volunteer.get("phone", ""),
                                })
                            
                            if arguments.get("include_emergency_contacts"):
                                volunteer_data["emergency_contact"] = "Emergency contact info would be retrieved from person details"
                            
                            volunteers.append(volunteer_data)
                    
                    format_type = arguments.get("format", "detailed")
                    
                    if format_type == "contact_sheet":
                        result = {
                            "date": date,
                            "volunteer_contact_sheet": volunteers,
                            "total_volunteers": len(volunteers)
                        }
                    elif format_type == "list":
                        result = {
                            "date": date,
                            "volunteer_list": [v["name"] for v in volunteers],
                            "total_volunteers": len(volunteers)
                        }
                    else:  # detailed
                        result = {
                            "date": date,
                            "volunteers": volunteers,
                            "total_volunteers": len(volunteers),
                            "summary": {
                                "headcounters": len(volunteers),
                                "with_contact_info": len([v for v in volunteers if v.get("email") or v.get("phone")])
                            }
                        }
                    
                    return [TextContent(type="text", text=json.dumps(result, indent=2))]
            except Exception as e:
                if "validation errors" in str(e):
                    # Fallback to direct API call
                    date = arguments["date"]
                    
                    # Get volunteers using direct API call
                    volunteers_data = await make_direct_api_call("/check_ins/v2/people", {'where[headcounter]': 'True'})
                    
                    volunteers = []
                    for volunteer in volunteers_data.get('data', []):
                        volunteer_data = {
                            "person_id": volunteer.get("id"),
                            "name": f"{volunteer.get('attributes', {}).get('first_name', '')} {volunteer.get('attributes', {}).get('last_name', '')}".strip(),
                            "role": "Headcounter",
                        }
                        
                        if arguments.get("include_contact_info"):
                            volunteer_data.update({
                                "email": volunteer.get("attributes", {}).get("email", ""),
                                "phone": volunteer.get("attributes", {}).get("phone", ""),
                            })
                        
                        if arguments.get("include_emergency_contacts"):
                            volunteer_data["emergency_contact"] = "Emergency contact info would be retrieved from person details"
                        
                        volunteers.append(volunteer_data)
                    
                    format_type = arguments.get("format", "detailed")
                    
                    if format_type == "contact_sheet":
                        result = {
                            "date": date,
                            "volunteer_contact_sheet": volunteers,
                            "total_volunteers": len(volunteers)
                        }
                    elif format_type == "list":
                        result = {
                            "date": date,
                            "volunteer_list": [v["name"] for v in volunteers],
                            "total_volunteers": len(volunteers)
                        }
                    else:  # detailed
                        result = {
                            "date": date,
                            "volunteers": volunteers,
                            "total_volunteers": len(volunteers),
                            "summary": {
                                "headcounters": len(volunteers),
                                "with_contact_info": len([v for v in volunteers if v.get("email") or v.get("phone")])
                            }
                        }
                    
                    return [TextContent(type="text", text=json.dumps(result, indent=2))]
                else:
                    raise e

        elif name == "get_attendance_anomalies":
            async with pco_client:
                start_date = arguments["start_date"]
                end_date = arguments["end_date"]
                sensitivity = arguments.get("sensitivity", "medium")
                
                # Get events in date range
                events_result = await pco_client.get(
                    PCOProduct.CHECK_INS,
                    "events",
                    filter_params={
                        "start_date": start_date,
                        "end_date": end_date
                    },
                )
                
                attendance_data = []
                if hasattr(events_result, 'data'):
                    for event in events_result.data:
                        # Get headcounts for each event
                        headcounts_result = await pco_client.get(
                            PCOProduct.CHECK_INS,
                            "headcounts",
                            filter_params={"event_id": event.get("id")},
                        )
                        
                        total_attendance = sum(hc.get("total", 0) for hc in headcounts_result.data) if hasattr(headcounts_result, 'data') else 0
                        
                        attendance_data.append({
                            "date": event.get("starts_at", "").split("T")[0] if event.get("starts_at") else "",
                            "event_name": event.get("name", ""),
                            "attendance": total_attendance,
                        })
                
                # Simple anomaly detection (in practice, you'd use more sophisticated algorithms)
                if len(attendance_data) > 1:
                    attendances = [d["attendance"] for d in attendance_data]
                    mean_attendance = sum(attendances) / len(attendances)
                    std_dev = (sum((x - mean_attendance) ** 2 for x in attendances) / len(attendances)) ** 0.5
                    
                    threshold_multiplier = {"low": 1.5, "medium": 2.0, "high": 2.5}[sensitivity]
                    threshold = std_dev * threshold_multiplier
                    
                    anomalies = []
                    for data in attendance_data:
                        deviation = abs(data["attendance"] - mean_attendance)
                        if deviation > threshold:
                            anomaly_type = "High" if data["attendance"] > mean_attendance else "Low"
                            anomaly = {
                                "date": data["date"],
                                "event_name": data["event_name"],
                                "attendance": data["attendance"],
                                "expected_range": f"{mean_attendance - threshold:.0f} - {mean_attendance + threshold:.0f}",
                                "anomaly_type": anomaly_type,
                                "deviation": round(deviation, 2),
                            }
                            
                            if arguments.get("include_explanations"):
                                if anomaly_type == "High":
                                    anomaly["possible_explanations"] = [
                                        "Special event or holiday",
                                        "Guest speaker or special program",
                                        "Weather conditions",
                                        "Promotional campaign"
                                    ]
                                else:
                                    anomaly["possible_explanations"] = [
                                        "Holiday weekend",
                                        "Weather conditions",
                                        "Competing events",
                                        "Seasonal factors"
                                    ]
                            
                            anomalies.append(anomaly)
                else:
                    anomalies = []
                
                result = {
                    "start_date": start_date,
                    "end_date": end_date,
                    "sensitivity": sensitivity,
                    "anomalies": anomalies,
                    "summary": {
                        "total_events": len(attendance_data),
                        "anomalies_detected": len(anomalies),
                        "average_attendance": sum(d["attendance"] for d in attendance_data) / len(attendance_data) if attendance_data else 0
                    }
                }
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

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

    # Load environment variables from .env file
    load_dotenv()

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
                        notification_options=NotificationOptions(),
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
