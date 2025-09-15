"""Basic usage examples for Planning Center API wrapper."""

import asyncio

from planning_center_api import PCOClient, PCOProduct


async def basic_examples():
    """Basic usage examples."""

    # Initialize client with your credentials
    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        # Get all people
        print("=== Getting all people ===")
        people = await client.get_people(per_page=10)
        print(f"Found {len(people)} people")

        for person in people.data[:3]:  # Show first 3
            print(f"- {person.get_first_name()} {person.get_last_name()}")

        # Get a specific person
        if people.data:
            person_id = people.data[0].id
            print(f"\n=== Getting person {person_id} ===")
            person = await client.get_person(
                person_id, include=["emails", "phone_numbers"]
            )
            print(f"Name: {person.get_full_name()}")
            print(f"Email: {person.get_email()}")
            print(f"Phone: {person.get_phone()}")

        # Search for people
        print("\n=== Searching for people ===")
        search_results = await client.search_people("john")
        print(f"Found {len(search_results)} people matching 'john'")

        # Get people by email
        print("\n=== Finding people by email ===")
        email_results = await client.get_people_by_email("john@example.com")
        print(f"Found {len(email_results)} people with that email")

        # Get active people only
        print("\n=== Getting active people ===")
        active_people = await client.get_active_people(per_page=5)
        print(f"Found {len(active_people)} active people")

        # Get services
        print("\n=== Getting services ===")
        services = await client.get_services(per_page=5)
        print(f"Found {len(services)} services")

        for service in services.data[:3]:  # Show first 3
            print(f"- {service.get_name()}")

        # Get plans for a service
        if services.data:
            service_id = services.data[0].id
            print(f"\n=== Getting plans for service {service_id} ===")
            plans = await client.get_plans(service_id=service_id, per_page=5)
            print(f"Found {len(plans)} plans for this service")

            for plan in plans.data[:3]:  # Show first 3
                print(f"- {plan.get_title()}")


async def pagination_example():
    """Example of paginating through all people."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        print("=== Paginating through all people ===")
        count = 0

        async for person in client.paginate_all(
            product=PCOProduct.PEOPLE, resource="people", per_page=25
        ):
            count += 1
            if count <= 5:  # Show first 5
                print(f"{count}. {person.get_full_name()}")
            elif count % 100 == 0:  # Progress indicator
                print(f"Processed {count} people...")

        print(f"Total people processed: {count}")


async def create_and_update_example():
    """Example of creating and updating resources."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        # Create a new person
        print("=== Creating a new person ===")
        new_person_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
        }

        try:
            new_person = await client.create_person(new_person_data)
            print(f"Created person: {new_person.get_full_name()} (ID: {new_person.id})")

            # Update the person
            print("\n=== Updating the person ===")
            update_data = {"phone": "555-123-4567"}

            updated_person = await client.update_person(
                new_person.id, update_data, include=["emails", "phone_numbers"]
            )
            print(f"Updated person: {updated_person.get_full_name()}")
            print(f"Phone: {updated_person.get_phone()}")

        except Exception as e:
            print(f"Error: {e}")


async def error_handling_example():
    """Example of proper error handling."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        try:
            # This will fail if the person doesn't exist
            person = await client.get_person("nonexistent_id")
            print(f"Found person: {person.get_full_name()}")

        except Exception as e:
            print(f"Error getting person: {e}")
            print(f"Error type: {type(e).__name__}")


if __name__ == "__main__":
    print("Planning Center API - Basic Usage Examples")
    print("=" * 50)

    # Run examples
    asyncio.run(basic_examples())
    print("\n" + "=" * 50)
    asyncio.run(pagination_example())
    print("\n" + "=" * 50)
    asyncio.run(create_and_update_example())
    print("\n" + "=" * 50)
    asyncio.run(error_handling_example())
