import pytest

from workbench_train.common import Metrics
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings
from workbench_train.train_settings_model import MetricType
from workbench_train.transformers.select_best_model import SelectBestModel


class TestTrainModels:
    def test_transform_returns_true(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
    ):
        result = SelectBestModel().transform(train_data, train_settings)

        assert result is True

    @pytest.mark.parametrize(
        ["metric", "n_models", "expected"],
        [
            (Metrics.RMSE, 1, ["model_2"]),
            (Metrics.RMSE, 2, ["model_2", "model_1"]),
            (Metrics.R2, 1, ["model_3"]),
            (Metrics.R2, 2, ["model_3", "model_2"]),
        ],
    )
    def test_transform_selects_the_model_with_the_lowest_mse(
        self,
        metric: MetricType,
        n_models: int,
        expected: list[str],
        train_data: TrainData,
        train_settings: TrainSettings,
    ):  # pylint: disable=too-many-arguments

        train_settings.model.selecting.metric = metric
        train_settings.model.selecting.n_models = n_models

        train_data.results = {
            "model_1": {"rmse": 5.0, "mse": 25.0, "r2": 0.1},
            "model_2": {"rmse": 1.0, "mse": 1.0, "r2": 0.5},
            "model_3": {"rmse": 10.0, "mse": 100.0, "r2": 0.9},
        }

        SelectBestModel().transform(train_data, train_settings)

        assert train_data.model_selection is not None
        assert len(train_data.model_selection) == len(expected)
        assert train_data.model_selection == expected
