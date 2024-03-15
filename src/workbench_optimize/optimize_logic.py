from workbench_components.workbench_logic.workbench_logic import WorkbenchLogic
from workbench_optimize.optimize_data import OptimizeData
from workbench_optimize.optimize_settings import OptimizeSettings
from workbench_optimize.transformers.load_model import LoadModel
from workbench_optimize.transformers.run_optimization import RunOptimization


class OptimizeLogic(WorkbenchLogic):

    def run(
        self,
        data: OptimizeData,
        settings: OptimizeSettings,
    ):
        self.log_info(self.run, "Running optimization")
        LoadModel().transform(data, settings)
        RunOptimization().transform(data, settings)
        self.log_info(self.run, "Optimization complete")

        return True
