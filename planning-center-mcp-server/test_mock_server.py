#!/usr/bin/env python3
"""Test script to demonstrate the mock Planning Center API server."""

import asyncio
import httpx


async def test_mock_server():
    """Test the mock server endpoints."""
    base_url = "http://localhost:8001"

    print("🧪 Testing Planning Center Mock API Server")
    print("=" * 50)

    async with httpx.AsyncClient() as client:
        # Test server status
        print("1. Testing server status...")
        try:
            response = await client.get(f"{base_url}/mock/status")
            if response.status_code == 200:
                status = response.json()
                print("✓ Server is running")
                print(f"  Data counts: {status['data_counts']}")
            else:
                print(f"✗ Server status check failed: {response.status_code}")
                return
        except Exception as e:
            print(f"✗ Cannot connect to server: {e}")
            print("Make sure the mock server is running on port 8001")
            return

        # Test get_people endpoint
        print("\n2. Testing get_people endpoint...")
        try:
            response = await client.post(
                f"{base_url}/get_people", json={"per_page": 5, "search": "john"}
            )
            if response.status_code == 200:
                data = response.json()
                print(f"✓ Found {len(data['data'])} people matching 'john'")
                for person in data["data"][:3]:
                    print(
                        f"  - {person['attributes']['full_name']} ({person['attributes']['email']})"
                    )
            else:
                print(f"✗ get_people failed: {response.status_code}")
        except Exception as e:
            print(f"✗ get_people error: {e}")

        # Test get_services endpoint
        print("\n3. Testing get_services endpoint...")
        try:
            response = await client.post(
                f"{base_url}/get_services", json={"per_page": 3}
            )
            if response.status_code == 200:
                data = response.json()
                print(f"✓ Found {len(data['data'])} services")
                for service in data["data"]:
                    print(f"  - {service['attributes']['name']}")
            else:
                print(f"✗ get_services failed: {response.status_code}")
        except Exception as e:
            print(f"✗ get_services error: {e}")

        # Test get_plans endpoint
        print("\n4. Testing get_plans endpoint...")
        try:
            response = await client.post(f"{base_url}/get_plans", json={"per_page": 3})
            if response.status_code == 200:
                data = response.json()
                print(f"✓ Found {len(data['data'])} plans")
                for plan in data["data"]:
                    print(f"  - {plan['attributes']['title']}")
            else:
                print(f"✗ get_plans failed: {response.status_code}")
        except Exception as e:
            print(f"✗ get_plans error: {e}")

        # Test get_registrations endpoint
        print("\n5. Testing get_registrations endpoint...")
        try:
            response = await client.post(
                f"{base_url}/get_registrations", json={"per_page": 3, "status": "open"}
            )
            if response.status_code == 200:
                data = response.json()
                print(f"✓ Found {len(data['data'])} open registrations")
                for registration in data["data"]:
                    print(
                        f"  - {registration['attributes']['name']} ({registration['attributes']['status']})"
                    )
            else:
                print(f"✗ get_registrations failed: {response.status_code}")
        except Exception as e:
            print(f"✗ get_registrations error: {e}")

        # Test get_attendees endpoint
        print("\n6. Testing get_attendees endpoint...")
        try:
            response = await client.post(
                f"{base_url}/get_attendees",
                json={"per_page": 3, "attendance_status": "checked_in"},
            )
            if response.status_code == 200:
                data = response.json()
                print(f"✓ Found {len(data['data'])} checked-in attendees")
                for attendee in data["data"]:
                    print(
                        f"  - {attendee['attributes']['first_name']} {attendee['attributes']['last_name']} ({attendee['attributes']['attendance_status']})"
                    )
            else:
                print(f"✗ get_attendees failed: {response.status_code}")
        except Exception as e:
            print(f"✗ get_attendees error: {e}")

        # Test pagination
        print("\n7. Testing pagination...")
        try:
            response = await client.post(
                f"{base_url}/get_people", json={"per_page": 2, "offset": 0}
            )
            if response.status_code == 200:
                data = response.json()
                print(f"✓ Pagination working - page 1: {len(data['data'])} items")
                print(
                    f"  Total: {data['meta']['total']}, Offset: {data['meta']['offset']}"
                )

                # Test next page
                if data["links"]["next"]:
                    next_response = await client.post(
                        f"{base_url}/get_people", json={"per_page": 2, "offset": 2}
                    )
                    if next_response.status_code == 200:
                        next_data = next_response.json()
                        print(f"✓ Page 2: {len(next_data['data'])} items")
            else:
                print(f"✗ Pagination test failed: {response.status_code}")
        except Exception as e:
            print(f"✗ Pagination error: {e}")

        # Test filtering
        print("\n8. Testing filtering...")
        try:
            response = await client.post(
                f"{base_url}/get_people", json={"per_page": 10, "status": "active"}
            )
            if response.status_code == 200:
                data = response.json()
                active_count = len(
                    [p for p in data["data"] if p["attributes"]["status"] == "active"]
                )
                print(f"✓ Filtering working - {active_count} active people found")
            else:
                print(f"✗ Filtering test failed: {response.status_code}")
        except Exception as e:
            print(f"✗ Filtering error: {e}")

    print("\n🎉 Mock server testing completed!")
    print("\nTo use the mock server:")
    print("1. Run: python run_mock_server.py")
    print("2. Visit: http://localhost:8001/docs for API documentation")
    print("3. MCP endpoint: http://localhost:8001/mcp")
    print("4. Reset data: http://localhost:8001/mock/reset")


if __name__ == "__main__":
    asyncio.run(test_mock_server())
