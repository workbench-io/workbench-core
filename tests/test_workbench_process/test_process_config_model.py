from workbench_process.process_config_model import ProcessConfigModel, SourcesModel


class TestProcessConfigModel:
    def test_process_config_model(self, config_dict: dict):

        process_config_model = ProcessConfigModel(**config_dict)

        assert isinstance(process_config_model, ProcessConfigModel)
        assert isinstance(process_config_model.sources, SourcesModel)
        assert isinstance(process_config_model.sources.compressive_strength, str)
