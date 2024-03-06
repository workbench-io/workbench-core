from feature_engine.imputation import AddMissingIndicator, DropMissingData, MeanMedianImputer
from feature_engine.selection import DropConstantFeatures, DropDuplicateFeatures, SmartCorrelatedSelection
from feature_engine.transformation import YeoJohnsonTransformer
from feature_engine.wrappers import SklearnTransformerWrapper
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings

STEP_TO_TRANSFORMER_MAP: dict[str, dict] = {
    "boolean_impute_missing": {
        "transformer": MeanMedianImputer,
        "feature_type": "bool",
        "args": {"imputation_method": "median"},
    },
    "numeric_add_missing_indicator": {
        "transformer": AddMissingIndicator,
        "feature_type": ["int", "float"],
        "args": {"missing_only": True},
    },
    "numeric_impute_missing_median": {
        "transformer": MeanMedianImputer,
        "feature_type": ["int", "float"],
        "args": {"imputation_method": "median"},
    },
    "numeric_yeojohnson": {
        "transformer": YeoJohnsonTransformer,
        "feature_type": ["int", "float"],
        "args": {},
    },
    "numeric_zscore_scaling": {
        "transformer": SklearnTransformerWrapper,
        "feature_type": ["int", "float"],
        "args": {"transformer": StandardScaler()},
    },
    "numeric_remove_correlated": {
        "transformer": SmartCorrelatedSelection,
        "feature_type": ["int", "float"],
        "args": {
            "threshold": 0.90,
            "method": "pearson",
            "selection_method": "missing_values",
            "missing_values": "ignore",
        },
    },
    "all_drop_duplicate": {
        "transformer": DropDuplicateFeatures,
        "feature_type": None,
        "args": {"missing_values": "ignore"},
    },
    "all_drop_constant": {
        "transformer": DropConstantFeatures,
        "feature_type": None,
        "args": {"missing_values": "ignore"},
    },
    "all_drop_missing": {
        "transformer": DropMissingData,
        "feature_type": None,
        "args": {},
    },
}


class CreatePreprocessor(WorkbenchTransformer):
    """Create data preprocessor"""

    def transform(self, data: TrainData, settings: TrainSettings) -> bool:
        """Create data preprocessor"""

        self.log_info(self.transform, "Creating pre-processor")
        data.preprocessor = self._create_preprocessor(data, settings)

        return True

    def _create_preprocessor(self, data: TrainData, settings: TrainSettings) -> Pipeline:

        steps = []

        for step_name, step_bool in settings.model.preprocessing:
            if step_bool:
                self.log_debug(
                    self._create_preprocessor,
                    f"Adding {step_name} to preprocessor pipeline",
                )
                step_dict = STEP_TO_TRANSFORMER_MAP[step_name]

                if step_dict["feature_type"] is None:
                    step_data = step_name, step_dict["transformer"](**step_dict["args"])
                else:
                    selected_features = data.features.select_dtypes(step_dict["feature_type"]).columns.tolist()
                    if selected_features:
                        step_data = step_name, step_dict["transformer"](
                            variables=selected_features, **step_dict["args"]
                        )
                    else:
                        continue

                steps.append(step_data)

        preprocessor = Pipeline(steps=steps)

        return preprocessor
