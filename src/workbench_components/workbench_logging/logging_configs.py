import json
import logging
import os
import pathlib
from enum import StrEnum, auto
from logging.config import dictConfig

from workbench_components.common.common_configs import ENCODING, FILEPATH_LOGS_DEFAULT


class EnvState(StrEnum):
    """Enum for the environment state."""

    DEV = auto()
    TEST = auto()
    PROD = auto()


LOG_FILEPATH = os.environ.get("LOG_FILEPATH", FILEPATH_LOGS_DEFAULT)

LOG_LEVEL_MAP: dict[EnvState, int] = {
    EnvState.DEV: logging.DEBUG,
    EnvState.TEST: logging.DEBUG,
    EnvState.PROD: logging.INFO,
}

LOG_MESSAGE_TEMPLATE = "{class_name}.{function_name}: {message}"


def setup_logging() -> None:
    """Set up the logging configuration."""

    config_file = pathlib.Path(__file__).parent.joinpath("logging_config.json")

    with open(config_file, encoding=ENCODING) as file:
        config = json.load(file)

    dictConfig(config)

    logging.getLogger().setLevel(LOG_LEVEL_MAP[os.environ.get("ENV_STATE", "dev")])
