from workbench_components.workbench_factory import WorkbenchFactory
from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings


class WorkbenchSettingsFactory(WorkbenchFactory):
    """Factory for Config classes."""

    _items: dict[str, WorkbenchSettings] | None = None
