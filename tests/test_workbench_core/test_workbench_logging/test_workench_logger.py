from workbench_core.workbench_logging.workbench_logger import WorkbenchLogger

# setup_logging()


class TestWorkbenchLogger:

    def test_create_logger(self):
        logger = WorkbenchLogger()
        logger.create_logger()

        assert logger._logger is not None  # pylint: disable=protected-access

    def test_create_log_message(self):
        logger = WorkbenchLogger()
        logger.create_logger()
        message = "This is a test message"
        log_message = logger.create_log_message(method=logger.create_log_message, message=message)

        assert log_message == f"WorkbenchLogger.WorkbenchLogger.create_log_message: {message}"
