#!/usr/bin/env python3
"""Fixed MCP mock server entry point for Planning Center API testing."""

import asyncio
import json
import logging
import random
import sys
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional
from uuid import uuid4

from mcp.server import Server
from mcp.server.models import InitializationOptions
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
            description="Get a specific person by ID (MOCK DATA)",
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
            description="Get a specific service by ID (MOCK DATA)",
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
            description="Get plans from Planning Center Services (MOCK DATA)",
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
            description="Get a specific plan by ID (MOCK DATA)",
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
            description="Get a specific registration by ID (MOCK DATA)",
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
            description="Get a specific attendee by ID (MOCK DATA)",
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
            name="reset_mock_data",
            description="Reset mock data to initial state",
            inputSchema={"type": "object", "properties": {}},
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
            if arguments.get("email"):
                filters["email"] = arguments["email"]
            if arguments.get("phone"):
                filters["phone"] = arguments["phone"]

            filtered_people = filter_data(mock_data["people"], filters)
            result = paginate_data(
                filtered_people,
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_person":
            person = next(
                (p for p in mock_data["people"] if p["id"] == arguments["person_id"]),
                None,
            )
            if not person:
                return [TextContent(type="text", text="Person not found")]
            return [TextContent(type="text", text=json.dumps(person, indent=2))]

        elif name == "get_services":
            result = paginate_data(
                mock_data["services"],
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_service":
            service = next(
                (
                    s
                    for s in mock_data["services"]
                    if s["id"] == arguments["service_id"]
                ),
                None,
            )
            if not service:
                return [TextContent(type="text", text="Service not found")]
            return [TextContent(type="text", text=json.dumps(service, indent=2))]

        elif name == "get_plans":
            filters = {}
            if arguments.get("service_id"):
                filters["service_id"] = arguments["service_id"]

            filtered_plans = filter_data(mock_data["plans"], filters)
            result = paginate_data(
                filtered_plans,
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_plan":
            plan = next(
                (p for p in mock_data["plans"] if p["id"] == arguments["plan_id"]), None
            )
            if not plan:
                return [TextContent(type="text", text="Plan not found")]
            return [TextContent(type="text", text=json.dumps(plan, indent=2))]

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

        elif name == "get_registration":
            registration = next(
                (
                    r
                    for r in mock_data["registrations"]
                    if r["id"] == arguments["registration_id"]
                ),
                None,
            )
            if not registration:
                return [TextContent(type="text", text="Registration not found")]
            return [TextContent(type="text", text=json.dumps(registration, indent=2))]

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

        elif name == "get_attendee":
            attendee = next(
                (
                    a
                    for a in mock_data["attendees"]
                    if a["id"] == arguments["attendee_id"]
                ),
                None,
            )
            if not attendee:
                return [TextContent(type="text", text="Attendee not found")]
            return [TextContent(type="text", text=json.dumps(attendee, indent=2))]

        elif name == "reset_mock_data":
            # Reset mock data
            mock_data.clear()
            mock_data.update(
                {
                    "people": [],
                    "services": [],
                    "plans": [],
                    "registrations": [],
                    "attendees": [],
                }
            )
            initialize_mock_data()
            result = {
                "message": "Mock data reset successfully",
                "counts": {k: len(v) for k, v in mock_data.items()},
            }
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_mock_status":
            result = {
                "message": "Mock Planning Center API Server",
                "data_counts": {k: len(v) for k, v in mock_data.items()},
                "endpoints": [
                    "get_people",
                    "get_person",
                    "get_services",
                    "get_service",
                    "get_plans",
                    "get_plan",
                    "get_registrations",
                    "get_registration",
                    "get_attendees",
                    "get_attendee",
                    "reset_mock_data",
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

    # Run the MCP server
    try:
        async with stdio_server() as (read_stream, write_stream):
            logger.info("MCP server transport established")
            await server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="planning-center-mock",
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
