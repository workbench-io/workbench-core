import json
import os

from workbench_components.workbench_config.workbench_config import WorkbenchSettings
from workbench_process.process_config_model import ProcessSettingsModel


class ProcessSettings(WorkbenchSettings):
    """Configuration for data extraction."""

    configs: ProcessSettingsModel

    def load_configs(self, filepath: os.PathLike) -> None:
        """Load configuration from a file."""

        with open(filepath, "r", encoding="utf-8") as file:
            config_dict = json.load(file)

        self.configs = ProcessSettingsModel(**config_dict)
