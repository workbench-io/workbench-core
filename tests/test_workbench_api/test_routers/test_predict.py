import pytest
from fastapi import status
from fastapi.testclient import TestClient

from workbench_train.common import Targets

# pylint: disable=line-too-long


@pytest.mark.parametrize(
    ["query_params", "expected_status_code"],
    [
        (
            "?water=8.33&coarse_aggregate=42.23&slag=0.0&cement=12.09&superplasticizer=0.0&fine_aggregate=37.35&fly_ash=0.0&age=28",  # noqa: E501
            status.HTTP_200_OK,
        ),  # noqa: E501
        (
            "?water=8.33&coarse_aggregate=42.23&slag=0.0&cement=12.09&superplasticizer=0.0&fine_aggregate=37.35&fly_ash=0.0",  # noqa: E501
            status.HTTP_200_OK,
        ),  # noqa: E501
        (
            "?water=8.33&coarse_aggregate=42.23&slag=0.0&cement=12.09&superplasticizer=0.0&fine_aggregate=37.35",
            status.HTTP_200_OK,
        ),
    ],
)
def test_make_prediction_target_returns_status_200(client: TestClient, query_params: str, expected_status_code: int):

    url = f"/predict/{Targets.COMPRESSIVE_STRENGTH}{query_params}"

    response = client.get(url)

    assert response.status_code == expected_status_code
    assert response.json().keys() == {"value", "feature", "version"}
    assert isinstance(response.json()["value"], float)
    assert isinstance(response.json()["feature"], str)
