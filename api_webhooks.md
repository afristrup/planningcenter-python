# Webhooks

AvailableEvent
Collection Only
An event supported by webhooks

Example Request
curl https://api.planningcenteronline.com/webhooks/v2/available_events
View in API Explorer
Example Object
{
  "type": "AvailableEvent",
  "id": "1",
  "attributes": {
    "name": "string",
    "app": "string",
    "version": "string",
    "type": "string",
    "resource": "string",
    "action": "string"
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
name
string
app
string
version
string
type
string
resource
string
action
string
URL Parameters
Pagination
Name
Parameter
Type
Description
per_page
per_page
integer
how many records to return per page (min=1, max=100, default=25)
offset
offset
integer
get results from given offset
Endpoints
Listing
HTTP Method
Endpoint
GET
/webhooks/v2/available_events

Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/webhooks/v2/available_events

Organization

---


Delivery
Example Request
curl https://api.planningcenteronline.com/webhooks/v2/webhook_subscriptions/{webhook_subscription_id}/events/{event_id}/deliveries
View in API Explorer
Example Object
{
  "type": "Delivery",
  "id": "1",
  "attributes": {
    "status": 1,
    "request_headers": "string",
    "request_body": "string",
    "response_headers": "string",
    "response_body": "string",
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "timing": 1.42,
    "object_url": "string"
  },
  "relationships": {
    "event": {
      "data": {
        "type": "Event",
        "id": "1"
      }
    }
  }
}
Attributes
Name
Type
Description
id
primary_key
status
integer
request_headers
string
request_body
string
response_headers
string
response_body
string
created_at
date_time
updated_at
date_time
timing
float
object_url
string
Relationships
Name
Type
Association Type
Note
event
Event
to_one
URL Parameters
Order By
Parameter
Value
Type
Description
order
created_at
string
prefix with a hyphen (-created_at) to reverse the order
Pagination
Name
Parameter
Type
Description
per_page
per_page
integer
how many records to return per page (min=1, max=100, default=25)
offset
offset
integer
get results from given offset
Endpoints
Listing
HTTP Method
Endpoint
GET
/webhooks/v2/webhook_subscriptions/{webhook_subscription_id}/events/{event_id}/deliveries

Reading
HTTP Method
Endpoint
GET
/webhooks/v2/webhook_subscriptions/{webhook_subscription_id}/events/{event_id}/deliveries/{id}

Belongs To
Event
HTTP Method
Endpoint
Association
Details
Filter By
GET
/webhooks/v2/webhook_subscriptions/{webhook_subscription_id}/events/{event_id}/deliveries

Event


----

Event
Example Request
curl https://api.planningcenteronline.com/webhooks/v2/webhook_subscriptions/{webhook_subscription_id}/events
View in API Explorer
Example Object
{
  "type": "Event",
  "id": "1",
  "attributes": {
    "created_at": "2000-01-01T12:00:00Z",
    "status": "value",
    "updated_at": "2000-01-01T12:00:00Z",
    "uuid": "string",
    "payload": "string"
  },
  "relationships": {
    "subscription": {
      "data": {
        "type": "Subscription",
        "id": "1"
      }
    },
    "person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    }
  }
}
Attributes
Name
Type
Description
Note
id
primary_key
created_at
date_time
status
string
Possible values: pending, delivered, failed, skipped, duplicated, ignored_failed, ignored_skipped, or ignored_duplicated

updated_at
date_time
uuid
string
payload
string
A string encoded JSON object. E.G. "{\"data\":{...}}"

Relationships
Name
Type
Association Type
Note
subscription
Subscription
to_one
person
Person
to_one
URL Parameters
Order By
Parameter
Value
Type
Description
order
created_at
string
prefix with a hyphen (-created_at) to reverse the order
Query By
Name
Parameter
Type
Description
Example
status
where[status]
string
Query on a specific status

Possible values: pending, delivered, failed, skipped, duplicated, ignored_failed, ignored_skipped, or ignored_duplicated

?where[status]=value
uuid
where[uuid]
string
Query on a specific uuid

?where[uuid]=string
Pagination
Name
Parameter
Type
Description
per_page
per_page
integer
how many records to return per page (min=1, max=100, default=25)
offset
offset
integer
get results from given offset
Endpoints
Listing
HTTP Method
Endpoint
GET
/webhooks/v2/webhook_subscriptions/{webhook_subscription_id}/events

Reading
HTTP Method
Endpoint
GET
/webhooks/v2/webhook_subscriptions/{webhook_subscription_id}/events/{id}

Actions
ignore
HTTP Method
Endpoint
POST
/webhooks/v2/webhook_subscriptions/{webhook_subscription_id}/events/{event_id}/ignore

Permissions:

Must be authenticated

redeliver
HTTP Method
Endpoint
POST
/webhooks/v2/webhook_subscriptions/{webhook_subscription_id}/events/{event_id}/redeliver

Permissions:

Must be authenticated

Associations
deliveries
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/webhooks/v2/webhook_subscriptions/{webhook_subscription_id}/events/{event_id}/deliveries

Delivery
Belongs To
WebhookSubscription
HTTP Method
Endpoint
Association
Details
Filter By
GET
/webhooks/v2/webhook_subscriptions/{webhook_subscription_id}/events

WebhookSubscription


---


Organization
Example Request
curl https://api.planningcenteronline.com/webhooks/v2
View in API Explorer
Example Object
{
  "type": "Organization",
  "id": "1",
  "attributes": {},
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
URL Parameters
Pagination
Name
Parameter
Type
Description
per_page
per_page
integer
how many records to return per page (min=1, max=100, default=25)
offset
offset
integer
get results from given offset
Endpoints
Listing
HTTP Method
Endpoint
GET
/webhooks/v2

Reading
HTTP Method
Endpoint
GET
/webhooks/v2/{id}

Associations
available_events
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/webhooks/v2/available_events

AvailableEvent
webhook_subscriptions
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/webhooks/v2/webhook_subscriptions

WebhookSubscription


---


WebhookSubscription
Example Request
curl https://api.planningcenteronline.com/webhooks/v2/webhook_subscriptions
View in API Explorer
Example Object
{
  "type": "WebhookSubscription",
  "id": "1",
  "attributes": {
    "name": "string",
    "url": "string",
    "active": true,
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "authenticity_secret": "string",
    "application_id": "string"
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
name
string
url
string
active
boolean
created_at
date_time
updated_at
date_time
authenticity_secret
string
Every delivery will include a header X-PCO-Webhooks-Authenticity.

This header will be the HMAC-SHA256 value of this the authenticity_secret used as the key, and the message as the webhook body.

hmac_sha256(authenticity_secret, webhook_body)

application_id
string
URL Parameters
Query By
Name
Parameter
Type
Description
Example
application_id
where[application_id]
string
Query on a specific application_id

?where[application_id]=string
Pagination
Name
Parameter
Type
Description
per_page
per_page
integer
how many records to return per page (min=1, max=100, default=25)
offset
offset
integer
get results from given offset
Endpoints
Listing
HTTP Method
Endpoint
GET
/webhooks/v2/webhook_subscriptions

Reading
HTTP Method
Endpoint
GET
/webhooks/v2/webhook_subscriptions/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/webhooks/v2/webhook_subscriptions

name
url
active
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/webhooks/v2/webhook_subscriptions/{id}

active
Deleting
HTTP Method
Endpoint
DELETE
/webhooks/v2/webhook_subscriptions/{id}

Actions
rotate_secret
HTTP Method
Endpoint
POST
/webhooks/v2/webhook_subscriptions/{webhook_subscription_id}/rotate_secret

Permissions:

Must be authenticated

Associations
events
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/webhooks/v2/webhook_subscriptions/{webhook_subscription_id}/events

Event
Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/webhooks/v2/webhook_subscriptions

Organization