from workbench_core.workbench_data.workbench_data import WorkbenchData


class TestWorkbenchData:

    def test___init__(self):
        data_object = WorkbenchData()
        assert data_object is not None
