"""Tests for ember_shared.models."""

import pytest
from pydantic import ValidationError

from ember_shared.models import BaseDataModel


class TestBaseDataModel:
    """Verify BaseDataModel works as a Pydantic BaseModel subclass."""

    def test_instantiation_with_fields(self):
        class SampleModel(BaseDataModel):
            name: str
            value: int

        m = SampleModel(name="test", value=42)
        assert m.name == "test"
        assert m.value == 42

    def test_serialization(self):
        class SampleModel(BaseDataModel):
            name: str

        m = SampleModel(name="hello")
        data = m.model_dump()
        assert data == {"name": "hello"}

    def test_json_round_trip(self):
        class SampleModel(BaseDataModel):
            name: str
            count: int

        m = SampleModel(name="test", count=5)
        json_str = m.model_dump_json()
        m2 = SampleModel.model_validate_json(json_str)
        assert m == m2

    def test_validation_error(self):
        class SampleModel(BaseDataModel):
            value: int

        with pytest.raises(ValidationError):
            SampleModel(value="not_an_int")
