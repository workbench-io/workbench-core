import logging

from workbench_core.workbench_logging.filters.stderr_filter import StderrFilter


class TestStderrFilter:

    def test_filter_returns_true_when_levelno_is_greater_than_info(self):
        # Arrange
        filter_obj = StderrFilter()
        record = logging.LogRecord(
            name="test_logger",
            level=logging.WARNING,
            pathname="/path/to/file.py",
            lineno=10,
            msg="Test message",
            args=None,
            exc_info=None,
        )

        # Act
        result = filter_obj.filter(record)

        # Assert
        assert result is True

    def test_filter_returns_false_when_levelno_is_info_or_lower(self):
        # Arrange
        filter_obj = StderrFilter()
        record = logging.LogRecord(
            name="test_logger",
            level=logging.INFO,
            pathname="/path/to/file.py",
            lineno=10,
            msg="Test message",
            args=None,
            exc_info=None,
        )

        # Act
        result = filter_obj.filter(record)

        # Assert
        assert result is False
