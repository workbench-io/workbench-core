from fastapi import status
from fastapi.testclient import TestClient

from workbench_train.common import Targets


def test_make_prediction_target(client: TestClient):

    query_params = "?cement=14.28&slag=14.28&fly_ash=14.28&water=14.28&superplasticizer=14.28&coarse_aggregate=14.28&fine_aggregate=14.28&age=28"  # pylint: disable=line-too-long # noqa: E501
    url = f"/predict/{Targets.COMPRESSIVE_STRENGTH}{query_params}"

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
