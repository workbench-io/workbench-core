"""Test WorkbenchTransformer class."""

from workbench_core.workbench_config.workbench_config import WorkbenchConfig
from workbench_core.workbench_data.workbench_data import WorkbenchData
from workbench_core.workbench_source.workbench_source import WorkbenchSource


class TestWorkbenchTransformer:
    """Test WorkbenchTransformer class."""

    def test_load(
        self,
        workbench_source: WorkbenchSource,
        workbench_data: WorkbenchData,
        workbench_config: WorkbenchConfig,
    ):

        result = workbench_source().load("./path/to/file", workbench_data, workbench_config)
        assert result is True
