from tests.conftest import FakeEstimator
from workbench_api.models.predict import PredictionInputModel
from workbench_api.utils import get_model, get_predicted_value


def test_get_predicted_value(concrete_composition_dict: dict, fake_estimator: FakeEstimator):
    prediction_input = PredictionInputModel(**concrete_composition_dict)
    model = fake_estimator

    result = get_predicted_value(prediction_input, model)

    assert isinstance(result, float)


def test_get_model():

    result = get_model()

    assert result is not None
    assert hasattr(result, "predict")
