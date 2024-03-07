from enum import StrEnum, auto


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
