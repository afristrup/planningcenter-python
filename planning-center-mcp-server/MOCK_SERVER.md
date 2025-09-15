# Planning Center Mock API Server

A mock server that provides fake Planning Center data for testing and development. This server mimics the real Planning Center API endpoints with realistic test data, allowing you to develop and test your applications without needing real API credentials.

## 🎭 Features

- **Realistic fake data** with proper data structures and relationships
- **All main endpoints** from the real Planning Center API
- **Filtering and pagination** support
- **MCP integration** for AI assistant testing
- **Easy data management** with reset and status endpoints
- **No authentication required** for testing

## 🚀 Quick Start

### 1. Run the Mock Server

```bash
# Run the mock server
python run_mock_server.py
```

The server will start on `http://localhost:8001`

### 2. Test the Server

```bash
# Run the test script
python test_mock_server.py
```

### 3. Access Documentation

Visit `http://localhost:8001/docs` for interactive Swagger UI documentation.

## 📊 Available Data

The mock server provides realistic test data for:

- **20 People** with names, emails, phone numbers, and status
- **5 Services** with different service types
- **10 Plans** linked to services
- **8 Registrations** with various statuses
- **15 Attendees** with different attendance statuses

## 🔧 Available Endpoints

### Core API Endpoints

All endpoints match the real Planning Center API structure:

- `POST /get_people` - Get people with filtering
- `POST /get_person` - Get specific person details
- `POST /get_services` - Get all services
- `POST /get_service` - Get specific service details
- `POST /get_plans` - Get plans (optionally by service)
- `POST /get_plan` - Get specific plan details
- `POST /get_registrations` - Get registrations with filtering
- `POST /get_registration` - Get specific registration details
- `POST /get_attendees` - Get attendees with filtering
- `POST /get_attendee` - Get specific attendee details

### Mock Management Endpoints

- `GET /mock/status` - Get server status and data counts
- `GET /mock/reset` - Reset all mock data to initial state

### MCP Integration

- `GET /mcp` - MCP server endpoint for AI assistants

## 🧪 Testing Examples

### Get People with Filtering

```bash
curl -X POST "http://localhost:8001/get_people" \
  -H "Content-Type: application/json" \
  -d '{
    "per_page": 5,
    "search": "john",
    "status": "active"
  }'
```

### Get Services

```bash
curl -X POST "http://localhost:8001/get_services" \
  -H "Content-Type: application/json" \
  -d '{
    "per_page": 10
  }'
```

### Get Plans by Service

```bash
curl -X POST "http://localhost:8001/get_plans" \
  -H "Content-Type: application/json" \
  -d '{
    "service_id": "service_id_here",
    "per_page": 5
  }'
```

### Get Open Registrations

```bash
curl -X POST "http://localhost:8001/get_registrations" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "open",
    "per_page": 10
  }'
```

### Get Checked-in Attendees

```bash
curl -X POST "http://localhost:8001/get_attendees" \
  -H "Content-Type: application/json" \
  -d '{
    "attendance_status": "checked_in",
    "per_page": 10
  }'
```

## 🔄 Data Management

### Check Server Status

```bash
curl http://localhost:8001/mock/status
```

Response:
```json
{
  "message": "Mock Planning Center API Server",
  "data_counts": {
    "people": 20,
    "services": 5,
    "plans": 10,
    "registrations": 8,
    "attendees": 15
  },
  "endpoints": [...]
}
```

### Reset Mock Data

```bash
curl http://localhost:8001/mock/reset
```

This will regenerate all mock data with new random values.

## 🤖 MCP Integration

The mock server is fully compatible with MCP (Model Context Protocol) and can be used to test AI assistant integrations:

1. **Start the mock server**: `python run_mock_server.py`
2. **Configure your MCP client** to connect to `http://localhost:8001/mcp`
3. **Test AI assistant interactions** with realistic Planning Center data

## 🛠 Development

### Adding New Mock Data

To add more realistic data, modify the `initialize_mock_data()` function in `mock_server.py`:

```python
def initialize_mock_data():
    # Add more services
    for _ in range(10):  # Increase from 5 to 10
        mock_data["services"].append(generate_mock_service())
    
    # Add more people
    for _ in range(50):  # Increase from 20 to 50
        mock_data["people"].append(generate_mock_person())
```

### Customizing Data Generation

Modify the generator functions to create more specific test data:

```python
def generate_mock_person(person_id: Optional[str] = None) -> Dict[str, Any]:
    # Add your custom logic here
    # For example, specific names, emails, etc.
```

### Adding New Endpoints

Add new endpoints by following the existing pattern:

```python
@mock_app.post("/get_new_resource", response_model=Dict[str, Any])
async def mock_get_new_resource(request: NewResourceRequest) -> Dict[str, Any]:
    # Your implementation here
    pass
```

## 🎯 Use Cases

### 1. **Development Testing**
- Test your application logic without API rate limits
- Develop offline when Planning Center API is unavailable
- Test error handling and edge cases

### 2. **CI/CD Pipelines**
- Run automated tests without real API credentials
- Test API integrations in isolated environments
- Validate data processing logic

### 3. **AI Assistant Development**
- Test MCP integrations with realistic data
- Develop and debug AI assistant workflows
- Prototype new features without API costs

### 4. **Demo and Presentations**
- Showcase your application with consistent test data
- Demonstrate features without exposing real data
- Create reproducible demos

## 🔍 Data Structure

The mock data follows the same structure as the real Planning Center API:

```json
{
  "data": [
    {
      "id": "uuid",
      "type": "Person",
      "attributes": {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "status": "active"
      },
      "relationships": {
        "emails": {"data": [...]},
        "phone_numbers": {"data": [...]}
      }
    }
  ],
  "meta": {
    "total": 20,
    "count": 5,
    "per_page": 5,
    "offset": 0
  },
  "links": {
    "self": "?per_page=5&offset=0",
    "next": "?per_page=5&offset=5"
  }
}
```

## 🚨 Limitations

- **No real data**: All data is generated and not connected to real Planning Center accounts
- **No write operations**: Only read operations are supported
- **No authentication**: No real authentication or authorization
- **Limited relationships**: Some complex relationships may not be fully modeled

## 🤝 Contributing

To improve the mock server:

1. Add more realistic data generators
2. Implement additional endpoints
3. Add more sophisticated filtering
4. Improve data relationships
5. Add error simulation capabilities

## 📄 License

This mock server is part of the Planning Center Python project and follows the same MIT License.
