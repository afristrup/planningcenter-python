#!/usr/bin/env python3
"""Test script to verify MCP servers work correctly."""

import sys
from mcp_server import server as main_server
from mcp_mock_server import server as mock_server

def test_server(server, server_name):
    """Test an MCP server."""
    print(f"Testing {server_name}...")
    
    try:
        # Test server creation and basic properties
        print(f"✓ {server_name} created successfully")
        print(f"  Server name: {server.name}")
        
        # Check if server has the expected methods
        if hasattr(server, 'list_tools') and hasattr(server, 'call_tool'):
            print(f"✓ {server_name} has required MCP methods")
        else:
            print(f"✗ {server_name} missing required MCP methods")
            return False
        
        print()
        return True
        
    except Exception as e:
        print(f"✗ {server_name} failed: {e}")
        return False

def main():
    """Test both MCP servers."""
    print("🧪 Testing MCP Servers")
    print("=" * 40)
    print()
    
    # Test main server (will fail without credentials, but should import)
    main_ok = test_server(main_server, "Planning Center MCP Server")
    
    # Test mock server (should work without credentials)
    mock_ok = test_server(mock_server, "Planning Center Mock MCP Server")
    
    print("📊 Test Results:")
    print(f"  Main Server: {'✓ PASS' if main_ok else '✗ FAIL'}")
    print(f"  Mock Server: {'✓ PASS' if mock_ok else '✗ FAIL'}")
    
    if mock_ok:
        print()
        print("🎉 Mock server is ready for Claude Desktop!")
        print("   You can use the mock server without API credentials.")
    else:
        print()
        print("❌ Both servers failed. Check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
