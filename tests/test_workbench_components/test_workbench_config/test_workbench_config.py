from workbench_components.workbench_config.workbench_config import WorkbenchConfig


class TestWorkbenchData:

    def test___init__(self):
        workbench_data = WorkbenchConfig()

        assert workbench_data is not None
        assert isinstance(workbench_data, WorkbenchConfig)
