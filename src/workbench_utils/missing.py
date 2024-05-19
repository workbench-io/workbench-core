import pandas as pd


def get_columns_with_missing_values(df: pd.DataFrame) -> list[str]:
    """
    Get columns with missing values.

    Args:
        df (pd.DataFrame): A pandas DataFrame.

    Returns:
        list[str]: A list of columns with missing values.

    Example:
        >>> df = pd.DataFrame({"a": [1, 2, None], "b": [None, 2, 3]})
        >>> get_columns_with_missing_values(df)
        ['a', 'b']
    """
    return df.columns[df.isnull().any()].tolist()
