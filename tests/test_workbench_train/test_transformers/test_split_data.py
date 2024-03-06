import pytest

from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings
from workbench_train.transformers.split_data import SplitData


class TestSplitData:
    def test_transform_returns_true(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
    ):

        result = SplitData().transform(train_data, train_settings)

        assert result is True

    @pytest.mark.xfail(reason="Not implemented.")
    def test_transform_create_train_and_test_sets_of_expected_proportions(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
    ):

        SplitData().transform(train_data, train_settings)

        assert False
