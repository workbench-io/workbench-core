import pytest

from workbench_process.process_config_model import ProcessConfigModel, SourcesModel, ZipFileModel


class TestProcessConfigModel:
    def test_process_config_model(self, config_dict: dict):

        process_config_model = ProcessConfigModel(**config_dict)

        assert isinstance(process_config_model, ProcessConfigModel)
        assert isinstance(process_config_model.sources, SourcesModel)
        assert isinstance(process_config_model.sources.compressive_strength, ZipFileModel)

    def test_process_config_model_type(self, config_dict: dict):

        process_config_model = ProcessConfigModel(**config_dict)

        assert isinstance(process_config_model, ProcessConfigModel)

    @pytest.mark.parametrize(
        ["attribute", "expected_type"],
        [
            ("sources", SourcesModel),
        ],
    )
    def test_process_config_model_types(self, attribute: str, expected_type, config_dict: dict):

        process_config_model = ProcessConfigModel(**config_dict)
        model_attribute = getattr(process_config_model, attribute)

        assert isinstance(model_attribute, expected_type)
