from workbench_core.workbench_factory import WorkbenchFactory
from workbench_core.workbench_transformer.workbench_transfomer import WorkbenchTransformer


class WorkbenchTransformerFactory(WorkbenchFactory):
    """Factory for WorkbenchTransformer classes."""

    _items: dict[str, WorkbenchTransformer] | None = None
