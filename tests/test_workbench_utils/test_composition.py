import pandas as pd
import pytest

from workbench_utils.composition import convert_to_percentage, create_composition_dataframe_from_percentages_list


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1], [100.0]),
        ([50, 50], [50.0, 50.0]),
        ([100] * 4, [25.0] * 4),
        ([0, 0, 1], [0.0, 0.0, 100.0]),
    ],
)
def test_convert_to_percentage(values: list[int | float], expected: list[float]):

    result = convert_to_percentage(values)
    assert result == expected


def test_create_composition_dataframe_from_percentages_list():

    values = [10, 20, 30, 0, 0, 0, 0]
    composition = create_composition_dataframe_from_percentages_list(values)

    assert isinstance(composition, pd.DataFrame)
    assert composition.shape == (1, 8)
    assert composition.columns.tolist() == [
        "superplasticizer",
        "cement",
        "slag",
        "fine_aggregate",
        "coarse_aggregate",
        "fly_ash",
        "water",
        "age",
    ]
    assert composition.values.tolist() == [[10, 20, 30, 0, 0, 0, 0, 28]]
