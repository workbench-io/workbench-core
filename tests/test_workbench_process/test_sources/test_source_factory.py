from workbench_components.workbench_source.workbench_source_factory import WorkbenchSourceFactory
from workbench_process.common import Source
from workbench_process.sources.source_compressive_strength import SourceCompressiveStrength


class TestSourceFactory:

    def test_workbench_source_factory_registers_source(self):

        source_factory = WorkbenchSourceFactory()
        source_factory.register(name=Source.COMPRESSIVE_STRENGTH, item=SourceCompressiveStrength)

        assert source_factory.contains(name=Source.COMPRESSIVE_STRENGTH)

    def test_workbench_source_factory_returns_instance(self):

        source_factory = WorkbenchSourceFactory()
        source_factory.register(name=Source.COMPRESSIVE_STRENGTH, item=SourceCompressiveStrength)

        instance = source_factory.create_instance(name=Source.COMPRESSIVE_STRENGTH)
        assert isinstance(instance, SourceCompressiveStrength)

    def test_workbench_source_factory_returns_(self):

        source_factory = WorkbenchSourceFactory()
        source_factory.register(name=Source.COMPRESSIVE_STRENGTH, item=SourceCompressiveStrength)

        source_object = source_factory.create(name=Source.COMPRESSIVE_STRENGTH)
        assert isinstance(source_object(), SourceCompressiveStrength)
