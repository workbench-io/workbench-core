from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings
from workbench_train.transformers.create_model_objects import MODEL_TO_MODEL_REGRESSOR_MAP, CreateModelObjects


class TestCreateModelObjects:
    def test_transform_returns_true(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
    ):
        result = CreateModelObjects().transform(train_data, train_settings)

        assert result is True

    def test_transform_creates_right_instance_type(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
    ):

        CreateModelObjects().transform(train_data, train_settings)

        assert train_data.model_objects
        assert isinstance(train_data.model_objects, dict)
        assert set(train_data.model_objects.keys()).issubset(MODEL_TO_MODEL_REGRESSOR_MAP.keys())
