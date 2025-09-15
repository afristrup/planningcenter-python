"""Tests for services functionality."""

from datetime import datetime
from unittest.mock import AsyncMock

import pytest

from planning_center_api.products.services import (
    PCOArrangement,
    PCOAttachment,
    PCOFolder,
    PCOItem,
    PCOKey,
    PCOMedia,
    PCOPlan,
    PCOPlanNote,
    PCOPlanPerson,
    PCOPlanTime,
    PCOService,
    PCOServiceService,
    PCOServiceType,
    PCOSong,
    PCOTeam,
    PCOTeamPosition,
    PCOTemplate,
)


class TestPCOService:
    """Test PCOService model."""

    def test_service_creation(self):
        """Test service creation."""
        data = {
            "id": "1",
            "type": "Service",
            "attributes": {
                "name": "Sunday Service",
                "description": "Main Sunday service",
                "start_time": "2023-01-01T10:00:00Z",
                "end_time": "2023-01-01T12:00:00Z",
                "created_at": "2023-01-01T09:00:00Z",
                "updated_at": "2023-01-01T09:00:00Z",
            },
        }
        service = PCOService(**data)

        assert service.id == "1"
        assert service.type == "Service"
        assert service.name == "Sunday Service"
        assert service.description == "Main Sunday service"
        assert isinstance(service.start_time, datetime)
        assert isinstance(service.end_time, datetime)
        assert isinstance(service.created_at, datetime)
        assert isinstance(service.updated_at, datetime)


class TestPCOServiceType:
    """Test PCOServiceType model."""

    def test_service_type_creation(self):
        """Test service type creation."""
        data = {
            "id": "1",
            "type": "ServiceType",
            "attributes": {
                "name": "Sunday Morning",
                "description": "Main Sunday morning service",
                "created_at": "2023-01-01T09:00:00Z",
                "updated_at": "2023-01-01T09:00:00Z",
            },
        }
        service_type = PCOServiceType(**data)

        assert service_type.id == "1"
        assert service_type.type == "ServiceType"
        assert service_type.name == "Sunday Morning"
        assert service_type.description == "Main Sunday morning service"
        assert isinstance(service_type.created_at, datetime)
        assert isinstance(service_type.updated_at, datetime)


class TestPCOPlan:
    """Test PCOPlan model."""

    def test_plan_creation(self):
        """Test plan creation."""
        data = {
            "id": "1",
            "type": "Plan",
            "attributes": {
                "title": "Sunday Service Plan",
                "series_title": "Advent Series",
                "plan_notes_count": 5,
                "other_time_count": 2,
                "service_time_count": 1,
                "sort_date": "2023-01-01T10:00:00Z",
                "created_at": "2023-01-01T09:00:00Z",
                "updated_at": "2023-01-01T09:00:00Z",
            },
        }
        plan = PCOPlan(**data)

        assert plan.id == "1"
        assert plan.type == "Plan"
        assert plan.title == "Sunday Service Plan"
        assert plan.series_title == "Advent Series"
        assert plan.plan_notes_count == 5
        assert plan.other_time_count == 2
        assert plan.service_time_count == 1
        assert isinstance(plan.sort_date, datetime)
        assert isinstance(plan.created_at, datetime)
        assert isinstance(plan.updated_at, datetime)


class TestPCOPlanTime:
    """Test PCOPlanTime model."""

    def test_plan_time_creation(self):
        """Test plan time creation."""
        data = {
            "id": "1",
            "type": "PlanTime",
            "attributes": {
                "name": "Service Time",
                "starts_at": "2023-01-01T10:00:00Z",
                "ends_at": "2023-01-01T12:00:00Z",
                "live": True,
                "created_at": "2023-01-01T09:00:00Z",
                "updated_at": "2023-01-01T09:00:00Z",
            },
        }
        plan_time = PCOPlanTime(**data)

        assert plan_time.id == "1"
        assert plan_time.type == "PlanTime"
        assert plan_time.name == "Service Time"
        assert isinstance(plan_time.starts_at, datetime)
        assert isinstance(plan_time.ends_at, datetime)
        assert plan_time.live is True
        assert isinstance(plan_time.created_at, datetime)
        assert isinstance(plan_time.updated_at, datetime)


class TestPCOPlanPerson:
    """Test PCOPlanPerson model."""

    def test_plan_person_creation(self):
        """Test plan person creation."""
        data = {
            "id": "1",
            "type": "PlanPerson",
            "attributes": {
                "status": "confirmed",
                "team_position_name": "Worship Leader",
                "created_at": "2023-01-01T09:00:00Z",
                "updated_at": "2023-01-01T09:00:00Z",
            },
        }
        plan_person = PCOPlanPerson(**data)

        assert plan_person.id == "1"
        assert plan_person.type == "PlanPerson"
        assert plan_person.status == "confirmed"
        assert plan_person.team_position_name == "Worship Leader"
        assert isinstance(plan_person.created_at, datetime)
        assert isinstance(plan_person.updated_at, datetime)


class TestPCOPlanNote:
    """Test PCOPlanNote model."""

    def test_plan_note_creation(self):
        """Test plan note creation."""
        data = {
            "id": "1",
            "type": "PlanNote",
            "attributes": {
                "content": "Remember to check sound system",
                "created_at": "2023-01-01T09:00:00Z",
                "updated_at": "2023-01-01T09:00:00Z",
            },
        }
        plan_note = PCOPlanNote(**data)

        assert plan_note.id == "1"
        assert plan_note.type == "PlanNote"
        assert plan_note.content == "Remember to check sound system"
        assert isinstance(plan_note.created_at, datetime)
        assert isinstance(plan_note.updated_at, datetime)


class TestPCOSong:
    """Test PCOSong model."""

    def test_song_creation(self):
        """Test song creation."""
        data = {
            "id": "1",
            "type": "Song",
            "attributes": {
                "title": "Amazing Grace",
                "author": "John Newton",
                "ccli_number": "12345",
                "created_at": "2023-01-01T09:00:00Z",
                "updated_at": "2023-01-01T09:00:00Z",
            },
        }
        song = PCOSong(**data)

        assert song.id == "1"
        assert song.type == "Song"
        assert song.title == "Amazing Grace"
        assert song.author == "John Newton"
        assert song.ccli_number == "12345"
        assert isinstance(song.created_at, datetime)
        assert isinstance(song.updated_at, datetime)


class TestPCOArrangement:
    """Test PCOArrangement model."""

    def test_arrangement_creation(self):
        """Test arrangement creation."""
        data = {
            "id": "1",
            "type": "Arrangement",
            "attributes": {
                "name": "Standard Arrangement",
                "bpm": 120.0,
                "length": 240,
                "meter": "4/4",
                "has_chords": True,
                "notes": "Standard arrangement",
                "lyrics": "Amazing grace, how sweet the sound",
                "created_at": "2023-01-01T09:00:00Z",
                "updated_at": "2023-01-01T09:00:00Z",
            },
        }
        arrangement = PCOArrangement(**data)

        assert arrangement.id == "1"
        assert arrangement.type == "Arrangement"
        assert arrangement.name == "Standard Arrangement"
        assert arrangement.bpm == 120.0
        assert arrangement.length == 240
        assert arrangement.meter == "4/4"
        assert arrangement.has_chords is True
        assert arrangement.notes == "Standard arrangement"
        assert arrangement.lyrics == "Amazing grace, how sweet the sound"
        assert isinstance(arrangement.created_at, datetime)
        assert isinstance(arrangement.updated_at, datetime)


class TestPCOKey:
    """Test PCOKey model."""

    def test_key_creation(self):
        """Test key creation."""
        data = {
            "id": "1",
            "type": "Key",
            "attributes": {
                "name": "C Major",
                "created_at": "2023-01-01T09:00:00Z",
                "updated_at": "2023-01-01T09:00:00Z",
            },
        }
        key = PCOKey(**data)

        assert key.id == "1"
        assert key.type == "Key"
        assert key.name == "C Major"
        assert isinstance(key.created_at, datetime)
        assert isinstance(key.updated_at, datetime)


class TestPCOAttachment:
    """Test PCOAttachment model."""

    def test_attachment_creation(self):
        """Test attachment creation."""
        data = {
            "id": "1",
            "type": "Attachment",
            "attributes": {
                "filename": "sermon_notes.pdf",
                "content_type": "application/pdf",
                "file_size": 1024000,
                "created_at": "2023-01-01T09:00:00Z",
                "updated_at": "2023-01-01T09:00:00Z",
            },
        }
        attachment = PCOAttachment(**data)

        assert attachment.id == "1"
        assert attachment.type == "Attachment"
        assert attachment.filename == "sermon_notes.pdf"
        assert attachment.content_type == "application/pdf"
        assert attachment.file_size == 1024000
        assert isinstance(attachment.created_at, datetime)
        assert isinstance(attachment.updated_at, datetime)


class TestPCOMedia:
    """Test PCOMedia model."""

    def test_media_creation(self):
        """Test media creation."""
        data = {
            "id": "1",
            "type": "Media",
            "attributes": {
                "filename": "worship_video.mp4",
                "content_type": "video/mp4",
                "file_size": 50000000,
                "created_at": "2023-01-01T09:00:00Z",
                "updated_at": "2023-01-01T09:00:00Z",
            },
        }
        media = PCOMedia(**data)

        assert media.id == "1"
        assert media.type == "Media"
        assert media.filename == "worship_video.mp4"
        assert media.content_type == "video/mp4"
        assert media.file_size == 50000000
        assert isinstance(media.created_at, datetime)
        assert isinstance(media.updated_at, datetime)


class TestPCOFolder:
    """Test PCOFolder model."""

    def test_folder_creation(self):
        """Test folder creation."""
        data = {
            "id": "1",
            "type": "Folder",
            "attributes": {
                "name": "Worship Songs",
                "created_at": "2023-01-01T09:00:00Z",
                "updated_at": "2023-01-01T09:00:00Z",
            },
        }
        folder = PCOFolder(**data)

        assert folder.id == "1"
        assert folder.type == "Folder"
        assert folder.name == "Worship Songs"
        assert isinstance(folder.created_at, datetime)
        assert isinstance(folder.updated_at, datetime)


class TestPCOTemplate:
    """Test PCOTemplate model."""

    def test_template_creation(self):
        """Test template creation."""
        data = {
            "id": "1",
            "type": "Template",
            "attributes": {
                "name": "Sunday Service Template",
                "created_at": "2023-01-01T09:00:00Z",
                "updated_at": "2023-01-01T09:00:00Z",
            },
        }
        template = PCOTemplate(**data)

        assert template.id == "1"
        assert template.type == "Template"
        assert template.name == "Sunday Service Template"
        assert isinstance(template.created_at, datetime)
        assert isinstance(template.updated_at, datetime)


class TestPCOItem:
    """Test PCOItem model."""

    def test_item_creation(self):
        """Test item creation."""
        data = {
            "id": "1",
            "type": "Item",
            "attributes": {
                "title": "Welcome & Announcements",
                "length": 300,
                "created_at": "2023-01-01T09:00:00Z",
                "updated_at": "2023-01-01T09:00:00Z",
            },
        }
        item = PCOItem(**data)

        assert item.id == "1"
        assert item.type == "Item"
        assert item.title == "Welcome & Announcements"
        assert item.length == 300
        assert isinstance(item.created_at, datetime)
        assert isinstance(item.updated_at, datetime)


class TestPCOTeam:
    """Test PCOTeam model."""

    def test_team_creation(self):
        """Test team creation."""
        data = {
            "id": "1",
            "type": "Team",
            "attributes": {
                "name": "Worship Team",
                "created_at": "2023-01-01T09:00:00Z",
                "updated_at": "2023-01-01T09:00:00Z",
            },
        }
        team = PCOTeam(**data)

        assert team.id == "1"
        assert team.type == "Team"
        assert team.name == "Worship Team"
        assert isinstance(team.created_at, datetime)
        assert isinstance(team.updated_at, datetime)


class TestPCOTeamPosition:
    """Test PCOTeamPosition model."""

    def test_team_position_creation(self):
        """Test team position creation."""
        data = {
            "id": "1",
            "type": "TeamPosition",
            "attributes": {
                "name": "Lead Vocalist",
                "created_at": "2023-01-01T09:00:00Z",
                "updated_at": "2023-01-01T09:00:00Z",
            },
        }
        team_position = PCOTeamPosition(**data)

        assert team_position.id == "1"
        assert team_position.type == "TeamPosition"
        assert team_position.name == "Lead Vocalist"
        assert isinstance(team_position.created_at, datetime)
        assert isinstance(team_position.updated_at, datetime)


class TestPCOServiceService:
    """Test PCOServiceService."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock client."""
        client = AsyncMock()
        client.get = AsyncMock()
        client.post = AsyncMock()
        client.patch = AsyncMock()
        client.delete = AsyncMock()
        return client

    @pytest.fixture
    def service_service(self, mock_client):
        """Create a service service with mock client."""
        return PCOServiceService(mock_client)

    async def test_get_service_types(self, service_service, mock_client):
        """Test getting service types."""
        mock_response = {
            "data": [
                {
                    "id": "1",
                    "type": "ServiceType",
                    "attributes": {
                        "name": "Sunday Morning",
                        "description": "Main Sunday morning service",
                    },
                }
            ]
        }
        mock_client.get.return_value = mock_response

        service_types = await service_service.get_service_types()

        assert len(service_types) == 1
        assert service_types[0].id == "1"
        assert service_types[0].name == "Sunday Morning"
        mock_client.get.assert_called_once_with(
            "/services/v2/service_types", params={}
        )

    async def test_get_service_type(self, service_service, mock_client):
        """Test getting a specific service type."""
        mock_response = {
            "data": {
                "id": "1",
                "type": "ServiceType",
                "attributes": {
                    "name": "Sunday Morning",
                    "description": "Main Sunday morning service",
                },
            }
        }
        mock_client.get.return_value = mock_response

        service_type = await service_service.get_service_type("1")

        assert service_type.id == "1"
        assert service_type.name == "Sunday Morning"
        mock_client.get.assert_called_once_with("/services/v2/service_types/1")

    async def test_get_plans(self, service_service, mock_client):
        """Test getting plans."""
        mock_response = {
            "data": [
                {
                    "id": "1",
                    "type": "Plan",
                    "attributes": {
                        "title": "Sunday Service Plan",
                        "series_title": "Advent Series",
                    },
                }
            ]
        }
        mock_client.get.return_value = mock_response

        plans = await service_service.get_plans()

        assert len(plans) == 1
        assert plans[0].id == "1"
        assert plans[0].title == "Sunday Service Plan"
        mock_client.get.assert_called_once_with("/services/v2/plans", params={})

    async def test_get_plan(self, service_service, mock_client):
        """Test getting a specific plan."""
        mock_response = {
            "data": {
                "id": "1",
                "type": "Plan",
                "attributes": {
                    "title": "Sunday Service Plan",
                    "series_title": "Advent Series",
                },
            }
        }
        mock_client.get.return_value = mock_response

        plan = await service_service.get_plan("1")

        assert plan.id == "1"
        assert plan.title == "Sunday Service Plan"
        mock_client.get.assert_called_once_with("/services/v2/plans/1")

    async def test_create_plan(self, service_service, mock_client):
        """Test creating a plan."""
        mock_response = {
            "data": {
                "id": "1",
                "type": "Plan",
                "attributes": {
                    "title": "New Service Plan",
                    "series_title": "New Series",
                },
            }
        }
        mock_client.post.return_value = mock_response

        plan = await service_service.create_plan(
            service_type_id="1",
            title="New Service Plan",
            series_title="New Series"
        )

        assert plan.id == "1"
        assert plan.title == "New Service Plan"
        mock_client.post.assert_called_once()
        call_args = mock_client.post.call_args
        assert call_args[0][0] == "/services/v2/plans"
        assert call_args[1]["json"]["data"]["attributes"]["title"] == "New Service Plan"

    async def test_update_plan(self, service_service, mock_client):
        """Test updating a plan."""
        mock_response = {
            "data": {
                "id": "1",
                "type": "Plan",
                "attributes": {
                    "title": "Updated Service Plan",
                    "series_title": "Updated Series",
                },
            }
        }
        mock_client.patch.return_value = mock_response

        plan = await service_service.update_plan(
            plan_id="1",
            title="Updated Service Plan",
            series_title="Updated Series"
        )

        assert plan.id == "1"
        assert plan.title == "Updated Service Plan"
        mock_client.patch.assert_called_once()
        call_args = mock_client.patch.call_args
        assert call_args[0][0] == "/services/v2/plans/1"
        assert call_args[1]["json"]["data"]["attributes"]["title"] == "Updated Service Plan"

    async def test_delete_plan(self, service_service, mock_client):
        """Test deleting a plan."""
        await service_service.delete_plan("1")

        mock_client.delete.assert_called_once_with("/services/v2/plans/1")

    async def test_get_songs(self, service_service, mock_client):
        """Test getting songs."""
        mock_response = {
            "data": [
                {
                    "id": "1",
                    "type": "Song",
                    "attributes": {
                        "title": "Amazing Grace",
                        "author": "John Newton",
                    },
                }
            ]
        }
        mock_client.get.return_value = mock_response

        songs = await service_service.get_songs()

        assert len(songs) == 1
        assert songs[0].id == "1"
        assert songs[0].title == "Amazing Grace"
        mock_client.get.assert_called_once_with("/services/v2/songs", params={})

    async def test_get_song(self, service_service, mock_client):
        """Test getting a specific song."""
        mock_response = {
            "data": {
                "id": "1",
                "type": "Song",
                "attributes": {
                    "title": "Amazing Grace",
                    "author": "John Newton",
                },
            }
        }
        mock_client.get.return_value = mock_response

        song = await service_service.get_song("1")

        assert song.id == "1"
        assert song.title == "Amazing Grace"
        mock_client.get.assert_called_once_with("/services/v2/songs/1")

    async def test_create_song(self, service_service, mock_client):
        """Test creating a song."""
        mock_response = {
            "data": {
                "id": "1",
                "type": "Song",
                "attributes": {
                    "title": "New Song",
                    "author": "New Author",
                },
            }
        }
        mock_client.post.return_value = mock_response

        song = await service_service.create_song(
            title="New Song",
            author="New Author",
            ccli_number="12345"
        )

        assert song.id == "1"
        assert song.title == "New Song"
        mock_client.post.assert_called_once()
        call_args = mock_client.post.call_args
        assert call_args[0][0] == "/services/v2/songs"
        assert call_args[1]["json"]["data"]["attributes"]["title"] == "New Song"

    async def test_get_arrangements(self, service_service, mock_client):
        """Test getting arrangements."""
        mock_response = {
            "data": [
                {
                    "id": "1",
                    "type": "Arrangement",
                    "attributes": {
                        "name": "Standard Arrangement",
                        "bpm": 120.0,
                    },
                }
            ]
        }
        mock_client.get.return_value = mock_response

        arrangements = await service_service.get_arrangements("1")

        assert len(arrangements) == 1
        assert arrangements[0].id == "1"
        assert arrangements[0].name == "Standard Arrangement"
        mock_client.get.assert_called_once_with(
            "/services/v2/songs/1/arrangements", params={}
        )

    async def test_get_arrangement(self, service_service, mock_client):
        """Test getting a specific arrangement."""
        mock_response = {
            "data": {
                "id": "1",
                "type": "Arrangement",
                "attributes": {
                    "name": "Standard Arrangement",
                    "bpm": 120.0,
                },
            }
        }
        mock_client.get.return_value = mock_response

        arrangement = await service_service.get_arrangement("1", "1")

        assert arrangement.id == "1"
        assert arrangement.name == "Standard Arrangement"
        mock_client.get.assert_called_once_with("/services/v2/songs/1/arrangements/1")

    async def test_get_keys(self, service_service, mock_client):
        """Test getting keys."""
        mock_response = {
            "data": [
                {
                    "id": "1",
                    "type": "Key",
                    "attributes": {
                        "name": "C Major",
                    },
                }
            ]
        }
        mock_client.get.return_value = mock_response

        keys = await service_service.get_keys()

        assert len(keys) == 1
        assert keys[0].id == "1"
        assert keys[0].name == "C Major"
        mock_client.get.assert_called_once_with("/services/v2/keys", params={})

    async def test_get_key(self, service_service, mock_client):
        """Test getting a specific key."""
        mock_response = {
            "data": {
                "id": "1",
                "type": "Key",
                "attributes": {
                    "name": "C Major",
                },
            }
        }
        mock_client.get.return_value = mock_response

        key = await service_service.get_key("1")

        assert key.id == "1"
        assert key.name == "C Major"
        mock_client.get.assert_called_once_with("/services/v2/keys/1")

    async def test_get_teams(self, service_service, mock_client):
        """Test getting teams."""
        mock_response = {
            "data": [
                {
                    "id": "1",
                    "type": "Team",
                    "attributes": {
                        "name": "Worship Team",
                    },
                }
            ]
        }
        mock_client.get.return_value = mock_response

        teams = await service_service.get_teams()

        assert len(teams) == 1
        assert teams[0].id == "1"
        assert teams[0].name == "Worship Team"
        mock_client.get.assert_called_once_with("/services/v2/teams", params={})

    async def test_get_team(self, service_service, mock_client):
        """Test getting a specific team."""
        mock_response = {
            "data": {
                "id": "1",
                "type": "Team",
                "attributes": {
                    "name": "Worship Team",
                },
            }
        }
        mock_client.get.return_value = mock_response

        team = await service_service.get_team("1")

        assert team.id == "1"
        assert team.name == "Worship Team"
        mock_client.get.assert_called_once_with("/services/v2/teams/1")
