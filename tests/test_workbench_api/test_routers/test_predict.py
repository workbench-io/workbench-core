import httpx
import pytest
from fastapi import status

from tests.test_workbench_api import examples
from tests.test_workbench_api.conftest import create_prediction, get_test_predictions_repository
from workbench_api.enums import RoutersPath
from workbench_train.common import Targets

# pylint: disable=unused-argument


@pytest.fixture(autouse=True)
async def created_predictions(async_client: httpx.AsyncClient):
    await create_prediction(examples.prediction_body_1, async_client)
    await create_prediction(examples.prediction_body_2, async_client)
    await create_prediction(examples.prediction_body_3, async_client)


@pytest.mark.anyio
class TestPredictRouter:

    @pytest.mark.parametrize(
        ["body", "expected_status_code"],
        [
            (
                examples.prediction_body_4,
                status.HTTP_201_CREATED,
            ),
            (
                examples.prediction_body_no_age_4,
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

        url = f"{RoutersPath.PREDICT}/{Targets.COMPRESSIVE_STRENGTH}"

        response = await async_client.post(url, json=body)

        assert response.status_code == expected_status_code
        assert response.json().keys() >= {"value", "feature", "version"}
        assert isinstance(response.json()["value"], float)
        assert isinstance(response.json()["feature"], str)
        assert len(get_test_predictions_repository().get_all()) == 4

    async def test_get_prediction_with_id_returns_status_200(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = f"{RoutersPath.PREDICT}/{Targets.COMPRESSIVE_STRENGTH}/1"
        response = await async_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), dict)
        assert response.json().keys() >= {"value", "feature", "version"}

    async def test_get_prediction_with_id_returns_status_404_for_non_existent_id(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = f"{RoutersPath.PREDICT}/{Targets.COMPRESSIVE_STRENGTH}/999"
        response = await async_client.get(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"detail": "Item with ID 999 not found"}

    async def test_get_all_predictions_returns_status_200(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = f"{RoutersPath.PREDICT}/{Targets.COMPRESSIVE_STRENGTH}"
        response = await async_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), list)
        assert len(response.json()) == 3

    async def test_get_all_optimizations_returns_status_200_when_there_are_no_entries(
        self,
        async_client: httpx.AsyncClient,
    ):

        repo = get_test_predictions_repository()
        repo._db.clear()  # pylint: disable=protected-access

        response = await async_client.get(RoutersPath.OPTIMIZE.value)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), list)
        assert len(response.json()) == 0
        assert response.json() == []

    async def test_get_last_prediction_returns_status_200(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = f"{RoutersPath.PREDICT}/{Targets.COMPRESSIVE_STRENGTH}/latest"
        response = await async_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json().keys() >= {"value", "feature", "version"}

    async def test_delete_prediction_return_204_for_existent_id(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = f"{RoutersPath.PREDICT}/{Targets.COMPRESSIVE_STRENGTH}/1"
        response = await async_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert len(get_test_predictions_repository().get_all()) == 2

    async def test_delete_prediction_return_404_for_non_existent_id(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = f"{RoutersPath.PREDICT}/{Targets.COMPRESSIVE_STRENGTH}/999"
        response = await async_client.delete(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert len(get_test_predictions_repository().get_all()) == 3
        assert response.json() == {"detail": "Item with ID 999 not found"}

    async def test_update_prediction_return_201_for_existent_id(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = f"{RoutersPath.PREDICT}/{Targets.COMPRESSIVE_STRENGTH}/1"
        response = await async_client.put(url, json={"version": "1.0.0"})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["version"] == "1.0.0"

    async def test_update_prediction_return_404_for_non_existent_id(
        self,
        async_client: httpx.AsyncClient,
    ):

        url = f"{RoutersPath.PREDICT}/{Targets.COMPRESSIVE_STRENGTH}/999"
        response = await async_client.put(url, json={})

        assert response.status_code == status.HTTP_404_NOT_FOUND
