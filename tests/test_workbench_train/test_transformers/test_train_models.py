import pandas as pd

from workbench_train.common import Models
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings
from workbench_train.transformers.create_model_objects import CreateModelObjects
from workbench_train.transformers.create_preprocessor import CreatePreprocessor
from workbench_train.transformers.split_train_test_set import SplitTrainTestSet
from workbench_train.transformers.train_models import TrainModels


class TestTrainModels:
    def test_transform_returns_true(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
        features_and_targets: tuple[pd.DataFrame, pd.DataFrame],
    ):

        train_data.features, train_data.targets = features_and_targets

        SplitTrainTestSet().transform(train_data, train_settings)
        CreatePreprocessor().transform(train_data, train_settings)
        CreateModelObjects().transform(train_data, train_settings)

        result = TrainModels().transform(train_data, train_settings)

        assert result is True

    def test_transform_saves_results_to_data_object_as_dictionary(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
        features_and_targets: tuple[pd.DataFrame, pd.DataFrame],
    ):

        train_data.features, train_data.targets = features_and_targets

        SplitTrainTestSet().transform(train_data, train_settings)
        CreatePreprocessor().transform(train_data, train_settings)
        CreateModelObjects().transform(train_data, train_settings)

        TrainModels().transform(train_data, train_settings)

        assert isinstance(train_data.results, dict)
        assert train_data.results != {}
        assert set(train_data.results.keys()).issubset(Models)
