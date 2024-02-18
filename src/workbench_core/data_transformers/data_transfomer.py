"""Base class for data transformers"""

from abc import ABC, abstractmethod

from workbench_core.logging.workbench_logger import WorkbenchLogger


class DataTransformer(ABC, WorkbenchLogger):
    """Base class for data transformers"""

    def __init__(self) -> None:
        self.create_logger()

    @abstractmethod
    def transform(self, data) -> bool:  # pylint: disable=unused-argument
        """Transform data and return True if successful, False otherwise."""

        return True
