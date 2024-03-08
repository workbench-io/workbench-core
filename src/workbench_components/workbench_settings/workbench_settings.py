"""Base class for settings objects."""

import json
import os
from abc import ABC

from pydantic import BaseModel

from workbench_components.common.common_configs import ENCODING
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

        with open(filepath, "r", encoding=ENCODING) as file:
            config_dict = json.load(file)

        self.model = self._settings_model(**config_dict)
