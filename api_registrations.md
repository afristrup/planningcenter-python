# Registrations

----


Attendee
An Attendee is a person registered for a signup.

Example Request
curl https://api.planningcenteronline.com/registrations/v2/signups/{signup_id}/attendees
View in API Explorer
Example Object
{
  "type": "Attendee",
  "id": "1",
  "attributes": {
    "complete": true,
    "active": true,
    "canceled": true,
    "waitlisted": true,
    "waitlisted_at": "2000-01-01T12:00:00Z",
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z"
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
complete
boolean
Whether or not attendee has completed all necessary items (personal information, questions, forms, add ons).

Only available when requested with the ?fields param

active
boolean
Whether or not the attendee is active.

canceled
boolean
Whether or not the attendee is canceled.

waitlisted
boolean
Whether or not the attendee is waitlisted.

waitlisted_at
date_time
UTC time at which the attendee was waitlisted.

created_at
date_time
updated_at
date_time
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
emergency_contact
include associated emergency_contact
include
person
include associated person
include
registration
include associated registration
include
selection_type
include associated selection_type
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
/registrations/v2/signups/{signup_id}/attendees

Notes:
Organization admins can see all attendees for all signups. Signup managers can only see the attendees for signups they manage.

Reading
HTTP Method
Endpoint
GET
/registrations/v2/signups/{signup_id}/attendees/{id}

Notes:
Organization admins can see all attendees for all signups. Signup managers can only see the attendees for signups they manage.

Associations
emergency_contact
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/attendees/{attendee_id}/emergency_contact

EmergencyContact
person
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/attendees/{attendee_id}/person

Person
registration
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/attendees/{attendee_id}/registration

Registration
selection_type
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/attendees/{attendee_id}/selection_type

SelectionType
Belongs To
Signup
HTTP Method
Endpoint
Association
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/attendees

Signup
active

canceled

waitlist


---


Campus
A Campus is a location belonging to an Organization.

Example Request
curl https://api.planningcenteronline.com/registrations/v2/campuses
View in API Explorer
Example Object
{
  "type": "Campus",
  "id": "1",
  "attributes": {
    "name": "string",
    "street": "string",
    "city": "string",
    "state": "string",
    "zip": "string",
    "country": "string",
    "full_formatted_address": "string",
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z"
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
Name of the campus.

street
string
Street address of the campus.

city
string
City where the campus is located.

state
string
State or province where the campus is located.

zip
string
Zip code of the campus.

country
string
Country where the campus is located.

full_formatted_address
string
created_at
date_time
updated_at
date_time
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
/registrations/v2/campuses

Reading
HTTP Method
Endpoint
GET
/registrations/v2/campuses/{id}

Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/registrations/v2/campuses

Organization
Signup
HTTP Method
Endpoint
Association
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/campuses

Signup

----


Category
A Category is a label used to group together and find signups more easily.

Example Request
curl https://api.planningcenteronline.com/registrations/v2/categories
View in API Explorer
Example Object
{
  "type": "Category",
  "id": "1",
  "attributes": {
    "name": "string",
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z"
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
Name of the category.

created_at
date_time
updated_at
date_time
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
/registrations/v2/categories

Reading
HTTP Method
Endpoint
GET
/registrations/v2/categories/{id}

Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/registrations/v2/categories

Organization
Signup
HTTP Method
Endpoint
Association
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/categories

Signup


----


EmergencyContact
Emergency_Contact is the person assigned as the emergency contact for an attendee.

Example Request
curl https://api.planningcenteronline.com/registrations/v2/signups/{signup_id}/attendees/{attendee_id}/emergency_contact
View in API Explorer
Example Object
{
  "type": "EmergencyContact",
  "id": "1",
  "attributes": {
    "name": "string",
    "phone_number": "string"
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
phone_number
string
Phone number of the emergency contact person.

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
/registrations/v2/signups/{signup_id}/attendees/{attendee_id}/emergency_contact

Reading
HTTP Method
Endpoint
GET
/registrations/v2/signups/{signup_id}/attendees/{attendee_id}/emergency_contact/{id}

Belongs To
Attendee
HTTP Method
Endpoint
Association
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/attendees/{attendee_id}/emergency_contact

Attendee


----

Organization
The root level Organization record which serves as a link to Signups.

Example Request
curl https://api.planningcenteronline.com/registrations/v2
View in API Explorer
Example Object
{
  "type": "Organization",
  "id": "1",
  "attributes": {
    "name": "string",
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z"
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
Name of the Organization.

created_at
date_time
updated_at
date_time
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
/registrations/v2

Reading
HTTP Method
Endpoint
GET
/registrations/v2/{id}

Associations
campuses
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/campuses

Campus
categories
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/categories

Category
signups
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/signups

Signup
archived

unarchived


----


Person
Example Request
curl https://api.planningcenteronline.com/registrations/v2/signups/{signup_id}/attendees/{attendee_id}/person
View in API Explorer
Example Object
{
  "type": "Person",
  "id": "1",
  "attributes": {
    "first_name": "string",
    "last_name": "string",
    "name": "string"
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
first_name
string
last_name
string
name
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
/registrations/v2/signups/{signup_id}/attendees/{attendee_id}/person

Reading
HTTP Method
Endpoint
GET
/registrations/v2/signups/{signup_id}/attendees/{attendee_id}/person/{id}

Belongs To
Attendee
HTTP Method
Endpoint
Association
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/attendees/{attendee_id}/person

Attendee
Registration
HTTP Method
Endpoint
Association
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/registrations/{registration_id}/created_by

Registration
Registration
HTTP Method
Endpoint
Association
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/registrations/{registration_id}/registrant_contact

Registration


----


Registration
Example Request
curl https://api.planningcenteronline.com/registrations/v2/signups/{signup_id}/registrations
View in API Explorer
Example Object
{
  "type": "Registration",
  "id": "1",
  "attributes": {
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z"
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
created_at
date_time
updated_at
date_time
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
created_by
include associated created_by
include
registrant_contact
include associated registrant_contact
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
/registrations/v2/signups/{signup_id}/registrations

Notes:
Organization admins can see all registrations for all signups. Signup managers can only see the registrations for signups they manage.

Reading
HTTP Method
Endpoint
GET
/registrations/v2/signups/{signup_id}/registrations/{id}

Notes:
Organization admins can see all registrations for all signups. Signup managers can only see the registrations for signups they manage.

Associations
created_by
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/registrations/{registration_id}/created_by

Person
registrant_contact
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/registrations/{registration_id}/registrant_contact

Person
Belongs To
Attendee
HTTP Method
Endpoint
Association
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/attendees/{attendee_id}/registration

Attendee
Signup
HTTP Method
Endpoint
Association
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/registrations

Signup


----

SelectionType
Selection_Types are used to present the options people register for in a signup.

Example Request
curl https://api.planningcenteronline.com/registrations/v2/signups/{signup_id}/selection_types
View in API Explorer
Example Object
{
  "type": "SelectionType",
  "id": "1",
  "attributes": {
    "name": "string",
    "publicly_available": true,
    "price_cents": 1,
    "price_currency": "string",
    "price_currency_symbol": "string",
    "price_formatted": "string",
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z"
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
Name of the selection type.

publicly_available
boolean
Whether or not the selection type is available to the public.

price_cents
integer
Price of selection type in cents.

price_currency
string
Signup currency code, example "USD".

Only available when requested with the ?fields param

price_currency_symbol
string
Signup currency symbol, example "$".

Only available when requested with the ?fields param

price_formatted
string
Price of selection type with currency formatting (symbol not included).

Only available when requested with the ?fields param

created_at
date_time
updated_at
date_time
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
/registrations/v2/signups/{signup_id}/selection_types

Notes:
Organization admins can see all selection types for all signups. Signup managers can only see the selection types for signups they manage.

Reading
HTTP Method
Endpoint
GET
/registrations/v2/signups/{signup_id}/selection_types/{id}

Notes:
Organization admins can see all selection types for all signups. Signup managers can only see the selection types for signups they manage.

Belongs To
Attendee
HTTP Method
Endpoint
Association
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/attendees/{attendee_id}/selection_type

Attendee


----

Signup
A Signup is an organization signup that people can register for.

Example Request
curl https://api.planningcenteronline.com/registrations/v2/signups
View in API Explorer
Example Object
{
  "type": "Signup",
  "id": "1",
  "attributes": {
    "archived": true,
    "close_at": "2000-01-01T12:00:00Z",
    "description": "string",
    "logo_url": "string",
    "name": "string",
    "new_registration_url": "string",
    "open_at": "2000-01-01T12:00:00Z",
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z"
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
archived
boolean
Whether the signup is archived or not.

close_at
date_time
UTC time at which regsitration closes.

description
string
Decription of the signup.

logo_url
string
URL for the image used for the signup.

name
string
Name of the signup.

new_registration_url
string
URL to allow people to register for signup.

open_at
date_time
UTC time at which regsitration opens.

created_at
date_time
updated_at
date_time
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
campuses
include associated campuses
include
categories
include associated categories
include
next_signup_time
include associated next_signup_time
include
signup_location
include associated signup_location
include
signup_times
include associated signup_times
Query By
Name
Parameter
Type
Description
Example
id
where[id]
primary_key
Query on a specific id

?where[id]=primary_key
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
/registrations/v2/signups

Notes:
Organization admins can see all signups. Signup managers can only see the signups they manage.

Reading
HTTP Method
Endpoint
GET
/registrations/v2/signups/{id}

Notes:
Organization admins can see all signups. Signup managers can only see the signups they manage.

Associations
attendees
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/attendees

Attendee
active

canceled

waitlist

campuses
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/campuses

Campus
categories
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/categories

Category
next_signup_time
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/next_signup_time

SignupTime
registrations
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/registrations

Registration
selection_types
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/selection_types

SelectionType
publicly_available

signup_location
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/signup_location

SignupLocation
signup_times
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/signup_times

SignupTime
future

past

Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/registrations/v2/signups

Organization
archived

unarchived


----


SignupLocation
Signup_location is the location of a signup.

Example Request
curl https://api.planningcenteronline.com/registrations/v2/signups/{signup_id}/signup_location
View in API Explorer
Example Object
{
  "type": "SignupLocation",
  "id": "1",
  "attributes": {
    "name": "string",
    "address_data": "json",
    "subpremise": "string",
    "latitude": "string",
    "longitude": "string",
    "location_type": "string",
    "url": "string",
    "formatted_address": "string",
    "full_formatted_address": "string",
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z"
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
The name of the signup location.

address_data
json
The address data of the signup location, which includes details like street, city, state, and postal code.

Only available when requested with the ?fields param

subpremise
string
The subpremise of the signup location, such as an building or room number.

latitude
string
The latitude of the signup location.

longitude
string
The longitude of the signup location.

location_type
string
The type of location, such as address, coords, or online.

url
string
The URL for the signup location, if applicable (e.g., for online events).

formatted_address
string
The formatted address of the signup location, which may not include subpremise details.

full_formatted_address
string
The fully formatted address of the signup location, including subpremise details.

created_at
date_time
updated_at
date_time
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
/registrations/v2/signups/{signup_id}/signup_location

Notes:
Organization admins can see signup locations for all signups. Signup managers can only see signup locations for signups they manage.

Reading
HTTP Method
Endpoint
GET
/registrations/v2/signups/{signup_id}/signup_location/{id}

Notes:
Organization admins can see signup locations for all signups. Signup managers can only see signup locations for signups they manage.

Belongs To
Signup
HTTP Method
Endpoint
Association
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/signup_location

Signup


----

SignupTime
Signup_times are associated with a signup, which can have multiple signup times.

Example Request
curl https://api.planningcenteronline.com/registrations/v2/signups/{signup_id}/next_signup_time
View in API Explorer
Example Object
{
  "type": "SignupTime",
  "id": "1",
  "attributes": {
    "starts_at": "2000-01-01T12:00:00Z",
    "ends_at": "2000-01-01T12:00:00Z",
    "all_day": true,
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z"
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
starts_at
date_time
Start date and time of signup time.

ends_at
date_time
End date and time of signup time.

all_day
boolean
Whether or not the signup time is all day.

created_at
date_time
updated_at
date_time
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
/registrations/v2/signups/{signup_id}/next_signup_time

Notes:
Organization admins can see all signup times for all signups. Signup managers can only see the signup times for signups they manage.

Reading
HTTP Method
Endpoint
GET
/registrations/v2/signups/{signup_id}/next_signup_time/{id}

Notes:
Organization admins can see all signup times for all signups. Signup managers can only see the signup times for signups they manage.

Belongs To
Signup
HTTP Method
Endpoint
Association
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/next_signup_time

Signup
Signup
HTTP Method
Endpoint
Association
Details
Filter By
GET
/registrations/v2/signups/{signup_id}/signup_times

Signup
future

past
