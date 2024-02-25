"""Base class for data objects."""

from abc import ABC

from workbench_components.workbench_logging.workbench_logger import WorkbenchLogger


class WorkbenchDataException(Exception):
    """Base class for WorkbenchDataException exceptions."""


class WorkbenchData(ABC, WorkbenchLogger):
    """Base class for data objects."""

    def __init__(self) -> None:
        self.create_logger()

    def get_data(self, name: str) -> object:
        try:
            data = getattr(self, name)
            return data
        except AttributeError as error:
            self.log_error(self.get_data, f"No data with name of '{name}'")
            raise WorkbenchDataException(f"AttributeError: {error}") from error
