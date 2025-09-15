#!/usr/bin/env python3
"""Example usage of Planning Center MCP Server tools."""

import asyncio
from planning_center_mcp.config import PCOConfig
from planning_center_mcp.client import PCOClient


async def example_usage():
    """Example of how to use the Planning Center client directly."""

    # Load configuration from environment
    config = PCOConfig.from_env()

    try:
        # Validate configuration
        config.get_auth_headers()
        print("✓ Configuration loaded successfully")
    except ValueError as e:
        print(f"✗ Configuration error: {e}")
        print(
            "Please set PCO_ACCESS_TOKEN or both PCO_APP_ID and PCO_SECRET environment variables"
        )
        return

    async with PCOClient(config) as client:
        print("✓ Connected to Planning Center API")

        # Example 1: Get people
        print("\n--- Getting People ---")
        try:
            people = await client.get_people(per_page=5)
            print(f"Found {len(people.data)} people")
            for person in people.data[:3]:  # Show first 3
                print(
                    f"  - {person.attributes.get('first_name', '')} {person.attributes.get('last_name', '')} (ID: {person.id})"
                )
        except Exception as e:
            print(f"Error getting people: {e}")

        # Example 2: Get services
        print("\n--- Getting Services ---")
        try:
            services = await client.get_services(per_page=5)
            print(f"Found {len(services.data)} services")
            for service in services.data[:3]:  # Show first 3
                print(
                    f"  - {service.attributes.get('name', 'Unknown')} (ID: {service.id})"
                )
        except Exception as e:
            print(f"Error getting services: {e}")

        # Example 3: Get registrations
        print("\n--- Getting Registrations ---")
        try:
            registrations = await client.get_registrations(per_page=5)
            print(f"Found {len(registrations.data)} registrations")
            for registration in registrations.data[:3]:  # Show first 3
                print(
                    f"  - {registration.attributes.get('name', 'Unknown')} (ID: {registration.id})"
                )
        except Exception as e:
            print(f"Error getting registrations: {e}")


if __name__ == "__main__":
    asyncio.run(example_usage())
