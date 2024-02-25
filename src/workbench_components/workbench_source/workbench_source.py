"""Base class for data objects."""

import os
from abc import ABC, abstractmethod
from typing import Union

from workbench_components.workbench_config.workbench_config import WorkbenchConfig
from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_components.workbench_logging.workbench_logger import WorkbenchLogger


class WorkbenchSource(ABC, WorkbenchLogger):
    """Base class for data source objects."""

    def __init__(self) -> None:
        self.create_logger()

    @abstractmethod
    def load(
        self,
        source: Union[str, os.PathLike],
        data: WorkbenchData,
        config: WorkbenchConfig,
    ) -> bool:
        """Load data from source and return True if successful, False otherwise."""
        return True
