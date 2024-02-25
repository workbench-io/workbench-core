"""Base class for logic."""

from abc import ABC, abstractmethod

from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_components.workbench_logging.workbench_logger import WorkbenchLogger
from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings


class WorkbenchLogic(ABC, WorkbenchLogger):
    """Base class for logic."""

    def __init__(self) -> None:
        self.create_logger()

    @abstractmethod
    def run(self, data: WorkbenchData, settings: WorkbenchSettings) -> bool:  # pylint: disable=unused-argument
        """
        Run logic with provided data and settings object.

        Return True if successful, False otherwise.
        """

        return True
