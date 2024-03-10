from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_optimize.optimize_data import OptimizeData
from workbench_optimize.optimize_settings import OptimizeSettings


class RunOptimizationError(Exception):
    """Run optimization error"""


class RunOptimization(WorkbenchTransformer):
    """Run optimization logic"""

    def transform(self, data: OptimizeData, settings: OptimizeSettings) -> bool:
        """Run optimization logic"""

        self.log_info(self.transform, "Starting optimization logic")

        self.log_info(self.transform, "Optimization logic completed")

        return True
