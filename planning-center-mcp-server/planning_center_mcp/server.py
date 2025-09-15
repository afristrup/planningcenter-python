"""Planning Center MCP Server using FastAPI-MCP."""

import logging
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException, Depends
from fastapi_mcp import FastApiMCP
from pydantic import BaseModel, Field

from planning_center_api import PCOClient

from .config import PCOConfig

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Planning Center MCP Server",
    description="MCP server for Planning Center API - Read-only operations",
    version="0.1.0",
)

# Global config - will be set during startup
config: Optional[PCOConfig] = None


def get_config() -> PCOConfig:
    """Dependency to get the global config."""
    if config is None:
        raise HTTPException(status_code=500, detail="Server not properly configured")
    return config


def get_pco_client(config: PCOConfig = Depends(get_config)) -> PCOClient:
    """Dependency to get a PCO client."""
    return PCOClient(
        app_id=config.app_id,
        secret=config.secret,
        access_token=config.access_token,
        webhook_secret=config.webhook_secret,
        config=config,
    )


# Request/Response Models
class GetPeopleRequest(BaseModel):
    """Request model for getting people."""

    per_page: Optional[int] = Field(
        default=25, description="Number of people per page (max 100)"
    )
    offset: Optional[int] = Field(default=0, description="Offset for pagination")
    include: Optional[List[str]] = Field(
        default=None, description="Related resources to include"
    )
    search: Optional[str] = Field(default=None, description="Search query for people")
    status: Optional[str] = Field(
        default=None, description="Filter by status (active, inactive)"
    )
    email: Optional[str] = Field(default=None, description="Filter by email address")
    phone: Optional[str] = Field(default=None, description="Filter by phone number")


class GetPersonRequest(BaseModel):
    """Request model for getting a specific person."""

    person_id: str = Field(description="ID of the person to retrieve")
    include: Optional[List[str]] = Field(
        default=None, description="Related resources to include"
    )


class GetServicesRequest(BaseModel):
    """Request model for getting services."""

    per_page: Optional[int] = Field(
        default=25, description="Number of services per page (max 100)"
    )
    offset: Optional[int] = Field(default=0, description="Offset for pagination")
    include: Optional[List[str]] = Field(
        default=None, description="Related resources to include"
    )


class GetServiceRequest(BaseModel):
    """Request model for getting a specific service."""

    service_id: str = Field(description="ID of the service to retrieve")
    include: Optional[List[str]] = Field(
        default=None, description="Related resources to include"
    )


class GetPlansRequest(BaseModel):
    """Request model for getting plans."""

    service_id: Optional[str] = Field(
        default=None, description="Filter plans by service ID"
    )
    per_page: Optional[int] = Field(
        default=25, description="Number of plans per page (max 100)"
    )
    offset: Optional[int] = Field(default=0, description="Offset for pagination")
    include: Optional[List[str]] = Field(
        default=None, description="Related resources to include"
    )


class GetPlanRequest(BaseModel):
    """Request model for getting a specific plan."""

    plan_id: str = Field(description="ID of the plan to retrieve")
    include: Optional[List[str]] = Field(
        default=None, description="Related resources to include"
    )


class GetRegistrationsRequest(BaseModel):
    """Request model for getting registrations."""

    per_page: Optional[int] = Field(
        default=25, description="Number of registrations per page (max 100)"
    )
    offset: Optional[int] = Field(default=0, description="Offset for pagination")
    include: Optional[List[str]] = Field(
        default=None, description="Related resources to include"
    )
    status: Optional[str] = Field(
        default=None, description="Filter by status (open, closed)"
    )


class GetRegistrationRequest(BaseModel):
    """Request model for getting a specific registration."""

    registration_id: str = Field(description="ID of the registration to retrieve")
    include: Optional[List[str]] = Field(
        default=None, description="Related resources to include"
    )


class GetAttendeesRequest(BaseModel):
    """Request model for getting attendees."""

    per_page: Optional[int] = Field(
        default=25, description="Number of attendees per page (max 100)"
    )
    offset: Optional[int] = Field(default=0, description="Offset for pagination")
    include: Optional[List[str]] = Field(
        default=None, description="Related resources to include"
    )
    event_id: Optional[str] = Field(default=None, description="Filter by event ID")
    registration_instance_id: Optional[str] = Field(
        default=None, description="Filter by registration instance ID"
    )
    attendance_status: Optional[str] = Field(
        default=None,
        description="Filter by attendance status (checked_in, checked_out)",
    )


class GetAttendeeRequest(BaseModel):
    """Request model for getting a specific attendee."""

    attendee_id: str = Field(description="ID of the attendee to retrieve")
    include: Optional[List[str]] = Field(
        default=None, description="Related resources to include"
    )


# FastAPI Endpoints
@app.post("/get_people", response_model=Dict[str, Any])
async def get_people(
    request: GetPeopleRequest, client: PCOClient = Depends(get_pco_client)
) -> Dict[str, Any]:
    """Get people from Planning Center People with optional filtering."""
    async with client:
        filter_params = {}
        if request.search:
            filter_params["search"] = request.search
        if request.status:
            filter_params["status"] = request.status
        if request.email:
            filter_params["email"] = request.email
        if request.phone:
            filter_params["phone"] = request.phone

        result = await client.get_people(
            per_page=request.per_page,
            offset=request.offset,
            include=request.include,
            filter_params=filter_params if filter_params else None,
        )

        return result.model_dump()


@app.post("/get_person", response_model=Dict[str, Any])
async def get_person(
    request: GetPersonRequest, client: PCOClient = Depends(get_pco_client)
) -> Dict[str, Any]:
    """Get a specific person from Planning Center People by ID."""
    async with client:
        result = await client.get_person(
            person_id=request.person_id, include=request.include
        )

        return result.model_dump()


@app.post("/get_services", response_model=Dict[str, Any])
async def get_services(
    request: GetServicesRequest, client: PCOClient = Depends(get_pco_client)
) -> Dict[str, Any]:
    """Get services from Planning Center Services."""
    async with client:
        result = await client.get_services(
            per_page=request.per_page, offset=request.offset, include=request.include
        )

        return result.model_dump()


@app.post("/get_service", response_model=Dict[str, Any])
async def get_service(
    request: GetServiceRequest, client: PCOClient = Depends(get_pco_client)
) -> Dict[str, Any]:
    """Get a specific service from Planning Center Services by ID."""
    async with client:
        result = await client.get_service(
            service_id=request.service_id, include=request.include
        )

        return result.model_dump()


@app.post("/get_plans", response_model=Dict[str, Any])
async def get_plans(
    request: GetPlansRequest, client: PCOClient = Depends(get_pco_client)
) -> Dict[str, Any]:
    """Get plans from Planning Center Services with optional service filtering."""
    async with client:
        result = await client.get_plans(
            service_id=request.service_id,
            per_page=request.per_page,
            offset=request.offset,
            include=request.include,
        )

        return result.model_dump()


@app.post("/get_plan", response_model=Dict[str, Any])
async def get_plan(
    request: GetPlanRequest, client: PCOClient = Depends(get_pco_client)
) -> Dict[str, Any]:
    """Get a specific plan from Planning Center Services by ID."""
    async with client:
        result = await client.get_plan(plan_id=request.plan_id, include=request.include)

        return result.model_dump()


@app.post("/get_registrations", response_model=Dict[str, Any])
async def get_registrations(
    request: GetRegistrationsRequest, client: PCOClient = Depends(get_pco_client)
) -> Dict[str, Any]:
    """Get registrations from Planning Center Registrations with optional status filtering."""
    async with client:
        filter_params = {}
        if request.status:
            filter_params["status"] = request.status

        result = await client.get_registrations(
            per_page=request.per_page,
            offset=request.offset,
            include=request.include,
            filter_params=filter_params if filter_params else None,
        )

        return result.model_dump()


@app.post("/get_registration", response_model=Dict[str, Any])
async def get_registration(
    request: GetRegistrationRequest, client: PCOClient = Depends(get_pco_client)
) -> Dict[str, Any]:
    """Get a specific registration from Planning Center Registrations by ID."""
    async with client:
        result = await client.get_registration(
            registration_id=request.registration_id, include=request.include
        )

        return result.model_dump()


@app.post("/get_attendees", response_model=Dict[str, Any])
async def get_attendees(
    request: GetAttendeesRequest, client: PCOClient = Depends(get_pco_client)
) -> Dict[str, Any]:
    """Get attendees from Planning Center Registrations with optional filtering."""
    async with client:
        filter_params = {}
        if request.event_id:
            filter_params["event_id"] = request.event_id
        if request.registration_instance_id:
            filter_params["registration_instance_id"] = request.registration_instance_id
        if request.attendance_status:
            filter_params["attendance_status"] = request.attendance_status

        result = await client.get_attendees(
            per_page=request.per_page,
            offset=request.offset,
            include=request.include,
            filter_params=filter_params if filter_params else None,
        )

        return result.model_dump()


@app.post("/get_attendee", response_model=Dict[str, Any])
async def get_attendee(
    request: GetAttendeeRequest, client: PCOClient = Depends(get_pco_client)
) -> Dict[str, Any]:
    """Get a specific attendee from Planning Center Registrations by ID."""
    async with client:
        result = await client.get_attendee(
            attendee_id=request.attendee_id, include=request.include
        )

        return result.model_dump()


# Initialize FastAPI-MCP
mcp = FastApiMCP(app)

# Mount the MCP server
mcp.mount()


def main():
    """Main entry point for the server."""
    global config

    # Load configuration from environment
    config = PCOConfig.from_env()

    # Validate configuration
    try:
        config.get_auth_headers()
        logger.info("✓ Configuration loaded successfully")
    except ValueError as e:
        logger.error(f"✗ Configuration error: {e}")
        logger.error(
            "Please set PCO_ACCESS_TOKEN or both PCO_APP_ID and PCO_SECRET environment variables"
        )
        return

    logger.info("Starting Planning Center MCP Server...")
    logger.info("Available endpoints:")
    logger.info("  - /get_people - Get people with filtering")
    logger.info("  - /get_person - Get specific person details")
    logger.info("  - /get_services - Get all services")
    logger.info("  - /get_service - Get specific service details")
    logger.info("  - /get_plans - Get plans (optionally by service)")
    logger.info("  - /get_plan - Get specific plan details")
    logger.info("  - /get_registrations - Get registrations with filtering")
    logger.info("  - /get_registration - Get specific registration details")
    logger.info("  - /get_attendees - Get attendees with filtering")
    logger.info("  - /get_attendee - Get specific attendee details")
    logger.info("MCP server available at: /mcp")


if __name__ == "__main__":
    import uvicorn

    main()
    uvicorn.run(app, host="0.0.0.0", port=8000)
