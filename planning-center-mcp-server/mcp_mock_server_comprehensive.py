#!/usr/bin/env python3
"""Comprehensive MCP mock server for Planning Center API testing with all major endpoints."""

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
server = Server("planning-center-comprehensive")

# Global mock data storage
mock_data = {
    # People API
    "people": [],
    "addresses": [],
    "emails": [],
    "phone_numbers": [],
    "households": [],
    "lists": [],
    "workflows": [],
    "workflow_cards": [],
    "workflow_categories": [],
    "workflow_steps": [],
    "notes": [],
    "note_categories": [],
    "field_definitions": [],
    "field_data": [],
    "forms": [],
    "form_submissions": [],
    "background_checks": [],
    "social_profiles": [],
    "reports": [],
    "school_options": [],
    "service_times": [],
    "tabs": [],
    "rules": [],
    "conditions": [],
    "spam_email_addresses": [],
    # Services API
    "services": [],
    "service_types": [],
    "plans": [],
    "plan_times": [],
    "plan_people": [],
    "plan_notes": [],
    "songs": [],
    "arrangements": [],
    "keys": [],
    "attachments": [],
    "media": [],
    "folders": [],
    "templates": [],
    "items": [],
    "teams": [],
    "team_positions": [],
    # Registrations API
    "registrations": [],
    "attendees": [],
    "emergency_contacts": [],
    "signups": [],
    "signup_locations": [],
    "signup_times": [],
    "selection_types": [],
    "categories": [],
    "campuses": [],
    # Check-ins API
    "locations": [],
    "stations": [],
    "check_ins": [],
    "check_in_people": [],
    "check_in_households": [],
    # Giving API
    "donations": [],
    "funds": [],
    "designations": [],
    "batches": [],
    "batch_groups": [],
    "recurring_donations": [],
    "pledges": [],
    "pledge_campaigns": [],
    "payment_methods": [],
    "payment_sources": [],
    "refunds": [],
    "in_kind_donations": [],
    "labels": [],
    "notes_giving": [],
    # Groups API
    "groups": [],
    "group_types": [],
    "group_events": [],
    "group_memberships": [],
    "group_people": [],
    "group_notes": [],
    "group_locations": [],
    "group_resources": [],
    "group_times": [],
    "group_tags": [],
    "group_tag_groups": [],
    "group_campuses": [],
    "group_applications": [],
    "attendances": [],
    "enrollments": [],
    "event_notes": [],
    "memberships": [],
    "owners": [],
    # Calendar API
    "events": [],
    "event_instances": [],
    "event_times": [],
    "event_connections": [],
    "event_resource_requests": [],
    "event_resource_answers": [],
    "resources": [],
    "resource_folders": [],
    "resource_bookings": [],
    "resource_questions": [],
    "resource_suggestions": [],
    "resource_approval_groups": [],
    "required_approvals": [],
    "room_setups": [],
    "tags": [],
    "tag_groups": [],
    "conflicts": [],
    "feeds": [],
    "job_statuses": [],
    "report_templates": [],
    "organizations": [],
    "calendar_persons": [],
    "calendar_attachments": [],
    # Publishing API
    "channels": [],
    "episodes": [],
    "episode_resources": [],
    "episode_times": [],
    "episode_statistics": [],
    "series": [],
    "speakers": [],
    "speakerships": [],
    "note_templates": [],
    "channel_default_episode_resources": [],
    "channel_default_times": [],
    "channel_next_times": [],
    "publishing_organizations": [],
    # Webhooks API
    "webhook_subscriptions": [],
    "webhook_events": [],
    "webhook_deliveries": [],
    "available_events": [],
    "webhook_organizations": [],
    "webhook_services": [],
    # Organization API
    "connected_applications": [],
    "connected_application_people": [],
    "oauth_applications": [],
    "oauth_application_maus": [],
    "organization_people": [],
    "personal_access_tokens": [],
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
        "William",
        "Jennifer",
        "Christopher",
        "Linda",
        "Daniel",
        "Barbara",
        "Matthew",
        "Elizabeth",
        "Anthony",
        "Jessica",
        "Mark",
        "Susan",
        "Donald",
        "Karen",
        "Steven",
        "Nancy",
        "Paul",
        "Betty",
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
        "Hernandez",
        "Lopez",
        "Gonzalez",
        "Wilson",
        "Anderson",
        "Thomas",
        "Taylor",
        "Moore",
        "Jackson",
        "Martin",
        "Lee",
        "Perez",
        "Thompson",
        "White",
        "Harris",
        "Sanchez",
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
            "birthdate": (
                datetime.now() - timedelta(days=random.randint(6570, 25550))
            ).isoformat(),
            "gender": random.choice(["male", "female", "other"]),
            "marital_status": random.choice(
                ["single", "married", "divorced", "widowed"]
            ),
            "anniversary": (
                datetime.now() - timedelta(days=random.randint(365, 10950))
            ).isoformat()
            if random.choice([True, False])
            else None,
        },
        "relationships": {
            "emails": {"data": [{"id": str(uuid4()), "type": "Email"}]},
            "phone_numbers": {"data": [{"id": str(uuid4()), "type": "PhoneNumber"}]},
            "addresses": {"data": [{"id": str(uuid4()), "type": "Address"}]},
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
        "Midweek Service",
        "Prayer Breakfast",
        "Men's Fellowship",
        "Women's Fellowship",
        "Senior Service",
        "Contemporary Service",
        "Traditional Service",
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
            "service_type_id": str(uuid4()),
        },
        "relationships": {
            "service_type": {"data": {"id": str(uuid4()), "type": "ServiceType"}},
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
        "Wedding Ceremony",
        "Funeral Service",
        "Baptism Service",
        "Communion Service",
        "Revival Meeting",
        "Concert of Prayer",
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
            "sort_date": (
                datetime.now() + timedelta(days=random.randint(1, 30))
            ).isoformat(),
            "public": random.choice([True, False]),
            "rehearsal": random.choice([True, False]),
            "notes": f"Notes for {title}",
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
        "Marriage Conference",
        "Leadership Training",
        "Volunteer Appreciation",
        "New Member Class",
        "Baptism Class",
        "Financial Peace University",
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
            "registration_opens_at": (
                datetime.now() - timedelta(days=random.randint(1, 30))
            ).isoformat(),
            "registration_closes_at": (
                datetime.now() + timedelta(days=random.randint(1, 30))
            ).isoformat(),
            "event_starts_at": (
                datetime.now() + timedelta(days=random.randint(1, 60))
            ).isoformat(),
            "event_ends_at": (
                datetime.now() + timedelta(days=random.randint(1, 65))
            ).isoformat(),
        },
    }


def generate_mock_attendee(attendee_id: Optional[str] = None, registration_id: Optional[str] = None) -> Dict[str, Any]:
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
            "registration_id": registration_id or str(uuid4()),
        },
        "relationships": {"person": {"data": {"id": person["id"], "type": "Person"}}},
    }


def generate_mock_donation(donation_id: Optional[str] = None) -> Dict[str, Any]:
    """Generate a mock donation with realistic data."""
    donation_id = donation_id or str(uuid4())

    return {
        "id": donation_id,
        "type": "Donation",
        "attributes": {
            "amount": round(random.uniform(10.0, 1000.0), 2),
            "currency": "USD",
            "donation_date": (
                datetime.now() - timedelta(days=random.randint(1, 30))
            ).isoformat(),
            "created_at": (
                datetime.now() - timedelta(days=random.randint(1, 30))
            ).isoformat(),
            "updated_at": datetime.now().isoformat(),
            "payment_method": random.choice(
                ["credit_card", "bank_account", "cash", "check"]
            ),
            "status": random.choice(["completed", "pending", "failed"]),
            "reference": f"REF-{random.randint(100000, 999999)}",
        },
        "relationships": {
            "person": {"data": {"id": str(uuid4()), "type": "Person"}},
            "fund": {"data": {"id": str(uuid4()), "type": "Fund"}},
        },
    }


def generate_mock_group(group_id: Optional[str] = None) -> Dict[str, Any]:
    """Generate a mock group with realistic data."""
    group_names = [
        "Small Group Alpha",
        "Bible Study Group",
        "Prayer Warriors",
        "Youth Group",
        "Men's Fellowship",
        "Women's Circle",
        "Senior Saints",
        "New Members Class",
        "Marriage Enrichment",
        "Financial Peace",
        "Recovery Group",
        "Missions Team",
        "Worship Team",
        "Children's Ministry",
        "Tech Team",
    ]

    group_id = group_id or str(uuid4())
    name = random.choice(group_names)

    return {
        "id": group_id,
        "type": "Group",
        "attributes": {
            "name": name,
            "description": f"A {name.lower()} for community building",
            "created_at": (
                datetime.now() - timedelta(days=random.randint(1, 365))
            ).isoformat(),
            "updated_at": datetime.now().isoformat(),
            "group_type_id": str(uuid4()),
            "campus_id": str(uuid4()),
            "status": random.choice(["active", "inactive"]),
            "member_count": random.randint(5, 50),
        },
        "relationships": {
            "group_type": {"data": {"id": str(uuid4()), "type": "GroupType"}},
            "campus": {"data": {"id": str(uuid4()), "type": "Campus"}},
        },
    }


def generate_mock_event(event_id: Optional[str] = None) -> Dict[str, Any]:
    """Generate a mock calendar event with realistic data."""
    event_names = [
        "Sunday Service",
        "Prayer Meeting",
        "Bible Study",
        "Youth Event",
        "Community Outreach",
        "Wedding",
        "Funeral",
        "Baptism",
        "Communion",
        "Special Service",
        "Concert",
        "Conference",
        "Retreat",
        "Training Session",
        "Volunteer Meeting",
    ]

    event_id = event_id or str(uuid4())
    name = random.choice(event_names)

    return {
        "id": event_id,
        "type": "Event",
        "attributes": {
            "name": name,
            "description": f"Description for {name}",
            "starts_at": (
                datetime.now() + timedelta(days=random.randint(1, 30))
            ).isoformat(),
            "ends_at": (
                datetime.now()
                + timedelta(days=random.randint(1, 30), hours=random.randint(1, 4))
            ).isoformat(),
            "created_at": (
                datetime.now() - timedelta(days=random.randint(1, 365))
            ).isoformat(),
            "updated_at": datetime.now().isoformat(),
            "public": random.choice([True, False]),
            "all_day": random.choice([True, False]),
        },
        "relationships": {
            "organization": {"data": {"id": str(uuid4()), "type": "Organization"}},
        },
    }


def generate_mock_workflow(workflow_id: Optional[str] = None) -> Dict[str, Any]:
    """Generate a mock workflow with realistic data."""
    workflow_names = [
        "New Member Process",
        "Volunteer Onboarding",
        "Pastoral Care",
        "Event Planning",
        "Ministry Application",
        "Leadership Development",
        "Discipleship Journey",
        "Missions Process",
        "Crisis Response",
        "Follow-up Process",
        "Gift Assessment",
        "Ministry Placement",
    ]

    workflow_id = workflow_id or str(uuid4())
    name = random.choice(workflow_names)

    return {
        "id": workflow_id,
        "type": "Workflow",
        "attributes": {
            "name": name,
            "description": f"Workflow for {name.lower()}",
            "created_at": (
                datetime.now() - timedelta(days=random.randint(1, 365))
            ).isoformat(),
            "updated_at": datetime.now().isoformat(),
            "workflow_category_id": str(uuid4()),
            "campus_id": str(uuid4()),
            "total_cards_count": random.randint(0, 100),
            "completed_card_count": random.randint(0, 50),
            "total_ready_card_count": random.randint(0, 25),
        },
        "relationships": {
            "workflow_category": {
                "data": {"id": str(uuid4()), "type": "WorkflowCategory"}
            },
            "campus": {"data": {"id": str(uuid4()), "type": "Campus"}},
        },
    }


def initialize_mock_data():
    """Initialize the mock data with comprehensive sample records."""
    logger.info("Initializing comprehensive mock data...")

    # Generate core data first
    for _ in range(10):
        mock_data["services"].append(generate_mock_service())

    for _ in range(50):
        mock_data["people"].append(generate_mock_person())

    for _ in range(30):
        mock_data["plans"].append(generate_mock_plan())

    for _ in range(20):
        mock_data["registrations"].append(generate_mock_registration())

    # Generate attendees linked to specific registrations
    for registration in mock_data["registrations"]:
        # Generate 2-8 attendees per registration
        num_attendees = random.randint(2, 8)
        for _ in range(num_attendees):
            mock_data["attendees"].append(
                generate_mock_attendee(registration_id=registration["id"])
            )

    # Generate additional data
    for _ in range(25):
        mock_data["donations"].append(generate_mock_donation())

    for _ in range(15):
        mock_data["groups"].append(generate_mock_group())

    for _ in range(20):
        mock_data["events"].append(generate_mock_event())

    for _ in range(10):
        mock_data["workflows"].append(generate_mock_workflow())

    # Generate supporting data
    for _ in range(5):
        mock_data["workflow_categories"].append(
            {
                "id": str(uuid4()),
                "type": "WorkflowCategory",
                "attributes": {
                    "name": random.choice(
                        [
                            "Ministry",
                            "Administration",
                            "Pastoral Care",
                            "Outreach",
                            "Discipleship",
                        ]
                    ),
                    "created_at": datetime.now().isoformat(),
                    "updated_at": datetime.now().isoformat(),
                },
            }
        )

    for _ in range(8):
        mock_data["campuses"].append(
            {
                "id": str(uuid4()),
                "type": "Campus",
                "attributes": {
                    "name": random.choice(
                        [
                            "Main Campus",
                            "North Campus",
                            "South Campus",
                            "East Campus",
                            "West Campus",
                            "Downtown Campus",
                            "Online Campus",
                            "Mobile Campus",
                        ]
                    ),
                    "created_at": datetime.now().isoformat(),
                    "updated_at": datetime.now().isoformat(),
                },
            }
        )

    for _ in range(6):
        mock_data["funds"].append(
            {
                "id": str(uuid4()),
                "type": "Fund",
                "attributes": {
                    "name": random.choice(
                        [
                            "General Fund",
                            "Missions",
                            "Building Fund",
                            "Youth Ministry",
                            "Children's Ministry",
                            "Worship Ministry",
                        ]
                    ),
                    "created_at": datetime.now().isoformat(),
                    "updated_at": datetime.now().isoformat(),
                },
            }
        )

    logger.info(
        f"Mock data initialized: {len(mock_data['people'])} people, {len(mock_data['services'])} services, "
        f"{len(mock_data['plans'])} plans, {len(mock_data['registrations'])} registrations, "
        f"{len(mock_data['attendees'])} attendees, {len(mock_data['donations'])} donations, "
        f"{len(mock_data['groups'])} groups, {len(mock_data['events'])} events, "
        f"{len(mock_data['workflows'])} workflows"
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
                or value.lower() in item["attributes"].get("name", "").lower()
                or value.lower() in item["attributes"].get("title", "").lower()
            ]
        elif key in [
            "status",
            "email",
            "phone",
            "attendance_status",
            "payment_method",
            "gender",
            "marital_status",
            "registration_id",
        ]:
            filtered = [
                item for item in filtered if item["attributes"].get(key) == value
            ]
        elif key == "service_id":
            filtered = [
                item
                for item in filtered
                if item["attributes"].get("service_id") == value
            ]
        elif key == "campus_id":
            filtered = [
                item
                for item in filtered
                if item["attributes"].get("campus_id") == value
            ]
        elif key == "workflow_category_id":
            filtered = [
                item
                for item in filtered
                if item["attributes"].get("workflow_category_id") == value
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
    logger.info("Listing comprehensive tools")
    return [
        # People API Tools
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
                    "gender": {
                        "type": "string",
                        "description": "Filter by gender (male, female, other)",
                    },
                    "marital_status": {
                        "type": "string",
                        "description": "Filter by marital status",
                    },
                },
            },
        ),
        Tool(
            name="get_workflows",
            description="Get workflows from Planning Center People (MOCK DATA)",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {
                        "type": "integer",
                        "description": "Number of workflows per page (max 100)",
                        "default": 25,
                    },
                    "offset": {
                        "type": "integer",
                        "description": "Offset for pagination",
                        "default": 0,
                    },
                    "campus_id": {
                        "type": "string",
                        "description": "Filter by campus ID",
                    },
                    "workflow_category_id": {
                        "type": "string",
                        "description": "Filter by workflow category ID",
                    },
                },
            },
        ),
        Tool(
            name="get_workflow_categories",
            description="Get workflow categories from Planning Center People (MOCK DATA)",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {
                        "type": "integer",
                        "description": "Number of categories per page (max 100)",
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
        # Services API Tools
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
                    "service_id": {
                        "type": "string",
                        "description": "Filter by service ID",
                    },
                    "public": {
                        "type": "boolean",
                        "description": "Filter by public status",
                    },
                },
            },
        ),
        # Registrations API Tools
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
            description="Get attendees from Planning Center Registrations (MOCK DATA)",
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
                        "description": "Filter by attendance status (checked_in, checked_out, registered)",
                    },
                    "registration_id": {
                        "type": "string",
                        "description": "Filter by registration/event ID to get attendees for a specific event",
                    },
                },
            },
        ),
        Tool(
            name="get_event_attendees",
            description="Get all attendees for a specific event/registration (MOCK DATA)",
            inputSchema={
                "type": "object",
                "properties": {
                    "registration_id": {
                        "type": "string",
                        "description": "Registration/event ID to get attendees for",
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
                    "attendance_status": {
                        "type": "string",
                        "description": "Filter by attendance status (checked_in, checked_out, registered)",
                    },
                },
                "required": ["registration_id"],
            },
        ),
        # Giving API Tools
        Tool(
            name="get_donations",
            description="Get donations from Planning Center Giving (MOCK DATA)",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {
                        "type": "integer",
                        "description": "Number of donations per page (max 100)",
                        "default": 25,
                    },
                    "offset": {
                        "type": "integer",
                        "description": "Offset for pagination",
                        "default": 0,
                    },
                    "payment_method": {
                        "type": "string",
                        "description": "Filter by payment method",
                    },
                    "status": {
                        "type": "string",
                        "description": "Filter by status (completed, pending, failed)",
                    },
                },
            },
        ),
        Tool(
            name="get_funds",
            description="Get funds from Planning Center Giving (MOCK DATA)",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {
                        "type": "integer",
                        "description": "Number of funds per page (max 100)",
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
        # Groups API Tools
        Tool(
            name="get_groups",
            description="Get groups from Planning Center Groups (MOCK DATA)",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {
                        "type": "integer",
                        "description": "Number of groups per page (max 100)",
                        "default": 25,
                    },
                    "offset": {
                        "type": "integer",
                        "description": "Offset for pagination",
                        "default": 0,
                    },
                    "status": {
                        "type": "string",
                        "description": "Filter by status (active, inactive)",
                    },
                    "campus_id": {
                        "type": "string",
                        "description": "Filter by campus ID",
                    },
                },
            },
        ),
        # Calendar API Tools
        Tool(
            name="get_events",
            description="Get events from Planning Center Calendar (MOCK DATA)",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {
                        "type": "integer",
                        "description": "Number of events per page (max 100)",
                        "default": 25,
                    },
                    "offset": {
                        "type": "integer",
                        "description": "Offset for pagination",
                        "default": 0,
                    },
                    "public": {
                        "type": "boolean",
                        "description": "Filter by public status",
                    },
                },
            },
        ),
        # Utility Tools
        Tool(
            name="get_campuses",
            description="Get campuses from Planning Center (MOCK DATA)",
            inputSchema={
                "type": "object",
                "properties": {
                    "per_page": {
                        "type": "integer",
                        "description": "Number of campuses per page (max 100)",
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
            name="get_mock_status",
            description="Get comprehensive status of mock data",
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
            for key in ["search", "status", "gender", "marital_status"]:
                if arguments.get(key):
                    filters[key] = arguments[key]

            filtered_people = filter_data(mock_data["people"], filters)
            result = paginate_data(
                filtered_people,
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_workflows":
            filters = {}
            for key in ["campus_id", "workflow_category_id"]:
                if arguments.get(key):
                    filters[key] = arguments[key]

            filtered_workflows = filter_data(mock_data["workflows"], filters)
            result = paginate_data(
                filtered_workflows,
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_workflow_categories":
            result = paginate_data(
                mock_data["workflow_categories"],
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
            filters = {}
            for key in ["service_id", "public"]:
                if arguments.get(key) is not None:
                    filters[key] = arguments[key]

            filtered_plans = filter_data(mock_data["plans"], filters)
            result = paginate_data(
                filtered_plans,
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
            for key in ["attendance_status", "registration_id"]:
                if arguments.get(key):
                    filters[key] = arguments[key]

            filtered_attendees = filter_data(mock_data["attendees"], filters)
            result = paginate_data(
                filtered_attendees,
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_event_attendees":
            filters = {"registration_id": arguments["registration_id"]}
            if arguments.get("attendance_status"):
                filters["attendance_status"] = arguments["attendance_status"]

            filtered_attendees = filter_data(mock_data["attendees"], filters)
            result = paginate_data(
                filtered_attendees,
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_donations":
            filters = {}
            for key in ["payment_method", "status"]:
                if arguments.get(key):
                    filters[key] = arguments[key]

            filtered_donations = filter_data(mock_data["donations"], filters)
            result = paginate_data(
                filtered_donations,
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_funds":
            result = paginate_data(
                mock_data["funds"],
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_groups":
            filters = {}
            for key in ["status", "campus_id"]:
                if arguments.get(key):
                    filters[key] = arguments[key]

            filtered_groups = filter_data(mock_data["groups"], filters)
            result = paginate_data(
                filtered_groups,
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_events":
            filters = {}
            if arguments.get("public") is not None:
                filters["public"] = arguments["public"]

            filtered_events = filter_data(mock_data["events"], filters)
            result = paginate_data(
                filtered_events,
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_campuses":
            result = paginate_data(
                mock_data["campuses"],
                arguments.get("per_page", 25),
                arguments.get("offset", 0),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_mock_status":
            result = {
                "message": "Comprehensive Mock Planning Center API Server",
                "data_counts": {k: len(v) for k, v in mock_data.items()},
                "endpoints": [
                    "get_people",
                    "get_workflows",
                    "get_workflow_categories",
                    "get_services",
                    "get_plans",
                    "get_registrations",
                    "get_attendees",
                    "get_event_attendees",
                    "get_donations",
                    "get_funds",
                    "get_groups",
                    "get_events",
                    "get_campuses",
                    "get_mock_status",
                ],
                "api_products": [
                    "People",
                    "Services",
                    "Registrations",
                    "Giving",
                    "Groups",
                    "Calendar",
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
    logger.info("Starting Comprehensive Planning Center Mock MCP Server...")

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
