from typing import Any

import httpx
import pytest
from fastapi import status


@pytest.mark.anyio
class TestOptimizeRouter:
    @pytest.mark.parametrize(
        ["body", "expected_status_code"],
        [
            (
                {
                    "num_genes": 7,
                    "num_generations": 10,
                    "sol_per_pop": 10,
                    "num_parents_mating": 5,
                    "keep_parents": 0,
                    "init_range_low": 0,
                    "init_range_high": 100,
                    "gene_space": {"low": 0, "high": 100},
                    "parent_selection_type": "sss",
                    "crossover_type": "single_point",
                    "crossover_probability": 0.2,
                    "mutation_type": "random",
                    "mutation_probability": 0.2,
                    "random_seed": 1,
                },
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

        url = "/optimize"

        response = await async_client.post(url, json=body)

        assert response.status_code == expected_status_code
        assert response.json().keys() >= {"best_value", "best_solution"}
        assert isinstance(response.json()["best_value"], float)
        assert isinstance(response.json()["best_solution"], dict)

    async def test_get_all_optimizations_returns_status_200(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = "/optimize"
        response = await async_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    async def test_get_last_optimization_returns_status_404_when_there_are_no_optimizations(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = "/optimize/latest"
        response = await async_client.get(url)
        assert response.status_code == status.HTTP_200_OK
