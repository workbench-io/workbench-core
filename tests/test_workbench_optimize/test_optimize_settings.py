from workbench_optimize.optimize_settings import OptimizeSettings


class TestOptimizeSettings:

    def test_load_configs(self, configs_path):
        optimize_settings = OptimizeSettings()
        optimize_settings.load_settings_from_file(configs_path)

        assert isinstance(optimize_settings, OptimizeSettings)
