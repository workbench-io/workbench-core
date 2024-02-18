from workbench_core.data_objects.data_object import DataObject
from workbench_core.data_objects.data_object_factory import DataObjectFactory


class TestDataObjectFactory:

    def test_register(self, data_object_factory: DataObjectFactory, data_object: DataObject):
        data_object_factory.register(name="name", item=data_object)

        assert data_object_factory._items["name"] == data_object  # pylint: disable=protected-access

    def test_create(self, data_object_factory: DataObjectFactory, data_object: DataObject):

        data_object_factory.register(name="name", item=data_object)
        result = data_object_factory.create(name="name")

        assert result == data_object

    def test_create_instance(self, data_object_factory: DataObjectFactory, data_object: DataObject):

        data_object_factory.register(name="name", item=data_object)
        result = data_object_factory.create_instance(name="name")

        assert result.__class__.__qualname__ == data_object.__qualname__
