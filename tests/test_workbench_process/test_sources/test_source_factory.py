from workbench_process.common import Source
from workbench_process.sources.source_compressive_strength import SourceCompressiveStrength
from workbench_process.sources.source_factory import SourceFactory


class TestSourceFactory:

    def test_register_registers_source(self):

        source_factory = SourceFactory()
        source_factory.register(name=Source.COMPRESSIVE_STRENGTH, item=SourceCompressiveStrength)

        assert source_factory.contains(name=Source.COMPRESSIVE_STRENGTH)

    def test_create_instance_returns_source_instance(self):

        source_factory = SourceFactory()
        source_factory.register(name=Source.COMPRESSIVE_STRENGTH, item=SourceCompressiveStrength)

        instance = source_factory.create_instance(name=Source.COMPRESSIVE_STRENGTH)
        assert isinstance(instance, SourceCompressiveStrength)

    def test_create_returns_source_object(self):

        source_factory = SourceFactory()
        source_factory.register(name=Source.COMPRESSIVE_STRENGTH, item=SourceCompressiveStrength)

        source_object = source_factory.create(name=Source.COMPRESSIVE_STRENGTH)
        assert isinstance(source_object(), SourceCompressiveStrength)
