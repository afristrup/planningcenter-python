"""Unit tests for Pydantic models."""

from datetime import datetime

from planning_center_api.models.base import (
    PCOCollection,
    PCOErrorResponse,
    PCOResource,
    PCOWebhookEvent,
    PCOWebhookPayload,
)
from planning_center_api.models.links import PCOLink, PCOLinks
from planning_center_api.models.meta import PCOMeta
from planning_center_api.models.relationships import PCORelationship, PCORelationships


class TestPCOResource:
    """Test PCOResource model."""

    def test_create_resource(self):
        """Test creating a resource."""
        resource = PCOResource(
            id="123",
            type="people",
            attributes={"first_name": "John", "last_name": "Doe"},
        )

        assert resource.id == "123"
        assert resource.type == "people"
        assert resource.attributes["first_name"] == "John"
        assert resource.attributes["last_name"] == "Doe"

    def test_get_attribute(self):
        """Test getting attributes."""
        resource = PCOResource(
            id="123",
            type="people",
            attributes={"first_name": "John", "last_name": "Doe"},
        )

        assert resource.get_attribute("first_name") == "John"
        assert resource.get_attribute("last_name") == "Doe"
        assert resource.get_attribute("email") is None
        assert resource.get_attribute("email", "default") == "default"

    def test_set_attribute(self):
        """Test setting attributes."""
        resource = PCOResource(
            id="123", type="people", attributes={"first_name": "John"}
        )

        resource.set_attribute("last_name", "Doe")
        assert resource.get_attribute("last_name") == "Doe"

    def test_get_relationship_data(self):
        """Test getting relationship data."""
        from planning_center_api.models.relationships import PCORelationship

        relationship = PCORelationship(data={"id": "456", "type": "emails"})

        relationships = PCORelationships()
        relationships.emails = relationship

        resource = PCOResource(
            id="123",
            type="people",
            attributes={"first_name": "John"},
            relationships=relationships,
        )

        data = resource.get_relationship_data("emails")
        assert data == {"id": "456", "type": "emails"}


class TestPCOCollection:
    """Test PCOCollection model."""

    def test_create_collection(self):
        """Test creating a collection."""
        resource1 = PCOResource(id="1", type="people", attributes={"name": "John"})
        resource2 = PCOResource(id="2", type="people", attributes={"name": "Jane"})

        collection = PCOCollection(data=[resource1, resource2])

        assert len(collection) == 2
        assert collection[0].id == "1"
        assert collection[1].id == "2"

    def test_iteration(self):
        """Test iterating over collection."""
        resource1 = PCOResource(id="1", type="people", attributes={"name": "John"})
        resource2 = PCOResource(id="2", type="people", attributes={"name": "Jane"})

        collection = PCOCollection(data=[resource1, resource2])

        ids = [resource.id for resource in collection]
        assert ids == ["1", "2"]

    def test_get_included_resource(self):
        """Test getting included resources."""
        included = PCOResource(
            id="456", type="emails", attributes={"address": "john@example.com"}
        )
        collection = PCOCollection(
            data=[PCOResource(id="1", type="people", attributes={"name": "John"})],
            included=[included],
        )

        email = collection.get_included_resource("emails", "456")
        assert email is not None
        assert email.get_attribute("address") == "john@example.com"

        # Test non-existent resource
        missing = collection.get_included_resource("emails", "999")
        assert missing is None

    def test_get_included_resources(self):
        """Test getting included resources by type."""
        email1 = PCOResource(
            id="1", type="emails", attributes={"address": "john@example.com"}
        )
        email2 = PCOResource(
            id="2", type="emails", attributes={"address": "jane@example.com"}
        )
        phone = PCOResource(
            id="3", type="phone_numbers", attributes={"number": "555-1234"}
        )

        collection = PCOCollection(
            data=[PCOResource(id="1", type="people", attributes={"name": "John"})],
            included=[email1, email2, phone],
        )

        emails = collection.get_included_resources("emails")
        assert len(emails) == 2
        assert emails[0].id == "1"
        assert emails[1].id == "2"

        phones = collection.get_included_resources("phone_numbers")
        assert len(phones) == 1
        assert phones[0].id == "3"


class TestPCOErrorResponse:
    """Test PCOErrorResponse model."""

    def test_create_error_response(self):
        """Test creating an error response."""
        from planning_center_api.models.base import PCOErrorDetail

        error = PCOErrorDetail(
            status="422", title="Validation Error", detail="Name is required"
        )

        error_response = PCOErrorResponse(errors=[error])

        assert len(error_response.errors) == 1
        assert error_response.errors[0].detail == "Name is required"

    def test_get_error_messages(self):
        """Test getting error messages."""
        from planning_center_api.models.base import PCOErrorDetail

        error1 = PCOErrorDetail(detail="Name is required")
        error2 = PCOErrorDetail(title="Validation Error")
        error3 = PCOErrorDetail(detail="Email is invalid")

        error_response = PCOErrorResponse(errors=[error1, error2, error3])

        messages = error_response.get_error_messages()
        assert len(messages) == 3
        assert "Name is required" in messages
        assert "Validation Error" in messages
        assert "Email is invalid" in messages

    def test_get_first_error_message(self):
        """Test getting first error message."""
        from planning_center_api.models.base import PCOErrorDetail

        error1 = PCOErrorDetail(detail="First error")
        error2 = PCOErrorDetail(detail="Second error")

        error_response = PCOErrorResponse(errors=[error1, error2])

        first_message = error_response.get_first_error_message()
        assert first_message == "First error"


class TestPCOWebhookEvent:
    """Test PCOWebhookEvent model."""

    def test_create_webhook_event(self):
        """Test creating a webhook event."""
        resource = PCOWebhookPayload(
            id="123",
            type="people",
            attributes={"first_name": "John", "last_name": "Doe"},
        )

        event = PCOWebhookEvent(
            event_type="people.created", resource=resource, timestamp=datetime.utcnow()
        )

        assert event.event_type == "people.created"
        assert event.resource.id == "123"
        assert event.resource.get_attribute("first_name") == "John"


class TestPCOLinks:
    """Test PCOLinks model."""

    def test_create_links(self):
        """Test creating links."""
        self_link = PCOLink(
            href="https://api.planningcenteronline.com/people/v2/people/123"
        )
        next_link = PCOLink(
            href="https://api.planningcenteronline.com/people/v2/people?page=2"
        )

        links = PCOLinks(self=self_link, next=next_link)

        assert (
            links.self.href
            == "https://api.planningcenteronline.com/people/v2/people/123"
        )
        assert (
            links.next.href
            == "https://api.planningcenteronline.com/people/v2/people?page=2"
        )

    def test_get_pagination_links(self):
        """Test getting pagination links."""
        first_link = PCOLink(
            href="https://api.planningcenteronline.com/people/v2/people?page=1"
        )
        last_link = PCOLink(
            href="https://api.planningcenteronline.com/people/v2/people?page=10"
        )
        prev_link = PCOLink(
            href="https://api.planningcenteronline.com/people/v2/people?page=1"
        )
        next_link = PCOLink(
            href="https://api.planningcenteronline.com/people/v2/people?page=3"
        )

        links = PCOLinks(
            first=first_link, last=last_link, prev=prev_link, next=next_link
        )

        pagination = links.get_pagination_links()
        assert (
            pagination["first"]
            == "https://api.planningcenteronline.com/people/v2/people?page=1"
        )
        assert (
            pagination["last"]
            == "https://api.planningcenteronline.com/people/v2/people?page=10"
        )
        assert (
            pagination["prev"]
            == "https://api.planningcenteronline.com/people/v2/people?page=1"
        )
        assert (
            pagination["next"]
            == "https://api.planningcenteronline.com/people/v2/people?page=3"
        )

    def test_has_next_page(self):
        """Test checking for next page."""
        links_with_next = PCOLinks(next=PCOLink(href="https://example.com/next"))
        links_without_next = PCOLinks()

        assert links_with_next.has_next_page() is True
        assert links_without_next.has_next_page() is False

    def test_has_prev_page(self):
        """Test checking for previous page."""
        links_with_prev = PCOLinks(prev=PCOLink(href="https://example.com/prev"))
        links_without_prev = PCOLinks()

        assert links_with_prev.has_prev_page() is True
        assert links_without_prev.has_prev_page() is False


class TestPCOMeta:
    """Test PCOMeta model."""

    def test_create_meta(self):
        """Test creating meta information."""
        meta = PCOMeta(
            count=25, total_count=100, total_pages=4, current_page=1, per_page=25
        )

        assert meta.count == 25
        assert meta.total_count == 100
        assert meta.total_pages == 4
        assert meta.current_page == 1
        assert meta.per_page == 25

    def test_get_pagination_info(self):
        """Test getting pagination information."""
        meta = PCOMeta(
            count=25, total_count=100, total_pages=4, current_page=1, per_page=25
        )

        info = meta.get_pagination_info()
        assert info["count"] == 25
        assert info["total_count"] == 100
        assert info["total_pages"] == 4
        assert info["current_page"] == 1
        assert info["per_page"] == 25

    def test_has_more_pages(self):
        """Test checking for more pages."""
        meta_with_more = PCOMeta(current_page=1, total_pages=4)
        meta_without_more = PCOMeta(current_page=4, total_pages=4)
        meta_incomplete = PCOMeta(current_page=1)

        assert meta_with_more.has_more_pages() is True
        assert meta_without_more.has_more_pages() is False
        assert meta_incomplete.has_more_pages() is False

    def test_get_remaining_items(self):
        """Test getting remaining items."""
        meta = PCOMeta(count=25, total_count=100)

        remaining = meta.get_remaining_items()
        assert remaining == 75


class TestPCORelationship:
    """Test PCORelationship model."""

    def test_create_relationship(self):
        """Test creating a relationship."""
        relationship = PCORelationship(data={"id": "123", "type": "emails"})

        assert relationship.data == {"id": "123", "type": "emails"}
        assert relationship.is_single_resource() is True
        assert relationship.is_collection() is False

    def test_collection_relationship(self):
        """Test collection relationship."""
        relationship = PCORelationship(
            data=[{"id": "1", "type": "emails"}, {"id": "2", "type": "emails"}]
        )

        assert relationship.is_single_resource() is False
        assert relationship.is_collection() is True

    def test_get_resource_ids(self):
        """Test getting resource IDs."""
        # Single resource
        single_rel = PCORelationship(data={"id": "123", "type": "emails"})
        assert single_rel.get_resource_ids() == ["123"]

        # Collection
        collection_rel = PCORelationship(
            data=[{"id": "1", "type": "emails"}, {"id": "2", "type": "emails"}]
        )
        assert collection_rel.get_resource_ids() == ["1", "2"]

        # Empty
        empty_rel = PCORelationship()
        assert empty_rel.get_resource_ids() == []

    def test_get_resource_types(self):
        """Test getting resource types."""
        # Single resource
        single_rel = PCORelationship(data={"id": "123", "type": "emails"})
        assert single_rel.get_resource_types() == ["emails"]

        # Collection
        collection_rel = PCORelationship(
            data=[{"id": "1", "type": "emails"}, {"id": "2", "type": "phone_numbers"}]
        )
        assert collection_rel.get_resource_types() == ["emails", "phone_numbers"]


class TestPCORelationships:
    """Test PCORelationships model."""

    def test_create_relationships(self):
        """Test creating relationships."""
        email_rel = PCORelationship(data={"id": "1", "type": "emails"})
        phone_rel = PCORelationship(data={"id": "2", "type": "phone_numbers"})

        relationships = PCORelationships()
        relationships.emails = email_rel
        relationships.phone_numbers = phone_rel

        assert relationships["emails"] == email_rel
        assert relationships["phone_numbers"] == phone_rel

    def test_get_relationship(self):
        """Test getting a relationship."""
        email_rel = PCORelationship(data={"id": "1", "type": "emails"})

        relationships = PCORelationships()
        relationships.emails = email_rel

        assert relationships.get_relationship("emails") == email_rel
        assert relationships.get_relationship("nonexistent") is None

    def test_has_relationship(self):
        """Test checking for relationship existence."""
        email_rel = PCORelationship(data={"id": "1", "type": "emails"})

        relationships = PCORelationships()
        relationships.emails = email_rel

        assert relationships.has_relationship("emails") is True
        assert relationships.has_relationship("nonexistent") is False

    def test_get_relationship_data(self):
        """Test getting relationship data."""
        email_rel = PCORelationship(data={"id": "1", "type": "emails"})

        relationships = PCORelationships()
        relationships.emails = email_rel

        data = relationships.get_relationship_data("emails")
        assert data == {"id": "1", "type": "emails"}

        # Non-existent relationship
        missing_data = relationships.get_relationship_data("nonexistent")
        assert missing_data is None
