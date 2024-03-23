from sqlmodel import Session, select

from workbench_db.models import Prediction
from workbench_db.sql_repository import SQLRepository
from workbench_train.common import Targets


class TestSQLRepository:

    def test_sql_repository_instantiates(self, engine_testing):

        repo = SQLRepository(engine_testing)
        assert repo is not None

    def test_add_inserts_instance_to_database(
        self,
        sql_repository_empty,
        engine_testing,
        prediction_example_1: Prediction,
    ):

        sql_repository_empty.add(prediction_example_1)

        with Session(engine_testing) as session:
            statement = select(Prediction)
            query = session.exec(statement).all()

            assert len(query) == 1

            assert isinstance(query[0], Prediction)
            assert query[0].id == 1
            assert query[0].value == 1.0
            assert query[0].feature == Targets.COMPRESSIVE_STRENGTH
            assert query[0].inputs == "{'a': 1.0, 'b': 1.0}"

    def test_add_inserts_instance_to_database_with_data(
        self,
        engine_testing,
        sql_repository,
        prediction_example_4: Prediction,
    ):

        sql_repository.add(prediction_example_4)

        with Session(engine_testing) as new_session:
            statement = select(Prediction)
            query = new_session.exec(statement).all()

            assert len(query) == 4

            assert isinstance(query[3], Prediction)
            assert query[3].id == 4
            assert query[3] == prediction_example_4

    def test_add_inserts_multiple_instances_to_database_with_data(
        self,
        engine_testing,
        sql_repository,
        prediction_example_4: Prediction,
        prediction_example_5: Prediction,
    ):

        sql_repository.add(prediction_example_4)
        sql_repository.add(prediction_example_5)

        with Session(engine_testing) as new_session:
            statement = select(Prediction)
            query = new_session.exec(statement).all()

            assert len(query) == 5
            assert query[3].id == 4
            assert query[3] == prediction_example_4
            assert isinstance(query[3], Prediction)

            assert query[4].id == 5
            assert query[4] == prediction_example_5
            assert isinstance(query[4], Prediction)

    def test_get_returns_the_right_object_by_id(
        self,
        sql_repository,
    ):

        result = sql_repository.get(Prediction, 1)

        assert result.id == 1
        assert result.value == 1.0
        assert result.feature == Targets.COMPRESSIVE_STRENGTH
        assert result.inputs == "{'a': 1.0, 'b': 1.0}"

    def test_get_all_returns_list_of_all_data_in_database(
        self,
        sql_repository,
    ):

        result = sql_repository.get_all(Prediction)

        assert isinstance(result, list)
        assert len(result) == 3

        for idx, item in enumerate(result):
            assert item.id == idx + 1
            assert isinstance(item, Prediction)
