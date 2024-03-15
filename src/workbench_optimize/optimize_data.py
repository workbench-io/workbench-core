# pylint: disable=too-many-instance-attributes

from dataclasses import dataclass

from sklearn.base import BaseEstimator

from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_optimize.common import OptimizationResult


@dataclass
class OptimizeData(WorkbenchData):

    model: BaseEstimator | None = None
    results: OptimizationResult | None = None

    def __post_init__(self):
        super().__init__()
