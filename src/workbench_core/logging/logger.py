"""Logger for the workbench project."""

import json
import logging
import os
from logging.config import dictConfig

from workbench_core.settings import ENCODING


class Logger:
    """Logger for the workbench project."""

    def __init__(self, name: str) -> None:
        self._logger: logging.Logger = logging.getLogger(name)

    def load_config(self, config: dict) -> None:
        """Load the logging configuration."""
        dictConfig(config)

    def load_config_from_file(self, filepath: os.PathLike) -> None:
        """Load the logging configuration from a file."""
        with open(filepath, "r", encoding=ENCODING) as file:
            logging_config = json.load(file)

        dictConfig(logging_config)
