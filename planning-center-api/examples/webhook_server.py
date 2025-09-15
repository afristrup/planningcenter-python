"""Webhook server example using FastAPI."""

from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from planning_center_api import PCOClient, WebhookEventTypes, handle_webhook_event
from planning_center_api.models.base import PCOWebhookEvent

# Initialize FastAPI app
app = FastAPI(title="Planning Center Webhook Server")

# Initialize client (you'll need to set your credentials)
client = PCOClient(
    app_id="your_app_id", secret="your_secret", webhook_secret="your_webhook_secret"
)

# In-memory storage for webhook events (use a database in production)
webhook_storage: dict[str, Any] = {}


async def person_created_handler(webhook_event: PCOWebhookEvent):
    """Handle person created events."""
    print(
        f"New person created: {webhook_event.resource.attributes.get('first_name')} {webhook_event.resource.attributes.get('last_name')}"
    )

    # Store the event
    event_key = f"person_created_{webhook_event.resource.id}_{webhook_event.timestamp.isoformat()}"
    webhook_storage[event_key] = {
        "event_type": webhook_event.event_type,
        "resource": webhook_event.resource.model_dump(),
        "timestamp": webhook_event.timestamp.isoformat(),
    }

    # You could also trigger other actions here, like:
    # - Send welcome email
    # - Add to mailing list
    # - Create user account in another system
    # - Log to analytics


async def person_updated_handler(webhook_event: PCOWebhookEvent):
    """Handle person updated events."""
    print(
        f"Person updated: {webhook_event.resource.attributes.get('first_name')} {webhook_event.resource.attributes.get('last_name')}"
    )

    # Store the event
    event_key = f"person_updated_{webhook_event.resource.id}_{webhook_event.timestamp.isoformat()}"
    webhook_storage[event_key] = {
        "event_type": webhook_event.event_type,
        "resource": webhook_event.resource.model_dump(),
        "timestamp": webhook_event.timestamp.isoformat(),
    }


async def email_created_handler(webhook_event: PCOWebhookEvent):
    """Handle email created events."""
    print(f"New email added: {webhook_event.resource.attributes.get('address')}")

    # Store the event
    event_key = f"email_created_{webhook_event.resource.id}_{webhook_event.timestamp.isoformat()}"
    webhook_storage[event_key] = {
        "event_type": webhook_event.event_type,
        "resource": webhook_event.resource.model_dump(),
        "timestamp": webhook_event.timestamp.isoformat(),
    }


async def service_created_handler(webhook_event: PCOWebhookEvent):
    """Handle service created events."""
    print(f"New service created: {webhook_event.resource.attributes.get('name')}")

    # Store the event
    event_key = f"service_created_{webhook_event.resource.id}_{webhook_event.timestamp.isoformat()}"
    webhook_storage[event_key] = {
        "event_type": webhook_event.event_type,
        "resource": webhook_event.resource.model_dump(),
        "timestamp": webhook_event.timestamp.isoformat(),
    }


@app.post("/webhook")
async def webhook_handler(request: Request):
    """Handle incoming webhook events from Planning Center."""
    try:
        # Get the raw payload
        payload = await request.body()
        payload_str = payload.decode("utf-8")

        # Get the signature from headers
        signature = request.headers.get("x-pco-signature")

        # Define event handlers
        event_handlers = {
            WebhookEventTypes.PEOPLE_CREATED: person_created_handler,
            WebhookEventTypes.PEOPLE_UPDATED: person_updated_handler,
            WebhookEventTypes.EMAILS_CREATED: email_created_handler,
            WebhookEventTypes.SERVICES_CREATED: service_created_handler,
        }

        # Handle the webhook event
        result = await handle_webhook_event(
            client=client,
            payload=payload_str,
            signature=signature,
            event_handlers=event_handlers,
            verify_signature=True,
        )

        return JSONResponse(
            status_code=200, content={"status": "success", "result": result}
        )

    except Exception as e:
        print(f"Webhook error: {e}")
        return JSONResponse(
            status_code=400, content={"status": "error", "message": str(e)}
        )


@app.get("/webhooks")
async def get_webhook_events():
    """Get all stored webhook events."""
    return JSONResponse(
        status_code=200,
        content={
            "count": len(webhook_storage),
            "events": list(webhook_storage.values()),
        },
    )


@app.get("/webhooks/{event_type}")
async def get_webhook_events_by_type(event_type: str):
    """Get webhook events by type."""
    filtered_events = {
        key: event
        for key, event in webhook_storage.items()
        if event["event_type"] == event_type
    }

    return JSONResponse(
        status_code=200,
        content={
            "event_type": event_type,
            "count": len(filtered_events),
            "events": list(filtered_events.values()),
        },
    )


@app.delete("/webhooks")
async def clear_webhook_events():
    """Clear all stored webhook events."""
    webhook_storage.clear()
    return JSONResponse(
        status_code=200,
        content={"status": "success", "message": "All webhook events cleared"},
    )


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return JSONResponse(
        status_code=200,
        content={
            "message": "Planning Center Webhook Server",
            "endpoints": {
                "webhook": "POST /webhook - Receive webhook events",
                "events": "GET /webhooks - Get all webhook events",
                "events_by_type": "GET /webhooks/{event_type} - Get events by type",
                "clear": "DELETE /webhooks - Clear all events",
            },
        },
    )


if __name__ == "__main__":
    import uvicorn

    print("Starting Planning Center Webhook Server...")
    print("Make sure to set your credentials in the client initialization above.")
    print("Server will be available at http://localhost:8000")
    print("Webhook endpoint: http://localhost:8000/webhook")

    uvicorn.run(app, host="0.0.0.0", port=8000)
