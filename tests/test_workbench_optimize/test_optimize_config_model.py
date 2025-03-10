from workbench_optimize.optimize_settings_model import OptimizeSettingsModel


class TestOptimizeSettingsModel:
    def test_optimize_config_model(self, config_dict: dict):

        optimize_settings_model = OptimizeSettingsModel(**config_dict)

        assert isinstance(optimize_settings_model, OptimizeSettingsModel)
