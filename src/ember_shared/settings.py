from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal


class Settings(BaseSettings):
    """
    Global application settings.
    Loads from environment variables.
    """

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    # Environment
    ENV: Literal["dev", "staging", "prod"] = "dev"
    DEBUG: bool = False

    # GCP
    GCP_PROJECT_ID: str = "ember-bio-dev"
    GCP_REGION: str = "us-central1"

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_JSON_FORMAT: bool = False


settings = Settings()
