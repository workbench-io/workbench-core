# pylint: disable=too-many-instance-attributes

from dataclasses import dataclass, field

import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline

from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_process.process_data import ProcessData
from workbench_train.train_settings_model import MetricType, ModelType
from workbench_utils.utils_dataframes import generate_dataframe


@dataclass
class TrainData(WorkbenchData):
    """
    Train data class.

    This class is used to store data used throughout the process of training models.

    - `features`: DataFrame with feature data. Data obtained from `ProcessData` object
    - `targets`: DataFrame with data of target(s) to predict. Data obtained from `ProcessData` object

    - `x_train`: DataFrame with feature data for training
    - `x_test`: DataFrame with feature data for testing
    - `y_train`: DataFrame with target data for training
    - `y_test`: DataFrame with target data for testing

    - `preprocessor`: Pipeline object to preprocess data
    - `model_objects`: Dictionary with model objects and parameters to tune

    - `results`: Dictionary with results of the models
    - `estimators`: Dictionary with estimators of fitted models
    """

    features: pd.DataFrame = field(default_factory=generate_dataframe)
    targets: pd.DataFrame = field(default_factory=generate_dataframe)

    x_train: pd.DataFrame = field(default_factory=generate_dataframe)
    x_test: pd.DataFrame = field(default_factory=generate_dataframe)
    y_train: pd.DataFrame = field(default_factory=generate_dataframe)
    y_test: pd.DataFrame = field(default_factory=generate_dataframe)

    preprocessor: Pipeline | None = None
    model_objects: dict[ModelType, dict] = field(default_factory=dict)

    results: dict[ModelType, dict[MetricType, float]] = field(default_factory=dict)
    estimators: dict[ModelType, BaseEstimator] = field(default_factory=dict)
    model_selection: list[ModelType] | None = None

    def __post_init__(self):
        super().__init__()

    def from_process_data(self, data: ProcessData) -> None:
        self.features = data.features
        self.targets = data.targets
