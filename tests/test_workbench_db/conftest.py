import shutil
from typing import Generator

import pytest
from anyio import Path
from sqlalchemy import Engine, create_engine
from sqlmodel import SQLModel

from tests.test_workbench_api import examples
from workbench_api.models.predict import PredictionOutputModel
from workbench_db.db import create_db_and_tables, get_database_engine
from workbench_db.list_repository import ListRepository
from workbench_db.main import Optimization, Prediction
from workbench_db.sql_repository import SQLRepository
from workbench_train.common import Targets

# pylint: disable=redefined-outer-name


@pytest.fixture(scope="session")
def dir_resources() -> Generator[Path, None, None]:

    dir_resources = Path(__file__).parent.joinpath("resources")
    yield dir_resources
    shutil.rmtree(dir_resources)


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


@pytest.fixture
def database_url(dir_resources: Path) -> str:
    # return "sqlite:///:memory:"
    return f"sqlite:///{dir_resources.joinpath('test.db')}"


@pytest.fixture
def engine_testing(database_url: str) -> Generator[Engine, None, None]:
    engine: Engine = create_engine(database_url)
    yield engine
    engine.dispose()


def db_testing(engine_testing: Engine, database_url: str) -> Generator[Engine, None, None]:

    assert isinstance(Optimization, SQLModel)
    assert isinstance(Prediction, SQLModel)

    create_db_and_tables(engine_testing, database_url)


@pytest.fixture
def sql_repository(database_url: str) -> Generator[SQLRepository, None, None]:
    repo = SQLRepository(get_database_engine, database_url)
    yield repo
