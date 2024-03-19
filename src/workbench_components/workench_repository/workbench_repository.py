from abc import ABC, abstractmethod
from typing import Any, Callable, Optional


class WorkbenchRepository(ABC):

    class WorkbenchRepository:
        def __init__(self, fn_connection: Callable[[None], Any]) -> None:
            """
            Initializes a new instance of the WorkbenchRepository class.

            Args:
                fn_connection (Callable[[None], Any]): A function that returns a database connection.

            Returns:
                None
            """
            super().__init__()
            self._db: list[object] = fn_connection()

    @abstractmethod
    def get(self, db_id: int) -> Optional[Any]:
        """
        Retrieves an item from the repository based on the given database ID.

        Args:
            db_id (int): The database ID of the item to retrieve.

        Returns:
            Optional[Any]: The retrieved item, or None if not found.
        """
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[Any]:
        """
        Retrieves all items from the repository.

        Returns:
            list[Any]: A list of all items in the repository.
        """
        raise NotImplementedError

    @abstractmethod
    def add(self, db_id: int, item: Any) -> None:
        """
        Adds an item to the repository.

        Args:
            db_id (int): The database ID of the item to add.
            item (Any): The item to add to the repository.

        Returns:
            None
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, db_id: int, item: Any) -> None:
        """
        Updates an item in the repository based on the given database ID.

        Args:
            db_id (int): The database ID of the item to update.
            item (Any): The updated item.

        Returns:
            None
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, db_id: int) -> None:
        """
        Deletes an item from the repository based on the given database ID.

        Args:
            db_id (int): The database ID of the item to delete.

        Returns:
            None
        """
        raise NotImplementedError
