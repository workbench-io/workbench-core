from workbench_core.workbench_factory import WorkbenchFactory
from workbench_core.workbench_source.workbench_source import WorkbenchSource


class WorkbenchSourceFactory(WorkbenchFactory):
    """Factory for WorkbenchSource classes."""

    _items: dict[str, WorkbenchSource] | None = None
