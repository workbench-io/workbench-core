import asyncio
import os

import httpx
import pytest
from asgi_lifespan import LifespanManager
from fastapi.testclient import TestClient

from workbench_api.main import app
from workbench_components.workbench_logging.logging_configs import EnvState

os.environ["ENV_STATE"] = EnvState.TEST


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture
def client():
    yield TestClient(app)


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def async_client():
    async with LifespanManager(app):
        async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
            yield ac
