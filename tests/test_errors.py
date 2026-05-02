"""Tests for ember_shared.errors."""

import pytest
from ember_shared.errors import ConfigurationError, DataAccessError, EmberError


class TestErrorHierarchy:
    """Verify exception class hierarchy."""

    def test_ember_error_is_exception(self):
        assert issubclass(EmberError, Exception)

    def test_configuration_error_is_ember_error(self):
        assert issubclass(ConfigurationError, EmberError)

    def test_data_access_error_is_ember_error(self):
        assert issubclass(DataAccessError, EmberError)

    def test_ember_error_message(self):
        err = EmberError("something went wrong")
        assert str(err) == "something went wrong"

    def test_configuration_error_catchable_as_ember_error(self):
        with pytest.raises(EmberError):
            raise ConfigurationError("bad config")

    def test_data_access_error_catchable_as_ember_error(self):
        with pytest.raises(EmberError):
            raise DataAccessError("db unreachable")
