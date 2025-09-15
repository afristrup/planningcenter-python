#!/usr/bin/env python3
"""Demo script showing how to use the Planning Center Mock API Server."""

import asyncio
import httpx


async def demo_mock_server():
    """Demonstrate the mock server capabilities."""

    print("🎭 Planning Center Mock API Server Demo")
    print("=" * 60)
    print()

    base_url = "http://localhost:8001"

    async with httpx.AsyncClient() as client:
        # Check if server is running
        try:
            response = await client.get(f"{base_url}/mock/status")
            if response.status_code != 200:
                print("❌ Mock server is not running!")
                print("Please start it with: python run_mock_server.py")
                return
        except Exception:
            print("❌ Cannot connect to mock server!")
            print("Please start it with: python run_mock_server.py")
            return

        print("✅ Mock server is running!")
        print()

        # Demo 1: Get people with search
        print("🔍 Demo 1: Search for people")
        print("-" * 30)

        response = await client.post(
            f"{base_url}/get_people", json={"per_page": 3, "search": "john"}
        )

        if response.status_code == 200:
            data = response.json()
            print(f"Found {len(data['data'])} people matching 'john':")
            for person in data["data"]:
                print(f"  👤 {person['attributes']['full_name']}")
                print(f"     📧 {person['attributes']['email']}")
                print(f"     📱 {person['attributes']['phone']}")
                print(f"     📊 Status: {person['attributes']['status']}")
                print()
        else:
            print(f"❌ Error: {response.status_code}")

        # Demo 2: Get services
        print("🏢 Demo 2: Get services")
        print("-" * 30)

        response = await client.post(f"{base_url}/get_services", json={"per_page": 3})

        if response.status_code == 200:
            data = response.json()
            print(f"Found {len(data['data'])} services:")
            for service in data["data"]:
                print(f"  🎵 {service['attributes']['name']}")
                print(f"     📝 {service['attributes']['description']}")
                print()
        else:
            print(f"❌ Error: {response.status_code}")

        # Demo 3: Get plans
        print("📅 Demo 3: Get upcoming plans")
        print("-" * 30)

        response = await client.post(f"{base_url}/get_plans", json={"per_page": 3})

        if response.status_code == 200:
            data = response.json()
            print(f"Found {len(data['data'])} plans:")
            for plan in data["data"]:
                print(f"  📋 {plan['attributes']['title']}")
                print(f"     📅 Date: {plan['attributes']['plan_date'][:10]}")
                print()
        else:
            print(f"❌ Error: {response.status_code}")

        # Demo 4: Get open registrations
        print("📝 Demo 4: Get open registrations")
        print("-" * 30)

        response = await client.post(
            f"{base_url}/get_registrations", json={"per_page": 3, "status": "open"}
        )

        if response.status_code == 200:
            data = response.json()
            print(f"Found {len(data['data'])} open registrations:")
            for registration in data["data"]:
                print(f"  🎫 {registration['attributes']['name']}")
                print(f"     👥 Capacity: {registration['attributes']['capacity']}")
                print(
                    f"     ✅ Registered: {registration['attributes']['registered_count']}"
                )
                print(f"     📊 Status: {registration['attributes']['status']}")
                print()
        else:
            print(f"❌ Error: {response.status_code}")

        # Demo 5: Get checked-in attendees
        print("✅ Demo 5: Get checked-in attendees")
        print("-" * 30)

        response = await client.post(
            f"{base_url}/get_attendees",
            json={"per_page": 3, "attendance_status": "checked_in"},
        )

        if response.status_code == 200:
            data = response.json()
            print(f"Found {len(data['data'])} checked-in attendees:")
            for attendee in data["data"]:
                print(
                    f"  👤 {attendee['attributes']['first_name']} {attendee['attributes']['last_name']}"
                )
                print(f"     📧 {attendee['attributes']['email']}")
                print(f"     ✅ Status: {attendee['attributes']['attendance_status']}")
                print()
        else:
            print(f"❌ Error: {response.status_code}")

        # Demo 6: Pagination
        print("📄 Demo 6: Pagination example")
        print("-" * 30)

        response = await client.post(
            f"{base_url}/get_people", json={"per_page": 2, "offset": 0}
        )

        if response.status_code == 200:
            data = response.json()
            print(
                f"Page 1: {len(data['data'])} people (offset: {data['meta']['offset']})"
            )
            print(f"Total people: {data['meta']['total']}")
            print(f"Next page available: {'Yes' if data['links']['next'] else 'No'}")
            print()

        # Demo 7: Server status
        print("📊 Demo 7: Server status")
        print("-" * 30)

        response = await client.get(f"{base_url}/mock/status")
        if response.status_code == 200:
            status = response.json()
            print("Mock data counts:")
            for resource, count in status["data_counts"].items():
                print(f"  📦 {resource}: {count} items")
            print()

    print("🎉 Demo completed!")
    print()
    print("💡 Next steps:")
    print("  • Visit http://localhost:8001/docs for interactive API documentation")
    print("  • Use http://localhost:8001/mcp for MCP client integration")
    print("  • Run 'python test_mock_server.py' for comprehensive testing")
    print("  • Check MOCK_SERVER.md for detailed documentation")


if __name__ == "__main__":
    asyncio.run(demo_mock_server())
