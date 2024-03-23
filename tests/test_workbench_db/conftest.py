import shutil
from pathlib import Path
from typing import Generator

import pytest
from sqlalchemy import Engine, create_engine

from tests.test_workbench_api import examples
from workbench_api.models.predict import PredictionOutputModel
from workbench_db.db import check_sql_model, create_db_and_tables, get_database_engine
from workbench_db.list_repository import ListRepository
from workbench_db.main import Optimization, Prediction
from workbench_db.sql_repository import SQLRepository
from workbench_train.common import Targets

# pylint: disable=redefined-outer-name

DIR_RESOURCES = Path(__file__).parent.joinpath("resources")


@pytest.fixture(scope="session")
def dir_resources() -> Generator[Path, None, None]:

    dir_path = DIR_RESOURCES

    if not dir_path.exists():
        dir_path.mkdir(parents=True, exist_ok=True)

    yield dir_path
    shutil.rmtree(dir_path)


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


@pytest.fixture(scope="session")
def database_url(dir_resources: Path) -> str:
    # return "sqlite:///:memory:"
    return f"sqlite:///{dir_resources.joinpath('test.db')}"


@pytest.fixture(scope="session")
def engine_testing(database_url: str) -> Generator[Engine, None, None]:
    engine: Engine = create_engine(database_url)
    yield engine
    engine.dispose()


@pytest.fixture
def db_testing(engine_testing: Engine, database_url: str) -> Generator[Engine, None, None]:

    DIR_RESOURCES.mkdir(parents=True, exist_ok=True)
    dir_test_db = DIR_RESOURCES.joinpath("test.db")
    database_url = f"sqlite:///{dir_test_db}"

    assert check_sql_model(Optimization)
    assert check_sql_model(Prediction)

    create_db_and_tables(engine_testing, database_url)


@pytest.fixture
def sql_repository(
    engine_testing, db_testing, database_url  # pylint: disable=unused-argument
) -> Generator[SQLRepository, None, None]:

    try:

        repo = SQLRepository(get_database_engine, database_url)
        yield repo

    finally:
        engine_testing.dispose()
