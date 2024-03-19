from workbench_components.workbench_factory import WorkbenchFactory
from workbench_components.workench_repository.workbench_repository import WorkbenchRepository


class WorkbenchRepositoryFactory(WorkbenchFactory):
    """Factory for WorkbenchRepository classes."""

    _items: dict[str, WorkbenchRepository] | None = None
