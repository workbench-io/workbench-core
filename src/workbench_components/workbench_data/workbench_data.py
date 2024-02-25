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
        """
        Retrieves the data with the given name.

        Args:
            name (str): The name of the data to retrieve.

        Returns:
            object: The retrieved data.

        Raises:
            WorkbenchDataException: If the data with the given name does not exist.
        """
        try:
            data = getattr(self, name)
            return data
        except AttributeError as error:
            self.log_error(self.get_data, f"No data with name of '{name}'")
            raise WorkbenchDataException(f"AttributeError: {error}") from error

    def has_data(self, name: str) -> bool:
        """
        Checks if the specified data attribute exists.

        Args:
            name (str): The name of the data attribute.

        Returns:
            bool: True if the data attribute exists, False otherwise.
        """
        try:
            getattr(self, name)
            return True
        except AttributeError:
            return False

    def set_data(self, name: str, data: object) -> None:
        """
        Sets the data with the given name.

        Args:
            name (str): The name of the data.
            data (object): The data to be set.

        Returns:
            None
        """
        setattr(self, name, data)
        self.log_info(self.set_data, f"Set data with name of '{name}'")
