import json
import logging
import os
import pathlib
from enum import StrEnum, auto
from logging.config import dictConfig

from workbench_components.workbench_settings import DEFAULT_LOG_FILEPATH


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

LOG_MESSAGE_TEMPLATE = "{class_name}.{function_name}: {message}"


def setup_logging() -> None:
    """Set up the logging configuration."""

    config_file = pathlib.Path(__file__).parent.joinpath("logging_config.json")

    with open(config_file, encoding="utf-8") as file:
        config = json.load(file)

    dictConfig(config)

    logging.getLogger().setLevel(LOG_LEVEL_MAP[ENV_STATE])
