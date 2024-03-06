from feature_engine.imputation import AddMissingIndicator, DropMissingData, MeanMedianImputer
from feature_engine.selection import DropConstantFeatures, DropDuplicateFeatures, SmartCorrelatedSelection
from feature_engine.transformation import YeoJohnsonTransformer
from feature_engine.wrappers import SklearnTransformerWrapper
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings

STEP_TO_TRANSFORMER_MAP = {
    "boolean_impute_missing": {
        "transformer": MeanMedianImputer,
        "args": {"imputation_method": "median"},
    },
    "numeric_add_missing_indicator": {
        "transformer": AddMissingIndicator,
        "args": {"missing_only": True},
    },
    "numeric_impute_missing_median": {
        "transformer": MeanMedianImputer,
        "args": {"imputation_method": "median"},
    },
    "numeric_yeojohnson": {
        "transformer": YeoJohnsonTransformer,
        "args": {},
    },
    "numeric_zscore_scaling": {
        "transformer": SklearnTransformerWrapper,
        "args": {"transformer": StandardScaler()},
    },
    "numeric_remove_correlated": {
        "transformer": SmartCorrelatedSelection,
        "args": {},
    },
    "all_drop_duplicate": {
        "transformer": DropDuplicateFeatures,
        "args": {"missing_values": "ignore"},
    },
    "all_drop_constant": {
        "transformer": DropConstantFeatures,
        "args": {"missing_values": "ignore"},
    },
    "all_drop_missing": {
        "transformer": DropMissingData,
        "args": {},
    },
}


class CreatePreprocessor(WorkbenchTransformer):
    """Create data preprocessor"""

    def transform(self, data: TrainData, settings: TrainSettings) -> bool:
        """Create data preprocessor"""

        self.log_info(self.transform, "Creating pre-processor")
        data.preprocessor = self._create_preprocessor(settings)

        return True

    def _create_preprocessor(self, settings):

        steps = []

        for step_name, step_bool in settings.model.preprocessing:
            if step_bool:
                step_dict = STEP_TO_TRANSFORMER_MAP[step_name]

                step_data = step_name, step_dict["transformer"](**step_dict["args"])
                steps.append(step_data)

        preprocessor = Pipeline(steps=steps)

        return preprocessor
