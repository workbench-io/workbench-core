"""Test WorkbenchTransformer class."""

from workbench_core.workbench_transformer.workbench_transformer import WorkbenchTransformer


class TestWorkbenchTransformer:
    """Test WorkbenchTransformer class."""

    def test_transform(self):

        class ConcreteWorkbenchTransformer(WorkbenchTransformer):
            def transform(self, data) -> bool:
                return True

        data_transformer = ConcreteWorkbenchTransformer()
        result = data_transformer.transform("data")
        assert result is True
