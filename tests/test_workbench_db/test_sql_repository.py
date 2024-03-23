from sqlmodel import Session, select

from workbench_db.db import get_database_engine
from workbench_db.main import Optimization
from workbench_db.sql_repository import SQLRepository


class TestSQLRepository:

    def test_sql_repository_instantiates(self, test_workbench_configs):

        repo = SQLRepository(get_database_engine, test_workbench_configs.database_url)
        assert repo is not None

    def test_add_inserts_instance_to_database(self, sql_repository, engine_testing):

        optimization = Optimization(
            value=42.0,
            solution="{'x': 123.0, 'y': 456.0}",
            inputs="{'a': 1.0, 'b': 2.0}",
        )
        sql_repository.add(optimization)

        with Session(engine_testing) as session:
            statement = select(Optimization)
            query = session.exec(statement).all()

            assert len(query) == 1
            assert query[0].id == 1
            assert query[0].value == 42.0
            assert query[0].solution == "{'x': 123.0, 'y': 456.0}"
            assert query[0].inputs == "{'a': 1.0, 'b': 2.0}"
