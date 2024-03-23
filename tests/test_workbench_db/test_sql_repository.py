from sqlmodel import Session, select

from workbench_db.db import get_database_engine
from workbench_db.models import Prediction
from workbench_db.sql_repository import SQLRepository
from workbench_train.common import Targets


class TestSQLRepository:

    def test_sql_repository_instantiates(self, test_workbench_configs):

        repo = SQLRepository(get_database_engine, test_workbench_configs.database_url)
        assert repo is not None

    def test_add_inserts_instance_to_database(self, sql_repository, engine_testing, prediction_example_1: Prediction):

        sql_repository.add(prediction_example_1)

        with Session(engine_testing) as session:
            statement = select(Prediction)
            query = session.exec(statement).all()

            assert len(query) == 1
            assert query[0].id == 1
            assert query[0].value == 1.0
            assert query[0].feature == Targets.COMPRESSIVE_STRENGTH
            assert query[0].inputs == "{'a': 1.0, 'b': 1.0}"
