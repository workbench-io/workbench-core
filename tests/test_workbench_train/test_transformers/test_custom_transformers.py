import pandas as pd

from workbench_train.transformers.custom_transformers import ProductTransformer, RatioTransformer, SumTransformer


def test_sum_transformer(dataframe: pd.DataFrame):
    transformer = SumTransformer(variables=["a", "b"], col_name="output")
    transformer.fit(dataframe)
    result = transformer.transform(dataframe)

    assert isinstance(result, pd.DataFrame)
    assert (result["output"] == pd.Series([5, 7, 9])).all()


def test_product_transformer(dataframe: pd.DataFrame):
    transformer = ProductTransformer(variables=["a", "b"], col_name="output")
    transformer.fit(dataframe)
    result = transformer.transform(dataframe)

    assert isinstance(result, pd.DataFrame)
    assert (result["output"] == pd.Series([4, 10, 18])).all()


def test_ratio_transformer(dataframe: pd.DataFrame):
    transformer = RatioTransformer(col_numerator=["a", "b"], col_denominator=["d"], col_name="output")
    transformer.fit(dataframe)
    result = transformer.transform(dataframe)

    assert isinstance(result, pd.DataFrame)
    assert (result["output"] == pd.Series([0.5, 0.7, 0.9])).all()
