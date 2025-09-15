# Services

----


Arrangement
Each arrangement belongs to a song and is a different version of that song.

Example Request
curl https://api.planningcenteronline.com/services/v2/songs/{song_id}/arrangements
View in API Explorer
Example Object
{
  "type": "Arrangement",
  "id": "1",
  "attributes": {
    "bpm": 1.42,
    "created_at": "2000-01-01T12:00:00Z",
    "has_chords": true,
    "length": 1,
    "meter": "string",
    "name": "string",
    "notes": "string",
    "print_margin": "string",
    "print_orientation": "string",
    "print_page_size": "string",
    "updated_at": "2000-01-01T12:00:00Z",
    "chord_chart": "string",
    "chord_chart_font": "string",
    "chord_chart_key": "string",
    "chord_chart_columns": 1,
    "chord_chart_font_size": 1,
    "has_chord_chart": true,
    "lyrics_enabled": true,
    "number_chart_enabled": true,
    "numeral_chart_enabled": true,
    "sequence": [],
    "sequence_short": [],
    "sequence_full": [],
    "chord_chart_chord_color": 1,
    "archived_at": "2000-01-01T12:00:00Z",
    "lyrics": "string"
  },
  "relationships": {
    "updated_by": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "created_by": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "song": {
      "data": {
        "type": "Song",
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
bpm
float
created_at
date_time
has_chords
boolean
length
integer
meter
string
Possible Values:

2/2

2/4

3/2

3/4

4/2

4/4

5/4

6/4

3/8

6/8

7/4

7/8

9/8

12/4

12/8

name
string
notes
string
print_margin
string
Possible Values:

0.0in

0.25in

0.5in

0.75in

1.0in

print_orientation
string
Possible Values:

Portrait

Landscape

print_page_size
string
Possible Values:

Widescreen (16x9)

Fullscreen (4x3)

A4

Letter

Legal

11x17

updated_at
date_time
chord_chart
string
A string of lyrics and chords. Supports standard and ChordPro formats.

chord_chart_font
string
chord_chart_key
string
chord_chart_columns
integer
chord_chart_font_size
integer
Possible Values:

10, 11, 12, 13, 14, 15, 16, 18, 20, 22, 24, 26, 28, 32, 36, 42, 48

has_chord_chart
boolean
lyrics_enabled
boolean
number_chart_enabled
boolean
numeral_chart_enabled
boolean
sequence
array
An array of strings containing a label and a number describing the section:

['Verse 1', 'Chorus 1', 'Verse 2']

sequence_short
array
sequence_full
array
chord_chart_chord_color
integer
archived_at
date_time
lyrics
string
Relationships
Name
Type
Association Type
Note
updated_by
Person
to_one
created_by
Person
to_one
song
Song
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
keys
include associated keys
include
sections
include associated sections
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
/services/v2/songs/{song_id}/arrangements

Reading
HTTP Method
Endpoint
GET
/services/v2/songs/{song_id}/arrangements/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/songs/{song_id}/arrangements

bpm
chord_chart
chord_chart_chord_color
chord_chart_columns
chord_chart_font
chord_chart_font_size
chord_chart_key
length
lyrics_enabled
meter
name
notes
number_chart_enabled
numeral_chart_enabled
print_margin
print_orientation
print_page_size
sequence
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/songs/{song_id}/arrangements/{id}

bpm
chord_chart
chord_chart_chord_color
chord_chart_columns
chord_chart_font
chord_chart_font_size
chord_chart_key
length
lyrics_enabled
meter
name
notes
number_chart_enabled
numeral_chart_enabled
print_margin
print_orientation
print_page_size
sequence
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/songs/{song_id}/arrangements/{id}

Actions
assign_tags
HTTP Method
Endpoint
Description
POST
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/assign_tags

Used to assign tags to an arrangement.

Details:

All tags will be replaced so the full data set must be sent.

It expects a body that looks like:

{
	"data": {
		"type": "TagAssignment",
		"attributes": {},
		"relationships": {
			"tags": {
				"data": [
					{
						"type": "Tag",
						"id": "5"
					}
				]
			}
		}
	}
}
On success you will get back a 204 No Content.

Permissions:

Must be authenticated

Associations
attachments
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/attachments

Attachment
keys
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/keys

Key
sections
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/sections

ArrangementSections
tags
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/tags

Tag
Belongs To
Item
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/arrangement

Item
Song
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/songs/{song_id}/arrangements

Song


----


ArrangementSections
Sections of an Arrangement, derived from its chord chart

Example Request
curl https://api.planningcenteronline.com/services/v2/songs/{song_id}/arrangements/{arrangement_id}/sections
View in API Explorer
Example Object
{
  "type": "ArrangementSections",
  "id": "1",
  "attributes": {
    "sections": []
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
sections
array
Given an arrangement with the folowing chord_chart:

VERSE 1
D          Bm       G          D
Be thou my vision O Lord of my heart
A             Bm         G              A
naught be all else to me save that Thou art
The value will be:

[
  {
    "label": "Verse",
    "lyrics": "Be thou my vision O Lord of my heart

naught be all else to me save that Thou art",
    "breaks_at": null
  }
]
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
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/sections

Reading
HTTP Method
Endpoint
GET
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/sections/{id}

Belongs To
Arrangement
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/sections

Arrangement


----


Attachment
A file, whether it's stored on Planning Center or linked from another location.

Example Request
curl https://api.planningcenteronline.com/services/v2/attachments
View in API Explorer
Example Object
{
  "type": "Attachment",
  "id": "1",
  "attributes": {
    "created_at": "2000-01-01T12:00:00Z",
    "page_order": "string",
    "updated_at": "2000-01-01T12:00:00Z",
    "filename": "string",
    "file_size": 1,
    "licenses_purchased": 1,
    "licenses_remaining": 1,
    "licenses_used": 1,
    "content": "string",
    "content_type": "string",
    "display_name": "string",
    "filetype": "string",
    "linked_url": "string",
    "pco_type": "string",
    "remote_link": "string",
    "thumbnail_url": "string",
    "url": "string",
    "allow_mp3_download": true,
    "web_streamable": true,
    "downloadable": true,
    "transposable": true,
    "import_to_item_details": true,
    "streamable": true,
    "has_preview": true,
    "file_upload_identifier": "string",
    "deleted_at": "2000-01-01T12:00:00Z"
  },
  "relationships": {
    "attachable": {
      "data": {
        "type": "Plan",
        "id": "1"
      }
    },
    "attachment_types": {
      "data": [
        {
          "type": "AttachmentType",
          "id": "1"
        }
      ]
    },
    "created_by": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "updated_by": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "administrator": {
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
id
primary_key
created_at
date_time
page_order
string
updated_at
date_time
filename
string
file_size
integer
licenses_purchased
integer
licenses_remaining
integer
licenses_used
integer
content
string
content_type
string
display_name
string
filetype
string
linked_url
string
pco_type
string
remote_link
string
thumbnail_url
string
url
string
allow_mp3_download
boolean
web_streamable
boolean
downloadable
boolean
transposable
boolean
import_to_item_details
boolean
streamable
boolean
has_preview
boolean
file_upload_identifier
string
Planning Center File UUID. Required only when creating a file attachment. See the "File Uploads" section of the API documentation for more information.

Only available when requested with the ?fields param

deleted_at
date_time
Relationships
Name
Type
Association Type
Note
attachable
(polymorphic)
to_one
Type will be the type of resource to which it is attached.

attachment_types
AttachmentType
to_many
created_by
Person
to_one
updated_by
Person
to_one
administrator
Person
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
zooms
include associated zooms
Order By
Parameter
Value
Type
Description
order
attachable_type
string
prefix with a hyphen (-attachable_type) to reverse the order
order
created_at
string
prefix with a hyphen (-created_at) to reverse the order
order
deleted_at
string
prefix with a hyphen (-deleted_at) to reverse the order
order
filename
string
prefix with a hyphen (-filename) to reverse the order
order
filetype
string
prefix with a hyphen (-filetype) to reverse the order
order
size
string
prefix with a hyphen (-size) to reverse the order
Query By
Name
Parameter
Type
Description
Example
administrator_id
where[administrator_id]
integer
Query on a related administrator

?where[administrator_id]=1
licenses_purchased
where[licenses_purchased]
integer
Query on a specific licenses_purchased

?where[licenses_purchased]=1
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
/services/v2/attachments

Reading
HTTP Method
Endpoint
GET
/services/v2/attachments/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/attachments

attachment_type_ids
content
file_upload_identifier
filename
import_to_item_details
remote_link
page_order
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/attachments/{id}

attachment_type_ids
content
file_upload_identifier
filename
import_to_item_details
remote_link
page_order
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/attachments/{id}

Actions
open
HTTP Method
Endpoint
Description
POST
/services/v2/attachments/{attachment_id}/open

This action is used to get the attachment file URL. It is accessed by POSTing to .../attachments/1/open

This will generate the URL and return it in the attachment_url attribute of the AttachmentActivity.

Permissions:

Must be authenticated

preview
HTTP Method
Endpoint
Description
POST
/services/v2/attachments/{attachment_id}/preview

This action is used to get a reduced resolution (preview) version of the attachment. It is accessed by POSTing to .../attachments/1/preview

This will generate the URL and return it in the attachment_url attribute of the AttachmentActivity.

The has_preview attribute of an Attachment indicates if a preview is available. When a preview is not available this action will return a Not Found error with a status code of 404.

Permissions:

Must be authenticated

Associations
zooms
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/attachments/{attachment_id}/zooms

Zoom
Belongs To
Arrangement
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/attachments

Arrangement
Item
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/attachments

Item
Item
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/selected_attachment

Item
Item
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/selected_background

Item
Key
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/keys/{key_id}/attachments

Key
Media
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/media/{media_id}/attachments

Media
Plan
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/all_attachments

Plan
attachable_type — filter attachments by their attachable_type as specified in the attachable_type parameter. Default: ["ServiceType", "Plan", "Item", "Media", "Song", "Arrangement", "Key"]. e.g. ?filter=attachable_type&attachable_type=Plan,ServiceType

extensions — filter to attachments with a file extension specified in the extensions parameter. e.g. ?filter=extensions&extensions=pdf,txt

Plan
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/attachments

Plan
ServiceType
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/attachments

ServiceType
Song
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/songs/{song_id}/attachments

Song


----


AttachmentActivity
Collection Only
Returned from the open attachment action.

Example Request
curl https://api.planningcenteronline.com/services/v2
View in API Explorer
Example Object
{
  "type": "AttachmentActivity",
  "id": "1",
  "attributes": {
    "date": "2000-01-01",
    "attachment_url": "string",
    "activity_type": "string"
  },
  "relationships": {
    "attachment": {
      "data": {
        "type": "Attachment",
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
date
date
attachment_url
string
activity_type
string
Relationships
Name
Type
Association Type
Note
attachment
Attachment
to_one
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
/services/v2

----

AttachmentType
Create an Attachment Type for each type of file you might want only specific people to see. When you attach a file, you can specify an attachment type to then be able to link the file to a position.

Example Request
curl https://api.planningcenteronline.com/services/v2/attachment_types
View in API Explorer
Example Object
{
  "type": "AttachmentType",
  "id": "1",
  "attributes": {
    "name": "string",
    "aliases": "string",
    "capoed_chord_charts": true,
    "chord_charts": true,
    "exclusions": "string",
    "lyrics": true,
    "number_charts": true,
    "numeral_charts": true,
    "built_in": true
  },
  "relationships": {
    "attachment_type_group": {
      "data": {
        "type": "AttachmentTypeGroup",
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
aliases
string
capoed_chord_charts
boolean
chord_charts
boolean
exclusions
string
lyrics
boolean
number_charts
boolean
numeral_charts
boolean
built_in
boolean
Relationships
Name
Type
Association Type
Note
attachment_type_group
AttachmentTypeGroup
to_one
URL Parameters
Order By
Parameter
Value
Type
Description
order
name
string
prefix with a hyphen (-name) to reverse the order
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
/services/v2/attachment_types

Reading
HTTP Method
Endpoint
GET
/services/v2/attachment_types/{id}

Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/attachment_types

Organization


---


AttachmentTypeGroup
Example Request
curl https://api.planningcenteronline.com/services/v2/attachment_type_groups
View in API Explorer
Example Object
{
  "type": "AttachmentTypeGroup",
  "id": "1",
  "attributes": {
    "name": "string",
    "readonly": true
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
readonly
boolean
URL Parameters
Order By
Parameter
Value
Type
Description
order
name
string
prefix with a hyphen (-name) to reverse the order
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
/services/v2/attachment_type_groups

Reading
HTTP Method
Endpoint
GET
/services/v2/attachment_type_groups/{id}


----


Attendance
Example Request
curl https://api.planningcenteronline.com/services/v2/series/{series_id}/plans/{plan_id}/attendances
View in API Explorer
Example Object
{
  "type": "Attendance",
  "id": "1",
  "attributes": {
    "checked_in_at": "2000-01-01T12:00:00Z",
    "check_ins_event_id": "primary_key",
    "check_ins_event_period_id": "primary_key"
  },
  "relationships": {
    "plan_time": {
      "data": {
        "type": "PlanTime",
        "id": "1"
      }
    },
    "plan_person": {
      "data": {
        "type": "PlanPerson",
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
checked_in_at
date_time
check_ins_event_id
primary_key
check_ins_event_period_id
primary_key
Relationships
Name
Type
Association Type
Note
plan_time
PlanTime
to_one
plan_person
PlanPerson
to_one
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
/services/v2/series/{series_id}/plans/{plan_id}/attendances

Reading
HTTP Method
Endpoint
GET
/services/v2/series/{series_id}/plans/{plan_id}/attendances/{id}

Belongs To
Plan
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/attendances

Plan

---

AvailableSignup
Signups that are available.

Example Request
curl https://api.planningcenteronline.com/services/v2/people/{person_id}/available_signups
View in API Explorer
Example Object
{
  "type": "AvailableSignup",
  "id": "1",
  "attributes": {
    "organization_name": "string",
    "planning_center_url": "string",
    "service_type_name": "string",
    "signups_available": true
  },
  "relationships": {
    "organization": {
      "data": {
        "type": "Organization",
        "id": "1"
      }
    },
    "person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "service_type": {
      "data": {
        "type": "ServiceType",
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
organization_name
string
planning_center_url
string
service_type_name
string
signups_available
boolean
Relationships
Name
Type
Association Type
Note
organization
Organization
to_one
person
Person
to_one
service_type
ServiceType
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
signup_sheets
include associated signup_sheets
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
/services/v2/people/{person_id}/available_signups

Reading
HTTP Method
Endpoint
GET
/services/v2/people/{person_id}/available_signups/{id}

Associations
signup_sheets
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/available_signups/{available_signup_id}/signup_sheets

SignupSheet
Belongs To
Person
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/available_signups

Person
current_organization

----

Blockout
An object representing a blockout date, and an optional recurrence pattern

Example Request
curl https://api.planningcenteronline.com/services/v2/people/{person_id}/blockouts
View in API Explorer
Example Object
{
  "type": "Blockout",
  "id": "1",
  "attributes": {
    "description": "string",
    "group_identifier": "string",
    "organization_name": "string",
    "reason": "string",
    "repeat_frequency": "string",
    "repeat_interval": "string",
    "repeat_period": "string",
    "settings": "string",
    "time_zone": "string",
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "repeat_until": "2000-01-01",
    "starts_at": "2000-01-01T12:00:00Z",
    "ends_at": "2000-01-01T12:00:00Z",
    "share": true
  },
  "relationships": {
    "person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "organization": {
      "data": {
        "type": "Organization",
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
description
string
group_identifier
string
organization_name
string
reason
string
repeat_frequency
string
Possible values:

no_repeat

every_1

every_2

every_3

every_4

every_5

every_6

every_7

every_8

repeat_interval
string
Possible values:

exact_day_of_month

week_of_month_1

week_of_month_2

week_of_month_3

week_of_month_4

week_of_month_last

repeat_period
string
Possible values:

daily

weekly

monthly

yearly

settings
string
time_zone
string
created_at
date_time
updated_at
date_time
repeat_until
date
starts_at
date_time
ends_at
date_time
share
boolean
Relationships
Name
Type
Association Type
Note
person
Person
to_one
organization
Organization
to_one
URL Parameters
Query By
Name
Parameter
Type
Description
Example
group_identifier
where[group_identifier]
string
Query on a specific group_identifier

?where[group_identifier]=string
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
/services/v2/people/{person_id}/blockouts

Reading
HTTP Method
Endpoint
GET
/services/v2/people/{person_id}/blockouts/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/people/{person_id}/blockouts

reason
repeat_frequency
repeat_interval
repeat_period
share
repeat_until
starts_at
ends_at
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/people/{person_id}/blockouts/{id}

reason
repeat_frequency
repeat_interval
repeat_period
share
repeat_until
starts_at
ends_at
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/people/{person_id}/blockouts/{id}

Associations
blockout_dates
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/blockouts/{blockout_id}/blockout_dates

BlockoutDate
blockout_exceptions
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/blockouts/{blockout_id}/blockout_exceptions

BlockoutException
Belongs To
Person
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/blockouts

Person
future

past


---


BlockoutDate
The actual dates generated by the blockout or its recurrence pattern. Generated up to a year in advance

Example Request
curl https://api.planningcenteronline.com/services/v2/people/{person_id}/blockouts/{blockout_id}/blockout_dates
View in API Explorer
Example Object
{
  "type": "BlockoutDate",
  "id": "1",
  "attributes": {
    "group_identifier": "string",
    "reason": "string",
    "time_zone": "string",
    "share": true,
    "starts_at": "2000-01-01T12:00:00Z",
    "ends_at": "2000-01-01T12:00:00Z",
    "ends_at_utc": "2000-01-01T12:00:00Z",
    "starts_at_utc": "2000-01-01T12:00:00Z"
  },
  "relationships": {
    "person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "blockout": {
      "data": {
        "type": "Blockout",
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
group_identifier
string
reason
string
time_zone
string
share
boolean
starts_at
date_time
Start time as a 'wall-clock' timestamp

ends_at
date_time
End time as a 'wall-clock' timestamp

ends_at_utc
date_time
starts_at_utc
date_time
Relationships
Name
Type
Association Type
Note
person
Person
to_one
blockout
Blockout
to_one
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
/services/v2/people/{person_id}/blockouts/{blockout_id}/blockout_dates

Reading
HTTP Method
Endpoint
GET
/services/v2/people/{person_id}/blockouts/{blockout_id}/blockout_dates/{id}

Belongs To
Blockout
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/blockouts/{blockout_id}/blockout_dates

Blockout


---

BlockoutException
A single exception for the dates generated from the blockout

Example Request
curl https://api.planningcenteronline.com/services/v2/people/{person_id}/blockouts/{blockout_id}/blockout_exceptions
View in API Explorer
Example Object
{
  "type": "BlockoutException",
  "id": "1",
  "attributes": {
    "date": "2000-01-01",
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z"
  },
  "relationships": {
    "blockout": {
      "data": {
        "type": "Blockout",
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
date
date
created_at
date_time
updated_at
date_time
Relationships
Name
Type
Association Type
Note
blockout
Blockout
to_one
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
/services/v2/people/{person_id}/blockouts/{blockout_id}/blockout_exceptions

Reading
HTTP Method
Endpoint
GET
/services/v2/people/{person_id}/blockouts/{blockout_id}/blockout_exceptions/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/people/{person_id}/blockouts/{blockout_id}/blockout_exceptions

date
Belongs To
Blockout
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/blockouts/{blockout_id}/blockout_exceptions

Blockout

---

BlockoutScheduleConflict
Example Request
curl https://api.planningcenteronline.com/services/v2
View in API Explorer
Example Object
{
  "type": "BlockoutScheduleConflict",
  "id": "1",
  "attributes": {
    "dates": "string",
    "organization_name": "string",
    "person_avatar": "string",
    "person_name": "string",
    "position_display_times": "string",
    "service_type_name": "string",
    "short_dates": "string",
    "status": "string",
    "team_name": "string",
    "team_position_name": "string",
    "sort_date": "2000-01-01T12:00:00Z",
    "can_accept_partial": true
  },
  "relationships": {
    "organization": {
      "data": {
        "type": "Organization",
        "id": "1"
      }
    },
    "person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "plan": {
      "data": {
        "type": "Plan",
        "id": "1"
      }
    },
    "plan_person": {
      "data": {
        "type": "PlanPerson",
        "id": "1"
      }
    },
    "service_type": {
      "data": {
        "type": "ServiceType",
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
dates
string
organization_name
string
person_avatar
string
person_name
string
position_display_times
string
service_type_name
string
short_dates
string
status
string
team_name
string
team_position_name
string
sort_date
date_time
can_accept_partial
boolean
Relationships
Name
Type
Association Type
Note
organization
Organization
to_one
person
Person
to_one
plan
Plan
to_one
plan_person
PlanPerson
to_one
service_type
ServiceType
to_one
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
/services/v2

Reading
HTTP Method
Endpoint
GET
/services/v2/{id}


---


Chat
Example Request
curl https://api.planningcenteronline.com/services/v2/chats
View in API Explorer
Example Object
{
  "type": "Chat",
  "id": "1",
  "attributes": {
    "payload": "string",
    "group_identifiers": [],
    "people": [],
    "plans": [],
    "teams": [],
    "teams_i_lead": [],
    "my_teams": []
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
payload
string
Only available when requested with the ?fields param

group_identifiers
array
Only available when requested with the ?fields param

people
array
Only available when requested with the ?fields param

plans
array
Only available when requested with the ?fields param

teams
array
Only available when requested with the ?fields param

teams_i_lead
array
Only available when requested with the ?fields param

my_teams
array
Only available when requested with the ?fields param

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
/services/v2/chats

Reading
HTTP Method
Endpoint
GET
/services/v2/chats/{id}

Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/chat

Organization

---

Contributor
A Contributor Resource

Example Request
curl https://api.planningcenteronline.com/services/v2/series/{series_id}/plans/{plan_id}/contributors
View in API Explorer
Example Object
{
  "type": "Contributor",
  "id": "1",
  "attributes": {
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "contributable_action": "string",
    "contributable_category": "string",
    "contributable_type": "string",
    "full_name": "string",
    "photo_thumbnail_url": "string"
  },
  "relationships": {
    "plan": {
      "data": {
        "type": "Plan",
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
id
primary_key
created_at
date_time
updated_at
date_time
contributable_action
string
contributable_category
string
contributable_type
string
full_name
string
photo_thumbnail_url
string
Relationships
Name
Type
Association Type
Note
plan
Plan
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
order
updated_at
string
prefix with a hyphen (-updated_at) to reverse the order
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
/services/v2/series/{series_id}/plans/{plan_id}/contributors

Reading
HTTP Method
Endpoint
GET
/services/v2/series/{series_id}/plans/{plan_id}/contributors/{id}

Belongs To
Plan
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/contributors

Plan

---

CustomSlide
A CustomSlide is used for adding text intended for display on a screen.

Example Request
curl https://api.planningcenteronline.com/services/v2/songs/{song_id}/last_scheduled_item/{last_scheduled_item_id}/custom_slides
View in API Explorer
Example Object
{
  "type": "CustomSlide",
  "id": "1",
  "attributes": {
    "body": "string",
    "label": "string",
    "order": 1,
    "enabled": true
  },
  "relationships": {
    "item": {
      "data": {
        "type": "Item",
        "id": "1"
      }
    },
    "attachment": {
      "data": {
        "type": "Attachment",
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
body
string
label
string
order
integer
enabled
boolean
Relationships
Name
Type
Association Type
Note
item
Item
to_one
attachment
Attachment
to_one
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
/services/v2/songs/{song_id}/last_scheduled_item/{last_scheduled_item_id}/custom_slides

Reading
HTTP Method
Endpoint
GET
/services/v2/songs/{song_id}/last_scheduled_item/{last_scheduled_item_id}/custom_slides/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/custom_slides

body
enabled
label
order
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/songs/{song_id}/last_scheduled_item/{last_scheduled_item_id}/custom_slides/{id}

body
enabled
label
order
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/songs/{song_id}/last_scheduled_item/{last_scheduled_item_id}/custom_slides/{id}

Belongs To
Item
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/custom_slides

Item

---

Email
A persons email

Example Request
curl https://api.planningcenteronline.com/services/v2/people/{person_id}/emails
View in API Explorer
Example Object
{
  "type": "Email",
  "id": "1",
  "attributes": {
    "primary": true,
    "address": "string"
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
primary
boolean
address
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
/services/v2/people/{person_id}/emails

Reading
HTTP Method
Endpoint
GET
/services/v2/people/{person_id}/emails/{id}

Belongs To
Person
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/emails

Person


---


EmailTemplate
A EmailTemplate Resource

Example Request
curl https://api.planningcenteronline.com/services/v2/email_templates
View in API Explorer
Example Object
{
  "type": "EmailTemplate",
  "id": "1",
  "attributes": {
    "kind": "string",
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "html_body": "string",
    "subject": "string"
  },
  "relationships": {
    "template_owner": {
      "data": {
        "type": "Organization",
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
kind
string
created_at
date_time
updated_at
date_time
html_body
string
subject
string
Relationships
Name
Type
Association Type
Note
template_owner
(polymorphic)
to_one
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
/services/v2/email_templates

Reading
HTTP Method
Endpoint
GET
/services/v2/email_templates/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/email_templates

html_body
subject
kind
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/email_templates/{id}

html_body
subject
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/email_templates/{id}

Actions
render
HTTP Method
Endpoint
Description
POST
/services/v2/email_templates/{email_template_id}/render

Render an email template and fill in the persons details

Details:

Render the template with information from the person.

{
  "data": {
    "attributes": {
      "format": "html|text"
    },
    "relationships": {
      "person": {
        "data": {
          "type": "Person",
          "id": "1"
        }
      }
    }
  }
}
Permissions:

Must be authenticated

Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/email_templates

Organization

---

EmailTemplateRenderedResponse
Collection Only
A EmailTemplateRenderedResponse Resource

Example Request
curl https://api.planningcenteronline.com/services/v2
View in API Explorer
Example Object
{
  "type": "EmailTemplateRenderedResponse",
  "id": "1",
  "attributes": {
    "body": "string",
    "subject": "string"
  },
  "relationships": {
    "person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "email_template": {
      "data": {
        "type": "EmailTemplate",
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
body
string
subject
string
Relationships
Name
Type
Association Type
Note
person
Person
to_one
email_template
EmailTemplate
to_one
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
/services/v2


---


Folder
A folder is a container used to organize multiple Service Types or other Folders.

Example Request
curl https://api.planningcenteronline.com/services/v2/folders
View in API Explorer
Example Object
{
  "type": "Folder",
  "id": "1",
  "attributes": {
    "created_at": "2000-01-01T12:00:00Z",
    "name": "string",
    "updated_at": "2000-01-01T12:00:00Z",
    "container": "string"
  },
  "relationships": {
    "ancestors": {
      "data": {
        "type": "Folder",
        "id": "1"
      }
    },
    "parent": {
      "data": {
        "type": "Folder",
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
created_at
date_time
name
string
updated_at
date_time
container
string
Relationships
Name
Type
Association Type
Note
ancestors
Folder
to_one
parent
Folder
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
service_types
include associated service_types
Order By
Parameter
Value
Type
Description
order
name
string
prefix with a hyphen (-name) to reverse the order
Query By
Name
Parameter
Type
Description
Example
parent_id
where[parent_id]
integer
Query on a related parent

?where[parent_id]=1
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
/services/v2/folders

Reading
HTTP Method
Endpoint
GET
/services/v2/folders/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/folders

name
parent_id
campus_id
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/folders/{id}

name
parent_id
campus_id
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/folders/{id}

Associations
folders
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/folders/{folder_id}/folders

Folder
service_types
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/folders/{folder_id}/service_types

ServiceType
Belongs To
Folder
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/folders/{folder_id}/folders

Folder
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/folders

Organization
TagGroup
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/tag_groups/{tag_group_id}/folder

TagGroup


----


FolderPath
The Folder path of a Folder

Example Request
curl https://api.planningcenteronline.com/services/v2
View in API Explorer
Example Object
{
  "type": "FolderPath",
  "id": "1",
  "attributes": {
    "path": []
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
path
array
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
/services/v2

Reading
HTTP Method
Endpoint
GET
/services/v2/{id}

---


Item
An item in a plan.

Example Request
curl https://api.planningcenteronline.com/services/v2/service_types/{service_type_id}/plans/{plan_id}/items
View in API Explorer
Example Object
{
  "type": "Item",
  "id": "1",
  "attributes": {
    "title": "string",
    "sequence": 1,
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "length": 1,
    "item_type": "string",
    "html_details": "string",
    "service_position": "string",
    "description": "string",
    "key_name": "string",
    "custom_arrangement_sequence": [],
    "custom_arrangement_sequence_short": [],
    "custom_arrangement_sequence_full": []
  },
  "relationships": {
    "plan": {
      "data": {
        "type": "Plan",
        "id": "1"
      }
    },
    "song": {
      "data": {
        "type": "Song",
        "id": "1"
      }
    },
    "arrangement": {
      "data": {
        "type": "Arrangement",
        "id": "1"
      }
    },
    "key": {
      "data": {
        "type": "Key",
        "id": "1"
      }
    },
    "selected_layout": {
      "data": {
        "type": "Layout",
        "id": "1"
      }
    },
    "selected_background": {
      "data": {
        "type": "Attachment",
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
title
string
sequence
integer
created_at
date_time
updated_at
date_time
length
integer
item_type
string
There are 4 possible values:

song: The item is a song

header: The item is a header

media: The item is a piece of media

item: The default item type

This value can only be set when an item is created. The only value that you can pass is header. If no value is passed then item will be used. To create a media item you'll attach a video media to the item, and to create a song item, you'll attach a song.

html_details
string
service_position
string
There are 3 possible values:

pre: the item happens before the service starts

post: the item happens after the service ends

during: the item happens during the service

description
string
key_name
string
custom_arrangement_sequence
array
An array of strings containing a label and a number describing the section:

['Verse 1', 'Chorus 1', 'Verse 2']

custom_arrangement_sequence_short
array
custom_arrangement_sequence_full
array
Relationships
Name
Type
Association Type
Note
plan
Plan
to_one
song
Song
to_one
arrangement
Arrangement
to_one
key
Key
to_one
selected_layout
Layout
to_one
selected_background
Attachment
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
arrangement
include associated arrangement
create and update
include
item_notes
include associated item_notes
include
item_times
include associated item_times
include
key
include associated key
create and update
include
media
include associated media
create and update
include
selected_attachment
include associated selected_attachment
create and update
include
song
include associated song
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
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items

Reading
HTTP Method
Endpoint
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items

arrangement_id
custom_arrangement_sequence
description
html_details
key_id
length
selected_layout_id
service_position
song_id
title
item_type
sequence
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{id}

arrangement_id
custom_arrangement_sequence
description
html_details
key_id
length
selected_layout_id
service_position
song_id
title
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{id}

Associations
arrangement
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/arrangement

Arrangement
attachments
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/attachments

Attachment
custom_slides
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/custom_slides

CustomSlide
item_notes
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/item_notes

ItemNote
item_times
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/item_times

ItemTime
key
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/key

Key
media
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/media

Media
selected_attachment
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/selected_attachment

Attachment
selected_background
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/selected_background

Attachment
song
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/song

Song
Belongs To
Live
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/series/{series_id}/plans/{plan_id}/live/{live_id}/items

Live
Plan
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items

Plan
PlanTemplate
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_templates/{plan_template_id}/items

PlanTemplate
Song
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/songs/{song_id}/last_scheduled_item

Song
The Song's most recently scheduled Item in a given Service Type. Requires a service_type query parameter. e.g. ?service_type=789


----


ItemNote
A plan item note that belongs to a category.

Note: You can only assign the category on create. If you want to change category; delete the current note, and create a new one passing in the item_note_category_id then.

Example Request
curl https://api.planningcenteronline.com/services/v2/songs/{song_id}/last_scheduled_item/{last_scheduled_item_id}/item_notes
View in API Explorer
Example Object
{
  "type": "ItemNote",
  "id": "1",
  "attributes": {
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "content": "string",
    "category_name": "string"
  },
  "relationships": {
    "item_note_category": {
      "data": {
        "type": "ItemNoteCategory",
        "id": "1"
      }
    },
    "item": {
      "data": {
        "type": "Item",
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
created_at
date_time
updated_at
date_time
content
string
category_name
string
Relationships
Name
Type
Association Type
Note
item_note_category
ItemNoteCategory
to_one
An ItemNoteCategory must be assigned when creating an ItemNote.

This can be done by assigning an item_note_category_id:

{
  "data": {
    "type": "ItemNote",
    "attributes": {
      "content": "ok",
      "item_note_category_id": 1
    }
  }
}
or including the relationship in the POST body:

{
  "data": {
    "type": "ItemNote",
    "attributes": {
      "content": "ok",
    },
    "relationships": {
      "item_note_category": {
        "data": {
          "type": "ItemNoteCategory",
          "id": 1
        }
      }
    }
  }
}
item
Item
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
item_note_category
include associated item_note_category
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
/services/v2/songs/{song_id}/last_scheduled_item/{last_scheduled_item_id}/item_notes

Reading
HTTP Method
Endpoint
GET
/services/v2/songs/{song_id}/last_scheduled_item/{last_scheduled_item_id}/item_notes/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/item_notes

content
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/songs/{song_id}/last_scheduled_item/{last_scheduled_item_id}/item_notes/{id}

content
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/songs/{song_id}/last_scheduled_item/{last_scheduled_item_id}/item_notes/{id}

Associations
item_note_category
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/songs/{song_id}/last_scheduled_item/{last_scheduled_item_id}/item_notes/{item_note_id}/item_note_category

ItemNoteCategory
Belongs To
Item
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/item_notes

Item

---

ItemNoteCategory
A category of plan item notes for an entire Service Type.

Example Request
curl https://api.planningcenteronline.com/services/v2/service_types/{service_type_id}/item_note_categories
View in API Explorer
Example Object
{
  "type": "ItemNoteCategory",
  "id": "1",
  "attributes": {
    "created_at": "2000-01-01T12:00:00Z",
    "deleted_at": "2000-01-01T12:00:00Z",
    "name": "string",
    "sequence": 1,
    "updated_at": "2000-01-01T12:00:00Z",
    "frequently_used": true
  },
  "relationships": {
    "service_type": {
      "data": {
        "type": "ServiceType",
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
created_at
date_time
deleted_at
date_time
name
string
sequence
integer
updated_at
date_time
frequently_used
boolean
Relationships
Name
Type
Association Type
Note
service_type
ServiceType
to_one
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
/services/v2/service_types/{service_type_id}/item_note_categories

Reading
HTTP Method
Endpoint
GET
/services/v2/service_types/{service_type_id}/item_note_categories/{id}

Belongs To
ItemNote
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/songs/{song_id}/last_scheduled_item/{last_scheduled_item_id}/item_notes/{item_note_id}/item_note_category

ItemNote
ServiceType
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/item_note_categories

ServiceType

---

ItemTime
Example Request
curl https://api.planningcenteronline.com/services/v2/songs/{song_id}/last_scheduled_item/{last_scheduled_item_id}/item_times
View in API Explorer
Example Object
{
  "type": "ItemTime",
  "id": "1",
  "attributes": {
    "live_start_at": "2000-01-01T12:00:00Z",
    "live_end_at": "2000-01-01T12:00:00Z",
    "exclude": true,
    "length": 1,
    "length_offset": 1
  },
  "relationships": {
    "item": {
      "data": {
        "type": "Item",
        "id": "1"
      }
    },
    "plan_time": {
      "data": {
        "type": "PlanTime",
        "id": "1"
      }
    },
    "plan": {
      "data": {
        "type": "Plan",
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
live_start_at
date_time
live_end_at
date_time
exclude
boolean
length
integer
length_offset
integer
Relationships
Name
Type
Association Type
Note
item
Item
to_one
plan_time
PlanTime
to_one
plan
Plan
to_one
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
/services/v2/songs/{song_id}/last_scheduled_item/{last_scheduled_item_id}/item_times

Reading
HTTP Method
Endpoint
GET
/services/v2/songs/{song_id}/last_scheduled_item/{last_scheduled_item_id}/item_times/{id}

Belongs To
Item
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/item_times

Item
Live
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/series/{series_id}/plans/{plan_id}/live/{live_id}/current_item_time

Live
Live
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/series/{series_id}/plans/{plan_id}/live/{live_id}/next_item_time

Live

---

Key
Each song arrangement can have multiple keys. A key is the pitch center of the song.

Example Request
curl https://api.planningcenteronline.com/services/v2/songs/{song_id}/arrangements/{arrangement_id}/keys
View in API Explorer
Example Object
{
  "type": "Key",
  "id": "1",
  "attributes": {
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "name": "string",
    "alternate_keys": "string",
    "ending_key": "string",
    "starting_key": "string",
    "starting_minor": true,
    "ending_minor": true
  },
  "relationships": {
    "arrangement": {
      "data": {
        "type": "Arrangement",
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
created_at
date_time
updated_at
date_time
name
string
alternate_keys
string
An array of objects.

{ "name": "My Alternate Key", "key": "B" }

ending_key
string
Possible Values:

Ab, A, A#, Bb, B, C, C#, Db, D, D#, Eb, E, F, F#, Gb, G, G#, Abm, Am, A#m, Bbm, Bm, Cm, C#m, Dbm, Dm, D#m, Ebm, Em, Fm, F#m, Gbm, Gm, G#m

To set the key to minor append m to the key. e.g. Cm

starting_key
string
Possible Values:

Ab, A, A#, Bb, B, C, C#, Db, D, D#, Eb, E, F, F#, Gb, G, G#, Abm, Am, A#m, Bbm, Bm, Cm, C#m, Dbm, Dm, D#m, Ebm, Em, Fm, F#m, Gbm, Gm, G#m

To set the key to minor append m to the key. e.g. Cm

starting_minor
boolean
ending_minor
boolean
Relationships
Name
Type
Association Type
Note
arrangement
Arrangement
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
order
updated_at
string
prefix with a hyphen (-updated_at) to reverse the order
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
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/keys

Reading
HTTP Method
Endpoint
GET
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/keys/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/keys

alternate_keys
ending_key
name
starting_key
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/keys/{id}

alternate_keys
ending_key
name
starting_key
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/keys/{id}

Associations
attachments
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/keys/{key_id}/attachments

Attachment
Belongs To
Arrangement
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/keys

Arrangement
Item
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/key

Item

---

Live
Example Request
curl https://api.planningcenteronline.com/services/v2/series/{series_id}/plans/{plan_id}/live
View in API Explorer
Example Object
{
  "type": "Live",
  "id": "1",
  "attributes": {
    "series_title": "string",
    "title": "string",
    "dates": "string",
    "live_channel": "string",
    "chat_room_channel": "string",
    "can_control": true,
    "can_take_control": true,
    "can_chat": true,
    "can_control_video_feed": true
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
series_title
string
title
string
dates
string
live_channel
string
chat_room_channel
string
can_control
boolean
can_take_control
boolean
can_chat
boolean
can_control_video_feed
boolean
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
controller
include associated controller
include
current_item_time
include associated current_item_time
include
items
include associated items
include
next_item_time
include associated next_item_time
include
service_type
include associated service_type
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
/services/v2/series/{series_id}/plans/{plan_id}/live

Reading
HTTP Method
Endpoint
GET
/services/v2/series/{series_id}/plans/{plan_id}/live/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/series/{series_id}/plans/{plan_id}/live

Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/series/{series_id}/plans/{plan_id}/live/{id}

Deleting
HTTP Method
Endpoint
DELETE
/services/v2/series/{series_id}/plans/{plan_id}/live/{id}

Actions
go_to_next_item
HTTP Method
Endpoint
POST
/services/v2/series/{series_id}/plans/{plan_id}/live/{live_id}/go_to_next_item

Permissions:

Must be authenticated

go_to_previous_item
HTTP Method
Endpoint
POST
/services/v2/series/{series_id}/plans/{plan_id}/live/{live_id}/go_to_previous_item

Permissions:

Must be authenticated

toggle_control
HTTP Method
Endpoint
POST
/services/v2/series/{series_id}/plans/{plan_id}/live/{live_id}/toggle_control

Permissions:

Must be authenticated

Associations
controller
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/series/{series_id}/plans/{plan_id}/live/{live_id}/controller

Person
current_item_time
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/series/{series_id}/plans/{plan_id}/live/{live_id}/current_item_time

ItemTime
items
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/series/{series_id}/plans/{plan_id}/live/{live_id}/items

Item
next_item_time
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/series/{series_id}/plans/{plan_id}/live/{live_id}/next_item_time

ItemTime
service_type
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/series/{series_id}/plans/{plan_id}/live/{live_id}/service_type

ServiceType
watchable_plans
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/series/{series_id}/plans/{plan_id}/live/{live_id}/watchable_plans

Plan
Belongs To
Plan
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/live

Plan

----
LiveController
A person who can control Services LIVE without the required permissions

Example Request
curl https://api.planningcenteronline.com/services/v2/service_types/{service_type_id}/live_controllers
View in API Explorer
Example Object
{
  "type": "LiveController",
  "id": "1",
  "attributes": {
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "full_name": "string",
    "photo_thumbnail_url": "string"
  },
  "relationships": {
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
id
primary_key
created_at
date_time
updated_at
date_time
full_name
string
photo_thumbnail_url
string
Relationships
Name
Type
Association Type
Note
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
order
updated_at
string
prefix with a hyphen (-updated_at) to reverse the order
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
/services/v2/service_types/{service_type_id}/live_controllers

Reading
HTTP Method
Endpoint
GET
/services/v2/service_types/{service_type_id}/live_controllers/{id}

Belongs To
ServiceType
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/live_controllers

ServiceType

---

Media
A piece of media

Example Request
curl https://api.planningcenteronline.com/services/v2/media
View in API Explorer
Example Object
{
  "type": "Media",
  "id": "1",
  "attributes": {
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "themes": "string",
    "title": "string",
    "thumbnail_file_name": "string",
    "thumbnail_content_type": "string",
    "thumbnail_file_size": 1,
    "thumbnail_updated_at": "2000-01-01T12:00:00Z",
    "preview_file_name": "string",
    "preview_content_type": "string",
    "preview_file_size": 1,
    "preview_updated_at": "2000-01-01T12:00:00Z",
    "length": 1,
    "media_type": "string",
    "media_type_name": "string",
    "thumbnail_url": "string",
    "creator_name": "string",
    "preview_url": "string",
    "image_url": "string"
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
themes
string
title
string
thumbnail_file_name
string
thumbnail_content_type
string
thumbnail_file_size
integer
thumbnail_updated_at
date_time
preview_file_name
string
preview_content_type
string
preview_file_size
integer
preview_updated_at
date_time
length
integer
media_type
string
Possible Values:

audio

background_audio

background_image

background_video

countdown

curriculum

document

drama

image

powerpoint

song_video

video

media_type_name
string
thumbnail_url
string
creator_name
string
preview_url
string
image_url
string
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
attachments
include associated attachments
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
title
string
prefix with a hyphen (-title) to reverse the order
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
creator_name
where[creator_name]
string
Query on a specific creator_name

?where[creator_name]=string
id
where[id]
primary_key
Query on a specific id

?where[id]=primary_key
themes
where[themes]
string
Query on a specific themes

?where[themes]=string
title
where[title]
string
Query on a specific title

?where[title]=string
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
/services/v2/media

Reading
HTTP Method
Endpoint
GET
/services/v2/media/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/media

media_type
title
creator_name
themes
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/media/{id}

media_type
title
creator_name
themes
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/media/{id}

Actions
archive
HTTP Method
Endpoint
Description
POST
/services/v2/media/{media_id}/archive

Archive a Media.

Details:

Accepts an optional time attribute (ISO 8601) for scheduling archival for a future time.

{
  "data": {
    "type": "MediaArchive",
    "attributes": {
      "time": "2025-12-15T00:00:00Z"
    }
  }
}
Permissions:

Must be authenticated

assign_tags
HTTP Method
Endpoint
Description
POST
/services/v2/media/{media_id}/assign_tags

Used to assign tags to a media.

Details:

All tags will be replaced so the full data set must be sent.

It expects a body that looks like:

{
	"data": {
		"type": "TagAssignment",
		"attributes": {},
		"relationships": {
			"tags": {
				"data": [
					{
						"type": "Tag",
						"id": "5"
					}
				]
			}
		}
	}
}
On success you will get back a 204 No Content.

Permissions:

Must be authenticated

unarchive
HTTP Method
Endpoint
Description
POST
/services/v2/media/{media_id}/unarchive

Restore an archived Media.

Permissions:

Must be authenticated

Associations
attachments
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/media/{media_id}/attachments

Attachment
media_schedules
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/media/{media_id}/media_schedules

MediaSchedule
tags
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/media/{media_id}/tags

Tag
Belongs To
Item
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/media

Item
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/media

Organization
archived

audio

background_audio

background_image

background_video

countdown

curriculum

document

drama

image

not_archived

powerpoint

song_video

video


----


MediaSchedule
Example Request
curl https://api.planningcenteronline.com/services/v2/media/{media_id}/media_schedules
View in API Explorer
Example Object
{
  "type": "MediaSchedule",
  "id": "1",
  "attributes": {
    "plan_dates": "string",
    "plan_short_dates": "string",
    "service_type_name": "string",
    "plan_sort_date": "2000-01-01T12:00:00Z"
  },
  "relationships": {
    "plan": {
      "data": {
        "type": "Plan",
        "id": "1"
      }
    },
    "service_type": {
      "data": {
        "type": "ServiceType",
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
plan_dates
string
plan_short_dates
string
service_type_name
string
plan_sort_date
date_time
Relationships
Name
Type
Association Type
Note
plan
Plan
to_one
service_type
ServiceType
to_one
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
/services/v2/media/{media_id}/media_schedules

Reading
HTTP Method
Endpoint
GET
/services/v2/media/{media_id}/media_schedules/{id}

Belongs To
Media
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/media/{media_id}/media_schedules

Media


----

NeededPosition
An amount of unfilled positions needed within a team in a plan.

Example Request
curl https://api.planningcenteronline.com/services/v2/series/{series_id}/plans/{plan_id}/needed_positions
View in API Explorer
Example Object
{
  "type": "NeededPosition",
  "id": "1",
  "attributes": {
    "quantity": 1,
    "team_position_name": "string",
    "scheduled_to": "string"
  },
  "relationships": {
    "team": {
      "data": {
        "type": "Team",
        "id": "1"
      }
    },
    "plan": {
      "data": {
        "type": "Plan",
        "id": "1"
      }
    },
    "time": {
      "data": {
        "type": "PlanTime",
        "id": "1"
      }
    },
    "time_preference_option": {
      "data": {
        "type": "TimePreferenceOption",
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
quantity
integer
team_position_name
string
scheduled_to
string
Relationships
Name
Type
Association Type
Note
team
Team
to_one
plan
Plan
to_one
time
PlanTime
to_one
time_preference_option
TimePreferenceOption
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
team
include associated team
create and update
include
time
include associated time
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
/services/v2/series/{series_id}/plans/{plan_id}/needed_positions

Reading
HTTP Method
Endpoint
GET
/services/v2/series/{series_id}/plans/{plan_id}/needed_positions/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/service_types/{service_type_id}/plans/{plan_id}/needed_positions

quantity
time_id
time_preference_option_id
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/series/{series_id}/plans/{plan_id}/needed_positions/{id}

quantity
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/series/{series_id}/plans/{plan_id}/needed_positions/{id}

Associations
team
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/series/{series_id}/plans/{plan_id}/needed_positions/{needed_position_id}/team

Team
time
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/series/{series_id}/plans/{plan_id}/needed_positions/{needed_position_id}/time

PlanTime
Belongs To
Plan
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/needed_positions

Plan

----

Organization
The root level of an organization where account-level settings are applied.

Example Request
curl https://api.planningcenteronline.com/services/v2
View in API Explorer
Example Object
{
  "type": "Organization",
  "id": "1",
  "attributes": {
    "ccli": "string",
    "created_at": "2000-01-01T12:00:00Z",
    "date_format": 1,
    "music_stand_enabled": true,
    "name": "string",
    "projector_enabled": true,
    "time_zone": "string",
    "twenty_four_hour_time": true,
    "updated_at": "2000-01-01T12:00:00Z",
    "owner_name": "string",
    "required_to_set_download_permission": "string",
    "secret": "string",
    "allow_mp3_download": true,
    "calendar_starts_on_sunday": true,
    "ccli_connected": true,
    "ccli_auto_reporting_enabled": true,
    "ccli_reporting_enabled": true,
    "extra_file_storage_allowed": true,
    "file_storage_exceeded": true,
    "file_storage_size": true,
    "file_storage_size_used": true,
    "file_storage_extra_enabled": true,
    "rehearsal_mix_enabled": true,
    "rehearsal_pack_connected": true,
    "legacy_id": "primary_key",
    "file_storage_extra_charges": 1,
    "people_allowed": 1,
    "people_remaining": 1,
    "beta": true
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
ccli
string
created_at
date_time
date_format
integer
Two possible values, US EU

music_stand_enabled
boolean
name
string
projector_enabled
boolean
time_zone
string
twenty_four_hour_time
boolean
updated_at
date_time
owner_name
string
required_to_set_download_permission
string
Possible values: editor, administrator, site_administrator

secret
string
allow_mp3_download
boolean
calendar_starts_on_sunday
boolean
ccli_connected
boolean
ccli_auto_reporting_enabled
boolean
ccli_reporting_enabled
boolean
extra_file_storage_allowed
boolean
file_storage_exceeded
boolean
file_storage_size
boolean
file_storage_size_used
boolean
file_storage_extra_enabled
boolean
rehearsal_mix_enabled
boolean
rehearsal_pack_connected
boolean
legacy_id
primary_key
file_storage_extra_charges
integer
people_allowed
integer
people_remaining
integer
beta
boolean
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
/services/v2

Reading
HTTP Method
Endpoint
GET
/services/v2/{id}

Associations
attachment_types
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/attachment_types

AttachmentType
chat
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/chat

Chat
email_templates
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/email_templates

EmailTemplate
folders
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/folders

Folder
media
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/media

Media
archived

audio

background_audio

background_image

background_video

countdown

curriculum

document

drama

image

not_archived

powerpoint

song_video

video

people
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people

Person
plans
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/plans

Organization
report_templates
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/report_templates

ReportTemplate
matrix

people

plans

without_defaults

series
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/series

Series
service_types
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types

ServiceType
no_parent

songs
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/songs

Song
tag_groups
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/tag_groups

TagGroup
arrangement

media

person

song

teams
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/teams

Team
editable

service_types

Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/plans

Organization


----


Person
A person added to Planning Center Services.

Example Request
curl https://api.planningcenteronline.com/services/v2/people
View in API Explorer
Example Object
{
  "type": "Person",
  "id": "1",
  "attributes": {
    "photo_url": "string",
    "photo_thumbnail_url": "string",
    "preferred_app": "string",
    "assigned_to_rehearsal_team": true,
    "archived_at": "2000-01-01T12:00:00Z",
    "created_at": "2000-01-01T12:00:00Z",
    "first_name": "string",
    "last_name": "string",
    "name_prefix": "string",
    "name_suffix": "string",
    "updated_at": "2000-01-01T12:00:00Z",
    "facebook_id": "primary_key",
    "legacy_id": "primary_key",
    "anniversary": "2000-01-01T12:00:00Z",
    "birthdate": "2000-01-01T12:00:00Z",
    "full_name": "string",
    "media_permissions": "string",
    "permissions": "string",
    "song_permissions": "string",
    "status": "string",
    "max_permissions": "string",
    "max_plan_permissions": "string",
    "given_name": "string",
    "middle_name": "string",
    "nickname": "string",
    "archived": true,
    "site_administrator": true,
    "logged_in_at": "2000-01-01T12:00:00Z",
    "notes": "string",
    "passed_background_check": true,
    "ical_code": "string",
    "access_media_attachments": true,
    "access_plan_attachments": true,
    "access_song_attachments": true,
    "preferred_max_plans_per_day": 1,
    "preferred_max_plans_per_month": 1,
    "praise_charts_enabled": true,
    "me_tab": "string",
    "plans_tab": "string",
    "songs_tab": "string",
    "media_tab": "string",
    "people_tab": "string",
    "can_edit_all_people": true,
    "can_view_all_people": true,
    "onboardings": []
  },
  "relationships": {
    "created_by": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "updated_by": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "current_folder": {
      "data": {
        "type": "Folder",
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
photo_url
string
photo_thumbnail_url
string
preferred_app
string
assigned_to_rehearsal_team
boolean
archived_at
date_time
created_at
date_time
first_name
string
last_name
string
name_prefix
string
name_suffix
string
updated_at
date_time
facebook_id
primary_key
DEPRECATED: this attribute will be removed in the next release and will return the string "DEPRECATED" in this version

legacy_id
primary_key
If you've used Person.id from API v1 this attribute can be used to map from those old IDs to the new IDs used in API v2

anniversary
date_time
birthdate
date_time
full_name
string
media_permissions
string
permissions
string
song_permissions
string
status
string
max_permissions
string
max_plan_permissions
string
given_name
string
middle_name
string
nickname
string
archived
boolean
site_administrator
boolean
logged_in_at
date_time
notes
string
passed_background_check
boolean
ical_code
string
access_media_attachments
boolean
access_plan_attachments
boolean
access_song_attachments
boolean
preferred_max_plans_per_day
integer
preferred_max_plans_per_month
integer
praise_charts_enabled
boolean
me_tab
string
plans_tab
string
songs_tab
string
media_tab
string
people_tab
string
can_edit_all_people
boolean
can_view_all_people
boolean
onboardings
array
Relationships
Name
Type
Association Type
Note
created_by
Person
to_one
updated_by
Person
to_one
current_folder
Folder
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
emails
include associated emails
include
tags
include associated tags
include
team_leaders
include associated team_leaders
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
first_name
string
prefix with a hyphen (-first_name) to reverse the order
order
last_name
string
prefix with a hyphen (-last_name) to reverse the order
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
assigned_to_rehearsal_team
where[assigned_to_rehearsal_team]
boolean
Query on a specific assigned_to_rehearsal_team

?where[assigned_to_rehearsal_team]=true
legacy_id
where[legacy_id]
primary_key
Query on a specific legacy_id

?where[legacy_id]=primary_key
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
/services/v2/people

Reading
HTTP Method
Endpoint
GET
/services/v2/people/{id}

Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/people/{id}

preferred_app
onboardings
access_media_attachments
access_plan_attachments
access_song_attachments
current_folder_id
media_permissions
permissions
song_permissions
Actions
assign_tags
HTTP Method
Endpoint
Description
POST
/services/v2/people/{person_id}/assign_tags

Used to assign tags to a person.

Details:

All tags will be replaced so the full data set must be sent.

It expects a body that looks like:

{
	"data": {
		"type": "TagAssignment",
		"attributes": {},
		"relationships": {
			"tags": {
				"data": [
					{
						"type": "Tag",
						"id": "5"
					}
				]
			}
		}
	}
}
On success you will get back a 204 No Content.

Permissions:

Must be authenticated

collapse_service_types
HTTP Method
Endpoint
Description
POST
/services/v2/people/{person_id}/collapse_service_types

Used to set Service Types as collapsed for the Person

Details:

It expects a body that looks like:

{
	"data": {
		"type": "CollapseServiceTypes",
		"attributes": {},
		"relationships": {
			"service_type": {
				"data": [
					{
						"type": "ServiceType",
						"id": "1"
					},
					{
						"type": "ServiceType",
						"id": "2"
					}
				]
			}
		}
	}
}
On success you will get back a 204 No Content.

Permissions:

Must be authenticated

expand_service_types
HTTP Method
Endpoint
Description
POST
/services/v2/people/{person_id}/expand_service_types

Used to set Service Types as expanded for the Person

Details:

It expects a body that looks like:

{
	"data": {
		"type": "ExpandServiceTypes",
		"attributes": {},
		"relationships": {
			"service_type": {
				"data": [
					{
						"type": "ServiceType",
						"id": "1"
					},
					{
						"type": "ServiceType",
						"id": "2"
					}
				]
			}
		}
	}
}
On success you will get back a 204 No Content.

Permissions:

Must be authenticated

Associations
available_signups
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/available_signups

AvailableSignup
current_organization

blockouts
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/blockouts

Blockout
future

past

emails
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/emails

Email
person_team_position_assignments
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/person_team_position_assignments

PersonTeamPositionAssignment
not_archived

not_deleted

plan_people
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/plan_people

PlanPerson
schedules
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/schedules

Schedule
after — Fetch schedules after the included after iso8601 date param. e.g. ?filter=after&after=2020-01-01T00:00:00Z

all

before — Fetch schedules before the included before iso8601 date param. e.g. ?filter=before&before=2020-01-01T00:00:00Z

future

not_across_organizations

past

with_declined

scheduling_preferences
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/scheduling_preferences

SchedulingPreference
tags
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/tags

Tag
team_leaders
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/team_leaders

TeamLeader
not_archived

not_deleted

text_settings
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/text_settings

TextSetting
Belongs To
Live
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/series/{series_id}/plans/{plan_id}/live/{live_id}/controller

Live
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people

Organization
PersonTeamPositionAssignment
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/team_positions/{team_position_id}/person_team_position_assignments/{person_team_position_assignment_id}/person

PersonTeamPositionAssignment
PlanPerson
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/plan_people/{plan_person_id}/person

PlanPerson
Schedule
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/schedules/{schedule_id}/respond_to

Schedule
TeamLeader
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/team_leaders/{team_leader_id}/people

TeamLeader
Team
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/teams/{team_id}/people

Team


---


PersonTeamPositionAssignment
A person's assignment to a position within a team.

Example Request
curl https://api.planningcenteronline.com/services/v2/service_types/{service_type_id}/team_positions/{team_position_id}/person_team_position_assignments
View in API Explorer
Example Object
{
  "type": "PersonTeamPositionAssignment",
  "id": "1",
  "attributes": {
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "schedule_preference": "string",
    "preferred_weeks": []
  },
  "relationships": {
    "person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "team_position": {
      "data": {
        "type": "TeamPosition",
        "id": "1"
      }
    },
    "time_preference_options": {
      "data": [
        {
          "type": "TimePreferenceOption",
          "id": "1"
        }
      ]
    }
  }
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
schedule_preference
string
Possible Values: "Every week" "Every other week" "Every 3rd week" "Every 4th week" "Every 5th week" "Every 6th week" "Once a month" "Twice a month" "Three times a month" "Choose Weeks"

preferred_weeks
array
When schedule_preference is set to "Choose Weeks" then this indicates which weeks are preferred (checked).

e.g. ['1', '3', '5'] to prefer odd numbered weeks.

Relationships
Name
Type
Association Type
Note
person
Person
to_one
team_position
TeamPosition
to_one
time_preference_options
TimePreferenceOption
to_many
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
include
team_position
include associated team_position
create and update
Order By
Parameter
Value
Type
Description
order
first_name
string
prefix with a hyphen (-first_name) to reverse the order
order
last_name
string
prefix with a hyphen (-last_name) to reverse the order
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
/services/v2/service_types/{service_type_id}/team_positions/{team_position_id}/person_team_position_assignments

Reading
HTTP Method
Endpoint
GET
/services/v2/service_types/{service_type_id}/team_positions/{team_position_id}/person_team_position_assignments/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/service_types/{service_type_id}/team_positions/{team_position_id}/person_team_position_assignments

schedule_preference
preferred_weeks
time_preference_option_ids
person_id
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/service_types/{service_type_id}/team_positions/{team_position_id}/person_team_position_assignments/{id}

schedule_preference
preferred_weeks
time_preference_option_ids
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/service_types/{service_type_id}/team_positions/{team_position_id}/person_team_position_assignments/{id}

Associations
person
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/team_positions/{team_position_id}/person_team_position_assignments/{person_team_position_assignment_id}/person

Person
team_position
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/team_positions/{team_position_id}/person_team_position_assignments/{person_team_position_assignment_id}/team_position

TeamPosition
Belongs To
Person
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/person_team_position_assignments

Person
not_archived

not_deleted

Team
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/teams/{team_id}/person_team_position_assignments

Team
TeamPosition
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/team_positions/{team_position_id}/person_team_position_assignments

TeamPosition
time_preference_options — pass an additonal array of time_preference_option_ids as a param to filter to people who prefer those times.use id 'none' to filter people who have no preferred times


----


Plan
A single plan within a Service Type.

Example Request
curl https://api.planningcenteronline.com/services/v2/service_types/{service_type_id}/plans
View in API Explorer
Example Object
{
  "type": "Plan",
  "id": "1",
  "attributes": {
    "can_view_order": true,
    "prefers_order_view": true,
    "rehearsable": true,
    "items_count": 1,
    "permissions": "string",
    "created_at": "2000-01-01T12:00:00Z",
    "title": "string",
    "updated_at": "2000-01-01T12:00:00Z",
    "public": true,
    "series_title": "string",
    "plan_notes_count": 1,
    "other_time_count": 1,
    "rehearsal_time_count": 1,
    "service_time_count": 1,
    "plan_people_count": 1,
    "needed_positions_count": 1,
    "total_length": 1,
    "multi_day": true,
    "files_expire_at": "2000-01-01T12:00:00Z",
    "sort_date": "2000-01-01T12:00:00Z",
    "last_time_at": "2000-01-01T12:00:00Z",
    "dates": "string",
    "short_dates": "string",
    "planning_center_url": "string",
    "reminders_disabled": true
  },
  "relationships": {
    "service_type": {
      "data": {
        "type": "ServiceType",
        "id": "1"
      }
    },
    "previous_plan": {
      "data": {
        "type": "Plan",
        "id": "1"
      }
    },
    "next_plan": {
      "data": {
        "type": "Plan",
        "id": "1"
      }
    },
    "series": {
      "data": {
        "type": "Series",
        "id": "1"
      }
    },
    "created_by": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "updated_by": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "linked_publishing_episode": {
      "data": {
        "type": "LinkedPublishingEpisode",
        "id": "1"
      }
    },
    "attachment_types": {
      "data": [
        {
          "type": "AttachmentType",
          "id": "1"
        }
      ]
    }
  }
}
Attributes
Name
Type
Description
id
primary_key
can_view_order
boolean
prefers_order_view
boolean
rehearsable
boolean
items_count
integer
The total number of items, including regular items, songs, media, and headers, that the current user can see in the plan.

permissions
string
The current user's permissions for this plan's Service Type.

created_at
date_time
title
string
updated_at
date_time
public
boolean
True if Public Access has been enabled.

series_title
string
plan_notes_count
integer
other_time_count
integer
rehearsal_time_count
integer
service_time_count
integer
plan_people_count
integer
needed_positions_count
integer
total_length
integer
The total of length of all items, excluding pre-service and post-service items.

multi_day
boolean
files_expire_at
date_time
A date 15 days after the last service time. Returns in the time zone specified in your organization's localization settings

sort_date
date_time
A time representing the chronological first Service Time, used to sort plan chronologically. If no Service Times exist, it uses Rehearsal Times, then Other Times, then NOW. Returns in the time zone specified in your organization's localization settings

last_time_at
date_time
Returns in the time zone specified in your organization's localization settings

dates
string
The full date string representing all Service Time dates.

short_dates
string
The shortened date string representing all Service Time dates. Months are abbreviated, and the year is omitted.

planning_center_url
string
reminders_disabled
boolean
Relationships
Name
Type
Association Type
Note
service_type
ServiceType
to_one
previous_plan
Plan
to_one
next_plan
Plan
to_one
series
Series
to_one
created_by
Person
to_one
updated_by
Person
to_one
linked_publishing_episode
LinkedPublishingEpisode
to_one
attachment_types
AttachmentType
to_many
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
contributors
include associated contributors
include
my_schedules
include associated my_schedules
include
plan_times
include associated plan_times
include
series
include associated series
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
sort_date
string
prefix with a hyphen (-sort_date) to reverse the order
order
title
string
prefix with a hyphen (-title) to reverse the order
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
id
where[id]
primary_key
Query on a specific id

?where[id]=primary_key
series_title
where[series_title]
string
Query on a specific series_title

?where[series_title]=string
title
where[title]
string
Query on a specific title

?where[title]=string
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
/services/v2/service_types/{service_type_id}/plans

Reading
HTTP Method
Endpoint
GET
/services/v2/service_types/{service_type_id}/plans/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/service_types/{service_type_id}/plans

title
public
series_id
series_title
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/service_types/{service_type_id}/plans/{id}

title
public
series_id
series_title
reminders_disabled
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/service_types/{service_type_id}/plans/{id}

Actions
autoschedule
HTTP Method
Endpoint
Description
POST
/services/v2/service_types/{service_type_id}/plans/{plan_id}/autoschedule

Auto-schedule for a team. Returns a collection of scheduled PlanPersonAutoscheduleVertex

Details:

Auto-schedule for a team. Returns a collection of scheduled PlanPersonAutoscheduleVertex.

It expects a POST body with a Team relationship.

{
  "data": {
    "type": "Autoschedule",
    "attributes": {},
    "relationship": {
      "team": {
        "data": {
          "id": 1,
          "type": 'Team'
        }
      }
    }
  }
}
Permissions:

Must be authenticated

import_template
Deprecated
HTTP Method
Endpoint
Description
POST
/services/v2/service_types/{service_type_id}/plans/{plan_id}/import_template

Import template to plan

Details:

This action allows the importing of a template into a plan.

Accepted attributes:

plan_id (Integer) ID of template to copying from

copy_items (Boolean) Copy Items from another plan. (default false)

copy_people (Boolean) Copy People from another plan. (default false)

copy_notes (Boolean) Copy Notes from another plan. (default false)

Permissions:

Must be authenticated

item_reorder
HTTP Method
Endpoint
Description
POST
/services/v2/service_types/{service_type_id}/plans/{plan_id}/item_reorder

Reorder plan items in one request.

Details:

This can be used to reorder all items in a plan in one request.

It expects a POST body with a sequence of Item ids in order. E.G.

{
  "data": {
    "type": "PlanItemReorder",
    "attributes": {
      "sequence": [
        "5",
        "1",
        "3"
      ]
    }
  }
}
On success you will get back a 204 No Content.

Permissions:

Must be authenticated

Associations
all_attachments
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/all_attachments

Attachment
attachable_type — filter attachments by their attachable_type as specified in the attachable_type parameter. Default: ["ServiceType", "Plan", "Item", "Media", "Song", "Arrangement", "Key"]. e.g. ?filter=attachable_type&attachable_type=Plan,ServiceType

extensions — filter to attachments with a file extension specified in the extensions parameter. e.g. ?filter=extensions&extensions=pdf,txt

attachments
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/attachments

Attachment
attendances
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/attendances

Attendance
contributors
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/contributors

Contributor
items
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items

Item
live
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/live

Live
my_schedules
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/my_schedules

Schedule
needed_positions
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/needed_positions

NeededPosition
next_plan
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/next_plan

Plan
notes
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/notes

PlanNote
team

plan_times
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/plan_times

PlanTime
previous_plan
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/previous_plan

Plan
series
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/series

Series
signup_teams
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/signup_teams

Team
team_members
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/team_members

PlanPerson
confirmed

not_archived

not_declined

not_deleted

Belongs To
Live
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/series/{series_id}/plans/{plan_id}/live/{live_id}/watchable_plans

Live
Plan
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/next_plan

Plan
PlanPerson
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/plan_people/{plan_person_id}/plan

PlanPerson
Plan
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/previous_plan

Plan
Series
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/series/{series_id}/plans

Series
ServiceType
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans

ServiceType
after — filter to plans with a time beginning after the after parameter

before — filter to plans with a time beginning before the before parameter

future

no_dates

past

ServiceType
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/unscoped_plans

ServiceType
deleted


-----


PlanNote
A specific plan note within a single plan.

Example Request
curl https://api.planningcenteronline.com/services/v2/service_types/{service_type_id}/plan_templates/{plan_template_id}/notes
View in API Explorer
Example Object
{
  "type": "PlanNote",
  "id": "1",
  "attributes": {
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "category_name": "string",
    "content": "string"
  },
  "relationships": {
    "created_by": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "plan_note_category": {
      "data": {
        "type": "PlanNoteCategory",
        "id": "1"
      }
    },
    "teams": {
      "data": {
        "type": "Team",
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
created_at
date_time
updated_at
date_time
category_name
string
content
string
Relationships
Name
Type
Association Type
Note
created_by
Person
to_one
plan_note_category
PlanNoteCategory
to_one
Required

teams
Team
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
plan_note_category
include associated plan_note_category
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
/services/v2/service_types/{service_type_id}/plan_templates/{plan_template_id}/notes

Reading
HTTP Method
Endpoint
GET
/services/v2/service_types/{service_type_id}/plan_templates/{plan_template_id}/notes/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/service_types/{service_type_id}/plans/{plan_id}/notes

content
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/service_types/{service_type_id}/plan_templates/{plan_template_id}/notes/{id}

content
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/service_types/{service_type_id}/plan_templates/{plan_template_id}/notes/{id}

Associations
plan_note_category
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_templates/{plan_template_id}/notes/{plan_note_id}/plan_note_category

PlanNoteCategory
Belongs To
Plan
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/notes

Plan
team

PlanTemplate
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_templates/{plan_template_id}/notes

PlanTemplate


----


PlanNoteCategory
A category of plan notes for an entire Service Type.

Example Request
curl https://api.planningcenteronline.com/services/v2/service_types/{service_type_id}/plan_note_categories
View in API Explorer
Example Object
{
  "type": "PlanNoteCategory",
  "id": "1",
  "attributes": {
    "created_at": "2000-01-01T12:00:00Z",
    "deleted_at": "2000-01-01T12:00:00Z",
    "name": "string",
    "sequence": 1,
    "updated_at": "2000-01-01T12:00:00Z"
  },
  "relationships": {
    "service_type": {
      "data": {
        "type": "ServiceType",
        "id": "1"
      }
    },
    "teams": {
      "data": {
        "type": "Team",
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
created_at
date_time
deleted_at
date_time
name
string
sequence
integer
updated_at
date_time
Relationships
Name
Type
Association Type
Note
service_type
ServiceType
to_one
teams
Team
to_one
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
/services/v2/service_types/{service_type_id}/plan_note_categories

Reading
HTTP Method
Endpoint
GET
/services/v2/service_types/{service_type_id}/plan_note_categories/{id}

Belongs To
PlanNote
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_templates/{plan_template_id}/notes/{plan_note_id}/plan_note_category

PlanNote
ServiceType
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_note_categories

ServiceType


----


PlanPerson
A person scheduled within a specific plan.

Example Request
curl https://api.planningcenteronline.com/services/v2/people/{person_id}/plan_people
View in API Explorer
Example Object
{
  "type": "PlanPerson",
  "id": "1",
  "attributes": {
    "status": "string",
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "notes": "string",
    "decline_reason": "string",
    "name": "string",
    "notification_changed_by_name": "string",
    "notification_sender_name": "string",
    "team_position_name": "string",
    "photo_thumbnail": "string",
    "scheduled_by_name": "string",
    "status_updated_at": "2000-01-01T12:00:00Z",
    "notification_changed_at": "2000-01-01T12:00:00Z",
    "notification_prepared_at": "2000-01-01T12:00:00Z",
    "notification_read_at": "2000-01-01T12:00:00Z",
    "notification_sent_at": "2000-01-01T12:00:00Z",
    "prepare_notification": true,
    "can_accept_partial": true
  },
  "relationships": {
    "person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "plan": {
      "data": {
        "type": "Plan",
        "id": "1"
      }
    },
    "scheduled_by": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "service_type": {
      "data": {
        "type": "ServiceType",
        "id": "1"
      }
    },
    "team": {
      "data": {
        "type": "Team",
        "id": "1"
      }
    },
    "responds_to": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "times": {
      "data": [
        {
          "type": "PlanTime",
          "id": "1"
        }
      ]
    },
    "service_times": {
      "data": [
        {
          "type": "PlanTime",
          "id": "1"
        }
      ]
    },
    "time_preference_options": {
      "data": [
        {
          "type": "TimePreferenceOption",
          "id": "1"
        }
      ]
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
string
Accepts one of 'C', 'U', 'D', or 'Confirmed', 'Unconfirmed', or 'Declined'

created_at
date_time
updated_at
date_time
notes
string
decline_reason
string
name
string
notification_changed_by_name
string
notification_sender_name
string
team_position_name
string
photo_thumbnail
string
scheduled_by_name
string
Only available when requested with the ?fields param

status_updated_at
date_time
notification_changed_at
date_time
notification_prepared_at
date_time
notification_read_at
date_time
notification_sent_at
date_time
prepare_notification
boolean
can_accept_partial
boolean
If the person is scheduled to a split team where they could potentially accept 1 time and decline another.

Relationships
Name
Type
Association Type
Note
person
Person
to_one
plan
Plan
to_one
scheduled_by
Person
to_one
service_type
ServiceType
to_one
team
Team
to_one
responds_to
Person
to_one
times
PlanTime
to_many
service_times
PlanTime
to_many
time_preference_options
TimePreferenceOption
to_many
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
declined_plan_times
include associated declined_plan_times
create and update
include
person
include associated person
create and update
include
plan
include associated plan
create and update
include
team
include associated team
create and update
Query By
Name
Parameter
Type
Description
Example
team_id
where[team_id]
integer
Query on a related team

?where[team_id]=1
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
/services/v2/people/{person_id}/plan_people

Reading
HTTP Method
Endpoint
GET
/services/v2/people/{person_id}/plan_people/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/service_types/{service_type_id}/plans/{plan_id}/team_members

person_id
team_id
status
decline_reason
notes
team_position_name
responds_to_id
prepare_notification
notification_prepared_at
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/people/{person_id}/plan_people/{id}

person_id
team_id
status
decline_reason
notes
team_position_name
responds_to_id
prepare_notification
notification_prepared_at
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/people/{person_id}/plan_people/{id}

Associations
declined_plan_times
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/plan_people/{plan_person_id}/declined_plan_times

PlanTime
person
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/plan_people/{plan_person_id}/person

Person
plan
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/plan_people/{plan_person_id}/plan

Plan
plan_person_times
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/plan_people/{plan_person_id}/plan_person_times

PlanPersonTime
plan_times
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/plan_people/{plan_person_id}/plan_times

PlanTime
team
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/plan_people/{plan_person_id}/team

Team
Belongs To
Person
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/plan_people

Person
Plan
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/team_members

Plan
confirmed

not_archived

not_declined

not_deleted

PlanTemplate
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_templates/{plan_template_id}/team_members

PlanTemplate

----


PlanPersonTime
Example Request
curl https://api.planningcenteronline.com/services/v2/people/{person_id}/plan_people/{plan_person_id}/plan_person_times
View in API Explorer
Example Object
{
  "type": "PlanPersonTime",
  "id": "1",
  "attributes": {
    "status": "string",
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z"
  },
  "relationships": {
    "plan_time": {
      "data": {
        "type": "PlanTime",
        "id": "1"
      }
    },
    "plan": {
      "data": {
        "type": "Plan",
        "id": "1"
      }
    },
    "plan_person": {
      "data": {
        "type": "PlanPerson",
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
string
created_at
date_time
updated_at
date_time
Relationships
Name
Type
Association Type
Note
plan_time
PlanTime
to_one
plan
Plan
to_one
plan_person
PlanPerson
to_one
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
/services/v2/people/{person_id}/plan_people/{plan_person_id}/plan_person_times

Reading
HTTP Method
Endpoint
GET
/services/v2/people/{person_id}/plan_people/{plan_person_id}/plan_person_times/{id}

Belongs To
PlanPerson
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/plan_people/{plan_person_id}/plan_person_times

PlanPerson


----

PlanTemplate
A PlanTemplate Resource

Example Request
curl https://api.planningcenteronline.com/services/v2/service_types/{service_type_id}/plan_templates
View in API Explorer
Example Object
{
  "type": "PlanTemplate",
  "id": "1",
  "attributes": {
    "name": "string",
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "item_count": 1,
    "team_count": 1,
    "note_count": 1,
    "can_view_order": true,
    "multi_day": true,
    "rehearsable": true,
    "prefers_order_view": true
  },
  "relationships": {
    "service_type": {
      "data": {
        "type": "ServiceType",
        "id": "1"
      }
    },
    "created_by": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "updated_by": {
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
id
primary_key
name
string
created_at
date_time
updated_at
date_time
item_count
integer
team_count
integer
note_count
integer
can_view_order
boolean
multi_day
boolean
rehearsable
boolean
prefers_order_view
boolean
Relationships
Name
Type
Association Type
Note
service_type
ServiceType
to_one
created_by
Person
to_one
updated_by
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
order
item_count
string
prefix with a hyphen (-item_count) to reverse the order
order
name
string
prefix with a hyphen (-name) to reverse the order
order
note_count
string
prefix with a hyphen (-note_count) to reverse the order
order
team_count
string
prefix with a hyphen (-team_count) to reverse the order
order
updated_at
string
prefix with a hyphen (-updated_at) to reverse the order
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
/services/v2/service_types/{service_type_id}/plan_templates

Reading
HTTP Method
Endpoint
GET
/services/v2/service_types/{service_type_id}/plan_templates/{id}

Actions
item_reorder
HTTP Method
Endpoint
Description
POST
/services/v2/service_types/{service_type_id}/plan_templates/{plan_template_id}/item_reorder

Reorder plan template items in one request.

Details:

This can be used to reorder all items in a plan template in one request.

It expects a POST body with a sequence of Item ids in order. E.G.

{
  "data": {
    "type": "PlanItemReorder",
    "attributes": {
      "sequence": [
        "5",
        "1",
        "3"
      ]
    }
  }
}
On success you will get back a 204 No Content.

Permissions:

Must be authenticated

Associations
items
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_templates/{plan_template_id}/items

Item
notes
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_templates/{plan_template_id}/notes

PlanNote
team_members
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_templates/{plan_template_id}/team_members

PlanPerson
confirmed

not_archived

not_declined

not_deleted

Belongs To
ServiceType
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_templates

ServiceType


----


PlanTime
A time in a plan.

Example Request
curl https://api.planningcenteronline.com/services/v2/service_types/{service_type_id}/plan_times
View in API Explorer
Example Object
{
  "type": "PlanTime",
  "id": "1",
  "attributes": {
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "name": "string",
    "time_type": "string",
    "recorded": true,
    "team_reminders": [],
    "starts_at": "2000-01-01T12:00:00Z",
    "ends_at": "2000-01-01T12:00:00Z",
    "live_starts_at": "2000-01-01T12:00:00Z",
    "live_ends_at": "2000-01-01T12:00:00Z"
  },
  "relationships": {
    "assigned_teams": {
      "data": [
        {
          "type": "Team",
          "id": "1"
        }
      ]
    },
    "assigned_positions": {
      "data": [
        {
          "type": "TeamPosition",
          "id": "1"
        }
      ]
    }
  }
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
name
string
time_type
string
Possible values are:

rehearsal

service

other

recorded
boolean
team_reminders
array
A Hash that maps a Team ID to a reminder value. If nothing is specified, no reminder is set for that team. A reminder value is an integer (0-7) equal to the number of days before the selected time a reminder should be sent.

starts_at
date_time
Planned start time.

ends_at
date_time
Planned end time.

live_starts_at
date_time
Start time as recorded by Services LIVE.

live_ends_at
date_time
End time as recorded by Services LIVE.

Relationships
Name
Type
Association Type
Note
assigned_teams
Team
to_many
assigned_positions
TeamPosition
to_many
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
split_team_rehearsal_assignments
include associated split_team_rehearsal_assignments
Order By
Parameter
Value
Type
Description
order
starts_at
string
prefix with a hyphen (-starts_at) to reverse the order
Query By
Name
Parameter
Type
Description
Example
time_type
where[time_type]
string
Query on a specific time_type

?where[time_type]=string
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
/services/v2/service_types/{service_type_id}/plan_times

Reading
HTTP Method
Endpoint
GET
/services/v2/service_types/{service_type_id}/plan_times/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/service_types/{service_type_id}/plans/{plan_id}/plan_times

starts_at
ends_at
name
time_type
team_reminders
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/service_types/{service_type_id}/plan_times/{id}

starts_at
ends_at
name
time_type
team_reminders
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/service_types/{service_type_id}/plan_times/{id}

Associations
split_team_rehearsal_assignments
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_times/{plan_time_id}/split_team_rehearsal_assignments

SplitTeamRehearsalAssignment
Belongs To
NeededPosition
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/series/{series_id}/plans/{plan_id}/needed_positions/{needed_position_id}/time

NeededPosition
PlanPerson
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/plan_people/{plan_person_id}/declined_plan_times

PlanPerson
PlanPerson
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/plan_people/{plan_person_id}/plan_times

PlanPerson
Plan
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/plan_times

Plan
Schedule
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/schedules/{schedule_id}/declined_plan_times

Schedule
Schedule
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/schedules/{schedule_id}/plan_times

Schedule
ServiceType
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_times

ServiceType
future

named

past

-----


PublicView
Manage options for a public plan

Example Request
curl https://api.planningcenteronline.com/services/v2/service_types/{service_type_id}/public_view
View in API Explorer
Example Object
{
  "type": "PublicView",
  "id": "1",
  "attributes": {
    "series_artwork": true,
    "series_and_plan_titles": true,
    "item_descriptions": true,
    "item_lengths": true,
    "service_times": true,
    "song_items": true,
    "media_items": true,
    "regular_items": true,
    "headers": true,
    "itunes": true,
    "amazon": true,
    "spotify": true,
    "youtube": true,
    "vimeo": true
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
series_artwork
boolean
series_and_plan_titles
boolean
item_descriptions
boolean
item_lengths
boolean
service_times
boolean
song_items
boolean
media_items
boolean
regular_items
boolean
headers
boolean
itunes
boolean
amazon
boolean
spotify
boolean
youtube
boolean
vimeo
boolean
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
/services/v2/service_types/{service_type_id}/public_view

Reading
HTTP Method
Endpoint
GET
/services/v2/service_types/{service_type_id}/public_view/{id}

Belongs To
ServiceType
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/public_view

ServiceType


-----


ReportTemplate
A template for generating reports

Example Request
curl https://api.planningcenteronline.com/services/v2/report_templates
View in API Explorer
Example Object
{
  "type": "ReportTemplate",
  "id": "1",
  "attributes": {
    "body": "string",
    "title": "string",
    "type": "string",
    "default": true
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
body
string
title
string
type
string
Possible values: ReportMatrix, ReportPeople, ReportPlan

default
boolean
A template provided by Planning Center

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
/services/v2/report_templates

Reading
HTTP Method
Endpoint
GET
/services/v2/report_templates/{id}

Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/report_templates

Organization
matrix

people

plans

without_defaults


----


Schedule
An instance of a PlanPerson with included data for displaying in a user's schedule

Example Request
curl https://api.planningcenteronline.com/services/v2/people/{person_id}/schedules
View in API Explorer
Example Object
{
  "type": "Schedule",
  "id": "1",
  "attributes": {
    "sort_date": "2000-01-01T12:00:00Z",
    "dates": "string",
    "decline_reason": "string",
    "organization_name": "string",
    "organization_time_zone": "string",
    "organization_twenty_four_hour_time": "string",
    "person_name": "string",
    "position_display_times": "string",
    "responds_to_name": "string",
    "service_type_name": "string",
    "short_dates": "string",
    "status": "string",
    "team_name": "string",
    "team_position_name": "string",
    "can_accept_partial": true,
    "can_accept_partial_one_time": true,
    "can_rehearse": true,
    "plan_visible": true,
    "plan_visible_to_me": true
  },
  "relationships": {
    "person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "service_type": {
      "data": {
        "type": "ServiceType",
        "id": "1"
      }
    },
    "organization": {
      "data": {
        "type": "Organization",
        "id": "1"
      }
    },
    "plan_person": {
      "data": {
        "type": "PlanPerson",
        "id": "1"
      }
    },
    "plan": {
      "data": {
        "type": "Plan",
        "id": "1"
      }
    },
    "team": {
      "data": {
        "type": "Team",
        "id": "1"
      }
    },
    "responds_to_person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "times": {
      "data": [
        {
          "type": "PlanTime",
          "id": "1"
        }
      ]
    }
  }
}
Attributes
Name
Type
Description
id
primary_key
sort_date
date_time
dates
string
decline_reason
string
organization_name
string
organization_time_zone
string
organization_twenty_four_hour_time
string
person_name
string
position_display_times
string
responds_to_name
string
service_type_name
string
short_dates
string
status
string
team_name
string
team_position_name
string
can_accept_partial
boolean
can_accept_partial_one_time
boolean
can_rehearse
boolean
plan_visible
boolean
True if the scheduled Plan is visible to the scheduled Person

plan_visible_to_me
boolean
True if the scheduled Plan is visible to the current Person

Relationships
Name
Type
Association Type
Note
person
Person
to_one
service_type
ServiceType
to_one
organization
Organization
to_one
plan_person
PlanPerson
to_one
plan
Plan
to_one
team
Team
to_one
responds_to_person
Person
to_one
times
PlanTime
to_many
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
plan_times
include associated plan_times
Order By
Parameter
Value
Type
Description
order
starts_at
string
prefix with a hyphen (-starts_at) to reverse the order
Query By
Name
Parameter
Type
Description
Example
plan_id
where[plan_id]
integer
Query on a related plan

?where[plan_id]=1
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
/services/v2/people/{person_id}/schedules

Reading
HTTP Method
Endpoint
GET
/services/v2/people/{person_id}/schedules/{id}

Actions
accept
HTTP Method
Endpoint
Description
POST
/services/v2/people/{person_id}/schedules/{schedule_id}/accept

Accept a Schedule

Details:

If this isn't a split time schedule, or you want to accept all times, an empty JSON body is accepted.

If the user wants to decline specific times you'll need to send the declined time IDs & a reason.

A POST body should be formated...

{
	"data": {
		"type": "ScheduleAccept",
		"attributes": {
			"reason": "Because reasons"
		},
		"relationships": {
			"declined_plan_times": {
				"data": [
          {
					  "type": "PlanTime",
					  "id": "1"
				  }
        ]
			}
		}
	}
}
Permissions:

Must be authenticated

decline
HTTP Method
Endpoint
Description
POST
/services/v2/people/{person_id}/schedules/{schedule_id}/decline

Decline a Schedule

Details:

If this is a split time request, all times will be declined.

If you want to decline specific times see ScheduleAcceptAction.

A POST body should be formated...

{
	"data": {
		"type": "ScheduleDecline",
		"attributes": {
			"reason": "A user supplied reason for declining the request or an empty string."
		},
		"relationships": null
	}
}
Permissions:

Must be authenticated

Associations
declined_plan_times
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/schedules/{schedule_id}/declined_plan_times

PlanTime
plan_times
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/schedules/{schedule_id}/plan_times

PlanTime
respond_to
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/schedules/{schedule_id}/respond_to

Person
team
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/schedules/{schedule_id}/team

Team
Belongs To
Person
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/schedules

Person
after — Fetch schedules after the included after iso8601 date param. e.g. ?filter=after&after=2020-01-01T00:00:00Z

all

before — Fetch schedules before the included before iso8601 date param. e.g. ?filter=before&before=2020-01-01T00:00:00Z

future

not_across_organizations

past

with_declined

Plan
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/my_schedules

Plan


---


ScheduledPerson
A person already scheduled to a SignupSheet

Example Request
curl https://api.planningcenteronline.com/services/v2/people/{person_id}/available_signups/{available_signup_id}/signup_sheets/{signup_sheet_id}/scheduled_people
View in API Explorer
Example Object
{
  "type": "ScheduledPerson",
  "id": "1",
  "attributes": {
    "full_name": "string",
    "status": "string",
    "thumbnail": "string"
  },
  "relationships": {
    "person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "signup_sheet": {
      "data": {
        "type": "SignupSheet",
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
full_name
string
status
string
thumbnail
string
Relationships
Name
Type
Association Type
Note
person
Person
to_one
signup_sheet
SignupSheet
to_one
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
/services/v2/people/{person_id}/available_signups/{available_signup_id}/signup_sheets/{signup_sheet_id}/scheduled_people

Reading
HTTP Method
Endpoint
GET
/services/v2/people/{person_id}/available_signups/{available_signup_id}/signup_sheets/{signup_sheet_id}/scheduled_people/{id}

Belongs To
SignupSheet
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/available_signups/{available_signup_id}/signup_sheets/{signup_sheet_id}/scheduled_people

SignupSheet


----


SchedulingPreference
Household member scheduling preference

Example Request
curl https://api.planningcenteronline.com/services/v2/people/{person_id}/scheduling_preferences
View in API Explorer
Example Object
{
  "type": "SchedulingPreference",
  "id": "1",
  "attributes": {
    "preference": "string"
  },
  "relationships": {
    "household_member": {
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
id
primary_key
preference
string
Relationships
Name
Type
Association Type
Note
household_member
Person
to_one
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
/services/v2/people/{person_id}/scheduling_preferences

Reading
HTTP Method
Endpoint
GET
/services/v2/people/{person_id}/scheduling_preferences/{id}

Belongs To
Person
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/scheduling_preferences

Person


----


Series
A Series can be specified for each plan to tie plans with similar messages together, even across Service Types.

Note: A series is not created until artwork is added from the plan. You can use series_title included in Plan attributes to get titles for series without artwork.

Example Request
curl https://api.planningcenteronline.com/services/v2/series
View in API Explorer
Example Object
{
  "type": "Series",
  "id": "1",
  "attributes": {
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "artwork_file_name": "string",
    "artwork_content_type": "string",
    "artwork_file_size": 1,
    "title": "string",
    "artwork_for_dashboard": "string",
    "artwork_for_mobile": "string",
    "artwork_for_plan": "string",
    "artwork_original": "string",
    "has_artwork": true
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
artwork_file_name
string
artwork_content_type
string
artwork_file_size
integer
title
string
artwork_for_dashboard
string
artwork_for_mobile
string
artwork_for_plan
string
artwork_original
string
has_artwork
boolean
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
title
where[title]
string
Query on a specific title

?where[title]=string
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
/services/v2/series

Reading
HTTP Method
Endpoint
GET
/services/v2/series/{id}

Associations
plans
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/series/{series_id}/plans

Plan
Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/series

Organization
Plan
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/series

Plan

----



ServiceType
A Service Type is a container for plans.

Example Request
curl https://api.planningcenteronline.com/services/v2/service_types
View in API Explorer
Example Object
{
  "type": "ServiceType",
  "id": "1",
  "attributes": {
    "archived_at": "2000-01-01T12:00:00Z",
    "created_at": "2000-01-01T12:00:00Z",
    "deleted_at": "2000-01-01T12:00:00Z",
    "name": "string",
    "sequence": 1,
    "updated_at": "2000-01-01T12:00:00Z",
    "permissions": "string",
    "attachment_types_enabled": true,
    "scheduled_publish": true,
    "custom_item_types": [],
    "standard_item_types": [],
    "background_check_permissions": "string",
    "comment_permissions": "string",
    "frequency": "string",
    "last_plan_from": "string"
  },
  "relationships": {
    "parent": {
      "data": {
        "type": "Folder",
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
archived_at
date_time
created_at
date_time
deleted_at
date_time
name
string
sequence
integer
updated_at
date_time
permissions
string
attachment_types_enabled
boolean
scheduled_publish
boolean
custom_item_types
array
A array of hashes that maps an item title substring matcher to a color:

[{ name: "Announcements", color: "#FFFFFF" }]

Valid substring matchers are any string that could be used as an item title.

A color is the hexadecimal value of a valid color e.g. #FFFFFF Valid colors values are #e8f6df, #e0f7ff, #e6e2fd, #ffe0e8, #ffedd1, #cfcfcf, #eaebeb, and #ffffff

standard_item_types
array
An array of hashes that maps an item type to a color:

[{ name: "Header", color: "#FFFFFF" }]

Valid names are Header, Song, and Media.

A color is the hexadecimal value of a valid color e.g. #FFFFFF Valid colors values are #e8f6df, #e0f7ff, #e6e2fd, #ffe0e8, #ffedd1, #cfcfcf, #eaebeb, and #ffffff

background_check_permissions
string
comment_permissions
string
frequency
string
last_plan_from
string
Relationships
Name
Type
Association Type
Note
parent
Folder
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
time_preference_options
include associated time_preference_options
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
name
where[name]
string
Query on a specific name

?where[name]=string
parent_id
where[parent_id]
integer
Query on a related parent

?where[parent_id]=1
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
/services/v2/service_types

Reading
HTTP Method
Endpoint
GET
/services/v2/service_types/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/service_types

attachment_types_enabled
background_check_permissions
comment_permissions
custom_item_types
frequency
last_plan_from
name
parent_id
scheduled_publish
sequence
standard_item_types
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/service_types/{id}

attachment_types_enabled
background_check_permissions
comment_permissions
custom_item_types
frequency
last_plan_from
name
parent_id
scheduled_publish
sequence
standard_item_types
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/service_types/{id}

Actions
create_plans
HTTP Method
Endpoint
Description
POST
/services/v2/service_types/{service_type_id}/create_plans

Create multiple plans

Details:

This action provides the abillity to create multiple plans with a single API request.

Accepted attributes:

count (Integer) The number of plans to create. (max 12, default 1)

copy_items (Boolean) Copy Items from another plan. (default false)

copy_people (Boolean) Copy People from another plan. (default false)

team_ids (Array[Integer]) IDs of teams to copy people from when copy_people is set to true. If nil, copy_people copies from all teams. (default nil)

copy_notes (Boolean) Copy Notes from another plan. (default false)

as_template (Boolean) Create the new plans as templates (default false)

base_date (ISO 8601 Date) The date from which to start building the plans. (default false)

Accepted Relationships

plan (optional) The plan from which to copy times, items, people, and notes

template (optional) Collection of templates from which to copy items, people, and notes (not times) for each new plan. Order dependant. Takes precedence over plan.

Permissions:

Must be authenticated

Associations
attachments
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/attachments

Attachment
item_note_categories
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/item_note_categories

ItemNoteCategory
live_controllers
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/live_controllers

LiveController
plan_note_categories
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_note_categories

PlanNoteCategory
plan_templates
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_templates

PlanTemplate
plan_times
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_times

PlanTime
future

named

past

plans
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans

Plan
after — filter to plans with a time beginning after the after parameter

before — filter to plans with a time beginning before the before parameter

future

no_dates

past

public_view
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/public_view

PublicView
team_positions
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/team_positions

TeamPosition
teams
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/teams

Team
time_preference_options
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/time_preference_options

TimePreferenceOption
unscoped_plans
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/unscoped_plans

Plan
deleted

Belongs To
Folder
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/folders/{folder_id}/service_types

Folder
Live
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/series/{series_id}/plans/{plan_id}/live/{live_id}/service_type

Live
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types

Organization
no_parent

Team
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/teams/{team_id}/service_types

Team


----


ServiceTypePath
The Folder path of a Service Type

Example Request
curl https://api.planningcenteronline.com/services/v2
View in API Explorer
Example Object
{
  "type": "ServiceTypePath",
  "id": "1",
  "attributes": {
    "path": []
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
path
array
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
/services/v2

Reading
HTTP Method
Endpoint
GET
/services/v2/{id}


----


SignupSheet
Available positions to sign up for

Example Request
curl https://api.planningcenteronline.com/services/v2/people/{person_id}/available_signups/{available_signup_id}/signup_sheets
View in API Explorer
Example Object
{
  "type": "SignupSheet",
  "id": "1",
  "attributes": {
    "sort_date": "2000-01-01T12:00:00Z",
    "group_key": "string",
    "team_name": "string",
    "display_times": "string",
    "position_name": "string",
    "title": "string",
    "sort_index": 1
  },
  "relationships": {
    "plan": {
      "data": {
        "type": "Plan",
        "id": "1"
      }
    },
    "team_position": {
      "data": {
        "type": "TeamPosition",
        "id": "1"
      }
    },
    "team": {
      "data": {
        "type": "Team",
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
sort_date
date_time
group_key
string
team_name
string
display_times
string
position_name
string
title
string
sort_index
integer
Relationships
Name
Type
Association Type
Note
plan
Plan
to_one
team_position
TeamPosition
to_one
team
Team
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
scheduled_people
include associated scheduled_people
include
signup_sheet_metadata
include associated signup_sheet_metadata
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
/services/v2/people/{person_id}/available_signups/{available_signup_id}/signup_sheets

Reading
HTTP Method
Endpoint
GET
/services/v2/people/{person_id}/available_signups/{available_signup_id}/signup_sheets/{id}

Actions
accept
HTTP Method
Endpoint
Description
POST
/services/v2/people/{person_id}/available_signups/{available_signup_id}/signup_sheets/{signup_sheet_id}/accept

Accept a signup sheet

Permissions:

Must be authenticated

Associations
scheduled_people
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/available_signups/{available_signup_id}/signup_sheets/{signup_sheet_id}/scheduled_people

ScheduledPerson
signup_sheet_metadata
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/available_signups/{available_signup_id}/signup_sheets/{signup_sheet_id}/signup_sheet_metadata

SignupSheetMetadata
Belongs To
AvailableSignup
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/available_signups/{available_signup_id}/signup_sheets

AvailableSignup


----

SignupSheetMetadata
Collection Only
A SignupSheetMetadata Resource

Example Request
curl https://api.planningcenteronline.com/services/v2/people/{person_id}/available_signups/{available_signup_id}/signup_sheets/{signup_sheet_id}/signup_sheet_metadata
View in API Explorer
Example Object
{
  "type": "SignupSheetMetadata",
  "id": "1",
  "attributes": {
    "conflicts": {},
    "time_type": "string",
    "time_name": "string",
    "ends_at": "2000-01-01T12:00:00Z",
    "starts_at": "2000-01-01T12:00:00Z"
  },
  "relationships": {
    "plan_time": {
      "data": {
        "type": "PlanTime",
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
conflicts
hash
time_type
string
time_name
string
ends_at
date_time
starts_at
date_time
Relationships
Name
Type
Association Type
Note
plan_time
PlanTime
to_one
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
/services/v2/people/{person_id}/available_signups/{available_signup_id}/signup_sheets/{signup_sheet_id}/signup_sheet_metadata

Belongs To
SignupSheet
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/available_signups/{available_signup_id}/signup_sheets/{signup_sheet_id}/signup_sheet_metadata

SignupSheet


----


SkippedAttachment
a skipped attachment

Example Request
curl https://api.planningcenteronline.com/services/v2
View in API Explorer
Example Object
{
  "type": "SkippedAttachment",
  "id": "1",
  "attributes": {
    "skipped": true
  },
  "relationships": {
    "person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "attachment": {
      "data": {
        "type": "Attachment",
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
skipped
boolean
Relationships
Name
Type
Association Type
Note
person
Person
to_one
attachment
Attachment
to_one
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
/services/v2

Reading
HTTP Method
Endpoint
GET
/services/v2/{id}


----


Song
A song

Example Request
curl https://api.planningcenteronline.com/services/v2/songs
View in API Explorer
Example Object
{
  "type": "Song",
  "id": "1",
  "attributes": {
    "title": "string",
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "admin": "string",
    "author": "string",
    "copyright": "string",
    "hidden": true,
    "notes": "string",
    "themes": "string",
    "last_scheduled_short_dates": "string",
    "last_scheduled_at": "2000-01-01T12:00:00Z",
    "ccli_number": 1
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
title
string
The name of the song.

When setting this value on a create you can pass a CCLI number and Services will fetch the song metadata for you.

created_at
date_time
updated_at
date_time
admin
string
author
string
copyright
string
hidden
boolean
notes
string
themes
string
last_scheduled_short_dates
string
last_scheduled_at
date_time
ccli_number
integer
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
last_scheduled_at
string
prefix with a hyphen (-last_scheduled_at) to reverse the order
order
title
string
prefix with a hyphen (-title) to reverse the order
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
author
where[author]
string
Query on a specific author

?where[author]=string
ccli_number
where[ccli_number]
integer
Query on a specific ccli_number

?where[ccli_number]=1
hidden
where[hidden]
boolean
Query on a specific hidden

?where[hidden]=true
themes
where[themes]
string
Query on a specific themes

?where[themes]=string
title
where[title]
string
Query on a specific title

?where[title]=string
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
/services/v2/songs

Reading
HTTP Method
Endpoint
GET
/services/v2/songs/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/songs

title
admin
author
copyright
ccli_number
hidden
themes
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/songs/{id}

title
admin
author
copyright
ccli_number
hidden
themes
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/songs/{id}

Actions
assign_tags
HTTP Method
Endpoint
Description
POST
/services/v2/songs/{song_id}/assign_tags

Used to assign tags to a song.

Details:

All tags will be replaced so the full data set must be sent.

It expects a body that looks like:

{
	"data": {
		"type": "TagAssignment",
		"attributes": {},
		"relationships": {
			"tags": {
				"data": [
					{
						"type": "Tag",
						"id": "5"
					}
				]
			}
		}
	}
}
On success you will get back a 204 No Content.

Permissions:

Must be authenticated

Associations
arrangements
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/songs/{song_id}/arrangements

Arrangement
attachments
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/songs/{song_id}/attachments

Attachment
last_scheduled_item
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/songs/{song_id}/last_scheduled_item

Item
The Song's most recently scheduled Item in a given Service Type. Requires a service_type query parameter. e.g. ?service_type=789

song_schedules
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/songs/{song_id}/song_schedules

SongSchedule
three_most_recent

tags
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/songs/{song_id}/tags

Tag
Belongs To
Item
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/items/{item_id}/song

Item
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/songs

Organization

----

SongSchedule
A upcoming schedule for a song

Example Request
curl https://api.planningcenteronline.com/services/v2/songs/{song_id}/song_schedules
View in API Explorer
Example Object
{
  "type": "SongSchedule",
  "id": "1",
  "attributes": {
    "arrangement_name": "string",
    "key_name": "string",
    "plan_dates": "string",
    "service_type_name": "string",
    "plan_sort_date": "string",
    "plan_visible": true
  },
  "relationships": {
    "arrangement": {
      "data": {
        "type": "Arrangement",
        "id": "1"
      }
    },
    "key": {
      "data": {
        "type": "Key",
        "id": "1"
      }
    },
    "plan": {
      "data": {
        "type": "Plan",
        "id": "1"
      }
    },
    "service_type": {
      "data": {
        "type": "ServiceType",
        "id": "1"
      }
    },
    "item": {
      "data": {
        "type": "Item",
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
arrangement_name
string
key_name
string
plan_dates
string
service_type_name
string
plan_sort_date
string
plan_visible
boolean
Relationships
Name
Type
Association Type
Note
arrangement
Arrangement
to_one
key
Key
to_one
plan
Plan
to_one
service_type
ServiceType
to_one
item
Item
to_one
URL Parameters
Order By
Parameter
Value
Type
Description
order
plan_sort_date
string
prefix with a hyphen (-plan_sort_date) to reverse the order
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
/services/v2/songs/{song_id}/song_schedules

Reading
HTTP Method
Endpoint
GET
/services/v2/songs/{song_id}/song_schedules/{id}

Belongs To
Song
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/songs/{song_id}/song_schedules

Song
three_most_recent

---

SongbookStatus
Used to get the status of an in progress songbook action. When FINISHED, will contain the url of the songbook.

Example Request
curl https://api.planningcenteronline.com/services/v2
View in API Explorer
Example Object
{
  "type": "SongbookStatus",
  "id": "1",
  "attributes": {
    "status": "string",
    "status_code": "string",
    "status_token": "string",
    "url": "string"
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
status
string
status_code
string
status_token
string
url
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
/services/v2

Reading
HTTP Method
Endpoint
GET
/services/v2/{id}


---


SplitTeamRehearsalAssignment
For Rehearsal/Other Times, maps a Split Team to selected Time Preference Options. For example, used to assign 8am Ushers to 7:30am call time, and 11am Ushers to 10:30am call time.

Example Request
curl https://api.planningcenteronline.com/services/v2/service_types/{service_type_id}/plan_times/{plan_time_id}/split_team_rehearsal_assignments
View in API Explorer
Example Object
{
  "type": "SplitTeamRehearsalAssignment",
  "id": "1",
  "attributes": {
    "schedule_special_service_times": true
  },
  "relationships": {
    "team": {
      "data": {
        "type": "Team",
        "id": "1"
      }
    },
    "time_preference_options": {
      "data": [
        {
          "type": "TimePreferenceOption",
          "id": "1"
        }
      ]
    }
  }
}
Attributes
Name
Type
Description
id
primary_key
schedule_special_service_times
boolean
Controls if the related rehearsal/other time is assigned when a person is scheduled to a split team service time that does not match a Time Preference Option

Relationships
Name
Type
Association Type
Note
team
Team
to_one
time_preference_options
TimePreferenceOption
to_many
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
/services/v2/service_types/{service_type_id}/plan_times/{plan_time_id}/split_team_rehearsal_assignments

Reading
HTTP Method
Endpoint
GET
/services/v2/service_types/{service_type_id}/plan_times/{plan_time_id}/split_team_rehearsal_assignments/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/service_types/{service_type_id}/plan_times/{plan_time_id}/split_team_rehearsal_assignments

schedule_special_service_times
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/service_types/{service_type_id}/plan_times/{plan_time_id}/split_team_rehearsal_assignments/{id}

schedule_special_service_times
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/service_types/{service_type_id}/plan_times/{plan_time_id}/split_team_rehearsal_assignments/{id}

Associations
team
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_times/{plan_time_id}/split_team_rehearsal_assignments/{split_team_rehearsal_assignment_id}/team

Team
Belongs To
PlanTime
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_times/{plan_time_id}/split_team_rehearsal_assignments

PlanTime

---- 

Tag
A tag belonging to a tag group.

Example Request
curl https://api.planningcenteronline.com/services/v2/media/{media_id}/tags
View in API Explorer
Example Object
{
  "type": "Tag",
  "id": "1",
  "attributes": {
    "name": "string"
  },
  "relationships": {
    "tag_group": {
      "data": {
        "type": "TagGroup",
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
Relationships
Name
Type
Association Type
Note
tag_group
TagGroup
to_one
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
/services/v2/media/{media_id}/tags

Reading
HTTP Method
Endpoint
GET
/services/v2/media/{media_id}/tags/{id}

Belongs To
Arrangement
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/songs/{song_id}/arrangements/{arrangement_id}/tags

Arrangement
Media
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/media/{media_id}/tags

Media
Person
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/tags

Person
Song
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/songs/{song_id}/tags

Song
TagGroup
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/tag_groups/{tag_group_id}/tags

TagGroup
TeamPosition
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/team_positions/{team_position_id}/tags

TeamPosition

----

TagGroup
A tag group contains tags

Example Request
curl https://api.planningcenteronline.com/services/v2/tag_groups
View in API Explorer
Example Object
{
  "type": "TagGroup",
  "id": "1",
  "attributes": {
    "name": "string",
    "required": true,
    "allow_multiple_selections": true,
    "tags_for": "string",
    "service_type_folder_name": "string"
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
required
boolean
allow_multiple_selections
boolean
tags_for
string
Scopes a tag group to person, song, arrangement, media

service_type_folder_name
string
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
folder
include associated folder
include
tags
include associated tags
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
tags_for
where[tags_for]
string
Query on a specific tags_for

?where[tags_for]=string
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
/services/v2/tag_groups

Reading
HTTP Method
Endpoint
GET
/services/v2/tag_groups/{id}

Associations
folder
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/tag_groups/{tag_group_id}/folder

Folder
tags
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/tag_groups/{tag_group_id}/tags

Tag
Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/tag_groups

Organization
arrangement

media

person

song


----

Team
A Team within a Service Type.

Example Request
curl https://api.planningcenteronline.com/services/v2/teams
View in API Explorer
Example Object
{
  "type": "Team",
  "id": "1",
  "attributes": {
    "name": "string",
    "rehearsal_team": true,
    "sequence": 1,
    "schedule_to": "string",
    "default_status": "string",
    "default_prepare_notifications": true,
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "archived_at": "2000-01-01T12:00:00Z",
    "viewers_see": 1,
    "assigned_directly": true,
    "secure_team": true,
    "last_plan_from": "string",
    "stage_color": "string",
    "stage_variant": "string"
  },
  "relationships": {
    "service_type": {
      "data": {
        "type": "ServiceType",
        "id": "1"
      }
    },
    "default_responds_to": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "service_types": {
      "data": {
        "type": "ServiceType",
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
rehearsal_team
boolean
sequence
integer
schedule_to
string
This determines whether a team is a split team or not.Accepted values: 1. "plan" (default) 2. "time" (designates as a split team)

default_status
string
default_prepare_notifications
boolean
created_at
date_time
updated_at
date_time
archived_at
date_time
viewers_see
integer
assigned_directly
boolean
secure_team
boolean
last_plan_from
string
stage_color
string
stage_variant
string
Relationships
Name
Type
Association Type
Note
service_type
ServiceType
to_one
default_responds_to
Person
to_one
A relationship with id 0 will be returned when "All Team Leaders" is the default.

service_types
ServiceType
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
people
include associated people
include
person_team_position_assignments
include associated person_team_position_assignments
include
service_types
include associated service_types
create and update
include
team_leaders
include associated team_leaders
include
team_positions
include associated team_positions
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
name
where[name]
string
Query on a specific name

?where[name]=string
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
/services/v2/teams

Reading
HTTP Method
Endpoint
GET
/services/v2/teams/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/service_types/{service_type_id}/teams

name
archived_at
assigned_directly
rehearsal_team
secure_team
schedule_to
stage_color
stage_variant
Associations
people
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/teams/{team_id}/people

Person
person_team_position_assignments
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/teams/{team_id}/person_team_position_assignments

PersonTeamPositionAssignment
service_types
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/teams/{team_id}/service_types

ServiceType
team_leaders
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/teams/{team_id}/team_leaders

TeamLeader
team_positions
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/teams/{team_id}/team_positions

TeamPosition
Belongs To
NeededPosition
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/series/{series_id}/plans/{plan_id}/needed_positions/{needed_position_id}/team

NeededPosition
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/teams

Organization
editable

service_types

PlanPerson
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/plan_people/{plan_person_id}/team

PlanPerson
Plan
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plans/{plan_id}/signup_teams

Plan
Schedule
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/schedules/{schedule_id}/team

Schedule
ServiceType
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/teams

ServiceType
SplitTeamRehearsalAssignment
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/plan_times/{plan_time_id}/split_team_rehearsal_assignments/{split_team_rehearsal_assignment_id}/team

SplitTeamRehearsalAssignment
TeamLeader
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/team_leaders/{team_leader_id}/team

TeamLeader
TeamPosition
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/team_positions/{team_position_id}/team

TeamPosition

----

TeamLeader
A leader of a specific Team in a Service Type.

Example Request
curl https://api.planningcenteronline.com/services/v2/people/{person_id}/team_leaders
View in API Explorer
Example Object
{
  "type": "TeamLeader",
  "id": "1",
  "attributes": {
    "send_responses_for_accepts": true,
    "send_responses_for_declines": true,
    "send_responses_for_blockouts": true
  },
  "relationships": {
    "person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "team": {
      "data": {
        "type": "Team",
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
send_responses_for_accepts
boolean
send_responses_for_declines
boolean
send_responses_for_blockouts
boolean
Relationships
Name
Type
Association Type
Note
person
Person
to_one
team
Team
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
people
include associated people
include
team
include associated team
create and update
Order By
Parameter
Value
Type
Description
order
first_name
string
prefix with a hyphen (-first_name) to reverse the order
order
last_name
string
prefix with a hyphen (-last_name) to reverse the order
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
/services/v2/people/{person_id}/team_leaders

Reading
HTTP Method
Endpoint
GET
/services/v2/people/{person_id}/team_leaders/{id}

Associations
people
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/team_leaders/{team_leader_id}/people

Person
team
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/people/{person_id}/team_leaders/{team_leader_id}/team

Team
Belongs To
Person
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/team_leaders

Person
not_archived

not_deleted

Team
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/teams/{team_id}/team_leaders

Team

---

TeamPosition
A position within a team.

Example Request
curl https://api.planningcenteronline.com/services/v2/service_types/{service_type_id}/team_positions
View in API Explorer
Example Object
{
  "type": "TeamPosition",
  "id": "1",
  "attributes": {
    "name": "string",
    "sequence": 1,
    "tags": [],
    "negative_tag_groups": [],
    "tag_groups": []
  },
  "relationships": {
    "team": {
      "data": {
        "type": "Team",
        "id": "1"
      }
    },
    "attachment_types": {
      "data": [
        {
          "type": "AttachmentType",
          "id": "1"
        }
      ]
    },
    "tags": {
      "data": [
        {
          "type": "Tag",
          "id": "1"
        }
      ]
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
sequence
integer
tags
array
If the Team is assigned via tags, these are specific Tags that are specified.

negative_tag_groups
array
If the Team is assigned via tags, these are Tags where the option "None" is specified.

tag_groups
array
If the Team is assigned via tags, these are Tags where the option "Any" is specified.

Relationships
Name
Type
Association Type
Note
team
Team
to_one
attachment_types
AttachmentType
to_many
tags
Tag
to_many
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
tags
include associated tags
create and update
include
team
include associated team
create and update
Order By
Parameter
Value
Type
Description
order
name
string
prefix with a hyphen (-name) to reverse the order
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
/services/v2/service_types/{service_type_id}/team_positions

Reading
HTTP Method
Endpoint
GET
/services/v2/service_types/{service_type_id}/team_positions/{id}

Associations
person_team_position_assignments
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/team_positions/{team_position_id}/person_team_position_assignments

PersonTeamPositionAssignment
time_preference_options — pass an additonal array of time_preference_option_ids as a param to filter to people who prefer those times.use id 'none' to filter people who have no preferred times

tags
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/team_positions/{team_position_id}/tags

Tag
team
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/team_positions/{team_position_id}/team

Team
Belongs To
PersonTeamPositionAssignment
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/team_positions/{team_position_id}/person_team_position_assignments/{person_team_position_assignment_id}/team_position

PersonTeamPositionAssignment
ServiceType
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/team_positions

ServiceType
Team
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/teams/{team_id}/team_positions

Team


---


TextSetting
Example Request
curl https://api.planningcenteronline.com/services/v2/people/{person_id}/text_settings
View in API Explorer
Example Object
{
  "type": "TextSetting",
  "id": "1",
  "attributes": {
    "scheduling_requests_enabled": true,
    "general_emails_enabled": true,
    "scheduling_replies_enabled": true,
    "reminders_enabled": true,
    "carrier": "string",
    "display_number": "string",
    "normalized_number": "string"
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
scheduling_requests_enabled
boolean
general_emails_enabled
boolean
scheduling_replies_enabled
boolean
reminders_enabled
boolean
carrier
string
display_number
string
normalized_number
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
/services/v2/people/{person_id}/text_settings

Reading
HTTP Method
Endpoint
GET
/services/v2/people/{person_id}/text_settings/{id}

Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/people/{person_id}/text_settings/{id}

general_emails_enabled
reminders_enabled
scheduling_replies_enabled
scheduling_requests_enabled
Belongs To
Person
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/people/{person_id}/text_settings

Person


---


TimePreferenceOption
A Service Time a person prefers to be scheduled to.

Example Request
curl https://api.planningcenteronline.com/services/v2/service_types/{service_type_id}/time_preference_options
View in API Explorer
Example Object
{
  "type": "TimePreferenceOption",
  "id": "1",
  "attributes": {
    "day_of_week": 1,
    "created_at": "2000-01-01T12:00:00Z",
    "updated_at": "2000-01-01T12:00:00Z",
    "description": "string",
    "sort_index": "string",
    "time_type": "string",
    "minute_of_day": 1,
    "starts_at": "2000-01-01T12:00:00Z"
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
day_of_week
integer
created_at
date_time
updated_at
date_time
description
string
sort_index
string
time_type
string
minute_of_day
integer
0 for 12:00 am, 1 for 12:01 am, 100 for 1:00 am, through 2359 for 11:59pm

starts_at
date_time
URL Parameters
Order By
Parameter
Value
Type
Description
order
day_of_week
string
prefix with a hyphen (-day_of_week) to reverse the order
order
hour_of_day
string
prefix with a hyphen (-hour_of_day) to reverse the order
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
/services/v2/service_types/{service_type_id}/time_preference_options

Reading
HTTP Method
Endpoint
GET
/services/v2/service_types/{service_type_id}/time_preference_options/{id}

Belongs To
ServiceType
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/service_types/{service_type_id}/time_preference_options

ServiceType


----


Zoom
Describes a zoom level for an attachment

Example Request
curl https://api.planningcenteronline.com/services/v2/media/{media_id}/attachments/{attachment_id}/zooms
View in API Explorer
Example Object
{
  "type": "Zoom",
  "id": "1",
  "attributes": {
    "aspect_ratio": 1.42,
    "zoom_level": 1.42,
    "x_offset": 1.42,
    "y_offset": 1.42
  },
  "relationships": {
    "person": {
      "data": {
        "type": "Person",
        "id": "1"
      }
    },
    "attachable": {
      "data": {
        "type": "Attachment",
        "id": "1"
      }
    },
    "attachment": {
      "data": {
        "type": "Attachment",
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
aspect_ratio
float
The aspect ratio of the device this zoom is for. It is rounded to the nearest 3 decimal places.

zoom_level
float
The percentage of the zoom. Must be a value between 1.0 and 5.0

x_offset
float
The percentage of the document's width the zoomed document should be offset by horizontally.

y_offset
float
The percentage of the document's height the zoomed document should be offset by vertically.

Relationships
Name
Type
Association Type
Note
person
Person
to_one
attachable
(polymorphic)
to_one
attachment
Attachment
to_one
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
/services/v2/media/{media_id}/attachments/{attachment_id}/zooms

Reading
HTTP Method
Endpoint
GET
/services/v2/media/{media_id}/attachments/{attachment_id}/zooms/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/services/v2/attachments/{attachment_id}/zooms

zoom_level
x_offset
y_offset
aspect_ratio
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/services/v2/media/{media_id}/attachments/{attachment_id}/zooms/{id}

zoom_level
x_offset
y_offset
Deleting
HTTP Method
Endpoint
DELETE
/services/v2/media/{media_id}/attachments/{attachment_id}/zooms/{id}

Belongs To
Attachment
HTTP Method
Endpoint
Association
Details
Filter By
GET
/services/v2/attachments/{attachment_id}/zooms

Attachment

