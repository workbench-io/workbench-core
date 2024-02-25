"""Base class for settings objects."""

from abc import ABC

from workbench_components.workbench_logging.workbench_logger import WorkbenchLogger


class WorkbenchSettings(ABC, WorkbenchLogger):
    """Base class for settings objects."""

    def __init__(self) -> None:
        self.create_logger()
