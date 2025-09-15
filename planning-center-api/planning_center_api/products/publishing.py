"""Publishing API models for Planning Center Online."""

from typing import Any

from ..models.base import PCOResource


class PCOChannel(PCOResource):
    """Represents a channel in Planning Center Publishing."""

    def get_art(self) -> dict[str, Any] | None:
        """Get the channel art."""
        return self.get_attribute("art")

    def get_podcast_art(self) -> dict[str, Any] | None:
        """Get the podcast art."""
        return self.get_attribute("podcast_art")

    def get_podcast_settings(self) -> dict[str, Any] | None:
        """Get the podcast settings."""
        return self.get_attribute("podcast_settings")

    def get_activate_episode_minutes_before(self) -> int | None:
        """Get the activation time for an episode, expressed in minutes before its start."""
        return self.get_attribute("activate_episode_minutes_before")

    def get_can_enable_chat(self) -> bool | None:
        """Get whether chat can be enabled."""
        return self.get_attribute("can_enable_chat")

    def get_church_center_url(self) -> str | None:
        """Get the church center URL."""
        return self.get_attribute("church_center_url")

    def get_created_at(self) -> str | None:
        """Get the creation timestamp."""
        return self.get_attribute("created_at")

    def get_default_video_embed_code(self) -> str | None:
        """Get the default video embed code."""
        return self.get_attribute("default_video_embed_code")

    def get_description(self) -> str | None:
        """Get the channel description."""
        return self.get_attribute("description")

    def get_url(self) -> str | None:
        """Get the channel URL."""
        return self.get_attribute("url")

    def get_default_video_duration(self) -> int | None:
        """Get the default video duration."""
        return self.get_attribute("default_video_duration")

    def get_default_video_url(self) -> str | None:
        """Get the default video URL."""
        return self.get_attribute("default_video_url")

    def get_enable_audio(self) -> bool | None:
        """Get whether audio is enabled."""
        return self.get_attribute("enable_audio")

    def get_enable_on_demand_video(self) -> bool | None:
        """Get whether on-demand video is enabled."""
        return self.get_attribute("enable_on_demand_video")

    def get_enable_watch_live(self) -> bool | None:
        """Get whether watch live is enabled."""
        return self.get_attribute("enable_watch_live")

    def get_general_chat_enabled(self) -> bool | None:
        """Get whether general chat is enabled."""
        return self.get_attribute("general_chat_enabled")

    def get_group_chat_enabled(self) -> bool | None:
        """Get whether group chat is enabled."""
        return self.get_attribute("group_chat_enabled")

    def get_name(self) -> str | None:
        """Get the channel name."""
        return self.get_attribute("name")

    def get_podcast_feed_url(self) -> str | None:
        """Get the podcast feed URL."""
        return self.get_attribute("podcast_feed_url")

    def get_position(self) -> int | None:
        """Get the channel position."""
        return self.get_attribute("position")

    def get_published(self) -> bool | None:
        """Get whether the channel is published."""
        return self.get_attribute("published")

    def get_sermon_notes_enabled(self) -> bool | None:
        """Get whether sermon notes are enabled."""
        return self.get_attribute("sermon_notes_enabled")

    def get_services_service_type_remote_identifier(self) -> str | None:
        """Get the id for the associated Services Service Type."""
        return self.get_attribute("services_service_type_remote_identifier")

    def get_updated_at(self) -> str | None:
        """Get the last update timestamp."""
        return self.get_attribute("updated_at")

    def get_channel_default_episode_resources(self) -> list[dict[str, Any]] | None:
        """Get associated channel default episode resources."""
        return self.get_relationship("channel_default_episode_resources")

    def get_channel_default_times(self) -> list[dict[str, Any]] | None:
        """Get associated channel default times."""
        return self.get_relationship("channel_default_times")

    def get_current_episode(self) -> dict[str, Any] | None:
        """Get the current episode."""
        return self.get_relationship("current_episode")

    def get_episodes(self) -> list[dict[str, Any]] | None:
        """Get associated episodes."""
        return self.get_relationship("episodes")

    def get_next_times(self) -> list[dict[str, Any]] | None:
        """Get associated next times."""
        return self.get_relationship("next_times")

    def get_series(self) -> list[dict[str, Any]] | None:
        """Get associated series."""
        return self.get_relationship("series")

    def get_statistics(self) -> list[dict[str, Any]] | None:
        """Get associated statistics."""
        return self.get_relationship("statistics")


class PCOChannelDefaultEpisodeResource(PCOResource):
    """Represents a channel default episode resource in Planning Center Publishing."""

    def get_featured(self) -> bool | None:
        """Get whether the resource is featured."""
        return self.get_attribute("featured")

    def get_icon(self) -> str | None:
        """Get the resource icon."""
        return self.get_attribute("icon")

    def get_kind(self) -> str | None:
        """Get the resource kind."""
        return self.get_attribute("kind")

    def get_position(self) -> int | None:
        """Get the resource position."""
        return self.get_attribute("position")

    def get_title(self) -> str | None:
        """Get the resource title."""
        return self.get_attribute("title")

    def get_type(self) -> str | None:
        """Get the resource type."""
        return self.get_attribute("type")

    def get_url(self) -> str | None:
        """Get the resource URL."""
        return self.get_attribute("url")

    def get_channel(self) -> dict[str, Any] | None:
        """Get the associated channel."""
        return self.get_relationship("channel")


class PCOChannelDefaultTime(PCOResource):
    """Represents a channel default time in Planning Center Publishing."""

    def get_day_of_week(self) -> int | None:
        """Get the day of the week. 0 is Sunday, 1 is Monday, etc."""
        return self.get_attribute("day_of_week")

    def get_hour(self) -> int | None:
        """Get the hour."""
        return self.get_attribute("hour")

    def get_minute(self) -> int | None:
        """Get the minute."""
        return self.get_attribute("minute")

    def get_frequency(self) -> str | None:
        """Get the frequency."""
        return self.get_attribute("frequency")

    def get_position(self) -> int | None:
        """Get the position."""
        return self.get_attribute("position")

    def get_channel(self) -> dict[str, Any] | None:
        """Get the associated channel."""
        return self.get_relationship("channel")


class PCOChannelNextTime(PCOResource):
    """Represents a channel next time in Planning Center Publishing."""

    def get_starts_at(self) -> str | None:
        """Get the start time."""
        return self.get_attribute("starts_at")

    def get_channel(self) -> dict[str, Any] | None:
        """Get the associated channel."""
        return self.get_relationship("channel")


class PCOEpisode(PCOResource):
    """Represents an episode in Planning Center Publishing."""

    def get_art(self) -> dict[str, Any] | None:
        """Get the episode art."""
        return self.get_attribute("art")

    def get_church_center_url(self) -> str | None:
        """Get the church center URL."""
        return self.get_attribute("church_center_url")

    def get_created_at(self) -> str | None:
        """Get the creation timestamp."""
        return self.get_attribute("created_at")

    def get_description(self) -> str | None:
        """Get the episode description."""
        return self.get_attribute("description")

    def get_library_audio_url(self) -> str | None:
        """Get the library audio URL."""
        return self.get_attribute("library_audio_url")

    def get_library_streaming_service(self) -> str | None:
        """Get the library streaming service."""
        return self.get_attribute("library_streaming_service")

    def get_library_video_embed_code(self) -> str | None:
        """Get the library video embed code."""
        return self.get_attribute("library_video_embed_code")

    def get_library_video_thumbnail_url(self) -> str | None:
        """Get the library video thumbnail URL."""
        return self.get_attribute("library_video_thumbnail_url")

    def get_library_video_url(self) -> str | None:
        """Get the library video URL."""
        return self.get_attribute("library_video_url")

    def get_needs_library_audio_or_video_url(self) -> bool | None:
        """Get whether library audio or video URL is needed."""
        return self.get_attribute("needs_library_audio_or_video_url")

    def get_needs_notes_template(self) -> bool | None:
        """Get whether notes template is needed."""
        return self.get_attribute("needs_notes_template")

    def get_needs_video_url(self) -> bool | None:
        """Get whether video URL is needed."""
        return self.get_attribute("needs_video_url")

    def get_page_actions(self) -> list[dict[str, Any]] | None:
        """Get the page actions."""
        return self.get_attribute("page_actions")

    def get_published_live_at(self) -> str | None:
        """Get the published live timestamp."""
        return self.get_attribute("published_live_at")

    def get_published_to_library_at(self) -> str | None:
        """Get the published to library timestamp."""
        return self.get_attribute("published_to_library_at")

    def get_sermon_audio(self) -> dict[str, Any] | None:
        """Get the sermon audio."""
        return self.get_attribute("sermon_audio")

    def get_stream_type(self) -> str | None:
        """Get the stream type."""
        return self.get_attribute("stream_type")

    def get_streaming_service(self) -> str | None:
        """Get the streaming service."""
        return self.get_attribute("streaming_service")

    def get_title(self) -> str | None:
        """Get the episode title."""
        return self.get_attribute("title")

    def get_updated_at(self) -> str | None:
        """Get the last update timestamp."""
        return self.get_attribute("updated_at")

    def get_video_thumbnail_url(self) -> str | None:
        """Get the video thumbnail URL."""
        return self.get_attribute("video_thumbnail_url")

    def get_video_embed_code(self) -> str | None:
        """Get the video embed code."""
        return self.get_attribute("video_embed_code")

    def get_video_url(self) -> str | None:
        """Get the video URL."""
        return self.get_attribute("video_url")

    def get_services_plan_remote_identifier(self) -> str | None:
        """Get the id for the associated Services Plan."""
        return self.get_attribute("services_plan_remote_identifier")

    def get_services_service_type_remote_identifier(self) -> str | None:
        """Get the id for the associated Services Service Type."""
        return self.get_attribute("services_service_type_remote_identifier")

    def get_series(self) -> dict[str, Any] | None:
        """Get the associated series."""
        return self.get_relationship("series")

    def get_channel(self) -> dict[str, Any] | None:
        """Get the associated channel."""
        return self.get_relationship("channel")

    def get_episode_resources(self) -> list[dict[str, Any]] | None:
        """Get associated episode resources."""
        return self.get_relationship("episode_resources")

    def get_episode_times(self) -> list[dict[str, Any]] | None:
        """Get associated episode times."""
        return self.get_relationship("episode_times")

    def get_note_template(self) -> dict[str, Any] | None:
        """Get the associated note template."""
        return self.get_relationship("note_template")

    def get_speakerships(self) -> list[dict[str, Any]] | None:
        """Get associated speakerships."""
        return self.get_relationship("speakerships")


class PCOEpisodeResource(PCOResource):
    """Represents an episode resource in Planning Center Publishing."""

    def get_featured(self) -> bool | None:
        """Get whether the resource is featured."""
        return self.get_attribute("featured")

    def get_icon(self) -> str | None:
        """Get the resource icon."""
        return self.get_attribute("icon")

    def get_kind(self) -> str | None:
        """Get the resource kind."""
        return self.get_attribute("kind")

    def get_position(self) -> int | None:
        """Get the resource position."""
        return self.get_attribute("position")

    def get_title(self) -> str | None:
        """Get the resource title."""
        return self.get_attribute("title")

    def get_type(self) -> str | None:
        """Get the resource type."""
        return self.get_attribute("type")

    def get_url(self) -> str | None:
        """Get the resource URL."""
        return self.get_attribute("url")

    def get_episode(self) -> dict[str, Any] | None:
        """Get the associated episode."""
        return self.get_relationship("episode")


class PCOEpisodeStatistics(PCOResource):
    """Represents episode statistics in Planning Center Publishing."""

    def get_times(self) -> list[dict[str, Any]] | None:
        """Get watch count per EpisodeTime."""
        return self.get_attribute("times")

    def get_library_watch_count(self) -> bool | None:
        """Get the library watch count."""
        return self.get_attribute("library_watch_count")

    def get_live_watch_count(self) -> bool | None:
        """Get the live watch count."""
        return self.get_attribute("live_watch_count")

    def get_published_to_library_at(self) -> str | None:
        """Get the published to library timestamp."""
        return self.get_attribute("published_to_library_at")

    def get_published_live_at(self) -> str | None:
        """Get the published live timestamp."""
        return self.get_attribute("published_live_at")

    def get_title(self) -> str | None:
        """Get the episode title."""
        return self.get_attribute("title")

    def get_channel(self) -> dict[str, Any] | None:
        """Get the associated channel."""
        return self.get_relationship("channel")


class PCOEpisodeTime(PCOResource):
    """Represents an episode time in Planning Center Publishing."""

    def get_starts_at(self) -> str | None:
        """Get the start time."""
        return self.get_attribute("starts_at")

    def get_ends_at(self) -> str | None:
        """Get the end time."""
        return self.get_attribute("ends_at")

    def get_video_url(self) -> str | None:
        """Get the video URL."""
        return self.get_attribute("video_url")

    def get_video_embed_code(self) -> str | None:
        """Get the video embed code."""
        return self.get_attribute("video_embed_code")

    def get_current_timestamp(self) -> float | None:
        """Get the current timestamp."""
        return self.get_attribute("current_timestamp")

    def get_current_state(self) -> str | None:
        """Get the current state."""
        return self.get_attribute("current_state")

    def get_streaming_service(self) -> str | None:
        """Get the streaming service."""
        return self.get_attribute("streaming_service")

    def get_caveats(self) -> list[dict[str, Any]] | None:
        """Get the caveats."""
        return self.get_attribute("caveats")

    def get_episode(self) -> dict[str, Any] | None:
        """Get the associated episode."""
        return self.get_relationship("episode")


class PCONoteTemplate(PCOResource):
    """Represents a note template in Planning Center Publishing."""

    def get_enabled(self) -> bool | None:
        """Get whether the template is enabled."""
        return self.get_attribute("enabled")

    def get_template(self) -> str | None:
        """Get the template content."""
        return self.get_attribute("template")

    def get_auto_create_free_form_notes(self) -> bool | None:
        """Get whether to auto-create free form notes."""
        return self.get_attribute("auto_create_free_form_notes")

    def get_published_at(self) -> str | None:
        """Get the published timestamp."""
        return self.get_attribute("published_at")

    def get_episode(self) -> dict[str, Any] | None:
        """Get the associated episode."""
        return self.get_relationship("episode")


class PCOPublishingOrganization(PCOResource):
    """Represents an organization in Planning Center Publishing."""

    def get_name(self) -> str | None:
        """Get the organization name."""
        return self.get_attribute("name")

    def get_subdomain(self) -> str | None:
        """Get the organization subdomain."""
        return self.get_attribute("subdomain")

    def get_downloads_used(self) -> int | None:
        """Get the downloads used."""
        return self.get_attribute("downloads_used")

    def get_channels(self) -> list[dict[str, Any]] | None:
        """Get associated channels."""
        return self.get_relationship("channels")

    def get_episodes(self) -> list[dict[str, Any]] | None:
        """Get associated episodes."""
        return self.get_relationship("episodes")

    def get_series(self) -> list[dict[str, Any]] | None:
        """Get associated series."""
        return self.get_relationship("series")

    def get_speakers(self) -> list[dict[str, Any]] | None:
        """Get associated speakers."""
        return self.get_relationship("speakers")


class PCOSeries(PCOResource):
    """Represents a series in Planning Center Publishing."""

    def get_art(self) -> dict[str, Any] | None:
        """Get the series art."""
        return self.get_attribute("art")

    def get_church_center_url(self) -> str | None:
        """Get the church center URL."""
        return self.get_attribute("church_center_url")

    def get_description(self) -> str | None:
        """Get the series description."""
        return self.get_attribute("description")

    def get_ended_at(self) -> str | None:
        """Get the ended timestamp."""
        return self.get_attribute("ended_at")

    def get_episodes_count(self) -> int | None:
        """Get the episodes count."""
        return self.get_attribute("episodes_count")

    def get_published(self) -> bool | None:
        """Get whether the series is published."""
        return self.get_attribute("published")

    def get_started_at(self) -> str | None:
        """Get the started timestamp."""
        return self.get_attribute("started_at")

    def get_title(self) -> str | None:
        """Get the series title."""
        return self.get_attribute("title")

    def get_created_at(self) -> str | None:
        """Get the creation timestamp."""
        return self.get_attribute("created_at")

    def get_updated_at(self) -> str | None:
        """Get the last update timestamp."""
        return self.get_attribute("updated_at")

    def get_channel(self) -> dict[str, Any] | None:
        """Get the associated channel."""
        return self.get_relationship("channel")

    def get_organization(self) -> dict[str, Any] | None:
        """Get the associated organization."""
        return self.get_relationship("organization")


class PCOSpeaker(PCOResource):
    """Represents a speaker in Planning Center Publishing."""

    def get_avatar_url(self) -> str | None:
        """Get the avatar URL."""
        return self.get_attribute("avatar_url")

    def get_episodes_count(self) -> int | None:
        """Get the episodes count."""
        return self.get_attribute("episodes_count")

    def get_first_name(self) -> str | None:
        """Get the first name."""
        return self.get_attribute("first_name")

    def get_formatted_name(self) -> str | None:
        """Get the formatted name."""
        return self.get_attribute("formatted_name")

    def get_last_name(self) -> str | None:
        """Get the last name."""
        return self.get_attribute("last_name")

    def get_name_prefix(self) -> str | None:
        """Get the name prefix."""
        return self.get_attribute("name_prefix")

    def get_name_suffix(self) -> str | None:
        """Get the name suffix."""
        return self.get_attribute("name_suffix")

    def get_speaker_type(self) -> str | None:
        """Get the speaker type."""
        return self.get_attribute("speaker_type")

    def get_organization(self) -> dict[str, Any] | None:
        """Get the associated organization."""
        return self.get_relationship("organization")

    def get_speakerships(self) -> list[dict[str, Any]] | None:
        """Get associated speakerships."""
        return self.get_relationship("speakerships")


class PCOSpeakership(PCOResource):
    """Represents a speakership in Planning Center Publishing."""

    def get_speaker(self) -> dict[str, Any] | None:
        """Get the associated speaker."""
        return self.get_relationship("speaker")

    def get_episode(self) -> dict[str, Any] | None:
        """Get the associated episode."""
        return self.get_relationship("episode")
