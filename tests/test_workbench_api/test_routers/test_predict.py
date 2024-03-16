import pytest
from fastapi import status
from fastapi.testclient import TestClient

from workbench_train.common import Targets

# pylint: disable=line-too-long


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
            status.HTTP_200_OK,
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
            status.HTTP_200_OK,
        ),
    ],
    ids=["all_fields", "no_age"],
)
def test_make_prediction_target_returns_status_200(client: TestClient, body: str, expected_status_code: int):

    url = f"/predict/{Targets.COMPRESSIVE_STRENGTH}"

    response = client.post(url, json=body)

    assert response.status_code == expected_status_code
    assert response.json().keys() >= {"value", "feature", "version"}
    assert isinstance(response.json()["value"], float)
    assert isinstance(response.json()["feature"], str)
