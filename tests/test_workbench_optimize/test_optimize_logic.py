from workbench_optimize.common import OptimizationResult
from workbench_optimize.optimize_data import OptimizeData
from workbench_optimize.optimize_logic import OptimizeLogic
from workbench_optimize.optimize_settings import OptimizeSettings


class TestOptimizeLogic:

    def test_run_should_return_true(
        self,
        optimize_data: OptimizeData,
        optimize_settings: OptimizeSettings,
    ):

        optimize = OptimizeLogic()

        result = optimize.run(optimize_data, optimize_settings)

        assert isinstance(result, bool)
        assert result

        assert optimize_data.results is not None
        assert isinstance(optimize_data.results, OptimizationResult)
