from typing import Any, Optional, Protocol


class WorkbenchRepository(Protocol):
    """Repository class used to connect to data storage and perform CRUD operations."""

    def get(self, db_id: int) -> Optional[Any]:
        """
        Retrieves an item from the repository based on the given database ID.

        Args:
            db_id (int): The database ID of the item to retrieve.

        Returns:
            Optional[Any]: The retrieved item, or None if not found.
        """
        raise NotImplementedError

    def get_all(self) -> list[Any]:
        """
        Retrieves all items from the repository.

        Returns:
            list[Any]: A list of all items in the repository.
        """
        raise NotImplementedError

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

    def update(self, db_id: int, new_item: Any) -> None:
        """
        Updates an item in the repository based on the given database ID.

        Args:
            db_id (int): The database ID of the item to update.
            new_item (Any): The updated item.

        Returns:
            None
        """
        raise NotImplementedError

    def delete(self, db_id: int) -> None:
        """
        Deletes an item from the repository based on the given database ID.

        Args:
            db_id (int): The database ID of the item to delete.

        Returns:
            None
        """
        raise NotImplementedError
