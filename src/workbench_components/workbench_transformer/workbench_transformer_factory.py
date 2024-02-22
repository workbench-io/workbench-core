from workbench_components.workbench_factory import WorkbenchFactory
from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer


class WorkbenchTransformerFactory(WorkbenchFactory):
    """Factory for WorkbenchTransformer classes."""

    _items: dict[str, WorkbenchTransformer] | None = None
