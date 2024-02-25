"""Test WorkbenchLogic class."""

from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_components.workbench_process.workbench_process import WorkbenchLogic
from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings


class TestWorkbenchLogic:
    """Test WorkbenchLogic class."""

    def test___init__(self, workbench_process: WorkbenchLogic):

        result = workbench_process().__init__()  # pylint: disable=unnecessary-dunder-call
        assert result is None

    def test_run(
        self, workbench_process: WorkbenchLogic, workbench_data: WorkbenchData, workbench_config: WorkbenchSettings
    ):

        result = workbench_process().run(workbench_data, workbench_config)
        assert result is True
