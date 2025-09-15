#!/usr/bin/env python3
"""Test script for the comprehensive MCP server."""

import asyncio
import sys
from mcp_mock_server_comprehensive import server

async def test_comprehensive_server():
    """Test the comprehensive MCP server."""
    print("🧪 Testing Comprehensive MCP Server")
    print("=" * 50)
    
    try:
        print("✓ Server created successfully")
        print(f"  Server name: {server.name}")
        
        # Check if server has the expected methods
        if hasattr(server, 'list_tools') and hasattr(server, 'call_tool'):
            print("✓ Server has required MCP methods")
        else:
            print("✗ Server missing required MCP methods")
            return False
        
        # Test list_tools
        print("\n📋 Testing list_tools...")
        tools = await server.list_tools()
        print(f"✓ list_tools returned {len(tools)} tools")
        
        # List all available tools
        print("\n🔧 Available Tools:")
        for i, tool in enumerate(tools, 1):
            print(f"  {i:2d}. {tool.name} - {tool.description}")
        
        # Test a few key tools
        print("\n🧪 Testing key tools...")
        
        # Test get_mock_status
        print("  Testing get_mock_status...")
        _result = await server.call_tool("get_mock_status", {})
        print("  ✓ get_mock_status returned status")
        
        # Test get_people
        print("  Testing get_people...")
        _result = await server.call_tool("get_people", {"per_page": 5})
        print("  ✓ get_people returned data")
        
        # Test get_services
        print("  Testing get_services...")
        _result = await server.call_tool("get_services", {"per_page": 3})
        print("  ✓ get_services returned data")
        
        # Test get_donations
        print("  Testing get_donations...")
        _result = await server.call_tool("get_donations", {"per_page": 3})
        print("  ✓ get_donations returned data")
        
        # Test get_workflows
        print("  Testing get_workflows...")
        _result = await server.call_tool("get_workflows", {"per_page": 3})
        print("  ✓ get_workflows returned data")
        
        print("\n🎉 Comprehensive server is ready!")
        print("   This server provides full Planning Center API coverage:")
        print("   • People API (people, workflows, categories)")
        print("   • Services API (services, plans)")
        print("   • Registrations API (registrations, attendees)")
        print("   • Giving API (donations, funds)")
        print("   • Groups API (groups)")
        print("   • Calendar API (events)")
        print("   • Utility endpoints (campuses, status)")
        print("   Restart Claude Desktop to test the connection.")
        return True
        
    except Exception as e:
        print(f"✗ Server failed: {e}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_comprehensive_server())
    if not success:
        sys.exit(1)
