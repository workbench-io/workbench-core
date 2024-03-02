from workbench_train.train_settings import TrainSettings


class TestTrainSettings:

    def test_load_configs(self, configs_path):
        train_settings = TrainSettings()
        train_settings.load_settings_from_file(configs_path)

        assert isinstance(train_settings, TrainSettings)
