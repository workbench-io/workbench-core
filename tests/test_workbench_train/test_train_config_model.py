from workbench_train.train_settings_model import TrainSettingsModel


class TestTrainSettingsModel:
    def test_train_config_model(self, config_dict: dict):

        train_settings_model = TrainSettingsModel(**config_dict)

        assert isinstance(train_settings_model, TrainSettingsModel)

    def test_train_config_model_type(self, config_dict: dict):

        train_settings_model = TrainSettingsModel(**config_dict)

        assert isinstance(train_settings_model, TrainSettingsModel)
