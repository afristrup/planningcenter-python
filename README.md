# Planning Center Python

A comprehensive, modern Python wrapper for the Planning Center API using Pydantic and async/await patterns. This library provides type-safe access to all Planning Center products including People, Services, Check-Ins, Giving, Groups, and Calendar.

## 🚀 Features

- **Type-safe** with full Pydantic models for all data structures
- **Async/await** support using httpx for modern Python patterns  
- **Webhook native** with built-in signature verification and event handling
- **All Products** supported: People, Services, Check-Ins, Giving, Groups, Calendar, Publishing, Webhooks, Organization
- **Auto-pagination** for seamless handling of large datasets
- **Rate limiting** with automatic exponential backoff
- **Comprehensive error handling** with specific exception types
- **CLI tools** for common operations
- **Utility functions** for data processing and analysis
- **MCP Server** for AI assistant integration with 80+ tools including advanced analytics

## 📦 Installation

### Core API Package

```bash
# Install with uv (recommended)
cd planning-center-api
uv pip install "planning_center_api@."

# Or with pip
cd planning-center-api
pip install .
```

### MCP Server (Optional)

For AI assistant integration:

```bash
# Install MCP server
cd planning-center-mcp-server
uv pip install "planning_center_mcp@."

# Or with pip
cd planning-center-mcp-server
pip install .
```

## 🛠 Quick Start

### Basic Usage

```python
import asyncio
from planning_center_api import PCOClient, PCOProduct

async def main():
    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        # Get all people with emails
        people = await client.get_people(include=["emails"])
        
        # Create new person
        person = await client.create_person({
            "first_name": "John",
            "last_name": "Doe"
        })
        
        # Auto-paginate through all services
        async for service in client.paginate_all(
            product=PCOProduct.SERVICES,
            resource="services"
        ):
            print(f"Service: {service.attributes.get('title')}")

asyncio.run(main())
```

### Authentication

The library supports both OAuth 2.0 and Personal Access Token authentication:

```python
# OAuth 2.0 (recommended)
client = PCOClient(access_token="your_oauth_token")

# Personal Access Token
client = PCOClient(app_id="your_app_id", secret="your_secret")
```

### Webhook Handling

```python
from fastapi import FastAPI, Request
from planning_center_api import PCOClient, handle_webhook_event

app = FastAPI()
client = PCOClient(webhook_secret="your_secret")

@app.post("/webhook")
async def webhook_handler(request: Request):
    payload = await request.body()
    signature = request.headers.get("x-pco-signature")
    
    async def person_created(webhook_payload):
        print(f"New person: {webhook_payload.resource.attributes}")
    
    await handle_webhook_event(
        client=client,
        payload=payload.decode(),
        signature=signature,
        event_handlers={"people.created": person_created}
    )
    return {"status": "success"}
```

## 📚 API Reference

### Core Client

#### `PCOClient`

Main client for Planning Center API operations.

```python
async with PCOClient(
    app_id="your_app_id",
    secret="your_secret",
    access_token="your_token",  # Alternative to app_id/secret
    webhook_secret="your_webhook_secret"
) as client:
    # Use client here
```

#### Generic CRUD Operations

```python
# Get resources
people = await client.get(PCOProduct.PEOPLE, "people")
person = await client.get(PCOProduct.PEOPLE, "people", "person_id")

# Create resources
new_person = await client.create(PCOProduct.PEOPLE, "people", {
    "first_name": "John",
    "last_name": "Doe"
})

# Update resources
updated_person = await client.update(
    PCOProduct.PEOPLE, "people", "person_id", {
        "phone": "555-123-4567"
    }
)

# Delete resources
success = await client.delete(PCOProduct.PEOPLE, "people", "person_id")
```

#### Pagination

```python
# Auto-paginate through all resources
async for person in client.paginate_all(
    product=PCOProduct.PEOPLE,
    resource="people",
    per_page=25
):
    print(person.get_full_name())
```

### Product-Specific Methods

#### People

```python
# Get people
people = await client.get_people(per_page=50, include=["emails", "phone_numbers"])
person = await client.get_person("person_id", include=["emails"])

# Search and filter
results = await client.search_people("john")
email_results = await client.get_people_by_email("john@example.com")
active_people = await client.get_active_people()

# Create and update
person = await client.create_person({
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com"
})
updated = await client.update_person("person_id", {"phone": "555-123-4567"})
```

#### Services

```python
# Get services and plans
services = await client.get_services(per_page=25)
service = await client.get_service("service_id")
plans = await client.get_plans(service_id="service_id")
plan = await client.get_plan("plan_id")
```

## 🖥 CLI Usage

The library includes a comprehensive CLI tool:

```bash
# Get people
pco-cli get --product people --resource people --per-page 10

# Search people
pco-cli search-people --query "john" --output table

# Create a person
pco-cli create --product people --resource people --data '{"first_name": "John", "last_name": "Doe"}'

# Paginate through all services
pco-cli paginate --product services --resource services --output csv

# Find by email
pco-cli find-by-email --email "john@example.com"
```

## 🤖 MCP Server for AI Assistants

The repository includes a comprehensive Model Context Protocol (MCP) server that exposes **all major Planning Center APIs** as tools for AI assistants like Claude, Cursor, and other MCP-compatible clients.

### 🚀 Features

- **Comprehensive Coverage**: 80+ read-only tools across 9 Planning Center products
- **Native MCP Integration**: Built using the official MCP protocol for seamless AI assistant integration
- **Read-only operations** for data safety
- **Mock server included** for testing without API credentials
- **Claude Desktop ready** with pre-configured setup
- **Advanced filtering** and pagination support
- **Advanced Analytics**: 10+ specialized analytics tools for data-driven insights
- **Event attendee filtering** for enhanced event management

### 📋 Available MCP Tools (80+ tools)

#### **People API** (15 tools)
- `get_people`, `get_person`, `get_person_addresses`, `get_person_emails`, `get_person_phones`, `get_person_background_checks`, `get_field_definitions`, `get_forms`, `get_form`, `get_campuses`, `get_campus`

#### **Services API** (12 tools)
- `get_services`, `get_service`, `get_plans`, `get_plan`, `get_songs`, `get_song`, `get_arrangements`, `get_arrangement`, `get_keys`, `get_key`, `get_teams`, `get_team`, `get_team_positions`, `get_team_position`

#### **Registrations API** (5 tools)
- `get_registrations`, `get_registration`, `get_attendees`, `get_attendee`, `get_event_attendees`

#### **Giving API** (10 tools)
- `get_donations`, `get_donation`, `get_funds`, `get_fund`, `get_batches`, `get_batch`, `get_pledges`, `get_pledge`, `get_pledge_campaigns`, `get_pledge_campaign`, `get_recurring_donations`, `get_recurring_donation`

#### **Groups API** (8 tools)
- `get_groups`, `get_group`, `get_group_events`, `get_group_event`, `get_group_memberships`, `get_group_membership`, `get_group_types`, `get_group_type`

#### **Calendar API** (2 tools)
- `get_calendar_events`, `get_calendar_event`

#### **Check-ins API** (4 tools)
- `get_check_in_events`, `get_check_in_event`, `get_locations`, `get_location`

#### **Publishing API** (4 tools)
- `get_channels`, `get_channel`, `get_episodes`, `get_episode`

#### **Webhooks API** (2 tools)
- `get_webhook_subscriptions`, `get_webhook_subscription`

#### **Organization API** (4 tools)
- `get_connected_applications`, `get_connected_application`, `get_oauth_applications`, `get_oauth_application`

### 🚀 Quick Start

#### **Option 1: Mock Server (No Credentials Required)**
Perfect for testing and development:

```bash
# Navigate to MCP server directory
cd planning-center-mcp-server

# Run the mock server
uv run python mcp_mock_server_comprehensive.py

# Or use the batch file
run_comprehensive_server.bat
```

#### **Option 2: Real Server (Requires API Credentials)**
For production use with real Planning Center data:

```bash
# Set up environment variables
cp env.example .env
# Edit .env with your Planning Center API credentials

# Run the real server
uv run python mcp_server_fixed.py

# Or use the batch file
run_real_server.bat
```

### 🤖 Claude Desktop Integration

The servers are pre-configured for Claude Desktop integration:

1. **Edit your Claude Desktop config**: `%APPDATA%\Claude\claude_desktop_config.json`
2. **Add server configuration** (already done if you followed the setup)
3. **Restart Claude Desktop**
4. **Start asking questions** about Planning Center data!

#### **Available in Claude Desktop**
- **Mock Server**: `planning-center-mock` (no credentials needed)
- **Real Server**: `planning-center-api` (requires API credentials)

### 💡 Usage Examples

Once configured, you can ask Claude questions like:

- *"Show me all active people in our database"*
- *"Get the attendees for Summer Camp 2024"*
- *"Find all donations from last month"*
- *"List all groups and their members"*
- *"Show me upcoming calendar events"*

### 🎭 Mock Server Features

- **14+ tools** covering the most commonly used endpoints
- **Realistic fake data** with proper relationships between entities
- **No authentication required** for testing
- **Same API structure** as the real server
- **MCP integration** for AI assistant testing

For detailed MCP server documentation, see [planning-center-mcp-server/README.md](planning-center-mcp-server/README.md).

### CLI Configuration

Set environment variables or use a config file:

```bash
export PCO_APP_ID="your_app_id"
export PCO_SECRET="your_secret"
# or
export PCO_ACCESS_TOKEN="your_token"
```

Or create a `config.json` file:

```json
{
    "app_id": "your_app_id",
    "secret": "your_secret",
    "timeout": 30.0,
    "max_retries": 3
}
```

## 🚨 Error Handling

The library provides specific exception types for different error scenarios:

```python
from planning_center_api.exceptions import (
    PCOError,
    PCOAuthenticationError,
    PCOPermissionError,
    PCONotFoundError,
    PCOValidationError,
    PCORateLimitError,
    PCOServerError
)

try:
    person = await client.get_person("invalid_id")
except PCONotFoundError:
    print("Person not found")
except PCOAuthenticationError:
    print("Authentication failed")
except PCORateLimitError as e:
    print(f"Rate limited. Retry after: {e.retry_after}")
except PCOError as e:
    print(f"API error: {e.message}")
```

## 📊 Data Models

All data is returned as Pydantic models with type safety:

```python
# Resource models
person = await client.get_person("person_id")
print(person.get_first_name())  # Type-safe access
print(person.get_email())
print(person.get_full_name())

# Collection models
people = await client.get_people()
print(len(people))  # Collection length
for person in people:  # Iterable
    print(person.get_full_name())

# Access included resources
person = await client.get_person("person_id", include=["emails"])
emails = person.get_relationship_data("emails")
```

## 🔄 Rate Limiting

The library automatically handles rate limiting with exponential backoff:

```python
# Rate limiting is handled automatically
# You can configure it in PCOConfig
config = PCOConfig(
    rate_limit_requests=100,  # Requests per window
    rate_limit_window=60,     # Window in seconds
    max_retries=3,            # Max retry attempts
    backoff_factor=2.0        # Exponential backoff factor
)
```

## 🧪 Testing

```bash
# Run tests
cd planning-center-api
pytest

# Run with coverage
pytest --cov=planning_center_api

# Run specific test file
pytest tests/test_client.py
```

## 📝 Examples

Check the `planning-center-api/examples/` directory for comprehensive examples:

- `basic_usage.py` - Basic API operations
- `webhook_server.py` - FastAPI webhook server
- `data_export.py` - Data export and analysis
- `advanced_usage.py` - Advanced patterns and utilities

## 🛠 Development

### Setup

```bash
# Clone the repository
git clone <repository-url>
cd planningcenter-wrapper

# Install development dependencies
cd planning-center-api
uv sync --group dev

# Run linting
uv run ruff check --fix planning_center_api/

# Run tests
uv run pytest
```

### Project Structure

```
planningcenter-wrapper/
├── planning-center-api/          # Core API package
│   ├── planning_center_api/      # Source code
│   ├── examples/                 # Usage examples
│   ├── tests/                    # Test suite
│   ├── docs/                     # Documentation
│   └── pyproject.toml           # Package configuration
├── planning-center-mcp-server/   # Comprehensive MCP server for AI assistants
│   ├── planning_center_mcp/      # MCP server source code
│   ├── mcp_server_fixed.py      # Real server with 65+ tools
│   ├── mcp_mock_server_comprehensive.py  # Mock server for testing
│   ├── run_real_server.bat      # Batch file for real server
│   ├── run_comprehensive_server.bat  # Batch file for mock server
│   ├── README.md                 # Comprehensive MCP server documentation
│   ├── COMPREHENSIVE_API_COVERAGE.md  # Complete API coverage documentation
│   ├── CLAUDE_DESKTOP_SETUP.md  # Claude Desktop setup guide
│   ├── QUICKSTART.md            # Quick start guide
│   └── pyproject.toml           # MCP server configuration
├── _apis/                        # API documentation
└── README.md                     # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

- Check the [examples](planning-center-api/examples/) directory
- Review the [API documentation](https://developer.planning.center/docs/)
- **MCP Server Documentation**:
  - [Comprehensive MCP Server README](planning-center-mcp-server/README.md)
  - [Complete API Coverage Guide](planning-center-mcp-server/COMPREHENSIVE_API_COVERAGE.md)
  - [Claude Desktop Setup Guide](planning-center-mcp-server/CLAUDE_DESKTOP_SETUP.md)
  - [Quick Start Guide](planning-center-mcp-server/QUICKSTART.md)
- Open an issue for bugs or feature requests

## 🔗 Links

- [Planning Center API Documentation](https://developer.planning.center/docs/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [httpx Documentation](https://www.python-httpx.org/)
- [FastAPI-MCP Documentation](https://github.com/tadata-org/fastapi_mcp)