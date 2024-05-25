import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class SumTransformer(BaseEstimator, TransformerMixin):
    """
    Create feature with the sum of the values of selected columns
    """

    def __init__(self, variables: list[str], col_name: str = "total") -> None:

        if not isinstance(variables, list):
            raise ValueError("variables must be a list")

        self.variables = variables
        self.col_name = col_name

    def fit(self, X: pd.DataFrame, y=None):  # pylint: disable=unused-argument, invalid-name
        return self

    def transform(self, X: pd.DataFrame):  # pylint: disable=invalid-name
        X = X.copy()

        values = X[self.variables].sum(axis=1)

        X[self.col_name] = values

        return X


class ProductTransformer(BaseEstimator, TransformerMixin):
    """
    Create feature with the product of the values of selected columns
    """

    def __init__(self, variables: list[str], col_name: str = "product") -> None:

        if not isinstance(variables, list):
            raise ValueError("variables must be a list")

        self.variables = variables
        self.col_name = col_name

    def fit(self, X: pd.DataFrame, y=None):  # pylint: disable=unused-argument, invalid-name
        return self

    def transform(self, X: pd.DataFrame):  # pylint: disable=invalid-name
        X = X.copy()

        values = X[self.variables].prod(axis=1)

        X[self.col_name] = values

        return X


class PercentageTransformer(BaseEstimator, TransformerMixin):
    """
    Converts counts to percentages
    """

    def __init__(self, col_numerator: list[str], col_denominator: list[str] | None = None) -> None:

        if not isinstance(col_numerator, list):
            raise ValueError("col_numerator must be a list")

        self.col_numerator = col_numerator
        self.col_denominator = col_denominator

    def fit(self, X: pd.DataFrame, y=None):  # pylint: disable=unused-argument, invalid-name
        return self

    def transform(self, X: pd.DataFrame):  # pylint: disable=invalid-name
        X = X.copy()

        if isinstance(self.col_denominator, list):
            denomitator = X[self.col_denominator].sum(axis=1)
        else:
            denomitator = X[self.col_numerator].sum(axis=1)

        X[self.col_numerator] = X[self.col_numerator].div(denomitator, axis=0).mul(100)

        return X


class RatioTransformer(BaseEstimator, TransformerMixin):
    """
    Calculates ratios between one or more columns of a DataFrame
    """

    def __init__(self, col_numerator: list[str], col_denominator: list[str], col_name: str = "ratio") -> None:

        if not isinstance(col_numerator, list):
            raise ValueError("col_numerator must be a list")

        if not isinstance(col_denominator, list):
            raise ValueError("col_denominator must be a list")

        self.col_numerator = col_numerator
        self.col_denominator = col_denominator
        self.col_name = col_name

    def fit(self, X: pd.DataFrame, y=None):  # pylint: disable=unused-argument, invalid-name
        return self

    def transform(self, X: pd.DataFrame):  # pylint: disable=invalid-name

        X = X.copy()

        numerator = X[self.col_numerator].sum(axis=1)
        denomitator = X[self.col_denominator].sum(axis=1)

        X[self.col_name] = np.divide(numerator, denomitator)

        return X
