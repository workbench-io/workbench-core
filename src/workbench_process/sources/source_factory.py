from workbench_components.workbench_factory import WorkbenchFactory
from workbench_components.workbench_source.workbench_source import WorkbenchSource
from workbench_process.common import Source
from workbench_process.sources.source_compressive_strength import SourceCompressiveStrength


class SourceFactory(WorkbenchFactory):
    """Factory class for Source objects."""

    _items: dict[str, WorkbenchSource] | None = None


factory_source = SourceFactory()
factory_source.register(name=Source.COMPRESSIVE_STRENGTH, item=SourceCompressiveStrength)
