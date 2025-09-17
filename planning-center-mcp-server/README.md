# Planning Center MCP Server

A comprehensive Model Context Protocol (MCP) server that provides read-only access to **all major Planning Center APIs**. This server exposes Planning Center data through 80+ MCP tools, including advanced analytics and workflow tools, allowing AI assistants to interact with your Planning Center data safely across all products.

## 🚀 Features

- **Comprehensive Coverage**: 80+ read-only tools across 9 Planning Center products
- **Native MCP Integration**: Built using the official MCP protocol for seamless AI assistant integration
- **Read-only operations**: All endpoints are designed for data retrieval only, ensuring data safety
- **Multiple Planning Center products**: Support for People, Services, Registrations, Giving, Groups, Calendar, Check-ins, Publishing, Webhooks, and Organization
- **Flexible authentication**: Supports both OAuth tokens and app ID/secret authentication
- **Advanced filtering**: Comprehensive filtering options for all endpoints
- **Pagination support**: Built-in pagination for large datasets
- **Mock server included**: Full testing environment with realistic fake data
- **Advanced Analytics**: 10+ specialized analytics tools for data-driven insights
- **Claude Desktop ready**: Pre-configured for immediate use with Claude Desktop

## 📋 Available MCP Tools

The server provides **80+ MCP tools** across all major Planning Center products:

### 👥 **People API** (15 tools)
- `get_people` - Get people with filtering (search, status, gender, marital status)
- `get_person` - Get specific person details
- `get_person_addresses` - Get addresses for a person
- `get_person_emails` - Get email addresses for a person
- `get_person_phones` - Get phone numbers for a person
- `get_person_background_checks` - Get background checks for a person
- `get_field_definitions` - Get field definitions
- `get_forms` - Get forms
- `get_form` - Get specific form
- `get_campuses` - Get campuses
- `get_campus` - Get specific campus

### 🎵 **Services API** (12 tools)
- `get_services` - Get services
- `get_service` - Get specific service
- `get_plans` - Get plans
- `get_plan` - Get specific plan
- `get_songs` - Get songs
- `get_song` - Get specific song
- `get_arrangements` - Get arrangements for a song
- `get_arrangement` - Get specific arrangement
- `get_keys` - Get keys
- `get_key` - Get specific key
- `get_teams` - Get teams
- `get_team` - Get specific team
- `get_team_positions` - Get team positions
- `get_team_position` - Get specific team position

### 📝 **Registrations API** (5 tools)
- `get_registrations` - Get registrations
- `get_registration` - Get specific registration
- `get_attendees` - Get attendees with filtering
- `get_attendee` - Get specific attendee
- `get_event_attendees` - Get attendees for specific event (convenience tool)

### 💰 **Giving API** (10 tools)
- `get_donations` - Get donations
- `get_donation` - Get specific donation
- `get_funds` - Get funds
- `get_fund` - Get specific fund
- `get_batches` - Get batches
- `get_batch` - Get specific batch
- `get_pledges` - Get pledges
- `get_pledge` - Get specific pledge
- `get_pledge_campaigns` - Get pledge campaigns
- `get_pledge_campaign` - Get specific pledge campaign
- `get_recurring_donations` - Get recurring donations
- `get_recurring_donation` - Get specific recurring donation

### 👥 **Groups API** (8 tools)
- `get_groups` - Get groups
- `get_group` - Get specific group
- `get_group_events` - Get events for a group
- `get_group_event` - Get specific group event
- `get_group_memberships` - Get memberships for a group
- `get_group_membership` - Get specific group membership
- `get_group_types` - Get group types
- `get_group_type` - Get specific group type

### 📅 **Calendar API** (2 tools)
- `get_calendar_events` - Get calendar events
- `get_calendar_event` - Get specific calendar event

### ✅ **Check-ins API** (25+ tools)
**Core Endpoints:**
- `get_check_in_events` - Get check-in events
- `get_check_in_event` - Get specific check-in event
- `get_locations` - Get locations
- `get_location` - Get specific location
- `get_attendance_types` - Get attendance types
- `get_attendance_type` - Get specific attendance type
- `get_check_ins` - Get check-ins
- `get_check_in` - Get specific check-in
- `get_check_in_groups` - Get check-in groups
- `get_check_in_group` - Get specific check-in group
- `get_check_in_times` - Get check-in times
- `get_check_in_time` - Get specific check-in time
- `get_event_periods` - Get event periods
- `get_event_period` - Get specific event period
- `get_event_times` - Get event times
- `get_event_time` - Get specific event time
- `get_headcounts` - Get headcounts
- `get_headcount` - Get specific headcount
- `get_integration_links` - Get integration links
- `get_integration_link` - Get specific integration link
- `get_labels` - Get labels
- `get_label` - Get specific label
- `get_options` - Get options
- `get_option` - Get specific option
- `get_check_ins_organization` - Get organization
- `get_passes` - Get passes
- `get_pass` - Get specific pass
- `get_check_ins_people` - Get people
- `get_check_ins_person` - Get specific person
- `get_person_events` - Get person events
- `get_person_event` - Get specific person event
- `get_stations` - Get stations
- `get_station` - Get specific station
- `get_themes` - Get themes
- `get_theme` - Get specific theme

**Advanced Analytics & Workflow Tools:**
- `get_volunteer_count_for_date` - Get volunteer counts for specific dates
- `get_attendance_summary_for_event` - Comprehensive event attendance analysis
- `get_weekly_attendance_trends` - Attendance trends over time
- `get_station_utilization_report` - Check-in station efficiency analysis
- `get_family_check_in_patterns` - Family attendance analysis
- `get_volunteer_availability_report` - Volunteer scheduling insights
- `get_attendance_by_demographics` - Demographic breakdowns
- `get_event_capacity_analysis` - Capacity utilization analysis
- `get_check_in_efficiency_metrics` - Operational efficiency metrics
- `get_volunteer_roster_for_date` - Complete volunteer rosters
- `get_attendance_anomalies` - Unusual pattern detection

### 📺 **Publishing API** (4 tools)
- `get_channels` - Get channels
- `get_channel` - Get specific channel
- `get_episodes` - Get episodes
- `get_episode` - Get specific episode

### 🔗 **Webhooks API** (2 tools)
- `get_webhook_subscriptions` - Get webhook subscriptions
- `get_webhook_subscription` - Get specific webhook subscription

### 🏢 **Organization API** (4 tools)
- `get_connected_applications` - Get connected applications
- `get_connected_application` - Get specific connected application
- `get_oauth_applications` - Get OAuth applications
- `get_oauth_application` - Get specific OAuth application

## 📊 Advanced Analytics & Workflow Tools

The server includes **10+ specialized analytics tools** designed to answer common data-driven questions and support team workflows:

### 🎯 **Volunteer Management**
- **`get_volunteer_count_for_date`** - Answer "How many volunteers on a given Sunday?"
- **`get_volunteer_roster_for_date`** - Get complete volunteer rosters with contact info
- **`get_volunteer_availability_report`** - Analyze volunteer scheduling patterns

### 📈 **Attendance Analytics**
- **`get_attendance_summary_for_event`** - Comprehensive event attendance analysis
- **`get_weekly_attendance_trends`** - Track attendance trends over time
- **`get_attendance_by_demographics`** - Break down attendance by age, family status, location
- **`get_attendance_anomalies`** - Detect unusual attendance patterns

### 🏢 **Operational Insights**
- **`get_station_utilization_report`** - Analyze check-in station efficiency
- **`get_check_in_efficiency_metrics`** - Measure processing speed and bottlenecks
- **`get_event_capacity_analysis`** - Identify overcrowding or underutilization

### 👨‍👩‍👧‍👦 **Family & Community Analysis**
- **`get_family_check_in_patterns`** - Understand family attendance dynamics

### 💡 **Common Use Cases**
These tools directly answer questions like:
- "How many volunteers do we have this Sunday?"
- "What's our attendance trend over the past month?"
- "Which check-in stations are most efficient?"
- "Are there any unusual attendance patterns we should investigate?"
- "What's our family attendance breakdown?"
- "How is our event capacity utilization?"

## 🚀 Quick Start

### **Option 1: Mock Server (No Credentials Required)**
Perfect for testing and development:

```bash
# Run the mock server
uv run python mcp_mock_server_comprehensive.py

# Or use the batch file
run_comprehensive_server.bat
```

### **Option 2: Real Server (Requires API Credentials)**
For production use with real Planning Center data:

```bash
# Set up environment variables first
cp env.example .env
# Edit .env with your credentials

# Run the real server
uv run python mcp_server_fixed.py

# Or use the batch file
run_real_server.bat
```

## 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd planning-center-mcp-server
   ```

2. **Install dependencies**:
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -r requirements.txt
   ```

## 🔑 Configuration

### **Environment Variables**

Copy `env.example` to `.env` and configure your Planning Center API credentials:

```bash
cp env.example .env
```

Edit `.env` with your credentials:

```env
# Option 1: OAuth Access Token (recommended)
PCO_ACCESS_TOKEN=your_access_token_here

# Option 2: Application ID and Secret
PCO_APP_ID=your_app_id_here
PCO_SECRET=your_secret_here

# Optional: Custom base URL
PCO_BASE_URL=https://api.planningcenteronline.com
```

### **Authentication Methods**

#### **OAuth Access Token (Recommended)**
1. Go to your Planning Center account settings
2. Navigate to "API Access" or "Personal Access Tokens"
3. Create a new token with appropriate permissions
4. Set the `PCO_ACCESS_TOKEN` environment variable

#### **Application ID and Secret**
1. Create a new application in Planning Center
2. Note the Application ID and Secret
3. Set both `PCO_APP_ID` and `PCO_SECRET` environment variables

## 🤖 Claude Desktop Integration

The servers are pre-configured for Claude Desktop integration:

### **Quick Setup**
1. **Edit your Claude Desktop config**: `%APPDATA%\Claude\claude_desktop_config.json`
2. **Add server configuration** (already done if you followed the setup)
3. **Restart Claude Desktop**
4. **Start asking questions** about Planning Center data!

### **Available in Claude Desktop**
- **Mock Server**: `planning-center-mock` (no credentials needed)
- **Real Server**: `planning-center-api` (requires API credentials)

**Full setup guide**: See [CLAUDE_DESKTOP_SETUP.md](CLAUDE_DESKTOP_SETUP.md) for detailed instructions.

## 💡 Usage Examples

### **Claude Desktop Examples**

Once configured, you can ask Claude questions like:

- *"Show me all active people in our database"*
- *"Get the attendees for Summer Camp 2024"*
- *"Find all donations from last month"*
- *"List all groups and their members"*
- *"Show me upcoming calendar events"*

### **MCP Tool Examples**

#### **Get People with Filtering**
```json
{
  "tool": "get_people",
  "arguments": {
    "per_page": 10,
    "search": "john",
    "status": "active",
    "gender": "male"
  }
}
```

#### **Get Event Attendees**
```json
{
  "tool": "get_event_attendees",
  "arguments": {
    "registration_id": "12345",
    "per_page": 25,
    "attendance_status": "checked_in"
  }
}
```

#### **Get Donations by Fund**
```json
{
  "tool": "get_donations",
  "arguments": {
    "fund_id": "67890",
    "per_page": 50,
    "payment_status": "succeeded"
  }
}
```

#### **Get Group Memberships**
```json
{
  "tool": "get_group_memberships",
  "arguments": {
    "group_id": "54321",
    "role": "leader",
    "per_page": 20
  }
}
```

### **Advanced Filtering Examples**

#### **People API**
- Search by name: `"search": "john"`
- Filter by status: `"status": "active"`
- Filter by gender: `"gender": "male"`
- Filter by marital status: `"marital_status": "married"`

#### **Services API**
- Filter plans by service: `"service_id": "12345"`
- Get team positions: `"team_id": "67890"`

#### **Registrations API**
- Filter by event: `"event_id": "12345"`
- Filter by registration: `"registration_instance_id": "67890"`
- Filter by attendance: `"attendance_status": "checked_in"`

#### **Giving API**
- Filter by person: `"person_id": "12345"`
- Filter by fund: `"fund_id": "67890"`
- Filter by payment method: `"payment_method": "credit_card"`
- Filter by status: `"payment_status": "succeeded"`

#### **Groups API**
- Filter by group type: `"group_type_id": "12345"`
- Filter by campus: `"campus_id": "67890"`
- Filter by role: `"role": "leader"`

#### **Calendar API**
- Filter by date range: `"start_date": "2024-01-01", "end_date": "2024-12-31"`
- Filter by approval: `"approval_status": "approved"`

## 🎭 Mock Server for Testing

The comprehensive mock server provides realistic fake data for testing and development:

### **Features**
- **14+ tools** covering the most commonly used endpoints
- **Realistic fake data** with proper relationships between entities
- **No authentication required** for testing
- **Same API structure** as the real server
- **MCP integration** for AI assistant testing

### **Available Mock Tools**
- `get_people` - Get people with filtering
- `get_workflows` - Get workflows
- `get_workflow_categories` - Get workflow categories
- `get_services` - Get services
- `get_plans` - Get plans
- `get_registrations` - Get registrations
- `get_attendees` - Get attendees with filtering
- `get_event_attendees` - Get attendees for specific event
- `get_donations` - Get donations
- `get_funds` - Get funds
- `get_groups` - Get groups
- `get_events` - Get events
- `get_campuses` - Get campuses
- `get_mock_status` - Get server status

### **Running the Mock Server**
```bash
# Run the comprehensive mock server
uv run python mcp_mock_server_comprehensive.py

# Or use the batch file
run_comprehensive_server.bat

# Test the mock server
uv run python test_comprehensive_server.py
```

**Documentation**: See [MOCK_SERVER.md](MOCK_SERVER.md) for detailed information.

## 📊 Comprehensive API Coverage

This MCP server provides **complete coverage** of all major Planning Center API products:

### **Coverage Statistics**
- **Total Tools**: 65+ read-only tools
- **API Products**: 9 (People, Services, Registrations, Giving, Groups, Calendar, Check-ins, Publishing, Webhooks, Organization)
- **Mock Server Tools**: 14 (covering most common use cases)
- **Authentication**: Real server requires Planning Center credentials, mock server requires none

### **Key Features**
- **Consistent API Design**: All tools follow the same parameter structure
- **Advanced Filtering**: Comprehensive filtering options for all endpoints
- **Event Attendee Filtering**: Enhanced filtering for event-specific attendee queries
- **Proper Relationships**: Mock data includes realistic relationships between entities
- **Production Ready**: Full error handling, logging, and rate limiting

**Detailed Coverage**: See [COMPREHENSIVE_API_COVERAGE.md](COMPREHENSIVE_API_COVERAGE.md) for complete documentation.

## API Reference

### Common Parameters

- `per_page`: Number of items per page (default: 25, max: 100)
- `offset`: Offset for pagination (default: 0)
- `include`: List of related resources to include in the response

### People Tools

#### get_people
- `search`: Search query for people names or emails
- `status`: Filter by status ("active" or "inactive")
- `email`: Filter by specific email address
- `phone`: Filter by specific phone number

#### get_person
- `person_id`: ID of the person to retrieve
- `include`: Related resources to include

### Services Tools

#### get_services
- Standard pagination parameters

#### get_service
- `service_id`: ID of the service to retrieve
- `include`: Related resources to include

#### get_plans
- `service_id`: Filter plans by service ID
- Standard pagination parameters

#### get_plan
- `plan_id`: ID of the plan to retrieve
- `include`: Related resources to include

### Registrations Tools

#### get_registrations
- `status`: Filter by status ("open" or "closed")
- Standard pagination parameters

#### get_registration
- `registration_id`: ID of the registration to retrieve
- `include`: Related resources to include

#### get_attendees
- `event_id`: Filter by event ID
- `registration_instance_id`: Filter by registration instance ID
- `attendance_status`: Filter by attendance status ("checked_in" or "checked_out")
- Standard pagination parameters

#### get_attendee
- `attendee_id`: ID of the attendee to retrieve
- `include`: Related resources to include

## Error Handling

The server includes comprehensive error handling for:
- Authentication failures
- Invalid parameters
- API rate limiting
- Network connectivity issues
- Invalid resource IDs

## Security Considerations

- **Read-only access**: This server only provides read access to Planning Center data
- **Environment variables**: Credentials are loaded from environment variables, not hardcoded
- **Input validation**: All input parameters are validated before making API calls
- **Rate limiting**: Built-in respect for Planning Center API rate limits

## Development

### Project Structure

```
planning-center-mcp-server/
├── planning_center_mcp/
│   ├── __init__.py
│   ├── config.py          # Configuration management
│   ├── client.py          # Planning Center API client
│   ├── tools.py           # MCP tool definitions
│   └── server.py          # MCP server setup
├── main.py                # Entry point
├── requirements.txt       # Dependencies
├── pyproject.toml         # Project configuration
├── env.example           # Environment variables example
└── README.md             # This file
```

### Adding New Tools

1. Define request models in `tools.py`
2. Implement the tool handler function
3. Register the tool in the `create_tools()` function
4. Update this README with the new tool documentation

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues and questions:
1. Check the Planning Center API documentation
2. Verify your authentication credentials
3. Check the server logs for detailed error messages
4. Open an issue in this repository
