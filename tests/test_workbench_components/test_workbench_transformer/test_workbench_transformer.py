"""Test WorkbenchTransformer class."""

from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings
from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer


class TestWorkbenchTransformer:
    """Test WorkbenchTransformer class."""

    def test___init__(self, workbench_transformer: WorkbenchTransformer):

        result = workbench_transformer().__init__()  # pylint: disable=unnecessary-dunder-call
        assert result is None

    def test_transform(
        self,
        workbench_transformer: WorkbenchTransformer,
        workbench_data: WorkbenchData,
        workbench_settings: WorkbenchSettings,
    ):

        result = workbench_transformer().transform(workbench_data, workbench_settings)
        assert result is True
