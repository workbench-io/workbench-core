"""Base class for data objects."""

from abc import ABC

from workbench_core.logging.workbench_logger import WorkbenchLogger


class DataObject(ABC, WorkbenchLogger):
    """Base class for data objects."""

    def __init__(self) -> None:
        self.create_logger()
