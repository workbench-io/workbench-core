from pathlib import Path
from typing import Literal, Optional

from pydantic import BaseModel, Field

MetricType = Literal["mse", "rmse", "mae", "max_error", "r2"]
ModelType = Literal["pls", "lasso", "elasticnet", "svr", "random_forest", "gbm", "neural_network"]


class MlflowSettingsModel(BaseModel):
    use: bool
    dir: Path
    tracking_uri: str


class PreprocessingSettingsModel(BaseModel):
    """Model for pre-processing settings"""

    boolean_impute_missing: bool = False
    numeric_add_missing_indicator: bool = False
    numeric_impute_missing_median: bool = False
    numeric_yeojohnson: bool = False
    numeric_zscore_scaling: bool = False
    numeric_remove_correlated: bool = False
    all_drop_duplicate: bool = False
    all_drop_constant: bool = False
    all_drop_missing: bool = False


class CrossValidationSettingsModel(BaseModel):
    """Model for cross-validation settings"""

    metric: MetricType
    folds: int = Field(ge=1)
    scores: list[MetricType]


class TrainingSettingsModel(BaseModel):
    """Model for training settings"""

    test_size: float = Field(gt=0, lt=1)
    search_iterations: int = Field(ge=1)
    n_jobs: int
    models: list[ModelType]
    cross_validation: CrossValidationSettingsModel


class SelectingSettingsModel(BaseModel):
    """Model for model selection settings"""

    metric: MetricType
    n_models: int = Field(ge=1)


class ExportingSettingsModel(BaseModel):
    """Model for model selection settings"""

    path: Path
    remove_previous: bool


class TrainSettingsModel(BaseModel):
    """Model for the settings of the train step."""

    seed: int
    verbose: bool
    preprocessing: PreprocessingSettingsModel
    training: TrainingSettingsModel
    selecting: SelectingSettingsModel
    exporting: ExportingSettingsModel
    mlflow: Optional[MlflowSettingsModel]
