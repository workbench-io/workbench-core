from workbench_components.workbench_factory import WorkbenchFactory
from workbench_components.workbench_logic.workbench_logic import WorkbenchLogic


class WorkbenchLogicFactory(WorkbenchFactory):
    """Factory for WorkbenchLogic classes."""

    _items: dict[str, WorkbenchLogic] | None = None
