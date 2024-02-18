"""Test WorkbenchTransformer class."""

from workbench_core.workbench_data.workbench_data import WorkbenchData
from workbench_core.workbench_transformer.workbench_transformer import WorkbenchTransformer


class TestWorkbenchTransformer:
    """Test WorkbenchTransformer class."""

    def test___init__(self, workbench_transformer: WorkbenchTransformer):

        result = workbench_transformer().__init__()  # pylint: disable=unnecessary-dunder-call
        assert result is None

    def test_transform(self, workbench_transformer: WorkbenchTransformer, workbench_data: WorkbenchData):

        result = workbench_transformer().transform(workbench_data)
        assert result is True
