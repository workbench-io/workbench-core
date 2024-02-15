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
