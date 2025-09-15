#!/usr/bin/env python3
"""Simple MCP mock server for Planning Center API testing."""

import asyncio
import json
import logging
import random
import sys
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional
from uuid import uuid4

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Set up logging to stderr so it appears in Claude Desktop logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

# Create MCP server
server = Server("planning-center-mock")

# Global mock data storage
mock_data = {
    "people": [],
    "services": [],
    "plans": [],
    "registrations": [],
    "attendees": [],
}


def generate_mock_person(person_id: Optional[str] = None) -> Dict[str, Any]:
    """Generate a mock person with realistic data."""
    first_names = [
        "John",
        "Jane",
        "Michael",
        "Sarah",
        "David",
        "Emily",
        "Robert",
        "Lisa",
        "James",
        "Maria",
    ]
    last_names = [
        "Smith",
        "Johnson",
        "Williams",
        "Brown",
        "Jones",
        "Garcia",
        "Miller",
        "Davis",
        "Rodriguez",
        "Martinez",
    ]

    person_id = person_id or str(uuid4())
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    return {
        "id": person_id,
        "type": "Person",
        "attributes": {
            "first_name": first_name,
            "last_name": last_name,
            "full_name": f"{first_name} {last_name}",
            "email": f"{first_name.lower()}.{last_name.lower()}@example.com",
            "phone": f"555-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "status": random.choice(["active", "inactive"]),
            "created_at": (
                datetime.now() - timedelta(days=random.randint(1, 365))
            ).isoformat(),
            "updated_at": datetime.now().isoformat(),
        },
        "relationships": {
            "emails": {"data": [{"id": str(uuid4()), "type": "Email"}]},
            "phone_numbers": {"data": [{"id": str(uuid4()), "type": "PhoneNumber"}]},
        },
    }


def generate_mock_service(service_id: Optional[str] = None) -> Dict[str, Any]:
    """Generate a mock service with realistic data."""
    service_names = [
        "Sunday Morning Service",
        "Evening Service",
        "Youth Service",
        "Children's Service",
        "Prayer Meeting",
        "Bible Study",
        "Worship Night",
        "Community Service",
        "Special Event",
    ]

    service_id = service_id or str(uuid4())
    name = random.choice(service_names)

    return {
        "id": service_id,
        "type": "Service",
        "attributes": {
            "name": name,
            "description": f"A {name.lower()} for the community",
            "created_at": (
                datetime.now() - timedelta(days=random.randint(1, 365))
            ).isoformat(),
            "updated_at": datetime.now().isoformat(),
        },
    }


def generate_mock_plan(
    plan_id: Optional[str] = None, service_id: Optional[str] = None
) -> Dict[str, Any]:
    """Generate a mock plan with realistic data."""
    plan_titles = [
        "Sunday Service Plan",
        "Christmas Eve Service",
        "Easter Service",
        "Youth Retreat",
        "Community Outreach",
        "Prayer Meeting",
        "Bible Study Session",
        "Worship Night",
        "Special Event",
    ]

    plan_id = plan_id or str(uuid4())
    service_id = (
        service_id or random.choice([s["id"] for s in mock_data["services"]])
        if mock_data["services"]
        else str(uuid4())
    )
    title = random.choice(plan_titles)

    return {
        "id": plan_id,
        "type": "Plan",
        "attributes": {
            "title": title,
            "service_id": service_id,
            "plan_date": (
                datetime.now() + timedelta(days=random.randint(1, 30))
            ).isoformat(),
            "created_at": (
                datetime.now() - timedelta(days=random.randint(1, 365))
            ).isoformat(),
            "updated_at": datetime.now().isoformat(),
        },
        "relationships": {"service": {"data": {"id": service_id, "type": "Service"}}},
    }


def generate_mock_registration(registration_id: Optional[str] = None) -> Dict[str, Any]:
    """Generate a mock registration with realistic data."""
    event_names = [
        "Summer Camp 2024",
        "Youth Retreat",
        "Community Picnic",
        "Christmas Party",
        "Easter Celebration",
        "Bible Study Group",
        "Prayer Meeting",
        "Worship Night",
        "Special Event",
    ]

    registration_id = registration_id or str(uuid4())
    name = random.choice(event_names)

    return {
        "id": registration_id,
        "type": "Registration",
        "attributes": {
            "name": name,
            "description": f"Registration for {name}",
            "status": random.choice(["open", "closed"]),
            "capacity": random.randint(10, 100),
            "registered_count": random.randint(0, 50),
            "created_at": (
                datetime.now() - timedelta(days=random.randint(1, 365))
            ).isoformat(),
            "updated_at": datetime.now().isoformat(),
        },
    }


def generate_mock_attendee(attendee_id: Optional[str] = None) -> Dict[str, Any]:
    """Generate a mock attendee with realistic data."""
    attendee_id = attendee_id or str(uuid4())
    person = generate_mock_person()

    return {
        "id": attendee_id,
        "type": "Attendee",
        "attributes": {
            "first_name": person["attributes"]["first_name"],
            "last_name": person["attributes"]["last_name"],
            "email": person["attributes"]["email"],
            "attendance_status": random.choice(
                ["checked_in", "checked_out", "registered"]
            ),
            "created_at": (
                datetime.now() - timedelta(days=random.randint(1, 30))
            ).isoformat(),
            "updated_at": datetime.now().isoformat(),
        },
        "relationships": {"person": {"data": {"id": person["id"], "type": "Person"}}},
    }


def initialize_mock_data():
    """Initialize the mock data with some sample records."""
    logger.info("Initializing mock data...")

    # Generate some services first
    for _ in range(5):
        mock_data["services"].append(generate_mock_service())

    # Generate some people
    for _ in range(20):
        mock_data["people"].append(generate_mock_person())

    # Generate some plans
    for _ in range(10):
        mock_data["plans"].append(generate_mock_plan())

    # Generate some registrations
    for _ in range(8):
        mock_data["registrations"].append(generate_mock_registration())

    # Generate some attendees
    for _ in range(15):
        mock_data["attendees"].append(generate_mock_attendee())

    logger.info(
        f"Mock data initialized: {len(mock_data['people'])} people, {len(mock_data['services'])} services, {len(mock_data['plans'])} plans, {len(mock_data['registrations'])} registrations, {len(mock_data['attendees'])} attendees"
    )


def filter_data(
    data_list: List[Dict[str, Any]], filters: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """Apply filters to a list of data."""
    filtered = data_list

    for key, value in filters.items():
        if key == "search":
            filtered = [
                item
                for item in filtered
                if value.lower() in item["attributes"].get("first_name", "").lower()
                or value.lower() in item["attributes"].get("last_name", "").lower()
                or value.lower() in item["attributes"].get("full_name", "").lower()
            ]
        elif key in ["status", "email", "phone", "attendance_status"]:
            filtered = [
                item for item in filtered if item["attributes"].get(key) == value
            ]
        elif key == "service_id":
            filtered = [
                item
                for item in filtered
                if item["attributes"].get("service_id") == value
            ]

    return filtered


def paginate_data(
    data_list: List[Dict[str, Any]], per_page: int, offset: int
) -> Dict[str, Any]:
    """Paginate data and return collection format."""
    total = len(data_list)
    start = offset
    end = min(start + per_page, total)

    paginated_data = data_list[start:end]

    return {
        "data": paginated_data,
        "meta": {
            "total": total,
            "count": len(paginated_data),
            "per_page": per_page,
            "offset": offset,
        },
        "links": {
            "self": f"?per_page={per_page}&offset={offset}",
            "first": f"?per_page={per_page}&offset=0",
            "last": f"?per_page={per_page}&offset={max(0, total - per_page)}",
            "next": f"?per_page={per_page}&offset={end}" if end < total else None,
            "prev": f"?per_page={per_page}&offset={max(0, start - per_page)}"
            if start > 0
            else None,
        },
    }


@server.list_tools()
async def list_tools() -> List[Tool]:
    """List available tools."""
    logger.info("Listing tools")
    return [
        Tool(
            name="get_people",
            description="Get people from Planning Center People with optional filtering (MOCK DATA)",
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
                    "search": {
                        "type": "string",
                        "description": "Search query for people",
                    },
                    "status": {
                        "type": "string",
                        "description": "Filter by status (active, inactive)",
                    },
                },
            },
        ),
        Tool(
            name="get_services",
            description="Get services from Planning Center Services (MOCK DATA)",
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
                },
            },
        ),
        Tool(
            name="get_plans",
            description="Get plans from Planning Center Services (MOCK DATA)",
            inputSchema={
                "type": "object",
                "properties": {
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
                },
            },
        ),
        Tool(
            name="get_registrations",
            description="Get registrations from Planning Center Registrations (MOCK DATA)",
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
                    "status": {
                        "type": "string",
                        "description": "Filter by status (open, closed)",
                    },
                },
            },
        ),
        Tool(
            name="get_attendees",
            description="Get attendees from Planning Center Check-ins (MOCK DATA)",
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
                    "attendance_status": {
                        "type": "string",
                        "description": "Filter by attendance status (checked_in, checked_out)",
                    },
                },
            },
        ),
        Tool(
            name="get_mock_status",
            description="Get status of mock data",
            inputSchema={"type": "object", "properties": {}},
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Handle tool calls."""
    logger.info(f"Calling tool: {name} with arguments: {arguments}")

    try:
        if name == "get_people":
            filters = {}
            if arguments.get("search"):
                filters["search"] = arguments["search"]
            if arguments.get("status"):
                filters["status"] = arguments["status"]

            filtered_people = filter_data(mock_data["people"], filters)
            result = paginate_data(
                filtered_people,
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_services":
            result = paginate_data(
                mock_data["services"],
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_plans":
            result = paginate_data(
                mock_data["plans"],
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_registrations":
            filters = {}
            if arguments.get("status"):
                filters["status"] = arguments["status"]

            filtered_registrations = filter_data(mock_data["registrations"], filters)
            result = paginate_data(
                filtered_registrations,
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_attendees":
            filters = {}
            if arguments.get("attendance_status"):
                filters["attendance_status"] = arguments["attendance_status"]

            filtered_attendees = filter_data(mock_data["attendees"], filters)
            result = paginate_data(
                filtered_attendees,
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_mock_status":
            result = {
                "message": "Mock Planning Center API Server",
                "data_counts": {k: len(v) for k, v in mock_data.items()},
                "endpoints": [
                    "get_people",
                    "get_services",
                    "get_plans",
                    "get_registrations",
                    "get_attendees",
                    "get_mock_status",
                ],
            }
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]

    except Exception as e:
        logger.error(f"Error calling tool {name}: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


async def main():
    """Main entry point."""
    logger.info("Starting Planning Center Mock MCP Server...")

    # Initialize mock data
    initialize_mock_data()

    logger.info("Starting MCP server with stdio transport...")

    # Run the MCP server with proper error handling
    try:
        async with stdio_server() as (read_stream, write_stream):
            logger.info("MCP server transport established")

            # Create initialization options
            init_options = server.create_initialization_options()
            logger.info("Initialization options created successfully")

            # Run the server
            logger.info("Starting server.run()...")
            await server.run(
                read_stream,
                write_stream,
                init_options,
            )
            logger.info("Server.run() completed successfully")

    except Exception as e:
        logger.error(f"Error running MCP server: {e}")
        import traceback

        logger.error(f"Traceback: {traceback.format_exc()}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        import traceback

        logger.error(f"Traceback: {traceback.format_exc()}")
        sys.exit(1)
