import asyncio
import os
from typing import AsyncGenerator, Generator

import httpx
import pytest
from asgi_lifespan import LifespanManager
from fastapi.testclient import TestClient

from tests.test_workbench_api import examples
from workbench_api.data.repository import ListRepository
from workbench_api.main import app
from workbench_api.models.optimize import OptimizeOutputModel
from workbench_api.models.predict import PredictionOutputModel
from workbench_api.utils import create_list
from workbench_components.workbench_logging.logging_configs import EnvState
from workbench_train.common import Targets

os.environ["ENV_STATE"] = EnvState.TEST

# pylint: disable=redefined-outer-name


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(autouse=True)
async def db() -> AsyncGenerator:
    class DB:
        predictions: list[PredictionOutputModel] = create_list()
        optimizations: list[OptimizeOutputModel] = create_list()

    yield DB()


@pytest.fixture
def client() -> Generator:
    yield TestClient(app)


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def async_client() -> AsyncGenerator:
    async with LifespanManager(app):
        async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
            yield ac


async def create_prediction(body: dict, async_client: httpx.AsyncClient) -> httpx.Response:
    url = f"/predict/{Targets.COMPRESSIVE_STRENGTH}"
    response = await async_client.post(url, json=body)
    return response.json()


async def create_optimization(body: dict, async_client: httpx.AsyncClient) -> httpx.Response:
    url = "/optimize"
    response = await async_client.post(url, json=body)
    return response.json()


@pytest.fixture
async def created_prediction(async_client: httpx.AsyncClient):
    return await create_prediction(examples.prediction_body_1, async_client)


@pytest.fixture
async def created_optimization(async_client: httpx.AsyncClient):
    return await create_optimization(examples.optimization_body_1, async_client)


@pytest.fixture(scope="session")
def prediction_output_model_1() -> PredictionOutputModel:
    return PredictionOutputModel(
        id=1,
        value=1.0,
        feature=Targets.COMPRESSIVE_STRENGTH,
        prediction_input=examples.prediction_body_1,
    )


@pytest.fixture(scope="session")
def prediction_output_model_2() -> PredictionOutputModel:
    return PredictionOutputModel(
        id=2,
        value=2.0,
        feature=Targets.COMPRESSIVE_STRENGTH,
        prediction_input=examples.prediction_body_2,
    )


@pytest.fixture(scope="session")
def prediction_output_model_3() -> PredictionOutputModel:
    return PredictionOutputModel(
        id=3,
        value=3.0,
        feature=Targets.COMPRESSIVE_STRENGTH,
        prediction_input=examples.prediction_body_3,
    )


@pytest.fixture(scope="session")
def prediction_output_model_42() -> PredictionOutputModel:
    return PredictionOutputModel(
        id=1,
        value=42.0,
        feature=Targets.COMPRESSIVE_STRENGTH,
        prediction_input=examples.prediction_body_1,
    )


@pytest.fixture
def list_repository(prediction_output_model_1, prediction_output_model_2, prediction_output_model_3) -> Generator:
    list_repository = ListRepository()
    list_repository._db = [  # pylint: disable=protected-access
        prediction_output_model_1,
        prediction_output_model_2,
        prediction_output_model_3,
    ]

    yield list_repository


@pytest.fixture
def list_repository_empty() -> Generator:
    list_repository = ListRepository()

    yield list_repository
