from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings


class TestWorkbenchData:

    def test___init__(self):
        workbench_data = WorkbenchSettings()

        assert workbench_data is not None
        assert isinstance(workbench_data, WorkbenchSettings)
