from workbench_core.process.process import Process
from workbench_core.workbench_factory import WorkbenchFactory


class ProcessFactory(WorkbenchFactory):
    """Factory for Process classes."""

    _items: dict[str, Process] | None = None
