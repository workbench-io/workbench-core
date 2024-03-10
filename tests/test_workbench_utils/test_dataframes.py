import pandas as pd

from workbench_utils.dataframes import generate_dataframe


def test_generate_dataframe():

    result = generate_dataframe()

    assert result is not None
    assert isinstance(result, pd.DataFrame)
    assert result.empty
