"""Advanced usage examples for Planning Center API wrapper."""

import asyncio
from datetime import datetime, timedelta

from planning_center_api import PCOClient, PCOProduct
from planning_center_api.utils import (
    PCODataAnalyzer,
    PCODataTransformer,
    PCODataValidator,
    chunk_list,
    format_date,
)


async def data_validation_example():
    """Example of validating data before sending to Planning Center."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        print("=== Data Validation Example ===")

        # Sample person data
        person_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "555-123-4567",
        }

        # Validate the data
        validator = PCODataValidator()
        errors = validator.validate_person_data(person_data)

        if errors:
            print(f"Validation errors: {errors}")
        else:
            print("Data is valid!")

            # Create the person
            try:
                new_person = await client.create_person(person_data)
                print(f"Created person: {new_person.get_full_name()}")
            except Exception as e:
                print(f"Error creating person: {e}")


async def data_transformation_example():
    """Example of transforming data between formats."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        print("\n=== Data Transformation Example ===")

        # Get some people
        people = await client.get_people(per_page=5)

        transformer = PCODataTransformer()

        # Transform people to contact format
        contacts = []
        for person in people.data:
            contact = transformer.person_to_contact_dict(person)
            contacts.append(contact)

        print("Transformed people to contacts:")
        for contact in contacts:
            print(f"- {contact['name']}: {contact['email']}")

        # Get some services
        services = await client.get_services(per_page=3)

        # Transform services to event format
        events = []
        for service in services.data:
            event = transformer.service_to_event_dict(service)
            events.append(event)

        print("\nTransformed services to events:")
        for event in events:
            print(f"- {event['title']}: {event['start_time']}")


async def data_analysis_example():
    """Example of analyzing Planning Center data."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        print("\n=== Data Analysis Example ===")

        analyzer = PCODataAnalyzer(client)

        # Get people statistics
        people_stats = await analyzer.get_people_stats()
        print("People Statistics:")
        print(f"- Total people: {people_stats['total_people']}")
        print(f"- Active people: {people_stats['active_people']}")
        print(f"- Inactive people: {people_stats['inactive_people']}")
        print(f"- Active percentage: {people_stats['active_percentage']:.1f}%")

        # Get services statistics
        services_stats = await analyzer.get_services_stats()
        print("\nServices Statistics:")
        print(f"- Total services: {services_stats['total_services']}")
        print(f"- Total plans: {services_stats['total_plans']}")
        print(f"- Plans per service: {services_stats['plans_per_service']:.1f}")


async def bulk_operations_example():
    """Example of performing bulk operations."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        print("\n=== Bulk Operations Example ===")

        # Get all active people
        active_people = []
        async for person in client.paginate_all(
            product=PCOProduct.PEOPLE,
            resource="people",
            filter_params={"status": "active"},
            per_page=100,
        ):
            active_people.append(person)

        print(f"Found {len(active_people)} active people")

        # Process in chunks
        chunk_size = 10
        people_chunks = chunk_list(active_people, chunk_size)

        print(f"Processing {len(people_chunks)} chunks of {chunk_size} people each")

        for i, chunk in enumerate(people_chunks):
            print(f"Processing chunk {i + 1}/{len(people_chunks)}")

            # Process each person in the chunk
            for person in chunk:
                # Example: Update last contact date
                try:
                    await client.update_person(
                        person.id, {"last_contact_date": datetime.utcnow().isoformat()}
                    )
                except Exception as e:
                    print(f"Error updating person {person.id}: {e}")

            # Add delay between chunks to respect rate limits
            await asyncio.sleep(1)


async def advanced_filtering_example():
    """Example of advanced filtering and querying."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        print("\n=== Advanced Filtering Example ===")

        # Get people created in the last 30 days
        thirty_days_ago = (datetime.utcnow() - timedelta(days=30)).isoformat()

        recent_people = await client.get_people(
            filter_params={"created_at": f"gte:{thirty_days_ago}"},
            sort="created_at desc",
        )

        print(f"Found {len(recent_people)} people created in the last 30 days")

        # Get people with specific statuses
        statuses = ["active", "inactive"]
        for status in statuses:
            people_with_status = await client.get_people(
                filter_params={"status": status}, per_page=10
            )
            print(f"Found {len(people_with_status)} people with status '{status}'")

        # Get services with specific criteria
        services = await client.get_services(
            filter_params={"name": "Sunday"}, per_page=10
        )
        print(f"Found {len(services)} services with 'Sunday' in the name")


async def error_handling_and_retry_example():
    """Example of robust error handling and retry logic."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        print("\n=== Error Handling and Retry Example ===")

        # List of person IDs to process (some may not exist)
        person_ids = ["12345", "67890", "nonexistent_id", "11111"]

        for person_id in person_ids:
            max_retries = 3
            retry_count = 0

            while retry_count < max_retries:
                try:
                    person = await client.get_person(person_id)
                    print(
                        f"Successfully retrieved person {person_id}: {person.get_full_name()}"
                    )
                    break

                except Exception as e:
                    retry_count += 1
                    print(f"Attempt {retry_count} failed for person {person_id}: {e}")

                    if retry_count < max_retries:
                        # Exponential backoff
                        wait_time = 2**retry_count
                        print(f"Waiting {wait_time} seconds before retry...")
                        await asyncio.sleep(wait_time)
                    else:
                        print(
                            f"Failed to retrieve person {person_id} after {max_retries} attempts"
                        )


async def concurrent_operations_example():
    """Example of performing concurrent operations."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        print("\n=== Concurrent Operations Example ===")

        # Get some person IDs
        people = await client.get_people(per_page=5)
        person_ids = [person.id for person in people.data]

        # Define async function to get person details
        async def get_person_details(person_id: str):
            try:
                person = await client.get_person(
                    person_id, include=["emails", "phone_numbers", "addresses"]
                )
                return {
                    "id": person.id,
                    "name": person.get_full_name(),
                    "email": person.get_email(),
                    "phone": person.get_phone(),
                    "status": person.get_attribute("status"),
                }
            except Exception as e:
                return {"id": person_id, "error": str(e)}

        # Process all people concurrently
        print(f"Fetching details for {len(person_ids)} people concurrently...")

        tasks = [get_person_details(person_id) for person_id in person_ids]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Display results
        for result in results:
            if isinstance(result, dict) and "error" not in result:
                print(f"- {result['name']}: {result['email']} ({result['status']})")
            else:
                print(f"- Error: {result}")


async def data_export_with_formatting():
    """Example of exporting data with custom formatting."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        print("\n=== Data Export with Formatting Example ===")

        # Get people with financial data (if available)
        people = await client.get_people(per_page=10)

        formatted_data = []
        for person in people.data:
            # Format dates
            created_at = person.get_attribute("created_at")
            updated_at = person.get_attribute("updated_at")

            formatted_person = {
                "id": person.id,
                "name": person.get_full_name(),
                "email": person.get_email(),
                "phone": person.get_phone(),
                "status": person.get_attribute("status"),
                "created_at": format_date(created_at) if created_at else "",
                "updated_at": format_date(updated_at) if updated_at else "",
                "created_relative": format_relative_date(created_at)
                if created_at
                else "",
            }

            formatted_data.append(formatted_person)

        # Display formatted data
        print("Formatted people data:")
        for person in formatted_data:
            print(f"- {person['name']}")
            print(f"  Email: {person['email']}")
            print(f"  Created: {person['created_at']} ({person['created_relative']})")
            print(f"  Status: {person['status']}")
            print()


def format_relative_date(date_str: str) -> str:
    """Format date as relative time."""
    if not date_str:
        return ""

    try:
        date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        now = datetime.utcnow()
        diff = now - date

        if diff.days > 0:
            return f"{diff.days} day{'s' if diff.days != 1 else ''} ago"
        elif diff.seconds > 3600:
            hours = diff.seconds // 3600
            return f"{hours} hour{'s' if hours != 1 else ''} ago"
        elif diff.seconds > 60:
            minutes = diff.seconds // 60
            return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
        else:
            return "Just now"
    except Exception:
        return "Invalid date"


if __name__ == "__main__":
    print("Planning Center API - Advanced Usage Examples")
    print("=" * 50)

    # Run advanced examples
    asyncio.run(data_validation_example())
    asyncio.run(data_transformation_example())
    asyncio.run(data_analysis_example())
    asyncio.run(bulk_operations_example())
    asyncio.run(advanced_filtering_example())
    asyncio.run(error_handling_and_retry_example())
    asyncio.run(concurrent_operations_example())
    asyncio.run(data_export_with_formatting())

    print("\nAdvanced examples completed!")
