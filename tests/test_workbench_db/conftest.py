import shutil
from pathlib import Path
from typing import Generator

import pytest
from sqlalchemy import Engine, create_engine
from sqlmodel import Session

from tests.test_workbench_api import examples
from workbench_api.models.predict import PredictionOutputModel
from workbench_db.db import check_sql_model, create_db_and_tables
from workbench_db.main import Optimization, Prediction
from workbench_db.repositories.list_repository import ListRepository
from workbench_db.repositories.sql_repository import PredictionsRepository
from workbench_train.common import Targets

# pylint: disable=redefined-outer-name

DIR_RESOURCES = Path(__file__).parent.joinpath("resources")


@pytest.fixture(scope="function")
def prediction_example_1() -> Prediction:
    return Prediction(
        value=1.0,
        feature=Targets.COMPRESSIVE_STRENGTH,
        inputs="{'a': 1.0, 'b': 1.0}",
    )


@pytest.fixture(scope="function")
def prediction_example_2() -> Prediction:
    return Prediction(
        value=2.0,
        feature=Targets.COMPRESSIVE_STRENGTH,
        inputs="{'a': 2.0, 'b': 2.0}",
    )


@pytest.fixture(scope="function")
def prediction_example_3() -> Prediction:
    return Prediction(
        value=3.0,
        feature=Targets.COMPRESSIVE_STRENGTH,
        inputs="{'a': 3.0, 'b': 3.0}",
    )


@pytest.fixture(scope="function")
def prediction_example_4() -> Prediction:
    return Prediction(
        value=4.0,
        feature=Targets.COMPRESSIVE_STRENGTH,
        inputs="{'a': 4.0, 'b': 4.0}",
    )


@pytest.fixture(scope="function")
def prediction_example_5() -> Prediction:
    return Prediction(
        value=5.0,
        feature=Targets.COMPRESSIVE_STRENGTH,
        inputs="{'a': 5.0, 'b': 5.0}",
    )


@pytest.fixture(scope="session")
def dir_resources() -> Generator[Path, None, None]:

    dir_path = DIR_RESOURCES

    if not dir_path.exists():
        dir_path.mkdir(parents=True, exist_ok=True)

    yield dir_path

    shutil.rmtree(dir_path)


@pytest.fixture(scope="function")
def prediction_output_model_1() -> PredictionOutputModel:
    return PredictionOutputModel(
        id=1,
        value=1.0,
        feature=Targets.COMPRESSIVE_STRENGTH,
        inputs=examples.prediction_body_1,
    )


@pytest.fixture(scope="function")
def prediction_output_model_2() -> PredictionOutputModel:
    return PredictionOutputModel(
        id=2,
        value=2.0,
        feature=Targets.COMPRESSIVE_STRENGTH,
        inputs=examples.prediction_body_2,
    )


@pytest.fixture(scope="function")
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

    dir_test_db = dir_resources.joinpath("test.db")
    database_url = f"sqlite:///{dir_test_db}"

    return database_url


@pytest.fixture(scope="session")
def engine_testing(database_url: str) -> Generator[Engine, None, None]:
    engine: Engine = create_engine(database_url)
    yield engine
    engine.dispose()


@pytest.fixture
def db_testing_empty(engine_testing: Engine, database_url: str) -> Generator[Engine, None, None]:

    assert check_sql_model(Optimization)
    assert check_sql_model(Prediction)

    create_db_and_tables(engine_testing, database_url)


@pytest.fixture
def db_testing_with_data(
    engine_testing: Engine,
    database_url: str,
    prediction_example_1: Prediction,
    prediction_example_2: Prediction,
    prediction_example_3: Prediction,
) -> Generator[Engine, None, None]:

    assert check_sql_model(Optimization)
    assert check_sql_model(Prediction)

    create_db_and_tables(engine_testing, database_url)

    with Session(engine_testing) as session:

        session.add(prediction_example_1)
        session.add(prediction_example_2)
        session.add(prediction_example_3)
        session.commit()


@pytest.fixture
def predictions_repository_empty(
    engine_testing, db_testing_empty  # pylint: disable=unused-argument
) -> Generator[PredictionsRepository, None, None]:

    try:
        repo = PredictionsRepository(engine_testing)
        yield repo

    finally:
        engine_testing.dispose()


@pytest.fixture
def predictions_repository(
    engine_testing, db_testing_with_data  # pylint: disable=unused-argument
) -> Generator[PredictionsRepository, None, None]:

    try:
        repo = PredictionsRepository(engine_testing)
        yield repo

    finally:
        engine_testing.dispose()
