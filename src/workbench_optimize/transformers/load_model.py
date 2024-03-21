from workbench_components.workbench_configs import FILEPATH_MODELS_DEFAULT, REGEX_MODELS_DEFAULT
from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_optimize.optimize_data import OptimizeData
from workbench_optimize.optimize_settings import OptimizeSettings
from workbench_utils.export import load_estimator_from_directory


class LoadModelError(Exception):
    """Load model error"""


class LoadModel(WorkbenchTransformer):
    """Load model logic"""

    def transform(self, data: OptimizeData, settings: OptimizeSettings) -> bool:  # pylint: disable=unused-argument
        """Load model logic"""

        self.log_info(self.transform, "Starting loading model logic")

        model = load_estimator_from_directory(FILEPATH_MODELS_DEFAULT, REGEX_MODELS_DEFAULT)
        data.model = model

        self.log_info(self.transform, "Loading model completed")

        return True
