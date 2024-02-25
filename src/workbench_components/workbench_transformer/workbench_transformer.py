"""Base class for transformers"""

from abc import ABC, abstractmethod

from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_components.workbench_logging.workbench_logger import WorkbenchLogger
from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings


class WorkbenchTransformer(ABC, WorkbenchLogger):
    """Base class for transformers"""

    def __init__(self) -> None:
        self.create_logger()

    @abstractmethod
    def transform(self, data: WorkbenchData, settings: WorkbenchSettings) -> bool:  # pylint: disable=unused-argument
        """Transform data and return True if successful, False otherwise."""

        return True
