from typing import Any

import pandas as pd
import pytest


class FakeEstimator:

    def __init__(self) -> None:
        pass

    def predict(self, x: Any):  # pylint: disable=unused-argument
        return [[42.0]]


@pytest.fixture(scope="session")
def fake_estimator() -> FakeEstimator:
    return FakeEstimator()


@pytest.fixture(scope="session")
def concrete_composition_dict() -> dict:
    return {
        "water": 8.33,
        "coarse_aggregate": 42.23,
        "slag": 0.0,
        "cement": 12.09,
        "superplasticizer": 0.0,
        "fine_aggregate": 37.35,
        "fly_ash": 0.0,
        "age": 28,
    }


@pytest.fixture(scope="session")
def concrete_composition_df(concrete_composition_dict: dict) -> pd.DataFrame:  # pylint: disable=redefined-outer-name
    return pd.DataFrame(concrete_composition_dict, index=[0])
