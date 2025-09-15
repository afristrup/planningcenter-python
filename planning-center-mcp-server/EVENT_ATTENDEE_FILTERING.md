# Event Attendee Filtering Enhancement

## Overview

Both the mock and real Planning Center MCP servers now support enhanced attendee filtering functionality, making it easy to get attendees for specific events or registrations.

## Features Added

### Mock Server (`mcp_mock_server_comprehensive.py`)

1. **Enhanced `get_attendees` tool**:
   - Added `registration_id` filter parameter
   - Can now filter attendees by specific registration/event ID

2. **New `get_event_attendees` tool**:
   - Convenience tool specifically for getting attendees by event
   - Requires either `registration_id` parameter
   - Supports all standard filtering and pagination options

3. **Improved mock data generation**:
   - Attendees are now properly linked to registrations
   - Each registration has 2-8 associated attendees
   - Realistic data relationships for testing

### Real Server (`mcp_server_fixed.py`)

1. **New `get_event_attendees` tool**:
   - Convenience tool for filtering attendees by event
   - Supports both `event_id` and `registration_instance_id` parameters
   - Uses `anyOf` validation to require one of these parameters
   - Includes all standard Planning Center API options

2. **Enhanced functionality**:
   - Leverages existing `get_attendees` tool with proper filters
   - Supports `attendance_status` filtering (checked_in, checked_out)
   - Full pagination support with `per_page` and `offset`
   - Related resource inclusion with `include` parameter

## Usage Examples

### Mock Server

```python
# Get attendees for a specific registration
get_event_attendees(registration_id="some-registration-id")

# Get only checked-in attendees for an event
get_event_attendees(
    registration_id="some-registration-id",
    attendance_status="checked_in"
)

# Paginate through attendees
get_event_attendees(
    registration_id="some-registration-id",
    per_page=10,
    offset=20
)
```

### Real Server

```python
# Get attendees for a specific event
get_event_attendees(event_id="some-event-id")

# Get attendees for a specific registration instance
get_event_attendees(registration_instance_id="some-registration-instance-id")

# Get only checked-in attendees with pagination
get_event_attendees(
    event_id="some-event-id",
    attendance_status="checked_in",
    per_page=25,
    offset=0
)

# Include related resources
get_event_attendees(
    event_id="some-event-id",
    include=["person", "registration"]
)
```

## Benefits

1. **Easier Event Management**: Quickly get all attendees for a specific event
2. **Better Filtering**: Filter by attendance status within events
3. **Consistent API**: Same interface for both mock and real servers
4. **Full Feature Support**: All standard Planning Center API features available
5. **Realistic Testing**: Mock server now has proper data relationships

## Technical Implementation

- **Mock Server**: Enhanced data generation and filtering logic
- **Real Server**: Convenience wrapper around existing `get_attendees` functionality
- **Validation**: Proper schema validation with `anyOf` requirements
- **Error Handling**: Consistent error handling across both servers
- **Documentation**: Clear parameter descriptions and usage examples

## Testing

Both servers have been tested to ensure:
- ✅ Tools are properly registered
- ✅ Schema validation works correctly
- ✅ Server startup and initialization
- ✅ MCP protocol compliance
- ✅ Claude Desktop integration compatibility

The functionality is now available in both the comprehensive mock server and the real Planning Center MCP server, providing a consistent and powerful way to manage event attendees.
