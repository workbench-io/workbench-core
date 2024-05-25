import pandas as pd
import pytest

from workbench_train.transformers.custom_transformers import (
    PercentageTransformer,
    ProductTransformer,
    RatioTransformer,
    SumTransformer,
)


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


def test_percentage_transformer(dataframe: pd.DataFrame):
    transformer = PercentageTransformer(col_numerator=["a", "b"])
    transformer.fit(dataframe)
    result = transformer.transform(dataframe)

    assert isinstance(result, pd.DataFrame)
    assert result["a"].dtype == float
    assert result["b"].dtype == float
    assert pytest.approx(result.loc[0, "a"]) == 20.0
    assert pytest.approx(result.loc[0, "b"]) == 80.0
