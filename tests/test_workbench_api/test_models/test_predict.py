import pytest

from workbench_api.models.predict import PredictionInputModel


# pylint: disable=too-many-function-args
class TestPredictionInputModel:

    def test_prediction_input_model(self):

        prediction_input_model = PredictionInputModel(
            water=8.33,
            coarse_aggregate=42.23,
            slag=0.0,
            cement=12.09,
            superplasticizer=0.0,
            fine_aggregate=37.35,
            age=28.0,
            fly_ash=0.0,
        )

        assert isinstance(prediction_input_model, PredictionInputModel)

    def test_prediction_input_model_raises_value_error_when_sum_is_not_100(self):

        with pytest.raises(ValueError):
            PredictionInputModel(
                water=0.0,
                coarse_aggregate=0.0,
                slag=0.0,
                cement=0.0,
                superplasticizer=0.0,
                fine_aggregate=0.0,
                age=0.0,
                fly_ash=0.0,
            )
