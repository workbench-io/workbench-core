import pandas as pd

from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings
from workbench_train.transformers.select_best_model import SelectBestModel


class TestTrainModels:
    def test_transform_returns_true(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
    ):
        result = SelectBestModel().transform(train_data, train_settings)

        assert result is True

    def test_transform_selects_the_model_with_the_lowest_mse(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
        features_and_targets: tuple[pd.DataFrame, pd.DataFrame],
    ):

        pass
