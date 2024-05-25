from feature_engine.encoding import OneHotEncoder, RareLabelEncoder
from feature_engine.imputation import AddMissingIndicator, CategoricalImputer, DropMissingData, MeanMedianImputer
from feature_engine.outliers import OutlierTrimmer, Winsorizer
from feature_engine.selection import DropConstantFeatures, DropDuplicateFeatures, DropFeatures, SmartCorrelatedSelection
from feature_engine.transformation import YeoJohnsonTransformer
from feature_engine.wrappers import SklearnTransformerWrapper
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_train.enums import Transformers
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings

STEP_TO_TRANSFORMER_MAP: dict[str, dict] = {
    Transformers.BOOLEAN_IMPUTE_MISSING: {
        "transformer": MeanMedianImputer,
        "feature_type": "bool",
        "args": {"imputation_method": "median"},
    },
    Transformers.NUMERIC_ADD_MISSING_INDICATOR: {
        "transformer": AddMissingIndicator,
        "feature_type": ["int", "float"],
        "args": {"missing_only": True},
    },
    Transformers.NUMERIC_IMPUTE_MISSING_MEDIAN: {
        "transformer": MeanMedianImputer,
        "feature_type": ["int", "float"],
        "args": {"imputation_method": "median"},
    },
    Transformers.NUMERIC_IMPUTE_MISSING_MEAN: {
        "transformer": MeanMedianImputer,
        "feature_type": ["int", "float"],
        "args": {"imputation_method": "mean"},
    },
    Transformers.NUMERIC_YEOJOHNSON: {
        "transformer": YeoJohnsonTransformer,
        "feature_type": ["int", "float"],
        "args": {},
    },
    Transformers.NUMERIC_ZSCORE_SCALING: {
        "transformer": SklearnTransformerWrapper,
        "feature_type": ["int", "float"],
        "args": {"transformer": StandardScaler()},
    },
    Transformers.NUMERIC_MINMAX_SCALING: {
        "transformer": SklearnTransformerWrapper,
        "feature_types": ["int", "float"],
        "args": {"transformer": MinMaxScaler()},
    },
    Transformers.NUMERIC_REMOVE_CORRELATED: {
        "transformer": SmartCorrelatedSelection,
        "feature_type": ["int", "float"],
        "args": {
            "threshold": 0.90,
            "method": "pearson",
            "selection_method": "missing_values",
            "missing_values": "ignore",
        },
    },
    Transformers.CATEGORICAL_RARE_LABEL_ENCODER: {
        "transformer": RareLabelEncoder,
        "feature_types": ["object", "category"],
        "args": {
            "n_categories": 5,
            "tol": 0.05,
        },
    },
    Transformers.NUMERIC_WINSORIZER: {
        "transformer": Winsorizer,
        "feature_types": ["int", "float"],
        "args": {
            "capping_method": "gaussian",
            "fold": 3,
            "tail": "both",
            "missing_values": "ignore",
        },
    },
    Transformers.NUMERIC_OUTLIER_TRIMMER: {
        "transformer": OutlierTrimmer,
        "feature_types": ["int", "float"],
        "args": {
            "capping_method": "gaussian",
            "fold": 3,
            "tail": "both",
        },
    },
    Transformers.CATEGORICAL_IMPUTE_MISSING: {
        "transformer": CategoricalImputer,
        "feature_types": ["object", "category"],
        "args": {"imputation_method": "frequent"},
    },
    Transformers.CATEGORICAL_ONE_HOT_ENCODER: {
        "transformer": OneHotEncoder,
        "feature_types": ["object", "category"],
        "args": {
            "drop_last": True,
            "drop_last_binary": True,
        },
    },
    Transformers.ALL_DROP_DUPLICATE: {
        "transformer": DropDuplicateFeatures,
        "feature_type": None,
        "args": {"missing_values": "ignore"},
    },
    Transformers.ALL_DROP_CONSTANT: {
        "transformer": DropConstantFeatures,
        "feature_type": None,
        "args": {"missing_values": "ignore"},
    },
    Transformers.ALL_DROP_MISSING: {
        "transformer": DropMissingData,
        "feature_type": None,
        "args": {},
    },
    Transformers.OBJECT_DROP_COLUMNS: {
        "transformer": DropFeatures,
        "feature_types": ["object"],
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
                    f"Adding '{step_name}' to preprocessor pipeline",
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
