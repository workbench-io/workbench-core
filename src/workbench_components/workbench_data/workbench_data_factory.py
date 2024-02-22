from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_components.workbench_factory import WorkbenchFactory


class WorkbenchDataFactory(WorkbenchFactory):
    """Factory for WorkbenchData classes."""

    _items: dict[str, WorkbenchData] | None = None
