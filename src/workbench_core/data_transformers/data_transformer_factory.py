from workbench_core.data_transformers.data_transfomer import DataTransformer
from workbench_core.workbench_factory import WorkbenchFactory


class DataTransformerFactory(WorkbenchFactory):
    """Factory for DataTransformer classes."""

    _items: dict[str, DataTransformer] | None = None
