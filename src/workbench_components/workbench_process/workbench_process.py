"""Base class for processes."""

from abc import ABC, abstractmethod

from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_components.workbench_logging.workbench_logger import WorkbenchLogger
from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings


class WorkbenchProcess(ABC, WorkbenchLogger):
    """Base class for processes."""

    def __init__(self) -> None:
        self.create_logger()

    @abstractmethod
    def run(self, data: WorkbenchData, config: WorkbenchSettings) -> bool:  # pylint: disable=unused-argument
        """
        Run process with provided data and configuration object.

        Return True if successful, False otherwise.
        """

        return True
