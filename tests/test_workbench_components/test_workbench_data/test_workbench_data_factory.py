from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_components.workbench_data.workbench_data_factory import WorkbenchDataFactory


class TestWorkbenchDataFactory:

    def test_register(self, workbench_data_factory: WorkbenchDataFactory, workbench_data: WorkbenchData):
        workbench_data_factory.register(name="name", item=workbench_data)

        assert workbench_data_factory._items["name"] == workbench_data  # pylint: disable=protected-access

    def test_create(self, workbench_data_factory: WorkbenchDataFactory, workbench_data: WorkbenchData):

        workbench_data_factory.register(name="name", item=workbench_data)
        result = workbench_data_factory.create(name="name")

        assert result == workbench_data

    def test_create_instance(self, workbench_data_factory: WorkbenchDataFactory, workbench_data: WorkbenchData):

        workbench_data_factory.register(name="name", item=workbench_data)
        result = workbench_data_factory.create_instance(name="name")

        assert result.__class__.__qualname__ == workbench_data.__qualname__
