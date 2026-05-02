"""Base data model for Ember Bio."""

from pydantic import BaseModel


class BaseDataModel(BaseModel):
    """Base model for all Ember Bio data types.

    Provides consistent serialization and validation defaults.
    """

    model_config = {"from_attributes": True}
