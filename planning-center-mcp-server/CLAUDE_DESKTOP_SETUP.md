# Claude Desktop MCP Setup Guide

This guide explains how to set up the Planning Center MCP servers with Claude Desktop.

## 🎯 **Quick Setup (Mock Server - No Credentials Required)**

For testing and development without real API credentials:

### 1. **Update Claude Desktop Configuration**

Edit your Claude Desktop configuration file:

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Linux:** `~/.config/claude/claude_desktop_config.json`

Add this configuration:

```json
{
  "mcpServers": {
    "planning-center-mock": {
      "command": "uv",
      "args": [
        "run",
        "python",
        "mcp_mock_server.py"
      ],
      "cwd": "C:\\Users\\aksel\\Documents\\GitHub\\planningcenter-wrapper\\planning-center-mcp-server"
    }
  }
}
```

### 2. **Restart Claude Desktop**

Close and restart Claude Desktop completely.

### 3. **Test the Connection**

In Claude Desktop, you should now see Planning Center tools available. Try asking:

- "Show me some people from Planning Center"
- "Get the services available"
- "List some upcoming plans"

## 🔐 **Production Setup (Real API)**

For production use with real Planning Center API:

### 1. **Get API Credentials**

You need one of these authentication methods:

**Option A: Access Token (Recommended)**
- Get your access token from Planning Center
- Set environment variable: `PCO_ACCESS_TOKEN=your_token_here`

**Option B: App ID + Secret**
- Get your app ID and secret from Planning Center
- Set environment variables: `PCO_APP_ID=your_app_id` and `PCO_SECRET=your_secret`

### 2. **Update Claude Desktop Configuration**

```json
{
  "mcpServers": {
    "planning-center": {
      "command": "uv",
      "args": [
        "run",
        "python",
        "mcp_server.py"
      ],
      "cwd": "C:\\Users\\aksel\\Documents\\GitHub\\planningcenter-wrapper\\planning-center-mcp-server",
      "env": {
        "PCO_ACCESS_TOKEN": "your_access_token_here"
      }
    }
  }
}
```

### 3. **Restart Claude Desktop**

Close and restart Claude Desktop completely.

## 🛠 **Available Tools**

Both servers provide these tools:

### **People Management**
- `get_people` - Get people with filtering (search, status, email, phone)
- `get_person` - Get specific person details

### **Services & Plans**
- `get_services` - Get all services
- `get_service` - Get specific service details
- `get_plans` - Get plans (optionally by service)
- `get_plan` - Get specific plan details

### **Registrations & Attendees**
- `get_registrations` - Get registrations with filtering
- `get_registration` - Get specific registration details
- `get_attendees` - Get attendees with filtering
- `get_attendee` - Get specific attendee details

### **Mock Server Only**
- `reset_mock_data` - Reset mock data to initial state
- `get_mock_status` - Get status of mock data

## 🧪 **Testing Your Setup**

### **Test Mock Server**
```bash
cd planning-center-mcp-server
uv run python test_mcp_servers.py
```

### **Test Real Server**
```bash
cd planning-center-mcp-server
uv run python mcp_server.py
```

## 🔧 **Troubleshooting**

### **Server Not Connecting**

1. **Check the path** - Make sure the `cwd` path is correct
2. **Verify dependencies** - Ensure `uv` and Python are installed
3. **Check logs** - Look for error messages in Claude Desktop
4. **Test manually** - Run the server manually to verify it works

### **Common Issues**

**"Server transport closed unexpectedly"**
- Usually means the server is exiting early
- Check that all dependencies are installed
- Verify the Python path is correct

**"Configuration error"**
- Make sure environment variables are set correctly
- Check that your API credentials are valid

**"Import errors"**
- Run `uv sync` to install dependencies
- Check that the planning-center-api package is available

### **Debug Steps**

1. **Test server manually:**
   ```bash
   cd planning-center-mcp-server
   uv run python mcp_mock_server.py
   ```

2. **Check server status:**
   ```bash
   uv run python test_mcp_servers.py
   ```

3. **Verify configuration:**
   - Check the JSON syntax in your config file
   - Ensure paths are correct for your system
   - Verify environment variables are set

## 📝 **Example Usage**

Once connected, you can ask Claude things like:

- "Show me the first 5 people from Planning Center"
- "Get all services and their details"
- "Find people with 'john' in their name"
- "Show me open registrations"
- "Get attendees who are checked in"

## 🎭 **Mock vs Real Server**

### **Mock Server Benefits**
- ✅ No API credentials required
- ✅ Consistent test data
- ✅ No rate limits
- ✅ Perfect for development and testing

### **Real Server Benefits**
- ✅ Live data from your Planning Center
- ✅ Full API functionality
- ✅ Production-ready

## 🔄 **Switching Between Servers**

You can have both servers configured and switch between them by commenting/uncommenting sections in your config:

```json
{
  "mcpServers": {
    "planning-center-mock": {
      "command": "uv",
      "args": ["run", "python", "mcp_mock_server.py"],
      "cwd": "C:\\Users\\aksel\\Documents\\GitHub\\planningcenter-wrapper\\planning-center-mcp-server"
    }
    // "planning-center": {
    //   "command": "uv",
    //   "args": ["run", "python", "mcp_server.py"],
    //   "cwd": "C:\\Users\\aksel\\Documents\\GitHub\\planningcenter-wrapper\\planning-center-mcp-server",
    //   "env": {
    //     "PCO_ACCESS_TOKEN": "your_token_here"
    //   }
    // }
  }
}
```

## 📚 **Additional Resources**

- [Planning Center API Documentation](https://developer.planning.center/docs/)
- [MCP Documentation](https://modelcontextprotocol.io/)
- [Claude Desktop Documentation](https://claude.ai/desktop)

## 🆘 **Need Help?**

If you're still having issues:

1. Check the [troubleshooting section](#-troubleshooting) above
2. Review the server logs in Claude Desktop
3. Test the servers manually using the provided test scripts
4. Open an issue in the repository with your error details
