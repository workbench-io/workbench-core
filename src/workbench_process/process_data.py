from dataclasses import dataclass, field

import pandas as pd

from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_process.utils.utils_dataframes import generate_dataframe


@dataclass
class ProcessData(WorkbenchData):

    compressive_strength: pd.DataFrame = field(default_factory=generate_dataframe)
