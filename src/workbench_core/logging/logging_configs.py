import atexit
import json
import logging
import os
import pathlib
from enum import StrEnum, auto
from logging.config import dictConfig
from logging.handlers import QueueHandler

from workbench_core.settings import DEFAULT_LOG_FILEPATH


class EnvState(StrEnum):
    """Enum for the environment state."""

    DEV = auto()
    TEST = auto()
    PROD = auto()


LOG_FILEPATH = os.environ.get("LOG_FILEPATH", DEFAULT_LOG_FILEPATH)
ENV_STATE = os.environ.get("ENV_STATE", "dev")

LOG_LEVEL_MAP: dict[EnvState, int] = {
    EnvState.DEV: logging.DEBUG,
    EnvState.TEST: logging.DEBUG,
    EnvState.PROD: logging.INFO,
}

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "detailed": {
            "class": "logging.Formatter",
            "format": "[%(levelname)-8s|%(module)s|L%(lineno)d] %(asctime)s: %(name)-15s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S%z",
        },
        "simple": {
            "class": "logging.Formatter",
            "format": "%(asctime)s %(levelname)-8s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S%z",
        },
        "json": {
            "()": "src.workbench_core.logging.formatters.json_formatter.JSONFormatter",
            "fmt_keys": {
                "level": "levelname",
                "message": "message",
                "timestamp": "timestamp",
                "logger": "logger",
                "module": "module",
                "function": "funcName",
                "line": "lineno",
                "thread_name": "threadName",
            },
        },
    },
    "handlers": {
        "streaming_handler": {
            "class": "rich.logging.RichHandler",
            "level": LOG_LEVEL_MAP[ENV_STATE],
            "formatter": "console_formatter",
            "omit_repeated_times": False,
            "show_level": True,
            "show_path": False,
            "enable_link_path": True,
            "rich_tracebacks": True,
        },
        "file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": LOG_LEVEL_MAP[ENV_STATE],
            "formatter": "detailed",
            "filename": LOG_FILEPATH,
            "maxBytes": 1024 * 1024 * 10,
            "backupCount": 3,
            "encoding": "utf8",
        },
    },
    "loggers": {
        "": {
            "handlers": ["streaming_handler", "file_handler"],
            "level": LOG_LEVEL_MAP[ENV_STATE],
            "propagate": False,
        },
        "__main__": {
            "handlers": ["streaming_handler", "file_handler"],
            "level": LOG_LEVEL_MAP[ENV_STATE],
            "propagate": False,
        },
    },
}


def get_handler_by_name(logger: logging.Logger, handler_name: str):
    for handler in logger.handlers:
        if handler.name == handler_name:
            return handler
    return None


def setup_logging(logger: logging.Logger):
    config_file = pathlib.Path(__file__).parent.joinpath("logging_config.json")

    with open(config_file, encoding="utf-8") as file:
        config = json.load(file)

    dictConfig(config)

    queue_handler: QueueHandler = get_handler_by_name(logger, "queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)
