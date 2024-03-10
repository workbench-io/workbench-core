from enum import StrEnum, auto

import pandas as pd


class WorkbenchSteps(StrEnum):
    """
    Steps in Workbench.

    - PROCESS: Loading and processing data.
    - TRAIN: Training the model.
    """

    PROCESS = auto()
    TRAIN = auto()
    OPTIMIZE = auto()


def convert_to_percentage(values: list[float | int]) -> list[float]:
    """
    Converts a list of values to percentages.

    Args:
        values (list[float | int]): A list of numeric values.

    Returns:
        list[float]: A list of percentages corresponding to the input values.

    Raises:
        ZeroDivisionError: If the sum of the values is zero.

    Example:
        >>> convert_to_percentage([10, 20, 30])
        [16.666666666666664, 33.33333333333333, 50.0]
    """
    total = sum(values)
    percentages = [value / total * 100 for value in values]
    return percentages


def create_composition_dataframe_from_percentages_list(
    values: list[float | int],
    composition_features: tuple[str] | list[str] = (
        "superplasticizer",
        "cement",
        "slag",
        "fine_aggregate",
        "coarse_aggregate",
        "fly_ash",
        "water",
    ),
    age: int = 28,
    age_feature: str = "age",
) -> pd.DataFrame:
    """
    Create a composition dataframe from a list of percentages.

    Args:
        values (list[float | int]): A list of values representing the percentages.
        composition_features (list[str], optional): A list of composition features. \
        Defaults to `["superplasticizer", "cement", "slag", "fine_aggregate", "coarse_aggregate", "fly_ash", "water"]`.
        age (int, optional): The age of the composition. Defaults to `28`.
        age_feature (str, optional): The name of the age feature. Defaults to `"age"`.

    Returns:
        pd.DataFrame: A dataframe representing the composition with percentages and age.

    """
    composition = pd.DataFrame([values], columns=composition_features)
    composition[age_feature] = age

    return composition
