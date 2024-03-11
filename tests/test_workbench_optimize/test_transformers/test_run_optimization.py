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

    def test_transform_saves_results_to_data_object(
        self,
        optimize_data: OptimizeData,
        optimize_settings: OptimizeSettings,
    ):

        RunOptimization().transform(optimize_data, optimize_settings)

        assert optimize_data.results is not None

        assert isinstance(optimize_data.results.best_value, float)
        assert optimize_data.results.best_value > 0.0

        assert isinstance(optimize_data.results.best_solution, dict)
        assert optimize_data.results.best_solution != {}

        assert isinstance(optimize_data.results.metadata, dict)
        assert list(optimize_data.results.metadata.keys()) == ["summary"]
