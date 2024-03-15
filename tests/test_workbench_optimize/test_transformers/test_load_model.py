from sklearn.base import BaseEstimator

from workbench_optimize.optimize_data import OptimizeData
from workbench_optimize.optimize_settings import OptimizeSettings
from workbench_optimize.transformers.load_model import LoadModel


class TestLoadModel:
    def test_transform_returns_true(
        self,
        optimize_data: OptimizeData,
        optimize_settings: OptimizeSettings,
    ):

        result = LoadModel().transform(optimize_data, optimize_settings)

        assert result

    def test_transform_saves_estimator_instance_as_attribute_of_data_object(
        self,
        optimize_data: OptimizeData,
        optimize_settings: OptimizeSettings,
    ):

        LoadModel().transform(optimize_data, optimize_settings)

        assert optimize_data.model is not None
        assert isinstance(optimize_data.model, BaseEstimator)
        assert hasattr(optimize_data.model, "predict")
