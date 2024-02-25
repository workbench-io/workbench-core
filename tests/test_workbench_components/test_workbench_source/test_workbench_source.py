"""Test WorkbenchTransformer class."""

from workbench_components.workbench_config.workbench_config import WorkbenchSettings
from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_components.workbench_source.workbench_source import WorkbenchSource


class TestWorkbenchTransformer:
    """Test WorkbenchTransformer class."""

    def test_load(
        self,
        workbench_source: WorkbenchSource,
        workbench_data: WorkbenchData,
        workbench_config: WorkbenchSettings,
    ):

        result = workbench_source().load("./path/to/file", workbench_data, workbench_config)
        assert result is True
