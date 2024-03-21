from typing import Any

import httpx
import pytest
from fastapi import status

from tests.test_workbench_api import examples
from tests.test_workbench_api.conftest import create_optimization, get_test_optimizations_repository
from workbench_api.enums import RoutersPath

# pylint: disable=unused-argument


@pytest.fixture(autouse=True)
async def created_optimization(async_client: httpx.AsyncClient):
    await create_optimization(examples.optimization_body_1, async_client)
    await create_optimization(examples.optimization_body_2, async_client)
    await create_optimization(examples.optimization_body_3, async_client)


@pytest.mark.anyio
class TestOptimizeRouter:
    @pytest.mark.parametrize(
        ["body", "expected_status_code"],
        [
            (
                examples.optimization_body_4,
                status.HTTP_201_CREATED,
            ),
            (
                {},
                status.HTTP_201_CREATED,
            ),
        ],
        ids=["all_params", "no_params"],
    )
    async def test_run_optimization_returns_status_200(
        self,
        async_client: httpx.AsyncClient,
        body: dict[str, Any],
        expected_status_code: int,
    ):
        response = await async_client.post(RoutersPath.OPTIMIZE.value, json=body)

        assert response.status_code == expected_status_code
        assert response.json().keys() >= {"best_value", "best_solution"}
        assert isinstance(response.json()["best_value"], float)
        assert isinstance(response.json()["best_solution"], dict)
        assert len(get_test_optimizations_repository().get_all()) == 4

    async def test_get_optimization_with_id_returns_status_200(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = f"{RoutersPath.OPTIMIZE}/1"
        response = await async_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), dict)

    async def test_get_all_optimizations_returns_status_200(
        self,
        async_client: httpx.AsyncClient,
    ):
        response = await async_client.get(RoutersPath.OPTIMIZE.value)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), list)
        assert len(response.json()) == 3

    async def test_get_all_optimizations_returns_status_200_when_there_are_no_entries(
        self,
        async_client: httpx.AsyncClient,
    ):

        repo = get_test_optimizations_repository()
        repo._db.clear()  # pylint: disable=protected-access

        response = await async_client.get(RoutersPath.OPTIMIZE.value)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), list)
        assert len(response.json()) == 0

    async def test_get_last_optimization_returns_status_200(
        self,
        async_client: httpx.AsyncClient,
    ):
        response = await async_client.get(f"{RoutersPath.OPTIMIZE}/latest")

        assert response.status_code == status.HTTP_200_OK
        assert response.json().keys() >= {"best_value", "best_solution"}

    async def test_get_last_optimization_returns_status_404_when_there_are_no_optimizations(
        self,
        async_client: httpx.AsyncClient,
    ):

        repo = get_test_optimizations_repository()
        repo._db.clear()  # pylint: disable=protected-access

        response = await async_client.get(f"{RoutersPath.OPTIMIZE}/latest")

        assert response.status_code == status.HTTP_404_NOT_FOUND

    async def test_delete_optimization_return_204_for_existent_id(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = f"{RoutersPath.OPTIMIZE}/1"
        response = await async_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert len(get_test_optimizations_repository().get_all()) == 2

    async def test_delete_optimization_return_404_for_non_existent_id(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = f"{RoutersPath.OPTIMIZE}/999"
        response = await async_client.delete(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert len(get_test_optimizations_repository().get_all()) == 3

    async def test_update_optimization_return_201_for_existent_id(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = f"{RoutersPath.OPTIMIZE}/1"
        response = await async_client.put(url, json={"best_value": 42.0})

        assert response.status_code == status.HTTP_201_CREATED
        assert pytest.approx(response.json()["best_value"]) == 42.0

    async def test_update_optimization_return_404_for_non_existent_id(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = f"{RoutersPath.OPTIMIZE}/999"
        response = await async_client.put(url, json={})

        assert response.status_code == status.HTTP_404_NOT_FOUND
