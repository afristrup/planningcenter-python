"""Mock Planning Center API server for testing with fake data."""

import random
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from fastapi_mcp import FastApiMCP
from pydantic import BaseModel, Field

# Create FastAPI app for mock server
mock_app = FastAPI(
    title="Planning Center Mock API Server",
    description="Mock server for Planning Center API with fake data for testing",
    version="0.1.0"
)

# Global mock data storage
mock_data = {
    "people": [],
    "services": [],
    "plans": [],
    "registrations": [],
    "attendees": []
}


def generate_mock_person(person_id: Optional[str] = None) -> Dict[str, Any]:
    """Generate a mock person with realistic data."""
    first_names = ["John", "Jane", "Michael", "Sarah", "David", "Emily", "Robert", "Lisa", "James", "Maria"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    
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
            "created_at": (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat(),
            "updated_at": datetime.now().isoformat()
        },
        "relationships": {
            "emails": {
                "data": [
                    {
                        "id": str(uuid4()),
                        "type": "Email"
                    }
                ]
            },
            "phone_numbers": {
                "data": [
                    {
                        "id": str(uuid4()),
                        "type": "PhoneNumber"
                    }
                ]
            }
        }
    }


def generate_mock_service(service_id: Optional[str] = None) -> Dict[str, Any]:
    """Generate a mock service with realistic data."""
    service_names = [
        "Sunday Morning Service", "Evening Service", "Youth Service", 
        "Children's Service", "Prayer Meeting", "Bible Study",
        "Worship Night", "Community Service", "Special Event"
    ]
    
    service_id = service_id or str(uuid4())
    name = random.choice(service_names)
    
    return {
        "id": service_id,
        "type": "Service",
        "attributes": {
            "name": name,
            "description": f"A {name.lower()} for the community",
            "created_at": (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat(),
            "updated_at": datetime.now().isoformat()
        }
    }


def generate_mock_plan(plan_id: Optional[str] = None, service_id: Optional[str] = None) -> Dict[str, Any]:
    """Generate a mock plan with realistic data."""
    plan_titles = [
        "Sunday Service Plan", "Christmas Eve Service", "Easter Service",
        "Youth Retreat", "Community Outreach", "Prayer Meeting",
        "Bible Study Session", "Worship Night", "Special Event"
    ]
    
    plan_id = plan_id or str(uuid4())
    service_id = service_id or random.choice([s["id"] for s in mock_data["services"]]) if mock_data["services"] else str(uuid4())
    title = random.choice(plan_titles)
    
    return {
        "id": plan_id,
        "type": "Plan",
        "attributes": {
            "title": title,
            "service_id": service_id,
            "plan_date": (datetime.now() + timedelta(days=random.randint(1, 30))).isoformat(),
            "created_at": (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat(),
            "updated_at": datetime.now().isoformat()
        },
        "relationships": {
            "service": {
                "data": {
                    "id": service_id,
                    "type": "Service"
                }
            }
        }
    }


def generate_mock_registration(registration_id: Optional[str] = None) -> Dict[str, Any]:
    """Generate a mock registration with realistic data."""
    event_names = [
        "Summer Camp 2024", "Youth Retreat", "Community Picnic",
        "Christmas Party", "Easter Celebration", "Bible Study Group",
        "Prayer Meeting", "Worship Night", "Special Event"
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
            "created_at": (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat(),
            "updated_at": datetime.now().isoformat()
        }
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
            "attendance_status": random.choice(["checked_in", "checked_out", "registered"]),
            "created_at": (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat(),
            "updated_at": datetime.now().isoformat()
        },
        "relationships": {
            "person": {
                "data": {
                    "id": person["id"],
                    "type": "Person"
                }
            }
        }
    }


def initialize_mock_data():
    """Initialize the mock data with some sample records."""
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


# Request/Response Models (same as main server)
class GetPeopleRequest(BaseModel):
    """Request model for getting people."""
    per_page: Optional[int] = Field(default=25, description="Number of people per page (max 100)")
    offset: Optional[int] = Field(default=0, description="Offset for pagination")
    include: Optional[List[str]] = Field(default=None, description="Related resources to include")
    search: Optional[str] = Field(default=None, description="Search query for people")
    status: Optional[str] = Field(default=None, description="Filter by status (active, inactive)")
    email: Optional[str] = Field(default=None, description="Filter by email address")
    phone: Optional[str] = Field(default=None, description="Filter by phone number")


class GetPersonRequest(BaseModel):
    """Request model for getting a specific person."""
    person_id: str = Field(description="ID of the person to retrieve")
    include: Optional[List[str]] = Field(default=None, description="Related resources to include")


class GetServicesRequest(BaseModel):
    """Request model for getting services."""
    per_page: Optional[int] = Field(default=25, description="Number of services per page (max 100)")
    offset: Optional[int] = Field(default=0, description="Offset for pagination")
    include: Optional[List[str]] = Field(default=None, description="Related resources to include")


class GetServiceRequest(BaseModel):
    """Request model for getting a specific service."""
    service_id: str = Field(description="ID of the service to retrieve")
    include: Optional[List[str]] = Field(default=None, description="Related resources to include")


class GetPlansRequest(BaseModel):
    """Request model for getting plans."""
    service_id: Optional[str] = Field(default=None, description="Filter plans by service ID")
    per_page: Optional[int] = Field(default=25, description="Number of plans per page (max 100)")
    offset: Optional[int] = Field(default=0, description="Offset for pagination")
    include: Optional[List[str]] = Field(default=None, description="Related resources to include")


class GetPlanRequest(BaseModel):
    """Request model for getting a specific plan."""
    plan_id: str = Field(description="ID of the plan to retrieve")
    include: Optional[List[str]] = Field(default=None, description="Related resources to include")


class GetRegistrationsRequest(BaseModel):
    """Request model for getting registrations."""
    per_page: Optional[int] = Field(default=25, description="Number of registrations per page (max 100)")
    offset: Optional[int] = Field(default=0, description="Offset for pagination")
    include: Optional[List[str]] = Field(default=None, description="Related resources to include")
    status: Optional[str] = Field(default=None, description="Filter by status (open, closed)")


class GetRegistrationRequest(BaseModel):
    """Request model for getting a specific registration."""
    registration_id: str = Field(description="ID of the registration to retrieve")
    include: Optional[List[str]] = Field(default=None, description="Related resources to include")


class GetAttendeesRequest(BaseModel):
    """Request model for getting attendees."""
    per_page: Optional[int] = Field(default=25, description="Number of attendees per page (max 100)")
    offset: Optional[int] = Field(default=0, description="Offset for pagination")
    include: Optional[List[str]] = Field(default=None, description="Related resources to include")
    event_id: Optional[str] = Field(default=None, description="Filter by event ID")
    registration_instance_id: Optional[str] = Field(default=None, description="Filter by registration instance ID")
    attendance_status: Optional[str] = Field(default=None, description="Filter by attendance status (checked_in, checked_out)")


class GetAttendeeRequest(BaseModel):
    """Request model for getting a specific attendee."""
    attendee_id: str = Field(description="ID of the attendee to retrieve")
    include: Optional[List[str]] = Field(default=None, description="Related resources to include")


def filter_data(data_list: List[Dict[str, Any]], filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Apply filters to a list of data."""
    filtered = data_list
    
    for key, value in filters.items():
        if key == "search":
            filtered = [
                item for item in filtered
                if value.lower() in item["attributes"].get("first_name", "").lower() or
                   value.lower() in item["attributes"].get("last_name", "").lower() or
                   value.lower() in item["attributes"].get("full_name", "").lower()
            ]
        elif key in ["status", "email", "phone", "attendance_status"]:
            filtered = [
                item for item in filtered
                if item["attributes"].get(key) == value
            ]
        elif key == "service_id":
            filtered = [
                item for item in filtered
                if item["attributes"].get("service_id") == value
            ]
    
    return filtered


def paginate_data(data_list: List[Dict[str, Any]], per_page: int, offset: int) -> Dict[str, Any]:
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
            "offset": offset
        },
        "links": {
            "self": f"?per_page={per_page}&offset={offset}",
            "first": f"?per_page={per_page}&offset=0",
            "last": f"?per_page={per_page}&offset={max(0, total - per_page)}",
            "next": f"?per_page={per_page}&offset={end}" if end < total else None,
            "prev": f"?per_page={per_page}&offset={max(0, start - per_page)}" if start > 0 else None
        }
    }


# Mock API Endpoints
@mock_app.post("/get_people", response_model=Dict[str, Any])
async def mock_get_people(request: GetPeopleRequest) -> Dict[str, Any]:
    """Mock endpoint for getting people."""
    filters = {}
    if request.search:
        filters["search"] = request.search
    if request.status:
        filters["status"] = request.status
    if request.email:
        filters["email"] = request.email
    if request.phone:
        filters["phone"] = request.phone
    
    filtered_people = filter_data(mock_data["people"], filters)
    return paginate_data(filtered_people, request.per_page or 25, request.offset or 0)


@mock_app.post("/get_person", response_model=Dict[str, Any])
async def mock_get_person(request: GetPersonRequest) -> Dict[str, Any]:
    """Mock endpoint for getting a specific person."""
    person = next((p for p in mock_data["people"] if p["id"] == request.person_id), None)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person


@mock_app.post("/get_services", response_model=Dict[str, Any])
async def mock_get_services(request: GetServicesRequest) -> Dict[str, Any]:
    """Mock endpoint for getting services."""
    return paginate_data(mock_data["services"], request.per_page or 25, request.offset or 0)


@mock_app.post("/get_service", response_model=Dict[str, Any])
async def mock_get_service(request: GetServiceRequest) -> Dict[str, Any]:
    """Mock endpoint for getting a specific service."""
    service = next((s for s in mock_data["services"] if s["id"] == request.service_id), None)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service


@mock_app.post("/get_plans", response_model=Dict[str, Any])
async def mock_get_plans(request: GetPlansRequest) -> Dict[str, Any]:
    """Mock endpoint for getting plans."""
    filters = {}
    if request.service_id:
        filters["service_id"] = request.service_id
    
    filtered_plans = filter_data(mock_data["plans"], filters)
    return paginate_data(filtered_plans, request.per_page or 25, request.offset or 0)


@mock_app.post("/get_plan", response_model=Dict[str, Any])
async def mock_get_plan(request: GetPlanRequest) -> Dict[str, Any]:
    """Mock endpoint for getting a specific plan."""
    plan = next((p for p in mock_data["plans"] if p["id"] == request.plan_id), None)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan


@mock_app.post("/get_registrations", response_model=Dict[str, Any])
async def mock_get_registrations(request: GetRegistrationsRequest) -> Dict[str, Any]:
    """Mock endpoint for getting registrations."""
    filters = {}
    if request.status:
        filters["status"] = request.status
    
    filtered_registrations = filter_data(mock_data["registrations"], filters)
    return paginate_data(filtered_registrations, request.per_page or 25, request.offset or 0)


@mock_app.post("/get_registration", response_model=Dict[str, Any])
async def mock_get_registration(request: GetRegistrationRequest) -> Dict[str, Any]:
    """Mock endpoint for getting a specific registration."""
    registration = next((r for r in mock_data["registrations"] if r["id"] == request.registration_id), None)
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    return registration


@mock_app.post("/get_attendees", response_model=Dict[str, Any])
async def mock_get_attendees(request: GetAttendeesRequest) -> Dict[str, Any]:
    """Mock endpoint for getting attendees."""
    filters = {}
    if request.attendance_status:
        filters["attendance_status"] = request.attendance_status
    
    filtered_attendees = filter_data(mock_data["attendees"], filters)
    return paginate_data(filtered_attendees, request.per_page or 25, request.offset or 0)


@mock_app.post("/get_attendee", response_model=Dict[str, Any])
async def mock_get_attendee(request: GetAttendeeRequest) -> Dict[str, Any]:
    """Mock endpoint for getting a specific attendee."""
    attendee = next((a for a in mock_data["attendees"] if a["id"] == request.attendee_id), None)
    if not attendee:
        raise HTTPException(status_code=404, detail="Attendee not found")
    return attendee


# Additional mock endpoints for testing
@mock_app.get("/mock/reset")
async def reset_mock_data():
    """Reset mock data to initial state."""
    global mock_data
    mock_data = {
        "people": [],
        "services": [],
        "plans": [],
        "registrations": [],
        "attendees": []
    }
    initialize_mock_data()
    return {"message": "Mock data reset successfully", "counts": {k: len(v) for k, v in mock_data.items()}}


@mock_app.get("/mock/status")
async def mock_status():
    """Get status of mock data."""
    return {
        "message": "Mock Planning Center API Server",
        "data_counts": {k: len(v) for k, v in mock_data.items()},
        "endpoints": [
            "/get_people", "/get_person", "/get_services", "/get_service",
            "/get_plans", "/get_plan", "/get_registrations", "/get_registration",
            "/get_attendees", "/get_attendee"
        ]
    }


# Initialize FastAPI-MCP for mock server
mock_mcp = FastApiMCP(mock_app)
mock_mcp.mount()


def main():
    """Main entry point for the mock server."""
    # Initialize mock data
    initialize_mock_data()
    
    print("🎭 Planning Center Mock API Server")
    print("=" * 50)
    print("Mock data initialized:")
    for resource, items in mock_data.items():
        print(f"  - {resource}: {len(items)} items")
    print()
    print("Available endpoints:")
    print("  - /get_people - Get people with filtering")
    print("  - /get_person - Get specific person details")
    print("  - /get_services - Get all services")
    print("  - /get_service - Get specific service details")
    print("  - /get_plans - Get plans (optionally by service)")
    print("  - /get_plan - Get specific plan details")
    print("  - /get_registrations - Get registrations with filtering")
    print("  - /get_registration - Get specific registration details")
    print("  - /get_attendees - Get attendees with filtering")
    print("  - /get_attendee - Get specific attendee details")
    print()
    print("Mock management endpoints:")
    print("  - /mock/status - Get server status")
    print("  - /mock/reset - Reset mock data")
    print()
    print("MCP server available at: /mcp")
    print("API documentation at: /docs")


if __name__ == "__main__":
    import uvicorn
    main()
    uvicorn.run(mock_app, host="0.0.0.0", port=8001)
