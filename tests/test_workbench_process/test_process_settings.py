from workbench_process.process_settings import ProcessSettings
from workbench_process.process_settings_model import SourcesModel


class TestProcessSettings:

    def test_load_configs(self, configs_path):
        process_settings = ProcessSettings()
        process_settings.load_settings_from_file(configs_path)

        assert isinstance(process_settings, ProcessSettings)
        assert isinstance(process_settings.model.sources, SourcesModel)

    def test_all_features_returns_all_relevant_features(self, configs_path):
        process_settings = ProcessSettings()
        process_settings.load_settings_from_file(configs_path)

        all_features = [
            "age",
            "cement",
            "coarse_aggregate",
            "fine_aggregate",
            "fly_ash",
            "slag",
            "superplasticizer",
            "water",
        ]

        assert set(process_settings.model.features.all_features) == set(all_features)
        assert all(
            target not in process_settings.model.features.all_features
            for target in process_settings.model.features.targets
        )
        assert all(
            col not in process_settings.model.features.all_features for col in process_settings.model.features.ignore
        )
