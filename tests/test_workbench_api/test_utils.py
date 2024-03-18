import pytest

from tests.conftest import FakeEstimator
from tests.test_workbench_api import examples
from workbench_api.models.predict import PredictionInputModel, PredictionOutputModel
from workbench_api.utils import get_index_of_db_entry_by_id, get_model, get_predicted_value


def test_get_predicted_value(concrete_composition_dict: dict, fake_estimator: FakeEstimator):
    prediction_input = PredictionInputModel(**concrete_composition_dict)
    model = fake_estimator

    result = get_predicted_value(prediction_input, model)

    assert isinstance(result, float)


def test_get_model():

    result = get_model()

    assert result is not None
    assert hasattr(result, "predict")


@pytest.mark.parametrize(
    ["db_id", "expected_result"],
    [
        (1, 0),
        (2, 1),
        (3, 2),
        (999, None),
    ],
)
def test_get_index_of_db_entry_by_id(db_id: int, expected_result: int):

    predictions = [
        PredictionOutputModel(
            id=1, value=42.0, feature="compressive_strength", prediction_input=examples.prediction_body_1
        ),
        PredictionOutputModel(
            id=2, value=42.0, feature="compressive_strength", prediction_input=examples.prediction_body_2
        ),
        PredictionOutputModel(
            id=3, value=42.0, feature="compressive_strength", prediction_input=examples.prediction_body_3
        ),
    ]

    assert get_index_of_db_entry_by_id(predictions, db_id) == expected_result
