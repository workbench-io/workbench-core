from workbench_optimize.optimize_data import OptimizeData


class TestOptimizeData:

    def test_optimize_data(self):
        optimize_data = OptimizeData()

        assert isinstance(optimize_data, OptimizeData)
