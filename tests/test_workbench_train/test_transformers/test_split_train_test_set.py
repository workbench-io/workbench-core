import pandas as pd

from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings
from workbench_train.transformers.split_train_test_set import SplitTrainTestSet


class TestSplitData:
    def test_transform_returns_true(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
    ):

        train_data.features = pd.DataFrame({"A": range(0, 10)})
        train_data.targets = pd.DataFrame({"B": range(10, 20)})
        train_settings.model.training.test_size = 0.2

        result = SplitTrainTestSet().transform(train_data, train_settings)

        assert result is True

    def test_transform_create_train_and_test_sets_of_expected_proportions(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
    ):

        train_data.features = pd.DataFrame({"A": range(0, 10)})
        train_data.targets = pd.DataFrame({"B": range(10, 20)})
        train_settings.model.training.test_size = 0.2

        SplitTrainTestSet().transform(train_data, train_settings)

        assert len(train_data.x_train) == 8
        assert len(train_data.y_train) == 8

        assert len(train_data.x_test) == 2
        assert len(train_data.y_test) == 2
