from workbench_optimize.optimize_data import OptimizeData
from workbench_optimize.optimize_settings import OptimizeSettings
from workbench_optimize.transformers.run_optimization import RunOptimization


class TestRunOptimization:
    def test_transform_returns_true(
        self,
        optimize_data: OptimizeData,
        optimize_settings: OptimizeSettings,
    ):

        result = RunOptimization().transform(optimize_data, optimize_settings)

        assert result
