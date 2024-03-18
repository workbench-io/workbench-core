from typing import Any

import httpx
import pytest
from fastapi import status

from tests.test_workbench_api.examples import optimization_body_1


@pytest.mark.anyio
class TestOptimizeRouter:
    @pytest.mark.parametrize(
        ["body", "expected_status_code"],
        [
            (
                optimization_body_1,
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
        response = await async_client.post("/optimize", json=body)

        assert response.status_code == expected_status_code
        assert response.json().keys() >= {"best_value", "best_solution"}
        assert isinstance(response.json()["best_value"], float)
        assert isinstance(response.json()["best_solution"], dict)

    async def test_get_all_optimizations_returns_status_200(
        self,
        async_client: httpx.AsyncClient,
    ):
        response = await async_client.get("/optimize")

        assert response.status_code == status.HTTP_200_OK

    async def test_get_last_optimization_returns_status_404_when_there_are_no_optimizations(
        self,
        async_client: httpx.AsyncClient,
    ):
        response = await async_client.get("/optimize/latest")

        assert response.status_code == status.HTTP_200_OK
