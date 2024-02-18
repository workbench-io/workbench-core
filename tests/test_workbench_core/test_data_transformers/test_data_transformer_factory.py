from workbench_core.data_transformer.data_transfomer import DataTransformer
from workbench_core.data_transformer.data_transformer_factory import DataTransformerFactory


class TestDataTransformerFactory:

    def test_register(self, data_transformer_factory: DataTransformerFactory, data_transformer: DataTransformer):
        data_transformer_factory.register(name="name", item=data_transformer)

        assert data_transformer_factory._items["name"] == data_transformer  # pylint: disable=protected-access

    def test_create(self, data_transformer_factory: DataTransformerFactory, data_transformer: DataTransformer):

        data_transformer_factory.register(name="name", item=data_transformer)
        result = data_transformer_factory.create(name="name")

        assert result == data_transformer

    def test_create_instance(self, data_transformer_factory: DataTransformerFactory, data_transformer: DataTransformer):

        data_transformer_factory.register(name="name", item=data_transformer)
        result = data_transformer_factory.create_instance(name="name")

        assert result.__class__.__qualname__ == data_transformer.__qualname__
