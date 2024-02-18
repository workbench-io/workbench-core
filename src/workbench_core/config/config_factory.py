from workbench_core.config.config import WorkbenchConfig
from workbench_core.workbench_factory import WorkbenchFactory


class WorkbenchConfigFactory(WorkbenchFactory):
    """Factory for Config classes."""

    _items: dict[str, WorkbenchConfig] | None = None
