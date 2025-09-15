"""Data export examples using the Planning Center API wrapper."""

import asyncio
import csv
import json
from datetime import datetime
from pathlib import Path

from planning_center_api import PCOClient, PCOProduct
from planning_center_api.utils import (
    PCOBatchProcessor,
    PCODataAnalyzer,
    PCODataExporter,
)


async def export_people_to_json():
    """Export all people to JSON file."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        print("Exporting people to JSON...")

        exporter = PCODataExporter(client)
        people_data = await exporter.export_people_to_dict(
            include=["emails", "phone_numbers", "addresses"]
        )

        # Save to file
        output_file = Path("people_export.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(people_data, f, indent=2, default=str)

        print(f"Exported {len(people_data)} people to {output_file}")


async def export_people_to_csv():
    """Export people to CSV file."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        print("Exporting people to CSV...")

        # Get all people with their details
        people_data = []
        async for person in client.paginate_all(
            product=PCOProduct.PEOPLE,
            resource="people",
            include=["emails", "phone_numbers", "addresses"],
        ):
            # Extract relevant data
            person_data = {
                "id": person.id,
                "first_name": person.get_attribute("first_name", ""),
                "last_name": person.get_attribute("last_name", ""),
                "email": person.get_attribute("email", ""),
                "phone": person.get_attribute("phone", ""),
                "status": person.get_attribute("status", ""),
                "created_at": person.get_attribute("created_at", ""),
                "updated_at": person.get_attribute("updated_at", ""),
            }

            # Get primary email if available
            if person.relationships and hasattr(person.relationships, "emails"):
                emails_data = person.get_relationship_data("emails")
                if emails_data and isinstance(emails_data, list):
                    for email in emails_data:
                        if email.get("attributes", {}).get("primary"):
                            person_data["primary_email"] = email.get(
                                "attributes", {}
                            ).get("address", "")
                            break

            people_data.append(person_data)

        # Write to CSV
        if people_data:
            output_file = Path("people_export.csv")
            with open(output_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=people_data[0].keys())
                writer.writeheader()
                writer.writerows(people_data)

            print(f"Exported {len(people_data)} people to {output_file}")


async def export_services_and_plans():
    """Export services and their plans to JSON."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        print("Exporting services and plans...")

        services_data = []

        # Get all services
        async for service in client.paginate_all(
            product=PCOProduct.SERVICES, resource="services"
        ):
            service_data = {
                "id": service.id,
                "name": service.get_attribute("name", ""),
                "description": service.get_attribute("description", ""),
                "created_at": service.get_attribute("created_at", ""),
                "updated_at": service.get_attribute("updated_at", ""),
                "plans": [],
            }

            # Get plans for this service
            plans = await client.get_plans(service_id=service.id, per_page=100)
            for plan in plans.data:
                plan_data = {
                    "id": plan.id,
                    "title": plan.get_attribute("title", ""),
                    "series_title": plan.get_attribute("series_title", ""),
                    "created_at": plan.get_attribute("created_at", ""),
                    "updated_at": plan.get_attribute("updated_at", ""),
                }
                service_data["plans"].append(plan_data)

            services_data.append(service_data)

        # Save to file
        output_file = Path("services_plans_export.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(services_data, f, indent=2, default=str)

        print(f"Exported {len(services_data)} services to {output_file}")


async def generate_people_report():
    """Generate a comprehensive people report."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        print("Generating people report...")

        analyzer = PCODataAnalyzer(client)
        stats = await analyzer.get_people_stats()

        # Generate report
        report = {
            "generated_at": datetime.utcnow().isoformat(),
            "statistics": stats,
            "people": [],
        }

        # Get detailed people data
        async for person in client.paginate_all(
            product=PCOProduct.PEOPLE,
            resource="people",
            include=["emails", "phone_numbers", "addresses"],
        ):
            person_data = {
                "id": person.id,
                "name": f"{person.get_attribute('first_name', '')} {person.get_attribute('last_name', '')}".strip(),
                "first_name": person.get_attribute("first_name", ""),
                "last_name": person.get_attribute("last_name", ""),
                "status": person.get_attribute("status", ""),
                "email": person.get_attribute("email", ""),
                "phone": person.get_attribute("phone", ""),
                "birthdate": person.get_attribute("birthdate", ""),
                "anniversary": person.get_attribute("anniversary", ""),
                "created_at": person.get_attribute("created_at", ""),
                "updated_at": person.get_attribute("updated_at", ""),
                "emails": [],
                "phone_numbers": [],
                "addresses": [],
            }

            # Extract related data
            if person.relationships:
                # Emails
                emails_data = person.get_relationship_data("emails")
                if emails_data and isinstance(emails_data, list):
                    for email in emails_data:
                        person_data["emails"].append(
                            {
                                "address": email.get("attributes", {}).get(
                                    "address", ""
                                ),
                                "location": email.get("attributes", {}).get(
                                    "location", ""
                                ),
                                "primary": email.get("attributes", {}).get(
                                    "primary", False
                                ),
                            }
                        )

                # Phone numbers
                phones_data = person.get_relationship_data("phone_numbers")
                if phones_data and isinstance(phones_data, list):
                    for phone in phones_data:
                        person_data["phone_numbers"].append(
                            {
                                "number": phone.get("attributes", {}).get("number", ""),
                                "location": phone.get("attributes", {}).get(
                                    "location", ""
                                ),
                                "primary": phone.get("attributes", {}).get(
                                    "primary", False
                                ),
                            }
                        )

                # Addresses
                addresses_data = person.get_relationship_data("addresses")
                if addresses_data and isinstance(addresses_data, list):
                    for address in addresses_data:
                        person_data["addresses"].append(
                            {
                                "street": address.get("attributes", {}).get(
                                    "street", ""
                                ),
                                "city": address.get("attributes", {}).get("city", ""),
                                "state": address.get("attributes", {}).get("state", ""),
                                "zip": address.get("attributes", {}).get("zip", ""),
                                "country": address.get("attributes", {}).get(
                                    "country", ""
                                ),
                                "location": address.get("attributes", {}).get(
                                    "location", ""
                                ),
                                "primary": address.get("attributes", {}).get(
                                    "primary", False
                                ),
                            }
                        )

            report["people"].append(person_data)

        # Save report
        output_file = Path("people_report.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, default=str)

        print(f"Generated report with {len(report['people'])} people to {output_file}")
        print(f"Statistics: {stats}")


async def batch_process_people():
    """Example of batch processing people data."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        print("Batch processing people...")

        processor = PCOBatchProcessor(client, batch_size=50)

        # Define a processor function
        async def process_person(person):
            """Process a single person."""
            return {
                "id": person.id,
                "name": f"{person.get_attribute('first_name', '')} {person.get_attribute('last_name', '')}".strip(),
                "status": person.get_attribute("status", ""),
                "has_email": bool(person.get_attribute("email")),
                "has_phone": bool(person.get_attribute("phone")),
                "processed_at": datetime.utcnow().isoformat(),
            }

        # Process all people in batches
        results = await processor.process_people_batch(
            filter_params={"status": "active"},  # Only active people
            include=["emails", "phone_numbers"],
            processor=process_person,
        )

        print(f"Processed {len(results)} people in batches")

        # Save results
        output_file = Path("people_batch_processed.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, default=str)

        print(f"Saved batch processing results to {output_file}")


async def export_contact_list():
    """Export a simple contact list."""

    async with PCOClient(app_id="your_app_id", secret="your_secret") as client:
        print("Exporting contact list...")

        contacts = []

        # Get active people with contact information
        async for person in client.paginate_all(
            product=PCOProduct.PEOPLE,
            resource="people",
            include=["emails", "phone_numbers"],
            filter_params={"status": "active"},
        ):
            # Only include people with email or phone
            email = person.get_attribute("email")
            phone = person.get_attribute("phone")

            if email or phone:
                contact = {
                    "name": f"{person.get_attribute('first_name', '')} {person.get_attribute('last_name', '')}".strip(),
                    "email": email or "",
                    "phone": phone or "",
                    "id": person.id,
                }
                contacts.append(contact)

        # Sort by name
        contacts.sort(key=lambda x: x["name"])

        # Save to CSV
        if contacts:
            output_file = Path("contact_list.csv")
            with open(output_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["name", "email", "phone", "id"])
                writer.writeheader()
                writer.writerows(contacts)

            print(f"Exported {len(contacts)} contacts to {output_file}")


if __name__ == "__main__":
    print("Planning Center API - Data Export Examples")
    print("=" * 50)

    # Run export examples
    asyncio.run(export_people_to_json())
    print()
    asyncio.run(export_people_to_csv())
    print()
    asyncio.run(export_services_and_plans())
    print()
    asyncio.run(generate_people_report())
    print()
    asyncio.run(batch_process_people())
    print()
    asyncio.run(export_contact_list())

    print("\nExport completed! Check the generated files.")
