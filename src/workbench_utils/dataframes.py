import pandas as pd


def generate_dataframe() -> pd.DataFrame:
    """
    Generates an empty pandas DataFrame.

    Returns:
        pd.DataFrame: An empty DataFrame.
    """
    return pd.DataFrame()


def replace_string_in_column_pattern(
    df: pd.DataFrame,
    column: str,
    pattern: str,
    replacement: str,
) -> pd.DataFrame:
    df[column] = df[column].str.replace(pattern, replacement)
    return df


def replace_string_in_column_with_nan(
    df: pd.DataFrame,
    column: str,
    string_value: str,
) -> pd.DataFrame:
    df[column] = df[column].replace(string_value, pd.NA)
    return df


def replace_values_in_column_to_boolean(
    df: pd.DataFrame,
    column: str,
    yes_values: list[str],
) -> pd.DataFrame:
    df[column] = df[column].apply(lambda x: 1 if x in yes_values else 0).astype(bool)
    return df
