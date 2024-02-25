import json
import os

from workbench_components.common.common_configs import ENCODING
from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings
from workbench_process.process_config_model import ProcessSettingsModel


class ProcessSettings(WorkbenchSettings):
    """Configuration for data extraction."""

    configs: ProcessSettingsModel

    def load_configs(self, filepath: os.PathLike) -> None:
        """Load configuration from a file."""

        with open(filepath, "r", encoding=ENCODING) as file:
            config_dict = json.load(file)

        self.configs = ProcessSettingsModel(**config_dict)
