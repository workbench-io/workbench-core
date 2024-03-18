import httpx
import pytest
from fastapi import status

from workbench_train.common import Targets


@pytest.mark.anyio
class TestPredictRouter:

    @pytest.mark.parametrize(
        ["body", "expected_status_code"],
        [
            (
                {
                    "cement": 12.09,
                    "slag": 0.0,
                    "fly_ash": 0.0,
                    "water": 7.33,
                    "superplasticizer": 0.0,
                    "coarse_aggregate": 43.23,
                    "fine_aggregate": 37.35,
                    "age": 28,
                },
                status.HTTP_201_CREATED,
            ),
            (
                {
                    "cement": 12.09,
                    "slag": 0.0,
                    "fly_ash": 0.0,
                    "water": 7.33,
                    "superplasticizer": 0.0,
                    "coarse_aggregate": 43.23,
                    "fine_aggregate": 37.35,
                },
                status.HTTP_201_CREATED,
            ),
        ],
        ids=["all_fields", "no_age"],
    )
    async def test_make_prediction_target_returns_status_200(
        self,
        async_client: httpx.AsyncClient,
        body: str,
        expected_status_code: int,
    ):

        url = f"/predict/{Targets.COMPRESSIVE_STRENGTH}"

        response = await async_client.post(url, json=body)

        assert response.status_code == expected_status_code
        assert response.json().keys() >= {"value", "feature", "version"}
        assert isinstance(response.json()["value"], float)
        assert isinstance(response.json()["feature"], str)

    async def test_get_all_predictions_returns_status_200(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = f"/predict/{Targets.COMPRESSIVE_STRENGTH}"
        response = await async_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    async def test_get_last_prediction_returns_status_200(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = f"/predict/{Targets.COMPRESSIVE_STRENGTH}/latest"
        response = await async_client.get(url)
        assert response.status_code == status.HTTP_200_OK
