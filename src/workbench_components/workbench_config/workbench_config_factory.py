from workbench_components.workbench_config.workbench_config import WorkbenchSettings
from workbench_components.workbench_factory import WorkbenchFactory


class WorkbenchSettingsFactory(WorkbenchFactory):
    """Factory for Config classes."""

    _items: dict[str, WorkbenchSettings] | None = None
