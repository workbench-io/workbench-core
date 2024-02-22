from workbench_components.workbench_data.workbench_data import WorkbenchData


class TestWorkbenchData:

    def test___init__(self):
        workbench_data = WorkbenchData()
        assert workbench_data is not None
