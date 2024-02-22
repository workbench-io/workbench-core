from workbench_components.workbench_factory import WorkbenchFactory
from workbench_components.workbench_source.workbench_source import WorkbenchSource


class WorkbenchSourceFactory(WorkbenchFactory):
    """Factory for WorkbenchSource classes."""

    _items: dict[str, WorkbenchSource] | None = None
