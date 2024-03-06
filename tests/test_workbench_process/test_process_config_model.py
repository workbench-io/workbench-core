import pytest

from workbench_process.process_settings_model import ProcessSettingsModel, SourcesModel


class TestProcessSettingsModel:
    def test_process_config_model(self, config_dict: dict):

        process_settings_model = ProcessSettingsModel(**config_dict)

        assert isinstance(process_settings_model, ProcessSettingsModel)

    @pytest.mark.parametrize(
        ["attribute", "expected_type"],
        [
            ("sources", SourcesModel),
        ],
    )
    def test_process_config_model_types(self, attribute: str, expected_type, config_dict: dict):

        process_settings_model = ProcessSettingsModel(**config_dict)
        model_attribute = getattr(process_settings_model, attribute)

        assert isinstance(model_attribute, expected_type)
