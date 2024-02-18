from workbench_core.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_core.workbench_transformer.workbench_transformer_factory import WorkbenchTransformerFactory


class TestWorkbenchTransformerFactory:

    def test_register(
        self, workbench_transformer_factory: WorkbenchTransformerFactory, workbench_transformer: WorkbenchTransformer
    ):
        workbench_transformer_factory.register(name="name", item=workbench_transformer)

        assert workbench_transformer_factory._items["name"] == workbench_transformer  # pylint: disable=protected-access

    def test_create(
        self, workbench_transformer_factory: WorkbenchTransformerFactory, workbench_transformer: WorkbenchTransformer
    ):

        workbench_transformer_factory.register(name="name", item=workbench_transformer)
        result = workbench_transformer_factory.create(name="name")

        assert result == workbench_transformer

    def test_create_instance(
        self, workbench_transformer_factory: WorkbenchTransformerFactory, workbench_transformer: WorkbenchTransformer
    ):

        workbench_transformer_factory.register(name="name", item=workbench_transformer)
        result = workbench_transformer_factory.create_instance(name="name")

        assert isinstance(result, WorkbenchTransformer)
