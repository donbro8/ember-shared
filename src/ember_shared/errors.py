"""Error types for Ember Bio."""


class EmberError(Exception):
    """Base exception for all Ember Bio errors."""


class ConfigurationError(EmberError):
    """Raised when configuration is invalid or missing."""


class DataAccessError(EmberError):
    """Raised when a data source is unreachable or returns an error."""
