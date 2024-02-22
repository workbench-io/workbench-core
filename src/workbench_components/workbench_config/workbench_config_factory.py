from workbench_components.workbench_config.workbench_config import WorkbenchConfig
from workbench_components.workbench_factory import WorkbenchFactory


class WorkbenchConfigFactory(WorkbenchFactory):
    """Factory for Config classes."""

    _items: dict[str, WorkbenchConfig] | None = None
