from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

MetricType = Literal["mse", "rmse", "mae", "max_error", "r2"]
ModelType = Literal["pls", "lasso", "elasticnet", "svr", "random_forest", "gbm", "neural_network"]


class MlflowModel(BaseModel):
    use: bool
    dir: Path
    tracking_uri: str


class PreprocessingModel(BaseModel):
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


class CrossValidationModel(BaseModel):
    metric: MetricType
    folds: int = Field(ge=1)
    scores: list[MetricType]


class TrainingModel(BaseModel):
    """Model for training settings"""

    test_size: float = Field(gt=0, lt=1)
    search_iterations: int = Field(ge=1)
    n_jobs: int
    models: list[ModelType]
    cross_validation: CrossValidationModel


class SelectingModel(BaseModel):
    """Model for model selection settings"""

    metric: MetricType
    n_models: int = Field(ge=1)


class TrainSettingsModel(BaseModel):
    """Model for the settings of the train step."""

    seed: int
    verbose: bool
    preprocessing: PreprocessingModel
    training: TrainingModel
    selecting: SelectingModel
    mlflow: MlflowModel
