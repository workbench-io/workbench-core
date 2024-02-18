from workbench_core.data_objects.data_object import DataObject


class TestDataObject:

    def test___init__(self):
        data_object = DataObject()
        assert data_object is not None
