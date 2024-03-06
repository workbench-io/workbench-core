from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

ScoreType = Literal["mse", "rmse", "mae", "max_error", "r2"]


class CrossValidationModel(BaseModel):
    metric: ScoreType
    folds: int = Field(ge=1)
    scores: list[ScoreType]


class MlflowModel(BaseModel):
    use: bool
    dir: Path
    tracking_uri: str


class TrainSettingsModel(BaseModel):
    """Model for the settings of the train step."""

    seed: int
    test_size: float = Field(gt=0, lt=1)
    search_iterations: int = Field(ge=1)
    n_jobs: int
    cross_validation: CrossValidationModel
    mlflow: MlflowModel
