"""Base class for configuration objects."""

from abc import ABC

from workbench_core.logging.workbench_logger import WorkbenchLogger


class WorkbenchConfig(ABC, WorkbenchLogger):
    """Base class for configuration objects."""

    def __init__(self) -> None:
        self.create_logger()
