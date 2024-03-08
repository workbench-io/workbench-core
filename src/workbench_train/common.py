from enum import StrEnum, auto

EXPORTED_MODEL_FILENAME_TEMPLACE = "{model_name}.pkl"


class Models(StrEnum):
    """Enum for models available for training."""

    PLS = auto()
    LASSO = auto()
    ELASTICNET = auto()
    SVR = auto()
    RANDOM_FOREST = auto()
    GBM = auto()
    NEURAL_NETWORK = auto()


class Metrics(StrEnum):
    """Enum for metrics available for evaluating models."""

    MSE = auto()
    RMSE = auto()
    MAE = auto()
    MAX_ERROR = auto()
    R2 = auto()


METRIC_LOWER_IS_BETTER_MAP: dict[Metrics, bool] = {
    Metrics.MSE: True,
    Metrics.RMSE: True,
    Metrics.MAE: True,
    Metrics.MAX_ERROR: True,
    Metrics.R2: False,
}
