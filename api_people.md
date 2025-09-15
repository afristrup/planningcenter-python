Report
A report is editable liquid syntax that provides a powerful tool for presenting your Lists however you want.

Example Request
curl https://api.planningcenteronline.com/people/v2/reports
View in API Explorer
Example Object
{
  "type": "Report",
  "id": "1",
  "attributes": {
    "name": "string",
    "body": "string",
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
body
string
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
updated_by
include associated updated_by
Order By
Parameter
Value
Type
Description
order
body
string
prefix with a hyphen (-body) to reverse the order
order
created_at
string
prefix with a hyphen (-created_at) to reverse the order
order
name
string
prefix with a hyphen (-name) to reverse the order
order
updated_at
string
prefix with a hyphen (-updated_at) to reverse the order
Query By
Name
Parameter
Type
Description
Example
body
where[body]
string
Query on a specific body

?where[body]=string
created_at
where[created_at]
date_time
Query on a specific created_at

?where[created_at]=2000-01-01T12:00:00Z
name
where[name]
string
Query on a specific name

?where[name]=string
updated_at
where[updated_at]
date_time
Query on a specific updated_at

?where[updated_at]=2000-01-01T12:00:00Z
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
/people/v2/reports

Reading
HTTP Method
Endpoint
GET
/people/v2/reports/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/people/v2/reports

name
body
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/people/v2/reports/{id}

name
body
Deleting
HTTP Method
Endpoint
DELETE
/people/v2/reports/{id}

Associations
created_by
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/reports/{report_id}/created_by

Person
updated_by
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/reports/{report_id}/updated_by

Person
Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/reports

Organization




----


Rule
A rule belongs to a List and groups conditions together.

Example Request
curl https://api.planningcenteronline.com/people/v2/lists/{list_id}/rules
View in API Explorer
Example Object
{
  "type": "Rule",
  "id": "1",
  "attributes": {
    "subset": "string",
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
subset
string
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
conditions
include associated conditions
Order By
Parameter
Value
Type
Description
order
created_at
string
prefix with a hyphen (-created_at) to reverse the order
order
subset
string
prefix with a hyphen (-subset) to reverse the order
order
updated_at
string
prefix with a hyphen (-updated_at) to reverse the order
Query By
Name
Parameter
Type
Description
Example
created_at
where[created_at]
date_time
Query on a specific created_at

?where[created_at]=2000-01-01T12:00:00Z
subset
where[subset]
string
Query on a specific subset

?where[subset]=string
updated_at
where[updated_at]
date_time
Query on a specific updated_at

?where[updated_at]=2000-01-01T12:00:00Z
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
/people/v2/lists/{list_id}/rules

Reading
HTTP Method
Endpoint
GET
/people/v2/lists/{list_id}/rules/{id}

Associations
conditions
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/lists/{list_id}/rules/{rule_id}/conditions

Condition
Belongs To
List
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/lists/{list_id}/rules

List


----


SchoolOption
A school option represents a school name, school type, grades, etc. and can be selected for a person.

Example Request
curl https://api.planningcenteronline.com/people/v2/school_options
View in API Explorer
Example Object
{
  "type": "SchoolOption",
  "id": "1",
  "attributes": {
    "value": "string",
    "sequence": 1,
    "beginning_grade": "string",
    "ending_grade": "string",
    "school_types": []
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
value
string
sequence
integer
beginning_grade
string
ending_grade
string
school_types
array
URL Parameters
Order By
Parameter
Value
Type
Description
order
beginning_grade
string
prefix with a hyphen (-beginning_grade) to reverse the order
order
ending_grade
string
prefix with a hyphen (-ending_grade) to reverse the order
order
sequence
string
prefix with a hyphen (-sequence) to reverse the order
order
value
string
prefix with a hyphen (-value) to reverse the order
Query By
Name
Parameter
Type
Description
Example
beginning_grade
where[beginning_grade]
string
Query on a specific beginning_grade

?where[beginning_grade]=string
ending_grade
where[ending_grade]
string
Query on a specific ending_grade

?where[ending_grade]=string
school_types
where[school_types]
array
Query on a specific school_types

?where[school_types]=[]
sequence
where[sequence]
integer
Query on a specific sequence

?where[sequence]=1
value
where[value]
string
Query on a specific value

?where[value]=string
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
/people/v2/school_options

Reading
HTTP Method
Endpoint
GET
/people/v2/school_options/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/people/v2/school_options

value
sequence
beginning_grade
ending_grade
school_types
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/people/v2/school_options/{id}

value
sequence
beginning_grade
ending_grade
school_types
Deleting
HTTP Method
Endpoint
DELETE
/people/v2/school_options/{id}

Associations
promotes_to_school
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/school_options/{school_option_id}/promotes_to_school

SchoolOption
Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/school_options

Organization
Person
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/people/{person_id}/school

Person
SchoolOption
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/school_options/{school_option_id}/promotes_to_school

SchoolOption

---

ServiceTime
A ServiceTime Resource

Example Request
curl https://api.planningcenteronline.com/people/v2/campuses/{campus_id}/service_times
View in API Explorer
Example Object
{
  "type": "ServiceTime",
  "id": "1",
  "attributes": {
    "start_time": 1,
    "day": "value",
    "description": "string"
  },
  "relationships": {
    "organization": {
      "data": {
        "type": "Organization",
        "id": "1"
      }
    },
    "campus": {
      "data": {
        "type": "Campus",
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
start_time
integer
day
string
Possible values: sunday, monday, tuesday, wednesday, thursday, friday, or saturday

description
string
Relationships
Name
Type
Association Type
Note
organization
Organization
to_one
campus
Campus
to_one
URL Parameters
Order By
Parameter
Value
Type
Description
order
time
string
prefix with a hyphen (-time) to reverse the order
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
/people/v2/campuses/{campus_id}/service_times

Reading
HTTP Method
Endpoint
GET
/people/v2/campuses/{campus_id}/service_times/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/people/v2/campuses/{campus_id}/service_times

start_time
day
description
Notes:
Must be an Organization Administrator

Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/people/v2/campuses/{campus_id}/service_times/{id}

start_time
day
description
Notes:
Must be an Organization Administrator

Deleting
HTTP Method
Endpoint
DELETE
/people/v2/campuses/{campus_id}/service_times/{id}

Notes:
Must be an Organization Administrator

Belongs To
Campus
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/campuses/{campus_id}/service_times

Campus


----

SocialProfile
A social profile represents a members's Twitter, Facebook, or other social media account.

Example Request
curl https://api.planningcenteronline.com/people/v2/social_profiles
View in API Explorer
Example Object
{
  "type": "SocialProfile",
  "id": "1",
  "attributes": {
    "site": "string",
    "url": "string",
    "verified": true,
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
site
string
url
string
verified
boolean
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
person
include associated person
Order By
Parameter
Value
Type
Description
order
created_at
string
prefix with a hyphen (-created_at) to reverse the order
order
site
string
prefix with a hyphen (-site) to reverse the order
order
updated_at
string
prefix with a hyphen (-updated_at) to reverse the order
order
url
string
prefix with a hyphen (-url) to reverse the order
order
verified
string
prefix with a hyphen (-verified) to reverse the order
Query By
Name
Parameter
Type
Description
Example
created_at
where[created_at]
date_time
Query on a specific created_at

?where[created_at]=2000-01-01T12:00:00Z
site
where[site]
string
Query on a specific site

?where[site]=string
updated_at
where[updated_at]
date_time
Query on a specific updated_at

?where[updated_at]=2000-01-01T12:00:00Z
url
where[url]
string
Query on a specific url

?where[url]=string
verified
where[verified]
boolean
Query on a specific verified

?where[verified]=true
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
/people/v2/social_profiles

Reading
HTTP Method
Endpoint
GET
/people/v2/social_profiles/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/people/v2/people/{person_id}/social_profiles

site
url
verified
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/people/v2/social_profiles/{id}

site
url
verified
Deleting
HTTP Method
Endpoint
DELETE
/people/v2/social_profiles/{id}

Associations
person
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/social_profiles/{social_profile_id}/person

Person
Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/social_profiles

Organization
Person
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/people/{person_id}/social_profiles

Person

----

SpamEmailAddress
An email address that is marked as spam

Example Request
curl https://api.planningcenteronline.com/people/v2/spam_email_addresses
View in API Explorer
Example Object
{
  "type": "SpamEmailAddress",
  "id": "1",
  "attributes": {
    "address": "string",
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
address
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
/people/v2/spam_email_addresses

Reading
HTTP Method
Endpoint
GET
/people/v2/spam_email_addresses/{id}

Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/spam_email_addresses

Organization


----

Tab
A tab is a custom tab and groups like field definitions.

Example Request
curl https://api.planningcenteronline.com/people/v2/tabs
View in API Explorer
Example Object
{
  "type": "Tab",
  "id": "1",
  "attributes": {
    "name": "string",
    "sequence": 1,
    "slug": "string"
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
sequence
integer
slug
string
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
field_definitions
include associated field_definitions
include
field_options
include associated field_options
Order By
Parameter
Value
Type
Description
order
name
string
prefix with a hyphen (-name) to reverse the order
order
sequence
string
prefix with a hyphen (-sequence) to reverse the order
order
slug
string
prefix with a hyphen (-slug) to reverse the order
Query By
Name
Parameter
Type
Description
Example
name
where[name]
string
Query on a specific name

?where[name]=string
sequence
where[sequence]
integer
Query on a specific sequence

?where[sequence]=1
slug
where[slug]
string
Query on a specific slug

?where[slug]=string
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
/people/v2/tabs

Reading
HTTP Method
Endpoint
GET
/people/v2/tabs/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/people/v2/tabs

name
sequence
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/people/v2/tabs/{id}

name
sequence
Deleting
HTTP Method
Endpoint
DELETE
/people/v2/tabs/{id}

Associations
field_definitions
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/tabs/{tab_id}/field_definitions

FieldDefinition
with_deleted

field_options
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/tabs/{tab_id}/field_options

FieldOption
Belongs To
FieldDatum
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/field_data/{field_datum_id}/tab

FieldDatum
FieldDefinition
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/field_definitions/{field_definition_id}/tab

FieldDefinition
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/tabs

Organization
with_field_definitions


----


Workflow
A Workflow

Example Request
curl https://api.planningcenteronline.com/people/v2/workflows
View in API Explorer
Example Object
{
  "type": "Workflow",
  "id": "1",
  "attributes": {
    "name": "string",
    "my_ready_card_count": 1,
    "total_ready_card_count": 1,
    "completed_card_count": 1,
    "total_cards_count": 1,
    "total_ready_and_snoozed_card_count": 1,
    "total_steps_count": 1,
    "total_unassigned_steps_count": 1,
    "total_unassigned_card_count": 1,
    "total_overdue_card_count": 1,
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "deleted_at": "2000-01-01T12:00:00Z",
    "archived_at": "2000-01-01T12:00:00Z",
    "campus_id": "primary_key",
    "workflow_category_id": "primary_key",
    "my_overdue_card_count": 1,
    "my_due_soon_card_count": 1,
    "recently_viewed": true
  },
  "relationships": {
    "workflow_category": {
      "data": {
        "type": "WorkflowCategory",
        "id": "1"
      }
    },
    "campus": {
      "data": {
        "type": "Campus",
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
name
string
my_ready_card_count
integer
total_ready_card_count
integer
completed_card_count
integer
total_cards_count
integer
total_ready_and_snoozed_card_count
integer
total_steps_count
integer
total_unassigned_steps_count
integer
total_unassigned_card_count
integer
total_overdue_card_count
integer
created_at
date_time
updated_at
date_time
deleted_at
date_time
archived_at
date_time
campus_id
primary_key
workflow_category_id
primary_key
my_overdue_card_count
integer
Only available when requested with the ?fields param

my_due_soon_card_count
integer
Only available when requested with the ?fields param

recently_viewed
boolean
Relationships
Name
Type
Association Type
Note
workflow_category
WorkflowCategory
to_one
campus
Campus
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
category
include associated category
include
shares
include associated shares
include
steps
include associated steps
Order By
Parameter
Value
Type
Description
order
archived_at
string
prefix with a hyphen (-archived_at) to reverse the order
order
campus_id
string
prefix with a hyphen (-campus_id) to reverse the order
order
created_at
string
prefix with a hyphen (-created_at) to reverse the order
order
deleted_at
string
prefix with a hyphen (-deleted_at) to reverse the order
order
name
string
prefix with a hyphen (-name) to reverse the order
order
updated_at
string
prefix with a hyphen (-updated_at) to reverse the order
order
workflow_category_id
string
prefix with a hyphen (-workflow_category_id) to reverse the order
Query By
Name
Parameter
Type
Description
Example
archived_at
where[archived_at]
date_time
Query on a specific archived_at

?where[archived_at]=2000-01-01T12:00:00Z
campus_id
where[campus_id]
primary_key
Query on a specific campus_id

?where[campus_id]=primary_key
created_at
where[created_at]
date_time
Query on a specific created_at

?where[created_at]=2000-01-01T12:00:00Z
deleted_at
where[deleted_at]
date_time
Query on a specific deleted_at

?where[deleted_at]=2000-01-01T12:00:00Z
id
where[id]
primary_key
Query on a specific id

?where[id]=primary_key
name
where[name]
string
Query on a specific name

?where[name]=string
updated_at
where[updated_at]
date_time
Query on a specific updated_at

?where[updated_at]=2000-01-01T12:00:00Z
workflow_category_id
where[workflow_category_id]
primary_key
Query on a specific workflow_category_id

?where[workflow_category_id]=primary_key
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
/people/v2/workflows

Reading
HTTP Method
Endpoint
GET
/people/v2/workflows/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/people/v2/workflows

name
campus_id
workflow_category_id
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/people/v2/workflows/{id}

name
campus_id
workflow_category_id
Deleting
HTTP Method
Endpoint
DELETE
/people/v2/workflows/{id}

Associations
cards
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/workflows/{workflow_id}/cards

WorkflowCard
category
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/workflows/{workflow_id}/category

WorkflowCategory
shared_people
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/workflows/{workflow_id}/shared_people

Person
shares
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/workflows/{workflow_id}/shares

WorkflowShare
steps
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/workflows/{workflow_id}/steps

WorkflowStep
Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/workflows

Organization
archived

has_my_cards

manage_cards_allowed

not_archived

only_deleted

recently_viewed

unassigned

with_deleted

with_recoverable

with_steps

WorkflowCard
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/workflow

WorkflowCard


----


WorkflowCard
A Card

Example Request
curl https://api.planningcenteronline.com/people/v2/people/{person_id}/workflow_cards
View in API Explorer
Example Object
{
  "type": "WorkflowCard",
  "id": "1",
  "attributes": {
    "snooze_until": "2000-01-01T12:00:00Z",
    "overdue": true,
    "stage": "string",
    "calculated_due_at_in_days_ago": 1,
    "sticky_assignment": true,
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "completed_at": "2000-01-01T12:00:00Z",
    "flagged_for_notification_at": "2000-01-01T12:00:00Z",
    "removed_at": "2000-01-01T12:00:00Z",
    "moved_to_step_at": "2000-01-01T12:00:00Z"
  },
  "relationships": {
    "assignee": {
      "data": {
        "type": "Assignee",
        "id": "1"
      }
    },
    "person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "workflow": {
      "data": {
        "type": "Workflow",
        "id": "1"
      }
    },
    "current_step": {
      "data": {
        "type": "WorkflowStep",
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
snooze_until
date_time
overdue
boolean
stage
string
calculated_due_at_in_days_ago
integer
sticky_assignment
boolean
created_at
date_time
updated_at
date_time
completed_at
date_time
flagged_for_notification_at
date_time
removed_at
date_time
moved_to_step_at
date_time
Relationships
Name
Type
Association Type
Note
assignee
Assignee
to_one
person
Person
to_one
workflow
Workflow
to_one
current_step
WorkflowStep
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
assignee
include associated assignee
create and update
include
current_step
include associated current_step
create and update
include
person
include associated person
create and update
include
workflow
include associated workflow
create and update
Order By
Parameter
Value
Type
Description
order
completed_at
string
prefix with a hyphen (-completed_at) to reverse the order
order
created_at
string
prefix with a hyphen (-created_at) to reverse the order
order
first_name
string
prefix with a hyphen (-first_name) to reverse the order
order
flagged_for_notification_at
string
prefix with a hyphen (-flagged_for_notification_at) to reverse the order
order
last_name
string
prefix with a hyphen (-last_name) to reverse the order
order
moved_to_step_at
string
prefix with a hyphen (-moved_to_step_at) to reverse the order
order
removed_at
string
prefix with a hyphen (-removed_at) to reverse the order
order
stage
string
prefix with a hyphen (-stage) to reverse the order
order
updated_at
string
prefix with a hyphen (-updated_at) to reverse the order
Query By
Name
Parameter
Type
Description
Example
assignee_id
where[assignee_id]
integer
Query on a related assignee

?where[assignee_id]=1
overdue
where[overdue]
boolean
Query on a specific overdue

?where[overdue]=true
stage
where[stage]
string
Query on a specific stage

?where[stage]=string
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
/people/v2/people/{person_id}/workflow_cards

Reading
HTTP Method
Endpoint
GET
/people/v2/people/{person_id}/workflow_cards/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/people/v2/workflows/{workflow_id}/cards

sticky_assignment
assignee_id
person_id
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/people/v2/people/{person_id}/workflow_cards/{id}

sticky_assignment
assignee_id
person_id
Deleting
HTTP Method
Endpoint
DELETE
/people/v2/people/{person_id}/workflow_cards/{id}

Actions
go_back
HTTP Method
Endpoint
Description
POST
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/go_back

Move a Workflow Card back to the previous step.

Permissions:

Must be authenticated

promote
HTTP Method
Endpoint
Description
POST
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/promote

Move a Workflow Card to the next step.

Permissions:

Must be authenticated

remove
HTTP Method
Endpoint
Description
POST
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/remove

Removes a card

Permissions:

Must be authenticated

restore
HTTP Method
Endpoint
Description
POST
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/restore

Restore a card

Permissions:

Must be authenticated

send_email
HTTP Method
Endpoint
Description
POST
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/send_email

Sends an email to the subject of the card

Details:

Pass in a subject and note.

Example Post Body:

{
  "data": {
    "attributes": {
      "subject": "Thanks for visiting this past Sunday!",
      "note": "It was great to meet you this past Sunday! Hope to see you again."
    }
  }
}
Permissions:

Must be authenticated

skip_step
HTTP Method
Endpoint
Description
POST
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/skip_step

Move a Workflow Card to the next step without completing the current step.

Permissions:

Must be authenticated

snooze
HTTP Method
Endpoint
Description
POST
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/snooze

Snoozes a card for a specific duration

Details:

Pass in a duration in days.

Example Post Body:

{
  "data": {
    "attributes": {
      "duration": 15
    }
  }
}
Permissions:

Must be an editor or the person the card is assigned to

unsnooze
HTTP Method
Endpoint
Description
POST
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/unsnooze

Unsnoozes a card

Permissions:

Must be authenticated

Associations
activities
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/activities

WorkflowCardActivity
assignee
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/assignee

Person
current_step
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/current_step

WorkflowStep
notes
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/notes

WorkflowCardNote
person
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/person

Person
workflow
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/workflow

Workflow
Belongs To
Person
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/people/{person_id}/workflow_cards

Person
assigned

Workflow
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/workflows/{workflow_id}/cards

Workflow

----


WorkflowCardActivity
Workflow Card Activity is a record of an action performed on a card

Example Request
curl https://api.planningcenteronline.com/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/activities
View in API Explorer
Example Object
{
  "type": "WorkflowCardActivity",
  "id": "1",
  "attributes": {
    "comment": "string",
    "content": "string",
    "form_submission_url": "string",
    "automation_url": "string",
    "person_avatar_url": "string",
    "person_name": "string",
    "reassigned_to_avatar_url": "string",
    "reassigned_to_name": "string",
    "subject": "string",
    "type": "string",
    "content_is_html": true,
    "created_at": "2000-01-01T12:00:00Z"
  },
  "relationships": {
    "workflow_card": {
      "data": {
        "type": "WorkflowCard",
        "id": "1"
      }
    },
    "workflow_step": {
      "data": {
        "type": "WorkflowStep",
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
comment
string
content
string
form_submission_url
string
automation_url
string
person_avatar_url
string
person_name
string
reassigned_to_avatar_url
string
reassigned_to_name
string
subject
string
type
string
content_is_html
boolean
created_at
date_time
Relationships
Name
Type
Association Type
Note
workflow_card
WorkflowCard
to_one
workflow_step
WorkflowStep
to_one
Only available when type attribute is completion, skip, or reversal.

URL Parameters
Order By
Parameter
Value
Type
Description
order
id
string
prefix with a hyphen (-id) to reverse the order
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
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/activities

Reading
HTTP Method
Endpoint
GET
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/activities/{id}

Deleting
HTTP Method
Endpoint
DELETE
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/activities/{id}

Belongs To
WorkflowCard
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/activities

WorkflowCard

----


WorkflowCardNote
Workflow Note is a note that has been made on a Workflow Card

Example Request
curl https://api.planningcenteronline.com/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/notes
View in API Explorer
Example Object
{
  "type": "WorkflowCardNote",
  "id": "1",
  "attributes": {
    "note": "string",
    "created_at": "2000-01-01T12:00:00Z"
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
note
string
created_at
date_time
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
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/notes

Reading
HTTP Method
Endpoint
GET
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/notes/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/notes

note
Notes:
If you want to also create a matching profile note in the note category of your choice, pass in the ID of the note category.

    {
      "data": {
        "attributes": {
          "note": "this is a new note!",
          "note_category_id": 123
        }
      }
    }
The note_category_id is not actually stored on the workflow card note itself, so if you need to edit or delete the resulting profile note, you will need to do so via people/v2/notes.

You can GET all the existing note categories at /people/v2/note_categories.

Belongs To
WorkflowCard
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/notes

WorkflowCard


----

WorkflowCategory
A Workflow Category

Example Request
curl https://api.planningcenteronline.com/people/v2/workflow_categories
View in API Explorer
Example Object
{
  "type": "WorkflowCategory",
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
created_at
date_time
updated_at
date_time
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
order
name
string
prefix with a hyphen (-name) to reverse the order
order
updated_at
string
prefix with a hyphen (-updated_at) to reverse the order
Query By
Name
Parameter
Type
Description
Example
created_at
where[created_at]
date_time
Query on a specific created_at

?where[created_at]=2000-01-01T12:00:00Z
name
where[name]
string
Query on a specific name

?where[name]=string
updated_at
where[updated_at]
date_time
Query on a specific updated_at

?where[updated_at]=2000-01-01T12:00:00Z
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
/people/v2/workflow_categories

Reading
HTTP Method
Endpoint
GET
/people/v2/workflow_categories/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/people/v2/workflow_categories

name
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/people/v2/workflow_categories/{id}

name
Deleting
HTTP Method
Endpoint
DELETE
/people/v2/workflow_categories/{id}

Belongs To
Workflow
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/workflows/{workflow_id}/category

Workflow


----


WorkflowShare
A workflow share defines who can access a workflow.

Example Request
curl https://api.planningcenteronline.com/people/v2/people/{person_id}/workflow_shares
View in API Explorer
Example Object
{
  "type": "WorkflowShare",
  "id": "1",
  "attributes": {
    "group": "value",
    "permission": "value",
    "person_id": "primary_key"
  },
  "relationships": {
    "person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "workflow": {
      "data": {
        "type": "Workflow",
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
group
string
Possible values: No Access, Viewer, Editor, or Manager

permission
string
Possible values: view, manage_cards, or manage

person_id
primary_key
Relationships
Name
Type
Association Type
Note
person
Person
to_one
workflow
Workflow
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
person
include associated person
create and update
Query By
Name
Parameter
Type
Description
Example
permission
where[permission]
string
Query on a specific permission

Possible values: view, manage_cards, or manage

?where[permission]=value
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
/people/v2/people/{person_id}/workflow_shares

Reading
HTTP Method
Endpoint
GET
/people/v2/people/{person_id}/workflow_shares/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/people/v2/workflows/{workflow_id}/shares

group
permission
person_id
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/people/v2/people/{person_id}/workflow_shares/{id}

group
permission
Deleting
HTTP Method
Endpoint
DELETE
/people/v2/people/{person_id}/workflow_shares/{id}

Associations
person
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/people/{person_id}/workflow_shares/{workflow_share_id}/person

Person
Belongs To
Person
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/people/{person_id}/workflow_shares

Person
Workflow
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/workflows/{workflow_id}/shares

Workflow


---


WorkflowStep
A Step

Example Request
curl https://api.planningcenteronline.com/people/v2/workflows/{workflow_id}/steps
View in API Explorer
Example Object
{
  "type": "WorkflowStep",
  "id": "1",
  "attributes": {
    "sequence": 1,
    "name": "string",
    "description": "string",
    "expected_response_time_in_days": 1,
    "auto_snooze_value": 1,
    "auto_snooze_interval": "value",
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "auto_snooze_days": 1,
    "my_ready_card_count": 1,
    "total_ready_card_count": 1,
    "default_assignee_id": "primary_key"
  },
  "relationships": {
    "default_assignee": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "workflow": {
      "data": {
        "type": "Workflow",
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
sequence
integer
name
string
description
string
expected_response_time_in_days
integer
auto_snooze_value
integer
Must be a positive number

auto_snooze_interval
string
Valid values are day, week, or month

Possible values: day, week, or month

created_at
date_time
updated_at
date_time
auto_snooze_days
integer
my_ready_card_count
integer
total_ready_card_count
integer
default_assignee_id
primary_key
Relationships
Name
Type
Association Type
Note
default_assignee
Person
to_one
workflow
Workflow
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
default_assignee
include associated default_assignee
create and update
Order By
Parameter
Value
Type
Description
order
created_at
string
prefix with a hyphen (-created_at) to reverse the order
order
name
string
prefix with a hyphen (-name) to reverse the order
order
sequence
string
prefix with a hyphen (-sequence) to reverse the order
order
updated_at
string
prefix with a hyphen (-updated_at) to reverse the order
Query By
Name
Parameter
Type
Description
Example
created_at
where[created_at]
date_time
Query on a specific created_at

?where[created_at]=2000-01-01T12:00:00Z
name
where[name]
string
Query on a specific name

?where[name]=string
updated_at
where[updated_at]
date_time
Query on a specific updated_at

?where[updated_at]=2000-01-01T12:00:00Z
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
/people/v2/workflows/{workflow_id}/steps

Reading
HTTP Method
Endpoint
GET
/people/v2/workflows/{workflow_id}/steps/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/people/v2/workflows/{workflow_id}/steps

sequence
name
description
expected_response_time_in_days
default_assignee_id
auto_snooze_value
auto_snooze_interval
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/people/v2/workflows/{workflow_id}/steps/{id}

sequence
name
description
expected_response_time_in_days
default_assignee_id
auto_snooze_value
auto_snooze_interval
Deleting
HTTP Method
Endpoint
DELETE
/people/v2/workflows/{workflow_id}/steps/{id}

Associations
assignee_summaries
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/workflows/{workflow_id}/steps/{workflow_step_id}/assignee_summaries

WorkflowStepAssigneeSummary
default_assignee
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/workflows/{workflow_id}/steps/{workflow_step_id}/default_assignee

Person
Belongs To
WorkflowCard
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/people/{person_id}/workflow_cards/{workflow_card_id}/current_step

WorkflowCard
Workflow
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/workflows/{workflow_id}/steps

Workflow


----


WorkflowStepAssigneeSummary
The ready and snoozed count for an assignee & step

Example Request
curl https://api.planningcenteronline.com/people/v2/workflows/{workflow_id}/steps/{step_id}/assignee_summaries
View in API Explorer
Example Object
{
  "type": "WorkflowStepAssigneeSummary",
  "id": "1",
  "attributes": {
    "ready_count": 1,
    "snoozed_count": 1
  },
  "relationships": {
    "person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "step": {
      "data": {
        "type": "Step",
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
ready_count
integer
snoozed_count
integer
Relationships
Name
Type
Association Type
Note
person
Person
to_one
step
Step
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
person
include associated person
create and update
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
/people/v2/workflows/{workflow_id}/steps/{step_id}/assignee_summaries

Reading
HTTP Method
Endpoint
GET
/people/v2/workflows/{workflow_id}/steps/{step_id}/assignee_summaries/{id}

Associations
person
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/people/v2/workflows/{workflow_id}/steps/{step_id}/assignee_summaries/{workflow_step_assignee_summary_id}/person

Person
Belongs To
WorkflowStep
HTTP Method
Endpoint
Association
Details
Filter By
GET
/people/v2/workflows/{workflow_id}/steps/{workflow_step_id}/assignee_summaries

WorkflowStep