import pytest

from workbench_db.db import get_database_engine
from workbench_db.main import Optimization
from workbench_db.sql_repository import SQLRepository


class TestSQLRepository:

    def test_sql_repository_instantiates(self, test_workbench_configs):

        repo = SQLRepository(get_database_engine, test_workbench_configs.database_url)
        assert repo is not None

    @pytest.mark.skip("Not implemented yet")
    def test_add_inserts_instance_to_database(self, sql_repository):

        optimization = Optimization(value=42.0, solution="{'x': 123.0, 'y': 456.0}", inputs="{'a': 1.0, 'b': 2.0}")
        sql_repository.add(optimization)
