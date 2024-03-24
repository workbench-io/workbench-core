from typing import Any, Callable

from pydantic import BaseModel

from workbench_components.workench_repository.workbench_repository import WorkbenchRepository
from workbench_db.models import Optimization, Prediction
from workbench_utils.misc import create_list


class ListRepositoryError(Exception):
    """ListRepository error."""


# pylint: disable=keyword-arg-before-vararg
class ListRepository(WorkbenchRepository):

    def __init__(self, fn_connection: Callable[[None], Any] = create_list, *args, **kwargs) -> None:
        super().__init__()
        self._db: list[BaseModel] = fn_connection(*args, **kwargs)

    def get(self, db_id: int) -> BaseModel:
        result = [entry for entry in self._db if int(entry.id) == int(db_id)]

        if result:
            return result[0]
        return None

    def get_latest(self) -> BaseModel:
        try:
            return self._db[-1]
        except IndexError:
            return None

    def get_all(self) -> list[BaseModel]:
        return self._db

    def add(self, db_id: int, item: BaseModel) -> BaseModel:  # pylint: disable=unused-argument
        self._db.append(item)
        return item

    def update(self, db_id: int, new_item: BaseModel) -> BaseModel:
        index = self.get_index_of_db_entry_by_id(db_id)

        old_item = self._db[index]
        updated_item = old_item.model_copy(update=new_item.model_dump(exclude_unset=True, exclude_none=True))

        self._db[index] = updated_item

        return updated_item

    def delete(self, db_id: int) -> None:
        index = self.get_index_of_db_entry_by_id(db_id)
        self._db.pop(index)

    def get_index_of_db_entry_by_id(self, db_id: int) -> int | None:
        """
        Returns the index of the database entry with the given ID.

        Args:
            db_id (int): The ID of the database entry to search for.

        Returns:
            int | None: The index of the database entry if found, None otherwise.
        """
        for index, entry in enumerate(self._db):
            if entry.id == db_id:
                return index

        raise ListRepositoryError(f"Item with ID {db_id} not found")

    def get_next_id(self) -> int:
        """
        Returns the next available ID for the database.

        Returns:
            int: The next available ID for the database.
        """
        if self._db:
            return self._db[-1].id + 1
        return 1


class PredictionsRepository(ListRepository):
    """Repository for Prediction results"""

    _db: list[Prediction]


class OptimizationsRepository(ListRepository):
    """Repository for Optimization results"""

    _db: list[Optimization]
