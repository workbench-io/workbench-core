# pylint: disable=too-many-instance-attributes

from dataclasses import dataclass, field
from typing import Callable

from workbench_components.workbench_data.workbench_data import WorkbenchData


@dataclass
class OptimizeData(WorkbenchData):

    model: Callable | None = None
    results: dict = field(default_factory=dict)

    def __post_init__(self):
        super().__init__()
