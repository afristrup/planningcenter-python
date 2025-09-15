# Planning Center API Wrapper

A comprehensive, modern Python wrapper for the Planning Center API using Pydantic and async/await patterns. This library provides type-safe access to all Planning Center products including People, Services, Check-Ins, Giving, Groups, and Calendar.

## 🚀 Features

- **Type-safe** with full Pydantic models for all data structures
- **Async/await** support using httpx for modern Python patterns  
- **Webhook native** with built-in signature verification and event handling
- **All Products** supported: People, Services, Check-Ins, Giving, Groups, Calendar
- **Auto-pagination** for seamless handling of large datasets
- **Rate limiting** with automatic exponential backoff
- **Comprehensive error handling** with specific exception types
- **CLI tools** for common operations
- **Utility functions** for data processing and analysis

## 📦 Installation

```bash
# Install with uv (recommended)
uv add planning-center-api

# Or with pip
pip install planning-center-api
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

### Webhooks

#### `PCOWebhookHandler`

```python
from planning_center_api import PCOWebhookHandler, WebhookEventTypes

handler = PCOWebhookHandler(config)

# Register event handlers
handler.register_handler(WebhookEventTypes.PEOPLE_CREATED, person_created_handler)
handler.register_handler(WebhookEventTypes.PEOPLE_UPDATED, person_updated_handler)

# Handle webhook
result = await handler.handle_webhook(payload, signature)
```

#### Event Types

```python
from planning_center_api import WebhookEventTypes

# People events
WebhookEventTypes.PEOPLE_CREATED
WebhookEventTypes.PEOPLE_UPDATED
WebhookEventTypes.PEOPLE_DELETED

# Email events
WebhookEventTypes.EMAILS_CREATED
WebhookEventTypes.EMAILS_UPDATED
WebhookEventTypes.EMAILS_DELETED

# And many more...
```

### Utilities

#### Data Export

```python
from planning_center_api.utils import PCODataExporter

exporter = PCODataExporter(client)
people_data = await exporter.export_people_to_dict(include=["emails", "phone_numbers"])
```

#### Data Analysis

```python
from planning_center_api.utils import PCODataAnalyzer

analyzer = PCODataAnalyzer(client)
stats = await analyzer.get_people_stats()
print(f"Total people: {stats['total_people']}")
print(f"Active percentage: {stats['active_percentage']:.1f}%")
```

#### Batch Processing

```python
from planning_center_api.utils import PCOBatchProcessor

processor = PCOBatchProcessor(client, batch_size=100)

async def process_person(person):
    return {"id": person.id, "name": person.get_full_name()}

results = await processor.process_people_batch(processor=process_person)
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

## 🔧 Configuration

### `PCOConfig`

```python
from planning_center_api import PCOConfig

config = PCOConfig(
    app_id="your_app_id",
    secret="your_secret",
    access_token="your_token",
    webhook_secret="your_webhook_secret",
    timeout=30.0,
    max_retries=3,
    retry_delay=1.0,
    backoff_factor=2.0,
    rate_limit_requests=100,
    rate_limit_window=60,
    default_per_page=25,
    max_per_page=100
)
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
pytest

# Run with coverage
pytest --cov=planning_center_api

# Run specific test file
pytest tests/test_client.py
```

## 📝 Examples

Check the `examples/` directory for comprehensive examples:

- `basic_usage.py` - Basic API operations
- `webhook_server.py` - FastAPI webhook server
- `data_export.py` - Data export and analysis
- `advanced_usage.py` - Advanced patterns and utilities

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

- Check the [examples](examples/) directory
- Review the [API documentation](https://developer.planning.center/docs/)
- Open an issue for bugs or feature requests

## 🔗 Links

- [Planning Center API Documentation](https://developer.planning.center/docs/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [httpx Documentation](https://www.python-httpx.org/)
