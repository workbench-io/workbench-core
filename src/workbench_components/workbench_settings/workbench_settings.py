"""Base class for settings objects."""

import json
import os
from abc import ABC
from typing import Any

from pydantic import BaseModel

from workbench_components.workbench_configs import workbench_configs
from workbench_components.workbench_logging.workbench_logger import WorkbenchLogger


class WorkbenchSettings(ABC, WorkbenchLogger):
    """Base class for settings objects."""

    _settings_model: BaseModel

    def __init__(self) -> None:
        self.create_logger()
        self.model = None

    def load_settings_from_file(self, filepath: os.PathLike) -> None:
        """Load settings from a file."""

        self.log_info(self.load_settings_from_file, f"Loading settings from {filepath.absolute()}")

        with open(filepath, "r", encoding=workbench_configs.encoding) as file:
            settings_dict = json.load(file)

        self.model = self._settings_model(**settings_dict)

    def load_settings_from_dict(self, settings_dict: dict[str, Any]) -> None:
        """Load settings from a dictionary."""

        self.log_info(self.load_settings_from_file, f"Loading settings from dictionary: {settings_dict}")
        self.model = self._settings_model(**settings_dict)

    def load_settings_from_model(self, settings_model: BaseModel) -> None:
        """Load settings from a dictionary."""

        self.log_info(self.load_settings_from_file, f"Loading settings from model: {settings_model}")
        self.model = settings_model
