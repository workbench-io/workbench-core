import os
from typing import Union

from workbench_core.workbench_source.workbench_source import WorkbenchSource
from workbench_process.process_config import ProcessConfig
from workbench_process.process_data import ProcessData


class SourceCompressiveStrength(WorkbenchSource):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def load(
        self,
        source: Union[str, os.PathLike],
        data: ProcessData,
        config: ProcessConfig,
    ):  # pylint: disable=unused-argument
        self.log_info(self.load, f"Loading data from {source}")
        return True
