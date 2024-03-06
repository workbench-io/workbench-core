import pandas as pd
from sklearn.pipeline import Pipeline

from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings
from workbench_train.transformers.create_preprocessor import CreatePreprocessor


class TestCreatePreprocessor:
    def test_transform_returns_true(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
    ):
        result = CreatePreprocessor().transform(train_data, train_settings)

        assert result is True

    def test_transform_creates_right_instance_type(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
    ):

        CreatePreprocessor().transform(train_data, train_settings)

        assert train_data.preprocessor is not None
        assert isinstance(train_data.preprocessor, Pipeline)

    def test_transform_created_preprocessor_is_able_to_transform_data(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
        features_and_targets: tuple[pd.DataFrame, pd.DataFrame],
    ):
        train_data.features, train_data.targets = features_and_targets

        CreatePreprocessor().transform(train_data, train_settings)

        result = train_data.preprocessor.fit_transform(train_data.features)

        assert isinstance(result, pd.DataFrame)
        assert not result.empty
        assert set(result.columns).issubset(train_data.features.columns)
