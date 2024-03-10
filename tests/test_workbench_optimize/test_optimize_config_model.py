import pytest

from workbench_optimize.optimize_settings_model import OptimizeSettingsModel


class TestOptimizeSettingsModel:
    def test_optimize_config_model(self, config_dict: dict):

        optimize_settings_model = OptimizeSettingsModel(**config_dict)

        assert isinstance(optimize_settings_model, OptimizeSettingsModel)

    @pytest.mark.parametrize(
        ["attribute", "expected_type"],
        [
            ("verbose", bool),
            ("seed", int),
        ],
    )
    def test_process_config_model_types(self, attribute: str, expected_type, config_dict: dict):

        process_settings_model = OptimizeSettingsModel(**config_dict)
        model_attribute = getattr(process_settings_model, attribute)

        assert isinstance(model_attribute, expected_type)
