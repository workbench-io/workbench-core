from workbench_process.process_config import ProcessSettings
from workbench_process.process_config_model import SourcesModel


class TestProcessSettings:

    def test_load_configs(self, configs_path):
        process_config = ProcessSettings()
        process_config.load_configs(configs_path)

        assert isinstance(process_config, ProcessSettings)
        assert isinstance(process_config.configs.sources, SourcesModel)
