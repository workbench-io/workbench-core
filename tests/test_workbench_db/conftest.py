from typing import Generator

import pytest

from tests.test_workbench_api import examples
from workbench_api.models.predict import PredictionOutputModel
from workbench_db.repository import ListRepository
from workbench_train.common import Targets

# pylint: disable=redefined-outer-name


@pytest.fixture(scope="session")
def prediction_output_model_1() -> PredictionOutputModel:
    return PredictionOutputModel(
        id=1,
        value=1.0,
        feature=Targets.COMPRESSIVE_STRENGTH,
        inputs=examples.prediction_body_1,
    )


@pytest.fixture(scope="session")
def prediction_output_model_2() -> PredictionOutputModel:
    return PredictionOutputModel(
        id=2,
        value=2.0,
        feature=Targets.COMPRESSIVE_STRENGTH,
        inputs=examples.prediction_body_2,
    )


@pytest.fixture(scope="session")
def prediction_output_model_3() -> PredictionOutputModel:
    return PredictionOutputModel(
        id=3,
        value=3.0,
        feature=Targets.COMPRESSIVE_STRENGTH,
        inputs=examples.prediction_body_3,
    )


@pytest.fixture
def list_repository(prediction_output_model_1, prediction_output_model_2, prediction_output_model_3) -> Generator:
    repo = ListRepository()
    repo._db = [  # pylint: disable=protected-access
        prediction_output_model_1,
        prediction_output_model_2,
        prediction_output_model_3,
    ]

    yield repo


@pytest.fixture
def list_repository_empty() -> Generator:
    repo = ListRepository()

    yield repo
