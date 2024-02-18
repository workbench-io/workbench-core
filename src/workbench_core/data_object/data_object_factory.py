from workbench_core.data_object.data_object import DataObject
from workbench_core.workbench_factory import WorkbenchFactory


class DataObjectFactory(WorkbenchFactory):
    """Factory for DataObject classes."""

    _items: dict[str, DataObject] | None = None
