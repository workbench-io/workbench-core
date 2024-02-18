"""Test DataTransformer class."""

from workbench_core.data_transformer.data_transfomer import DataTransformer


class TestDataTransformer:
    """Test DataTransformer class."""

    def test_transform(self):

        class ConcreteDataTransformer(DataTransformer):
            def transform(self, data) -> bool:
                return True

        data_transformer = ConcreteDataTransformer()
        result = data_transformer.transform("data")
        assert result is True
