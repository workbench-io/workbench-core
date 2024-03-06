import pytest

from workbench_train.train_settings_model import CrossValidationModel, MlflowModel, TrainSettingsModel


class TestTrainSettingsModel:
    def test_train_config_model(self, config_dict: dict):

        train_settings_model = TrainSettingsModel(**config_dict)

        assert isinstance(train_settings_model, TrainSettingsModel)

    @pytest.mark.parametrize(
        ["attribute", "expected_type"],
        [
            ("cross_validation", CrossValidationModel),
            ("mlflow", MlflowModel),
        ],
    )
    def test_process_config_model_types(self, attribute: str, expected_type, config_dict: dict):

        process_settings_model = TrainSettingsModel(**config_dict)
        model_attribute = getattr(process_settings_model, attribute)

        assert isinstance(model_attribute, expected_type)
