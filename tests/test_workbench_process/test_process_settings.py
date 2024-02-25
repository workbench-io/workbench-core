from workbench_process.process_config_model import SourcesModel
from workbench_process.process_settings import ProcessSettings


class TestProcessSettings:

    def test_load_configs(self, configs_path):
        process_settings = ProcessSettings()
        process_settings.load_settings_from_file(configs_path)

        assert isinstance(process_settings, ProcessSettings)
        assert isinstance(process_settings.model.sources, SourcesModel)
