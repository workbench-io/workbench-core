import os
from typing import AsyncGenerator, Generator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from workbench_api.main import app
from workbench_components.workbench_logging.logging_configs import EnvState

os.environ["ENV_STATE"] = EnvState.TEST


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture
def client() -> Generator:
    yield TestClient(app)


@pytest.fixture()
async def async_client(client) -> AsyncGenerator:  # pylint: disable=redefined-outer-name
    async with AsyncClient(app=app, base_url=client.base_url) as ac:
        yield ac
