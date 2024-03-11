from workbench_components.workbench_logic.workbench_logic import WorkbenchLogic
from workbench_optimize.transformers.run_optimization import RunOptimization
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings


class OptimizeLogic(WorkbenchLogic):

    def run(
        self,
        data: TrainData,
        settings: TrainSettings,
    ):
        self.log_info(self.run, "Running optimization")
        RunOptimization().transform(data, settings)
        self.log_info(self.run, "Optimization complete")

        return True
