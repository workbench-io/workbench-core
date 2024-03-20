import pytest

from tests.test_workbench_api import examples
from workbench_api.data.repository import ListRepository, ListRepositoryError
from workbench_api.models.predict import PredictionOutputModel
from workbench_train.common import Targets


class TestListRepository:

    def test_get_returns_correct_object_for_existing_id(
        self, list_repository: ListRepository, prediction_output_model_1: PredictionOutputModel
    ):

        db_id = 1
        result = list_repository.get(db_id)

        assert result is not None
        assert result == prediction_output_model_1

    def test_get_returns_none_for_non_existing_id(self, list_repository: ListRepository):

        db_id = 999
        result = list_repository.get(db_id)

        assert result is None

    def test_get_latest_returns_correct_object(
        self, list_repository: ListRepository, prediction_output_model_3: PredictionOutputModel
    ):

        result = list_repository.get_latest()

        assert result is not None
        assert result == prediction_output_model_3

    def test_get_all_returns_list_of_all_object(self, list_repository: ListRepository):

        result = list_repository.get_all()

        assert result is not None
        assert len(result) == 3

    def test_add_adds_object_to_db(self, list_repository_empty: ListRepository):

        db_id = 42
        prediction_output_model_42 = PredictionOutputModel(
            id=db_id,
            value=42.0,
            feature=Targets.COMPRESSIVE_STRENGTH,
            prediction_input=examples.prediction_body_1,
        )
        list_repository_empty.add(db_id, prediction_output_model_42)

        result = list_repository_empty.get(db_id)

        assert result is not None
        assert result == prediction_output_model_42

    @pytest.mark.parametrize(
        ["db_id", "index"],
        [
            (1, 0),
            (2, 1),
            (3, 2),
        ],
    )
    def test_get_index_of_db_entry_by_id_returns_correct_index(
        self,
        db_id: int,
        index: int,
        list_repository: ListRepository,
    ):
        result = list_repository.get_index_of_db_entry_by_id(db_id)

        assert result is not None
        assert result == index

    def test_get_index_of_db_entry_by_id_raises_error_non_existing_entry(self, list_repository: ListRepository):

        with pytest.raises(ListRepositoryError):
            db_id = 999
            list_repository.get_index_of_db_entry_by_id(db_id)

    def test_update_updates_object_in_db(self, list_repository: ListRepository):

        db_id = 1
        prediction_output_modified = PredictionOutputModel(
            id=db_id,
            value=42.0,
            feature=Targets.COMPRESSIVE_STRENGTH,
            prediction_input=examples.prediction_body_1,
        )
        list_repository.update(db_id, prediction_output_modified)

        result = list_repository.get(db_id)

        assert result is not None
        assert result == prediction_output_modified

    def test_delete_deletes_object_from_db(self, list_repository: ListRepository):

        db_id = 1
        list_repository.delete(db_id)

        result = list_repository.get(db_id)

        assert result is None
        assert len(list_repository.get_all()) == 2

    def test_get_next_id_returns_next_available_id(self, list_repository: ListRepository):

        result = list_repository.get_next_id()

        assert result is not None
        assert result == 4

    def test_get_next_id_returns_next_available_id_from_empty_repo(self, list_repository_empty: ListRepository):

        result = list_repository_empty.get_next_id()

        assert result is not None
        assert result == 1
