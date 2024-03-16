from typing import Any

import pytest
from fastapi import status
from fastapi.testclient import TestClient


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
            status.HTTP_200_OK,
        ),
        (
            {},
            status.HTTP_200_OK,
        ),
    ],
    ids=["all_params", "no_params"],
)
def test_optimize_router_returns_status_200(
    client: TestClient,
    body: dict[str, Any],
    expected_status_code: int,
):

    url = "/optimize/"

    response = client.post(url, json=body)

    assert response.status_code == expected_status_code
    assert response.json().keys() == {"best_value", "best_solution"}
    assert isinstance(response.json()["best_value"], float)
    assert isinstance(response.json()["best_solution"], dict)
