#!/usr/bin/env python3
"""Test script for the simple MCP server."""

import sys
from mcp_mock_server_simple import server


def test_server():
    """Test the simple MCP server."""
    print("🧪 Testing Simple MCP Server")
    print("=" * 40)

    try:
        print("✓ Server created successfully")
        print(f"  Server name: {server.name}")

        # Check if server has the expected methods
        if hasattr(server, "list_tools") and hasattr(server, "call_tool"):
            print("✓ Server has required MCP methods")
        else:
            print("✗ Server missing required MCP methods")
            return False

        print()
        print("🎉 Simple server is ready!")
        print("   This server has fewer tools but should be more stable.")
        print("   Restart Claude Desktop to test the connection.")
        return True

    except Exception as e:
        print(f"✗ Server failed: {e}")
        return False


if __name__ == "__main__":
    success = test_server()
    if not success:
        sys.exit(1)
