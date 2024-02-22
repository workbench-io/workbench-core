from workbench_components.workbench_factory import WorkbenchFactory
from workbench_components.workbench_process.workbench_process import WorkbenchProcess


class WorkbenchProcessFactory(WorkbenchFactory):
    """Factory for WorkbenchProcess classes."""

    _items: dict[str, WorkbenchProcess] | None = None
