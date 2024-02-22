"""Base Factory class for workbench objects."""

from typing import TypeVar

from workbench_components.workbench_logging.workbench_logger import WorkbenchLogger

WorkbenchObject = TypeVar("WorkbenchObject")


class WorkbenchFactoryError(Exception):
    """Base class for WorkbenchFactory exceptions."""


class WorkbenchFactory(WorkbenchLogger):
    """Base Factory class for workbench objects."""

    _items: dict[str, WorkbenchObject] | None = None

    def __init__(self) -> None:
        self.create_logger()
        self.log_info(method=self.__init__, message="Factory created.")

        if self._items is None:
            self._items = {}

    def register(self, name: str, item: WorkbenchObject) -> None:
        """Register an item with the factory.

        Args:
            name (str): The name of the item.
            item (WorkbenchObject): The item to be registered.
        """
        self.log_info(method=self.register, message=f"Registering {name}.")
        self._items[name] = item

    def create(self, name: str) -> WorkbenchObject:
        """Create an item from the factory.

        Args:
            name (str): The name of the item to be created.

        Returns:
            WorkbenchObject: The created item.
        """
        self.log_info(method=self.create, message=f"Creating {name}.")

        return self._items[name]

    def create_instance(self, name: str) -> WorkbenchObject:
        """Create an instance of an item from the factory.

        Args:
            name (str): The name of the item to be created.

        Returns:
            WorkbenchObject: The created item.
        """
        self.log_info(method=self.create_instance, message=f"Creating instance of {name}.")

        if self.contains(name=name):
            return self._items[name]()

        raise WorkbenchFactoryError(f"Item {name} not found in factory.")

    def contains(self, name: str) -> bool:
        """Check if the factory contains an item.

        Args:
            name (str): The name of the item to be checked.

        Returns:
            bool: True if the item is in the factory, False otherwise.
        """
        return name in self._items

    def list_items(self) -> list[str]:
        """List all items in the factory.

        Returns:
            list[str]: A list of all items in the factory.
        """
        return list(self._items.keys())

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(items={self._items})"

    def __repr__(self) -> str:
        return self.__str__()
