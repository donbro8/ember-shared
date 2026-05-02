"""Tests for ember_shared.settings."""

import pytest
from ember_shared.settings import Settings


class TestSettingsDefaults:
    """Verify default values without any env vars set."""

    def test_default_env(self):
        s = Settings()
        assert s.ENV == "dev"

    def test_default_debug(self):
        s = Settings()
        assert s.DEBUG is False

    def test_default_gcp_project_id(self):
        s = Settings()
        assert s.GCP_PROJECT_ID == "ember-bio-dev"

    def test_default_gcp_region(self):
        s = Settings()
        assert s.GCP_REGION == "us-central1"

    def test_default_log_level(self):
        s = Settings()
        assert s.LOG_LEVEL == "INFO"

    def test_default_log_json_format(self):
        s = Settings()
        assert s.LOG_JSON_FORMAT is False


class TestSettingsEnvOverride:
    """Verify env var overrides via monkeypatch."""

    def test_env_override(self, monkeypatch):
        monkeypatch.setenv("ENV", "prod")
        s = Settings()
        assert s.ENV == "prod"

    def test_debug_override(self, monkeypatch):
        monkeypatch.setenv("DEBUG", "true")
        s = Settings()
        assert s.DEBUG is True

    def test_gcp_project_id_override(self, monkeypatch):
        monkeypatch.setenv("GCP_PROJECT_ID", "ember-bio-prod")
        s = Settings()
        assert s.GCP_PROJECT_ID == "ember-bio-prod"

    def test_gcp_region_override(self, monkeypatch):
        monkeypatch.setenv("GCP_REGION", "europe-west1")
        s = Settings()
        assert s.GCP_REGION == "europe-west1"

    def test_log_level_override(self, monkeypatch):
        monkeypatch.setenv("LOG_LEVEL", "DEBUG")
        s = Settings()
        assert s.LOG_LEVEL == "DEBUG"

    def test_log_json_format_override(self, monkeypatch):
        monkeypatch.setenv("LOG_JSON_FORMAT", "true")
        s = Settings()
        assert s.LOG_JSON_FORMAT is True

    def test_env_validation_rejects_invalid(self, monkeypatch):
        monkeypatch.setenv("ENV", "invalid")
        with pytest.raises(Exception):
            Settings()
