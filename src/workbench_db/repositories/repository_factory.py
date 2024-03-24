"""Factory class for Train objects."""

from workbench_components.workbench_factory import WorkbenchFactory
from workbench_components.workench_repository.workbench_repository import WorkbenchRepository
from workbench_db.enums import Repositories
from workbench_db.repositories.sql_repository import OptimizationsRepository, PredictionsRepository


class RepositoryFactory(WorkbenchFactory):
    """Factory class for Train objects."""

    _items: dict[str, WorkbenchRepository] | None = None


factory_repository = RepositoryFactory()
factory_repository.register(Repositories.OPTIMIZATIONS, OptimizationsRepository)
factory_repository.register(Repositories.PREDICTIONS, PredictionsRepository)
