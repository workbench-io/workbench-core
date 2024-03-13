import pytest
from fastapi import status
from fastapi.testclient import TestClient

from workbench_train.common import Targets

# pylint: disable=line-too-long


@pytest.mark.parametrize(
    ["query_params", "expected_status_code"],
    [
        (
            "?cement=14.2&slag=14.2&fly_ash=14.2&water=14.2&superplasticizer=14.2&coarse_aggregate=14.2&fine_aggregate=14.2&age=28",  # noqa: E501
            status.HTTP_200_OK,
        ),  # noqa: E501
        (
            "?cement=14.2&slag=14.2&fly_ash=14.2&water=14.2&superplasticizer=14.2&coarse_aggregate=14.2&fine_aggregate=14.2",  # noqa: E501
            status.HTTP_200_OK,
        ),  # noqa: E501
        ("?cement=14.2&slag=14.2&fly_ash=14.2&water=14.2", status.HTTP_200_OK),
        ("", status.HTTP_200_OK),
    ],
)
def test_make_prediction_target_returns_status_200(client: TestClient, query_params: str, expected_status_code: int):

    url = f"/predict/{Targets.COMPRESSIVE_STRENGTH}{query_params}"

    response = client.get(url)

    assert response.status_code == expected_status_code
    assert response.json().keys() == {"value", "feature", "version"}
    assert isinstance(response.json()["value"], float)
    assert isinstance(response.json()["feature"], str)
