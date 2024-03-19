from workbench_api.enums import Routers
from workbench_api.models.optimize import OptimizeOutputModel
from workbench_api.models.predict import PredictionOutputModel
from workbench_api.utils import create_list
from workbench_components.workench_repository.workbench_repository import WorkbenchRepository
from workbench_components.workench_repository.workbench_repository_factory import WorkbenchRepositoryFactory


class ListRepository(WorkbenchRepository):

    def __init__(self) -> None:
        super().__init__()
        self._db: list[object] = create_list()

    def get(self, db_id: int) -> object:
        result = [entry for entry in self._db if int(entry.id) == int(db_id)]

        if result:
            return result[0]
        return None

    def get_latest(self) -> object:
        try:
            return self._db[-1]
        except IndexError:
            return None

    def get_all(self) -> list[object]:
        return self._db

    def add(self, db_id: int, item: object) -> None:  # pylint: disable=unused-argument
        self._db.append(item)

    def update(self, db_id: int, item: object) -> None:
        index = self.get_index_of_db_entry_by_id(db_id)
        self._db[index] = item

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
        return None


class PredictionsRepository(ListRepository):
    """Repository for Prediction results"""

    _db: list[PredictionOutputModel]


class OptimizationsRepository(ListRepository):
    """Repository for Optimization results"""

    _db: list[OptimizeOutputModel]


factory_repository = WorkbenchRepositoryFactory()
factory_repository.register(Routers.PREDICT, PredictionsRepository)
factory_repository.register(Routers.OPTIMIZE, OptimizationsRepository)
