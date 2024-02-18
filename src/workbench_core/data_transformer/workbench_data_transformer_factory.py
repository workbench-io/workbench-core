from workbench_core.workbench_factory import WorkbenchFactory
from workbench_core.workbench_transformer.workbench_transformer import WorkbenchTransformer


class WorkbenchTransformerFactory(WorkbenchFactory):
    """Factory for WorkbenchTransformer classes."""

    _items: dict[str, WorkbenchTransformer] | None = None
