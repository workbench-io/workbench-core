import json
import os

from workbench_components.workbench_config.workbench_config import WorkbenchConfig
from workbench_process.process_config_model import ProcessConfigModel


class ProcessConfig(WorkbenchConfig):
    """Configuration for data extraction."""

    configs: ProcessConfigModel

    def load_configs(self, filepath: os.PathLike) -> None:
        """Load configuration from a file."""

        with open(filepath, "r", encoding="utf-8") as file:
            config_dict = json.load(file)

        self.configs = ProcessConfigModel(**config_dict)
