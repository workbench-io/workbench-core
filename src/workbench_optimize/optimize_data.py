# pylint: disable=too-many-instance-attributes

from dataclasses import dataclass

from workbench_components.workbench_data.workbench_data import WorkbenchData


@dataclass
class OptimizeData(WorkbenchData):

    def __post_init__(self):
        super().__init__()
