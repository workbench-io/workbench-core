from workbench_process.process_config import ProcessConfig
from workbench_process.process_config_model import SourcesModel


class TestProcessConfig:

    def test_load_configs(self, configs_path):
        process_config = ProcessConfig()
        process_config.load_configs(configs_path)

        assert isinstance(process_config, ProcessConfig)
        assert isinstance(process_config.configs.sources, SourcesModel)
