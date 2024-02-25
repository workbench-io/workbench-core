"""Test WorkbenchTransformer class."""

from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings
from workbench_components.workbench_source.workbench_source import WorkbenchSource


class TestWorkbenchTransformer:
    """Test WorkbenchTransformer class."""

    def test_load(
        self,
        workbench_source: WorkbenchSource,
        workbench_data: WorkbenchData,
        workbench_settings: WorkbenchSettings,
    ):

        result = workbench_source().load(workbench_data, workbench_settings)
        assert result is True
