#!/usr/bin/env python3
"""Test script to verify Planning Center API connection."""

import asyncio
import os
import sys
from planning_center_mcp.config import PCOConfig
from planning_center_mcp.client import PCOClient


async def test_connection():
    """Test the connection to Planning Center API."""
    
    print("Planning Center MCP Server - Connection Test")
    print("=" * 50)
    
    # Check environment variables
    print("Checking environment variables...")
    access_token = os.getenv("PCO_ACCESS_TOKEN")
    app_id = os.getenv("PCO_APP_ID")
    secret = os.getenv("PCO_SECRET")
    
    if access_token:
        print("✓ PCO_ACCESS_TOKEN found")
    elif app_id and secret:
        print("✓ PCO_APP_ID and PCO_SECRET found")
    else:
        print("✗ No authentication credentials found")
        print("Please set either:")
        print("  - PCO_ACCESS_TOKEN (recommended)")
        print("  - PCO_APP_ID and PCO_SECRET")
        return False
    
    # Load configuration
    try:
        config = PCOConfig.from_env()
        config.get_auth_headers()
        print("✓ Configuration loaded successfully")
    except Exception as e:
        print(f"✗ Configuration error: {e}")
        return False
    
    # Test API connection
    print("\nTesting API connection...")
    try:
        async with PCOClient(config) as client:
            # Try to get a small number of people to test the connection
            result = await client.get_people(per_page=1)
            print("✓ Successfully connected to Planning Center API")
            print(f"✓ API returned {len(result.data)} person(s)")
            return True
    except Exception as e:
        print(f"✗ API connection failed: {e}")
        return False


if __name__ == "__main__":
    success = asyncio.run(test_connection())
    if success:
        print("\n🎉 All tests passed! The MCP server should work correctly.")
        sys.exit(0)
    else:
        print("\n❌ Tests failed. Please check your configuration.")
        sys.exit(1)
