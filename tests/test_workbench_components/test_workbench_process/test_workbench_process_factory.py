from workbench_components.workbench_process.workbench_process import WorkbenchLogic
from workbench_components.workbench_process.workbench_process_factory import WorkbenchLogicFactory


class TestWorkbenchLogicFactory:

    def test_register(self, workbench_process_factory: WorkbenchLogicFactory, workbench_transformer: WorkbenchLogic):
        workbench_process_factory.register(name="name", item=workbench_transformer)

        assert workbench_process_factory._items["name"] == workbench_transformer  # pylint: disable=protected-access

    def test_create(self, workbench_process_factory: WorkbenchLogicFactory, workbench_transformer: WorkbenchLogic):

        workbench_process_factory.register(name="name", item=workbench_transformer)
        result = workbench_process_factory.create(name="name")

        assert result == workbench_transformer

    def test_create_instance(
        self, workbench_process_factory: WorkbenchLogicFactory, workbench_transformer: WorkbenchLogic
    ):

        workbench_process_factory.register(name="name", item=workbench_transformer)
        result = workbench_process_factory.create_instance(name="name")

        assert result.__class__.__qualname__ == workbench_transformer.__qualname__
