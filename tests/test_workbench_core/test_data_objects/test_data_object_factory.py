from workbench_core.workbench_data.workbench_data import WorkbenchData
from workbench_core.workbench_data.workbench_data_factory import WorkbenchDataFactory


class TestWorkbenchDataFactory:

    def test_register(self, data_object_factory: WorkbenchDataFactory, data_object: WorkbenchData):
        data_object_factory.register(name="name", item=data_object)

        assert data_object_factory._items["name"] == data_object  # pylint: disable=protected-access

    def test_create(self, data_object_factory: WorkbenchDataFactory, data_object: WorkbenchData):

        data_object_factory.register(name="name", item=data_object)
        result = data_object_factory.create(name="name")

        assert result == data_object

    def test_create_instance(self, data_object_factory: WorkbenchDataFactory, data_object: WorkbenchData):

        data_object_factory.register(name="name", item=data_object)
        result = data_object_factory.create_instance(name="name")

        assert result.__class__.__qualname__ == data_object.__qualname__
