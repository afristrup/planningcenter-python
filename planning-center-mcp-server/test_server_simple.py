#!/usr/bin/env python3
"""Simple test to see if the server can start without crashing."""

import asyncio
import sys
from mcp_mock_server_simple import server


async def test_server_start():
    """Test if the server can start."""
    print("Testing server startup...")

    try:
        # Test create_initialization_options
        print("Testing create_initialization_options...")
        init_options = server.create_initialization_options()
        print(f"✓ create_initialization_options returned: {type(init_options)}")

        # Test get_capabilities
        print("Testing get_capabilities...")
        capabilities = server.get_capabilities()
        print(f"✓ get_capabilities returned: {type(capabilities)}")

        print("✅ Server startup tests passed!")
        return True

    except Exception as e:
        print(f"✗ Test failed: {e}")
        import traceback

        print(f"Traceback: {traceback.format_exc()}")
        return False


if __name__ == "__main__":
    success = asyncio.run(test_server_start())
    sys.exit(0 if success else 1)
