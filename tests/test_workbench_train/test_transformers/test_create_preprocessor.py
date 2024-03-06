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

    def test_transform_create_train_and_test_sets_of_expected_proportions(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
    ):

        CreatePreprocessor().transform(train_data, train_settings)

        assert train_data.preprocessor is not None
        assert isinstance(train_data.preprocessor, Pipeline)
