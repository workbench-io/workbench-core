import asyncio
import os
from typing import AsyncGenerator, Generator

import httpx
import pytest
from asgi_lifespan import LifespanManager
from fastapi.testclient import TestClient

from workbench_api.enums import RoutersPath
from workbench_api.main import app
from workbench_components.workbench_logging.logging_configs import EnvState
from workbench_db.repositories.list_repository import (
    ListRepository,
    get_optimizations_repository,
    get_predictions_repository,
)
from workbench_train.common import Targets

os.environ["ENV_STATE"] = EnvState.TEST

# pylint: disable=redefined-outer-name
database_test_predictions = []
database_test_optimizations = []


def get_database_test_predictions():
    return database_test_predictions


def get_database_test_optimizations():
    return database_test_optimizations


def get_test_predictions_repository() -> ListRepository:
    return ListRepository(get_database_test_predictions)


def get_test_optimizations_repository() -> ListRepository:
    return ListRepository(get_database_test_optimizations)


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture
def client() -> Generator:
    app.dependency_overrides[get_predictions_repository] = get_test_predictions_repository
    app.dependency_overrides[get_optimizations_repository] = get_test_optimizations_repository

    yield TestClient(app)

    database_test_predictions.clear()
    database_test_optimizations.clear()


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def async_client() -> AsyncGenerator:
    app.dependency_overrides[get_predictions_repository] = get_test_predictions_repository
    app.dependency_overrides[get_optimizations_repository] = get_test_optimizations_repository

    async with LifespanManager(app):
        async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
            yield ac

    database_test_predictions.clear()
    database_test_optimizations.clear()


async def create_prediction(body: dict, async_client: httpx.AsyncClient) -> httpx.Response:
    url = f"{RoutersPath.PREDICT}/{Targets.COMPRESSIVE_STRENGTH}"
    response = await async_client.post(url, json=body)
    return response.json()


async def create_optimization(body: dict, async_client: httpx.AsyncClient) -> httpx.Response:
    url = RoutersPath.OPTIMIZE
    response = await async_client.post(url, json=body)
    return response.json()
