# Quick Start Guide

## 1. Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

## 2. Configuration

Copy the environment example file:
```bash
cp env.example .env
```

Edit `.env` with your Planning Center credentials:
```env
PCO_ACCESS_TOKEN=your_access_token_here
```

## 3. Test Connection

```bash
python test_connection.py
```

## 4. Run the Server

```bash
python run_server.py
```

The server will start at `http://localhost:8000`

## 5. Access Documentation

Visit `http://localhost:8000/docs` for interactive Swagger UI documentation.

## 6. MCP Integration

The MCP server is available at `http://localhost:8000/mcp`

## Available Endpoints

The server provides these FastAPI endpoints (automatically converted to MCP tools):

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

## Authentication

You need either:
- **OAuth Access Token** (recommended): Set `PCO_ACCESS_TOKEN`
- **App ID + Secret**: Set `PCO_APP_ID` and `PCO_SECRET`

Get these from your Planning Center account settings.

## Example Usage

```bash
# Test the API directly
curl -X POST "http://localhost:8000/get_people" \
  -H "Content-Type: application/json" \
  -d '{"per_page": 5}'
```

## 🎭 Mock Server (No Credentials Required)

For testing without real API credentials:

```bash
# Run the mock server
python run_mock_server.py

# Test the mock server
python test_mock_server.py
```

**Mock server**: `http://localhost:8001`
**MCP endpoint**: `http://localhost:8001/mcp`
**Documentation**: `http://localhost:8001/docs`
