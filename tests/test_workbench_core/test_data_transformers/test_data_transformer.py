from workbench_core.data_transformers.data_transfomer import DataTransformer


class TestDataTransformer:

    def test_transform(self):
        data_transformer = DataTransformer()
        result = data_transformer.transform("data")
        assert result is True
