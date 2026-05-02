"""Tests for ember_shared.logging."""

import json
import logging
import sys

from ember_shared.logging import JsonFormatter, setup_logging


class TestJsonFormatter:
    """Verify JsonFormatter produces valid JSON with expected fields."""

    def test_format_produces_valid_json(self):
        formatter = JsonFormatter()
        record = logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname="test.py",
            lineno=1,
            msg="hello world",
            args=(),
            exc_info=None,
        )
        output = formatter.format(record)
        parsed = json.loads(output)
        assert parsed["message"] == "hello world"
        assert parsed["severity"] == "INFO"
        assert parsed["logger"] == "test"

    def test_format_includes_exception(self):
        formatter = JsonFormatter()
        try:
            raise ValueError("test error")
        except ValueError:
            exc_info = sys.exc_info()

        record = logging.LogRecord(
            name="test",
            level=logging.ERROR,
            pathname="test.py",
            lineno=1,
            msg="error occurred",
            args=(),
            exc_info=exc_info,
        )
        output = formatter.format(record)
        parsed = json.loads(output)
        assert "exception" in parsed
        assert "ValueError" in parsed["exception"]


class TestSetupLogging:
    """Verify setup_logging configures root logger correctly."""

    def setup_method(self):
        """Reset root logger before each test."""
        root = logging.getLogger()
        root.handlers.clear()
        root.setLevel(logging.WARNING)

    def test_flat_format(self):
        setup_logging(level="DEBUG", json_format=False)
        root = logging.getLogger()
        assert root.level == logging.DEBUG
        assert len(root.handlers) == 1
        assert not isinstance(root.handlers[0].formatter, JsonFormatter)

    def test_json_format(self):
        setup_logging(level="INFO", json_format=True)
        root = logging.getLogger()
        assert root.level == logging.INFO
        assert len(root.handlers) == 1
        assert isinstance(root.handlers[0].formatter, JsonFormatter)

    def test_no_duplicate_handlers(self):
        setup_logging(level="INFO")
        setup_logging(level="DEBUG")
        root = logging.getLogger()
        assert len(root.handlers) == 1
