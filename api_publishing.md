# publishing


----

Channel
A collection of sermons

Example Request
curl https://api.planningcenteronline.com/publishing/v2/channels
View in API Explorer
Example Object
{
  "type": "Channel",
  "id": "1",
  "attributes": {
    "art": {},
    "podcast_art": {},
    "podcast_settings": {},
    "activate_episode_minutes_before": 1,
    "can_enable_chat": true,
    "church_center_url": "string",
    "created_at": "2000-01-01T12:00:00Z",
    "default_video_embed_code": "string",
    "description": "string",
    "url": "string",
    "default_video_duration": 1,
    "default_video_url": "string",
    "enable_audio": true,
    "enable_on_demand_video": true,
    "enable_watch_live": true,
    "general_chat_enabled": true,
    "group_chat_enabled": true,
    "name": "string",
    "podcast_feed_url": "string",
    "position": 1,
    "published": true,
    "sermon_notes_enabled": true,
    "services_service_type_remote_identifier": "string",
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
art
hash
podcast_art
hash
podcast_settings
hash
activate_episode_minutes_before
integer
The activation time for an episode, expressed in minutes before its start

can_enable_chat
boolean
church_center_url
string
created_at
date_time
default_video_embed_code
string
description
string
url
string
default_video_duration
integer
default_video_url
string
enable_audio
boolean
enable_on_demand_video
boolean
enable_watch_live
boolean
general_chat_enabled
boolean
group_chat_enabled
boolean
name
string
podcast_feed_url
string
position
integer
published
boolean
sermon_notes_enabled
boolean
services_service_type_remote_identifier
string
The id for the associated Services Service Type (https://developer.planning.center/docs/#/apps/services/2018-08-01/vertices/service_type)

updated_at
date_time
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
channel_default_episode_resources
include associated channel_default_episode_resources
create and update
include
channel_default_times
include associated channel_default_times
create and update
include
current_episode
include associated current_episode
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
position
string
prefix with a hyphen (-position) to reverse the order
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
/publishing/v2/channels

Reading
HTTP Method
Endpoint
GET
/publishing/v2/channels/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/publishing/v2/channels

art
podcast_art
podcast_settings
activate_episode_minutes_before
default_video_embed_code
description
url
default_video_duration
default_video_url
enable_audio
enable_on_demand_video
enable_watch_live
general_chat_enabled
group_chat_enabled
name
position
published
sermon_notes_enabled
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/publishing/v2/channels/{id}

art
podcast_art
podcast_settings
activate_episode_minutes_before
default_video_embed_code
description
url
default_video_duration
default_video_url
enable_audio
enable_on_demand_video
enable_watch_live
general_chat_enabled
group_chat_enabled
name
position
published
sermon_notes_enabled
Deleting
HTTP Method
Endpoint
DELETE
/publishing/v2/channels/{id}

Associations
channel_default_episode_resources
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/channels/{channel_id}/channel_default_episode_resources

ChannelDefaultEpisodeResource
channel_default_times
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/channels/{channel_id}/channel_default_times

ChannelDefaultTime
current_episode
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/channels/{channel_id}/current_episode

Episode
episodes
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/channels/{channel_id}/episodes

Episode
connected_to_services

not_connected_to_services

not_published

published

next_times
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/channels/{channel_id}/next_times

ChannelNextTime
series
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/channels/{channel_id}/series

Series
statistics
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/channels/{channel_id}/statistics

EpisodeStatistics
Belongs To
Episode
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/episodes/{episode_id}/channel

Episode
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/channels

Organization
Series
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/series/{series_id}/channel

Series

---

ChannelDefaultEpisodeResource
The default EpisodeResources for a Channel

Example Request
curl https://api.planningcenteronline.com/publishing/v2/channels/{channel_id}/channel_default_episode_resources
View in API Explorer
Example Object
{
  "type": "ChannelDefaultEpisodeResource",
  "id": "1",
  "attributes": {
    "featured": true,
    "icon": "string",
    "kind": "string",
    "position": 1,
    "title": "string",
    "type": "string",
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
featured
boolean
icon
string
kind
string
Possible values: giving_fund, people_form, generic_url, services_public_page

position
integer
title
string
type
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
/publishing/v2/channels/{channel_id}/channel_default_episode_resources

Reading
HTTP Method
Endpoint
GET
/publishing/v2/channels/{channel_id}/channel_default_episode_resources/{id}

Belongs To
Channel
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/channels/{channel_id}/channel_default_episode_resources

Channel


----


ChannelDefaultTime
The default times for a channel

Example Request
curl https://api.planningcenteronline.com/publishing/v2/channels/{channel_id}/channel_default_times
View in API Explorer
Example Object
{
  "type": "ChannelDefaultTime",
  "id": "1",
  "attributes": {
    "day_of_week": 1,
    "hour": 1,
    "minute": 1,
    "frequency": "string",
    "position": 1
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
The day of the week. 0 is Sunday, 1 is Monday, etc.

hour
integer
minute
integer
frequency
string
Possible values: weekly

position
integer
URL Parameters
Order By
Parameter
Value
Type
Description
order
position
string
prefix with a hyphen (-position) to reverse the order
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
/publishing/v2/channels/{channel_id}/channel_default_times

Reading
HTTP Method
Endpoint
GET
/publishing/v2/channels/{channel_id}/channel_default_times/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/publishing/v2/channels/{channel_id}/channel_default_times

day_of_week
hour
minute
frequency
position
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/publishing/v2/channels/{channel_id}/channel_default_times/{id}

day_of_week
hour
minute
frequency
position
Deleting
HTTP Method
Endpoint
DELETE
/publishing/v2/channels/{channel_id}/channel_default_times/{id}

Belongs To
Channel
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/channels/{channel_id}/channel_default_times

Channel


----


ChannelNextTime
The next default time for a channel

Example Request
curl https://api.planningcenteronline.com/publishing/v2/channels/{channel_id}/next_times
View in API Explorer
Example Object
{
  "type": "ChannelNextTime",
  "id": "1",
  "attributes": {
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
starts_at
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
/publishing/v2/channels/{channel_id}/next_times

Reading
HTTP Method
Endpoint
GET
/publishing/v2/channels/{channel_id}/next_times/{id}

Belongs To
Channel
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/channels/{channel_id}/next_times

Channel


----


Episode
Example Request
curl https://api.planningcenteronline.com/publishing/v2/episodes
View in API Explorer
Example Object
{
  "type": "Episode",
  "id": "1",
  "attributes": {
    "art": {},
    "church_center_url": "string",
    "created_at": "2000-01-01T12:00:00Z",
    "description": "string",
    "library_audio_url": "string",
    "library_streaming_service": "value",
    "library_video_embed_code": "string",
    "library_video_thumbnail_url": "string",
    "library_video_url": "string",
    "needs_library_audio_or_video_url": true,
    "needs_notes_template": true,
    "needs_video_url": true,
    "page_actions": [],
    "published_live_at": "2000-01-01T12:00:00Z",
    "published_to_library_at": "2000-01-01T12:00:00Z",
    "sermon_audio": {},
    "stream_type": "value",
    "streaming_service": "value",
    "title": "string",
    "updated_at": "2000-01-01T12:00:00Z",
    "video_thumbnail_url": "string",
    "video_embed_code": "string",
    "video_url": "string",
    "services_plan_remote_identifier": "string",
    "services_service_type_remote_identifier": "string"
  },
  "relationships": {
    "series": {
      "data": {
        "type": "Series",
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
art
hash
church_center_url
string
created_at
date_time
description
string
library_audio_url
string
library_streaming_service
string
Possible values: vimeo, youtube, livestream_com, resi, facebook, or boxcast

library_video_embed_code
string
library_video_thumbnail_url
string
library_video_url
string
needs_library_audio_or_video_url
boolean
needs_notes_template
boolean
needs_video_url
boolean
page_actions
array
published_live_at
date_time
published_to_library_at
date_time
sermon_audio
hash
stream_type
string
Possible values: channel_default_livestream, livestream, or prerecorded

streaming_service
string
Possible values: vimeo, youtube, livestream_com, resi, facebook, or boxcast

title
string
updated_at
date_time
video_thumbnail_url
string
video_embed_code
string
video_url
string
services_plan_remote_identifier
string
The id for the associated Services Plan (https://developer.planning.center/docs/#/apps/services/2018-08-01/vertices/plan)

services_service_type_remote_identifier
string
The id for the associated Services Service Type (https://developer.planning.center/docs/#/apps/services/2018-08-01/vertices/service_type)

Relationships
Name
Type
Association Type
Note
series
Series
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
channel
include associated channel
create and update
include
episode_resources
include associated episode_resources
create and update
include
episode_times
include associated episode_times
create and update
include
series
include associated series
create and update
include
speakerships
include associated speakerships
create and update
Order By
Parameter
Value
Type
Description
order
published_live_at
string
prefix with a hyphen (-published_live_at) to reverse the order
order
published_to_library_at
string
prefix with a hyphen (-published_to_library_at) to reverse the order
order
stream_type
string
prefix with a hyphen (-stream_type) to reverse the order
order
title
string
prefix with a hyphen (-title) to reverse the order
Query By
Name
Parameter
Type
Description
Example
series_id
where[series_id]
integer
Query on a related series

?where[series_id]=1
services_plan_remote_identifier
where[services_plan_remote_identifier]
string
Query on a specific services_plan_remote_identifier

?where[services_plan_remote_identifier]=string
services_service_type_remote_identifier
where[services_service_type_remote_identifier]
string
Query on a specific services_service_type_remote_identifier

?where[services_service_type_remote_identifier]=string
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
/publishing/v2/episodes

Reading
HTTP Method
Endpoint
GET
/publishing/v2/episodes/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/publishing/v2/episodes

art
series_id
title
description
sermon_audio
stream_type
video_url
published_to_library_at
library_audio_url
library_video_url
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/publishing/v2/episodes/{id}

art
series_id
title
description
sermon_audio
stream_type
video_url
published_to_library_at
library_audio_url
library_video_url
Deleting
HTTP Method
Endpoint
DELETE
/publishing/v2/episodes/{id}

Associations
channel
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/episodes/{episode_id}/channel

Channel
episode_resources
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/episodes/{episode_id}/episode_resources

EpisodeResource
episode_times
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/episodes/{episode_id}/episode_times

EpisodeTime
note_template
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/episodes/{episode_id}/note_template

NoteTemplate
series
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/episodes/{episode_id}/series

Series
speakerships
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/episodes/{episode_id}/speakerships

Speakership
Belongs To
Channel
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/channels/{channel_id}/current_episode

Channel
Channel
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/channels/{channel_id}/episodes

Channel
connected_to_services

not_connected_to_services

not_published

published

Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/episodes

Organization
connected_to_services

not_connected_to_services

not_published_live

published_live

published_on_church_center



----


EpisodeResource
Example Request
curl https://api.planningcenteronline.com/publishing/v2/episodes/{episode_id}/episode_resources
View in API Explorer
Example Object
{
  "type": "EpisodeResource",
  "id": "1",
  "attributes": {
    "featured": true,
    "icon": "string",
    "kind": "string",
    "position": 1,
    "title": "string",
    "type": "string",
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
featured
boolean
icon
string
kind
string
Possible values: giving_fund, people_form, generic_url, services_public_page

position
integer
title
string
type
string
url
string
URL Parameters
Order By
Parameter
Value
Type
Description
order
position
string
prefix with a hyphen (-position) to reverse the order
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
/publishing/v2/episodes/{episode_id}/episode_resources

Reading
HTTP Method
Endpoint
GET
/publishing/v2/episodes/{episode_id}/episode_resources/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/publishing/v2/episodes/{episode_id}/episode_resources

featured
icon
position
title
type
url
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/publishing/v2/episodes/{episode_id}/episode_resources/{id}

featured
icon
position
title
type
url
Deleting
HTTP Method
Endpoint
DELETE
/publishing/v2/episodes/{episode_id}/episode_resources/{id}

Belongs To
Episode
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/episodes/{episode_id}/episode_resources

Episode


----


EpisodeStatistics
Viewership statistics for an episode

Example Request
curl https://api.planningcenteronline.com/publishing/v2/channels/{channel_id}/statistics
View in API Explorer
Example Object
{
  "type": "EpisodeStatistics",
  "id": "1",
  "attributes": {
    "times": [],
    "library_watch_count": true,
    "live_watch_count": true,
    "published_to_library_at": "2000-01-01T12:00:00Z",
    "published_live_at": "2000-01-01T12:00:00Z",
    "title": "string"
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
times
array
watch_count per EpisodeTime

library_watch_count
boolean
live_watch_count
boolean
published_to_library_at
date_time
published_live_at
date_time
title
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
/publishing/v2/channels/{channel_id}/statistics

Reading
HTTP Method
Endpoint
GET
/publishing/v2/channels/{channel_id}/statistics/{id}

Belongs To
Channel
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/channels/{channel_id}/statistics

Channel


----


EpisodeTime
Live schedule times for an Episode

Example Request
curl https://api.planningcenteronline.com/publishing/v2/episodes/{episode_id}/episode_times
View in API Explorer
Example Object
{
  "type": "EpisodeTime",
  "id": "1",
  "attributes": {
    "starts_at": "2000-01-01T12:00:00Z",
    "ends_at": "2000-01-01T12:00:00Z",
    "video_url": "string",
    "video_embed_code": "string",
    "current_timestamp": 1.42,
    "current_state": "string",
    "streaming_service": "string",
    "caveats": []
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
ends_at
date_time
video_url
string
video_embed_code
string
current_timestamp
float
current_state
string
Possible values: upcoming, active, over

streaming_service
string
Possible values: vimeo, youtube, livestream_com, resi, facebook, boxcast

caveats
array
URL Parameters
Order By
Parameter
Value
Type
Description
order
starts_at
string
prefix with a hyphen (-starts_at) to reverse the order
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
/publishing/v2/episodes/{episode_id}/episode_times

Reading
HTTP Method
Endpoint
GET
/publishing/v2/episodes/{episode_id}/episode_times/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/publishing/v2/episodes/{episode_id}/episode_times

starts_at
video_embed_code
video_url
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/publishing/v2/episodes/{episode_id}/episode_times/{id}

starts_at
video_embed_code
video_url
Deleting
HTTP Method
Endpoint
DELETE
/publishing/v2/episodes/{episode_id}/episode_times/{id}

Belongs To
Episode
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/episodes/{episode_id}/episode_times

Episode


-----


NoteTemplate
Example Request
curl https://api.planningcenteronline.com/publishing/v2/episodes/{episode_id}/note_template
View in API Explorer
Example Object
{
  "type": "NoteTemplate",
  "id": "1",
  "attributes": {
    "enabled": true,
    "template": "string",
    "auto_create_free_form_notes": true,
    "published_at": "2000-01-01T12:00:00Z"
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
enabled
boolean
template
string
auto_create_free_form_notes
boolean
published_at
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
/publishing/v2/episodes/{episode_id}/note_template

Reading
HTTP Method
Endpoint
GET
/publishing/v2/episodes/{episode_id}/note_template/{id}

Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/publishing/v2/episodes/{episode_id}/note_template/{id}

enabled
template
auto_create_free_form_notes
Belongs To
Episode
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/episodes/{episode_id}/note_template

Episode


----


Organization
Example Request
curl https://api.planningcenteronline.com/publishing/v2
View in API Explorer
Example Object
{
  "type": "Organization",
  "id": "1",
  "attributes": {
    "name": "string",
    "subdomain": "string",
    "downloads_used": 1
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
subdomain
string
downloads_used
integer
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
/publishing/v2

Reading
HTTP Method
Endpoint
GET
/publishing/v2/{id}

Associations
channels
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/channels

Channel
episodes
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/episodes

Episode
connected_to_services

not_connected_to_services

not_published_live

published_live

published_on_church_center

series
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/series

Series
not_published

published

speakers
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/speakers

Speaker


---


Series
Example Request
curl https://api.planningcenteronline.com/publishing/v2/series
View in API Explorer
Example Object
{
  "type": "Series",
  "id": "1",
  "attributes": {
    "art": {},
    "church_center_url": "string",
    "description": "string",
    "ended_at": "2000-01-01T12:00:00Z",
    "episodes_count": 1,
    "published": true,
    "started_at": "2000-01-01T12:00:00Z",
    "title": "string",
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
art
hash
church_center_url
string
description
string
ended_at
date_time
episodes_count
integer
published
boolean
started_at
date_time
title
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
channel
include associated channel
Order By
Parameter
Value
Type
Description
order
ended_at
string
prefix with a hyphen (-ended_at) to reverse the order
order
episodes_count
string
prefix with a hyphen (-episodes_count) to reverse the order
order
started_at
string
prefix with a hyphen (-started_at) to reverse the order
order
title
string
prefix with a hyphen (-title) to reverse the order
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
/publishing/v2/series

Reading
HTTP Method
Endpoint
GET
/publishing/v2/series/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/publishing/v2/series

art
description
published
title
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/publishing/v2/series/{id}

art
description
published
title
Deleting
HTTP Method
Endpoint
DELETE
/publishing/v2/series/{id}

Associations
channel
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/series/{series_id}/channel

Channel
Belongs To
Channel
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/channels/{channel_id}/series

Channel
Episode
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/episodes/{episode_id}/series

Episode
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/series

Organization
not_published

published



-----

Speaker
Example Request
curl https://api.planningcenteronline.com/publishing/v2/speakers
View in API Explorer
Example Object
{
  "type": "Speaker",
  "id": "1",
  "attributes": {
    "avatar_url": "string",
    "episodes_count": 1,
    "first_name": "string",
    "formatted_name": "string",
    "last_name": "string",
    "name_prefix": "string",
    "name_suffix": "string",
    "speaker_type": "string"
  },
  "relationships": {}
}
Attributes
Name
Type
Description
id
primary_key
avatar_url
string
episodes_count
integer
first_name
string
formatted_name
string
last_name
string
name_prefix
string
name_suffix
string
speaker_type
string
URL Parameters
Order By
Parameter
Value
Type
Description
order
first_name
string
prefix with a hyphen (-first_name) to reverse the order
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
/publishing/v2/speakers

Reading
HTTP Method
Endpoint
GET
/publishing/v2/speakers/{id}

Belongs To
Organization
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/speakers

Organization
Speakership
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/episodes/{episode_id}/speakerships/{speakership_id}/speaker

Speakership


-----


Speakership
Example Request
curl https://api.planningcenteronline.com/publishing/v2/episodes/{episode_id}/speakerships
View in API Explorer
Example Object
{
  "type": "Speakership",
  "id": "1",
  "attributes": {},
  "relationships": {
    "speaker": {
      "data": {
        "type": "Speaker",
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
Relationships
Name
Type
Association Type
Note
speaker
(polymorphic)
to_one
URL Parameters
Can Include
Parameter
Value
Description
Assignable
include
speaker
include associated speaker
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
/publishing/v2/episodes/{episode_id}/speakerships

Reading
HTTP Method
Endpoint
GET
/publishing/v2/episodes/{episode_id}/speakerships/{id}

Creating
HTTP Method
Endpoint
Assignable Attributes
POST
/publishing/v2/episodes/{episode_id}/speakerships

speaker_id
Updating
HTTP Method
Endpoint
Assignable Attributes
PATCH
/publishing/v2/episodes/{episode_id}/speakerships/{id}

Deleting
HTTP Method
Endpoint
DELETE
/publishing/v2/episodes/{episode_id}/speakerships/{id}

Associations
speaker
HTTP Method
Endpoint
Returns
Details
Filter By
GET
/publishing/v2/episodes/{episode_id}/speakerships/{speakership_id}/speaker

Speaker
Belongs To
Episode
HTTP Method
Endpoint
Association
Details
Filter By
GET
/publishing/v2/episodes/{episode_id}/speakerships

Episode


