from sqlalchemy import Engine

from workbench_db.enums import Repositories
from workbench_db.repositories.repository_factory import RepositoryFactory
from workbench_db.repositories.sql_repository import OptimizationsRepository, PredictionsRepository


class TestRepositoryFactory:
    def test_register(self):
        factory = RepositoryFactory()
        factory.register(Repositories.OPTIMIZATIONS, OptimizationsRepository)
        factory.register(Repositories.PREDICTIONS, PredictionsRepository)

        assert len(factory._items) == 2  # pylint: disable=protected-access

    def test_create_instance(self, engine_testing: Engine):
        factory = RepositoryFactory()
        factory.register(Repositories.OPTIMIZATIONS, OptimizationsRepository)
        factory.register(Repositories.PREDICTIONS, PredictionsRepository)

        optimizations_repo = factory.create_instance(Repositories.OPTIMIZATIONS, engine_testing)
        predictions_repo = factory.create_instance(Repositories.PREDICTIONS, engine_testing)

        assert isinstance(optimizations_repo, OptimizationsRepository)
        assert isinstance(predictions_repo, PredictionsRepository)
