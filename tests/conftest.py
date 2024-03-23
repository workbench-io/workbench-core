import shutil
from pathlib import Path
from typing import Any, Generator, Literal

import pandas as pd
import pytest
from pydantic_settings import BaseSettings

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


@pytest.fixture
def test_workbench_configs(tmp_path: Path) -> Generator[BaseSettings, None, None]:

    class TestWorkbenchConfigs(BaseSettings):

        env_state: Literal["dev", "test", "prod"] = "test"
        logs_filepath: Path = tmp_path.joinpath("logs")
        models_filepath: Path = tmp_path.joinpath("models")
        database_url: str = "sqlite:///:memory:"
        models_regex: str = "*.pkl"
        encoding: str = "utf-8"

    configs = TestWorkbenchConfigs()
    yield configs

    shutil.rmtree(tmp_path)
