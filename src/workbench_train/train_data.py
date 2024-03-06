# pylint: disable=too-many-instance-attributes

from dataclasses import dataclass, field

import pandas as pd
from sklearn.pipeline import Pipeline

from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_process.process_data import ProcessData
from workbench_utils.utils_dataframes import generate_dataframe


@dataclass
class TrainData(WorkbenchData):

    features: pd.DataFrame = field(default_factory=generate_dataframe)
    targets: pd.DataFrame = field(default_factory=generate_dataframe)
    preprocessor: Pipeline | None = None
    model_objects: dict[str, dict] = field(default_factory=dict)
    x_train: pd.DataFrame = field(default_factory=generate_dataframe)
    x_test: pd.DataFrame = field(default_factory=generate_dataframe)
    y_train: pd.DataFrame = field(default_factory=generate_dataframe)
    y_test: pd.DataFrame = field(default_factory=generate_dataframe)

    def __post_init__(self):
        super().__init__()

    def from_process_data(self, data: ProcessData) -> None:
        self.features = data.features
        self.targets = data.targets
