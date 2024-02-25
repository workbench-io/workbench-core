"""Base class for data objects."""

from abc import ABC, abstractmethod

from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_components.workbench_logging.workbench_logger import WorkbenchLogger
from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings


class WorkbenchSource(ABC, WorkbenchLogger):
    """Base class for data source objects."""

    def __init__(self) -> None:
        self.create_logger()

    @abstractmethod
    def load(self, data: WorkbenchData, settings: WorkbenchSettings) -> bool:
        """Load data from source and return True if successful, False otherwise."""
        return True
