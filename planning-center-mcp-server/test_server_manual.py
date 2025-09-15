#!/usr/bin/env python3
"""Manual test of the MCP server to debug initialization issues."""

import asyncio
import sys
from mcp_mock_server_simple import server


async def test_server():
    """Test the server manually."""
    print("Testing MCP server...")

    try:
        # Test list_tools
        print("Testing list_tools...")
        tools = server.list_tools()
        print(f"✓ list_tools returned {len(tools)} tools")

        # Test call_tool with a simple tool
        print("Testing call_tool...")
        result = await server.call_tool("get_people", {"per_page": 5})
        print(f"✓ call_tool returned {len(result)} results")

        # Test create_initialization_options
        print("Testing create_initialization_options...")
        init_options = server.create_initialization_options()
        print(f"✓ create_initialization_options returned: {init_options}")

        print("✅ All tests passed!")
        return True

    except Exception as e:
        print(f"✗ Test failed: {e}")
        import traceback

        print(f"Traceback: {traceback.format_exc()}")
        return False


if __name__ == "__main__":
    success = asyncio.run(test_server())
    sys.exit(0 if success else 1)
