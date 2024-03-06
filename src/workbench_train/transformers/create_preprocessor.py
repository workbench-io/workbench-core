import warnings

import pandas as pd
from feature_engine.imputation import AddMissingIndicator, DropMissingData, MeanMedianImputer
from feature_engine.selection import DropConstantFeatures, DropDuplicateFeatures, SmartCorrelatedSelection
from feature_engine.transformation import YeoJohnsonTransformer
from feature_engine.wrappers import SklearnTransformerWrapper
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings


class CreatePreprocessor(WorkbenchTransformer):
    """Create data preprocessor"""

    def transform(self, data: TrainData, settings: TrainSettings) -> bool:
        """Create data preprocessor"""

        self.log_info(self.transform, "Creating pre-processor")


warnings.filterwarnings(action="ignore", category=pd.errors.PerformanceWarning)


def create_preprocessor(
    col_bool: list,
    col_numeric: list,
):

    preprocessor = Pipeline(
        steps=[
            # # Add Missing Indicator
            # ('bool_missing_indicator', AddMissingIndicator(variables=col_bool, missing_only=True)),
            # Impute Missing Values
            ("bool_impute_missing", MeanMedianImputer(variables=col_bool, imputation_method="median")),
            # Add Missing Indicator
            ("num_missing_indicator", AddMissingIndicator(variables=col_numeric, missing_only=True)),
            # Impute Missing Values
            ("num_impute_missing_median", MeanMedianImputer(variables=col_numeric, imputation_method="median")),
            # Yeo-Johnson Transform
            ("num_yeojohnson", YeoJohnsonTransformer(variables=col_numeric)),
            # Z-score Scaling
            ("num_zscore_scaling", SklearnTransformerWrapper(variables=col_numeric, transformer=StandardScaler())),
            # All Features
            # Remove Highly Correlated
            (
                "remove_correlated",
                SmartCorrelatedSelection(variables=col_numeric + col_bool),
            ),
            # Remove Duplicates
            ("all_drop_duplicate", DropDuplicateFeatures(missing_values="ignore")),
            # Remove Constant
            ("all_drop_constant", DropConstantFeatures(missing_values="ignore")),
            # Drop Missing Data
            ("all_drop_missing", DropMissingData()),
        ]
    )

    return preprocessor
