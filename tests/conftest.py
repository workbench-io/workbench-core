from typing import Any

import pandas as pd
import pytest

from tests.test_workbench_api import examples


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
    return examples.prediction_body_1


@pytest.fixture(scope="session")
def concrete_composition_dict_1(concrete_composition_dict) -> dict:  # pylint: disable=redefined-outer-name
    return concrete_composition_dict


@pytest.fixture(scope="session")
def concrete_composition_dict_2() -> dict:
    return examples.prediction_body_2


@pytest.fixture(scope="session")
def concrete_composition_dict_3() -> dict:
    return examples.prediction_body_3


@pytest.fixture(scope="session")
def concrete_composition_df(concrete_composition_dict: dict) -> pd.DataFrame:  # pylint: disable=redefined-outer-name
    return pd.DataFrame(concrete_composition_dict, index=[0])
