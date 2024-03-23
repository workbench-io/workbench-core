import pytest
from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, select

from workbench_db.models import Optimization, Prediction
from workbench_db.repositories.sql_repository import SQLRepository
from workbench_train.common import Targets


class TestSQLRepository:

    @pytest.mark.parametrize(
        [
            "model",
        ],
        [(Prediction,), (Optimization,)],
    )
    def test_sql_repository_instantiates(self, model: SQLModel, engine_testing):

        repo = SQLRepository(engine_testing, model)
        assert repo is not None

    def test_add_inserts_instance_to_database(
        self,
        sql_repository_empty: SQLRepository,
        engine_testing: Engine,
        prediction_example_1: Prediction,
    ):

        result = sql_repository_empty.add(prediction_example_1)

        assert isinstance(result, Prediction)
        assert result.id == 1

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
        engine_testing: Engine,
        sql_repository: SQLRepository,
        prediction_example_4: Prediction,
    ):

        result = sql_repository.add(prediction_example_4)

        assert isinstance(result, Prediction)
        assert result.id == 4

        with Session(engine_testing) as new_session:
            statement = select(Prediction)
            query = new_session.exec(statement).all()

            assert len(query) == 4

            assert isinstance(query[3], Prediction)
            assert query[3].id == 4
            assert query[3] == prediction_example_4

    def test_add_inserts_multiple_instances_to_database_with_data(
        self,
        engine_testing: Engine,
        sql_repository: SQLRepository,
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
        sql_repository: SQLRepository,
    ):

        result = sql_repository.get(1)

        assert result.id == 1
        assert result.value == 1.0
        assert result.feature == Targets.COMPRESSIVE_STRENGTH
        assert result.inputs == "{'a': 1.0, 'b': 1.0}"

    def test_get_all_returns_list_of_all_data_in_database(
        self,
        sql_repository: SQLRepository,
    ):

        result = sql_repository.get_all()

        assert isinstance(result, list)
        assert len(result) == 3

        for idx, item in enumerate(result):
            assert item.id == idx + 1
            assert isinstance(item, Prediction)

    def test_get_latest_returns_last_item_to_be_added_to_the_database(
        self,
        sql_repository: SQLRepository,
    ):

        result = sql_repository.get_latest()

        assert isinstance(result, Prediction)
        assert result.id == 3
        assert result.value == 3.0
        assert result.feature == Targets.COMPRESSIVE_STRENGTH
        assert result.inputs == "{'a': 3.0, 'b': 3.0}"

    def test_update_updates_an_item_in_the_database(
        self,
        sql_repository: SQLRepository,
    ):

        updated_item = Prediction(
            id=1,
            value=1.5,
            feature=Targets.COMPRESSIVE_STRENGTH,
            inputs="{'a': 1.5, 'b': 1.5}",
        )

        result = sql_repository.update(2, updated_item)

        assert result.id == updated_item.id
        assert result.value == updated_item.value
        assert result.feature == updated_item.feature
        assert result.inputs == updated_item.inputs

    def test_update_updates_an_item_in_the_database_with_partial_update(
        self,
        sql_repository: SQLRepository,
    ):

        updated_item = Prediction(
            id=1,
            value=1.5,
            feature=None,
            inputs=None,
        )

        result = sql_repository.update(1, updated_item)

        assert result.id == updated_item.id
        assert result.value == updated_item.value
        assert result.feature == Targets.COMPRESSIVE_STRENGTH
        assert result.inputs == "{'a': 1.0, 'b': 1.0}"

    def test_update_performs_no_update_when_only_id_is_provided(
        self,
        sql_repository: SQLRepository,
    ):

        updated_item = Prediction(
            id=1,
            value=None,
            feature=None,
            inputs=None,
        )

        result = sql_repository.update(1, updated_item)

        assert result.id == updated_item.id
        assert result.value == 1.0
        assert result.feature == Targets.COMPRESSIVE_STRENGTH
        assert result.inputs == "{'a': 1.0, 'b': 1.0}"

    def test_delete_removes_an_item_from_the_database(
        self,
        sql_repository: SQLRepository,
        engine_testing: Engine,
    ):

        result = sql_repository.delete(1)

        assert result.id == 1
        assert result.value == 1.0
        assert result.feature == Targets.COMPRESSIVE_STRENGTH
        assert result.inputs == "{'a': 1.0, 'b': 1.0}"

        with Session(engine_testing) as session:
            statement = select(Prediction).where(Prediction.id == 1)
            query = session.exec(statement).first()

            assert query is None
