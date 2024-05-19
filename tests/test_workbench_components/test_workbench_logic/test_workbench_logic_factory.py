from workbench_components.workbench_logic.workbench_logic import WorkbenchLogic
from workbench_components.workbench_logic.workbench_logic_factory import WorkbenchLogicFactory


class TestWorkbenchLogicFactory:

    def test_register(self, workbench_logic_factory: WorkbenchLogicFactory, workbench_transformer: WorkbenchLogic):
        workbench_logic_factory.register(name="name", item=workbench_transformer)

        assert workbench_logic_factory._items["name"] == workbench_transformer  # pylint: disable=protected-access

    def test_create(self, workbench_logic_factory: WorkbenchLogicFactory, workbench_transformer: WorkbenchLogic):

        workbench_logic_factory.register(name="name", item=workbench_transformer)
        result = workbench_logic_factory.create(name="name")

        assert result == workbench_transformer

    def test_create_instance(
        self, workbench_logic_factory: WorkbenchLogicFactory, workbench_transformer: WorkbenchLogic
    ):

        workbench_logic_factory.register(name="name", item=workbench_transformer)
        result = workbench_logic_factory.create_instance(name="name")

        assert result.__class__.__qualname__ == workbench_transformer.__qualname__
