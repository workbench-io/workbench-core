from workbench_core.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_core.workbench_transformer.workbench_transformer_factory import WorkbenchTransformerFactory


class TestWorkbenchTransformerFactory:

    def test_register(
        self, data_transformer_factory: WorkbenchTransformerFactory, data_transformer: WorkbenchTransformer
    ):
        data_transformer_factory.register(name="name", item=data_transformer)

        assert data_transformer_factory._items["name"] == data_transformer  # pylint: disable=protected-access

    def test_create(
        self, data_transformer_factory: WorkbenchTransformerFactory, data_transformer: WorkbenchTransformer
    ):

        data_transformer_factory.register(name="name", item=data_transformer)
        result = data_transformer_factory.create(name="name")

        assert result == data_transformer

    def test_create_instance(
        self, data_transformer_factory: WorkbenchTransformerFactory, data_transformer: WorkbenchTransformer
    ):

        data_transformer_factory.register(name="name", item=data_transformer)
        result = data_transformer_factory.create_instance(name="name")

        assert isinstance(result, WorkbenchTransformer)
