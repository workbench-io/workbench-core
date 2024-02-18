"""Base class for transformers"""

from abc import ABC, abstractmethod

from workbench_core.workbench_logging.workbench_logger import WorkbenchLogger


class WorkbenchTransformer(ABC, WorkbenchLogger):
    """Base class for transformers"""

    def __init__(self) -> None:
        self.create_logger()

    @abstractmethod
    def transform(self, data) -> bool:  # pylint: disable=unused-argument
        """Transform data and return True if successful, False otherwise."""

        return True
