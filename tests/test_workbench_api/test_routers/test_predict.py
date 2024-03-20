import httpx
import pytest
from fastapi import status

from tests.test_workbench_api import examples
from tests.test_workbench_api.conftest import create_prediction
from workbench_train.common import Targets

# pylint: disable=unused-argument


@pytest.fixture(autouse=True)
async def created_prediction(async_client: httpx.AsyncClient):
    return await create_prediction(examples.prediction_body_1, async_client)


@pytest.mark.anyio
class TestPredictRouter:

    @pytest.mark.parametrize(
        ["body", "expected_status_code"],
        [
            (
                examples.prediction_body_1,
                status.HTTP_201_CREATED,
            ),
            (
                examples.prediction_body_no_age_1,
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
        assert isinstance(response.json(), list)
        assert len(response.json()) == 1

    async def test_get_last_prediction_returns_status_200(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = f"/predict/{Targets.COMPRESSIVE_STRENGTH}/latest"
        response = await async_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json().keys() >= {"value", "feature", "version"}
