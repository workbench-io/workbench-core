from workbench_core.data_objects.data_object import DataObject
from workbench_core.workbench_factory import WorkbenchFactory


class DataObjectFactory(WorkbenchFactory):
    """Factory for DataObject classes."""

    _items: dict[str, DataObject] | None = None

    # def __init__(self) -> None:
    #     super().__init__()
