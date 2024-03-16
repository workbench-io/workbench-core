from workbench_components.workbench_logic.workbench_logic import WorkbenchLogic
from workbench_optimize.optimize_data import OptimizeData
from workbench_optimize.optimize_settings import OptimizeSettings
from workbench_optimize.transformers.load_model import LoadModel
from workbench_optimize.transformers.run_optimization import RunOptimization
from workbench_utils.enums import WorkbenchSteps
from workbench_utils.strings import STRING_LOGIC_END, STRING_LOGIC_START


class OptimizeLogic(WorkbenchLogic):

    def run(
        self,
        data: OptimizeData,
        settings: OptimizeSettings,
    ):
        self.log_info(self.run, STRING_LOGIC_START.format(step=WorkbenchSteps.OPTIMIZE))

        if data.model is None:
            self.log_info(self.run, "Loading the model")
            LoadModel().transform(data, settings)

        self.log_info(self.run, "Running optimization")
        RunOptimization().transform(data, settings)

        self.log_info(self.run, STRING_LOGIC_END.format(step=WorkbenchSteps.OPTIMIZE))

        return True
