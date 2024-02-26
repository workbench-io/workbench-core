import json
import os

from workbench_components.common.common_configs import ENCODING
from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings
from workbench_process.process_settings_model import ProcessSettingsModel


class ProcessSettings(WorkbenchSettings):
    """Settings for data processing step."""

    model: ProcessSettingsModel

    def load_settings_from_file(self, filepath: os.PathLike) -> None:
        """Load settings from a file."""

        with open(filepath, "r", encoding=ENCODING) as file:
            config_dict = json.load(file)

        self.model = ProcessSettingsModel(**config_dict)
