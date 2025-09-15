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

from planning_center_mcp.config import PCOConfig
from planning_center_mcp.client import PCOClient

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

        elif name == "get_attendee":
            async with pco_client:
                result = await pco_client.get_attendee(
                    attendee_id=arguments["attendee_id"],
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
