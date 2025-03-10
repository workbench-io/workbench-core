import httpx
import pytest
from fastapi import status


@pytest.mark.anyio
async def test_root(async_client: httpx.AsyncClient):

    response = await async_client.get("/")

    assert response.status_code == status.HTTP_200_OK
