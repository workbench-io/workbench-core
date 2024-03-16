import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Path, status

from workbench_api.models.predict import PredictionInputModel, PredictionOutputModel
from workbench_api.utils import get_predicted_value
from workbench_components.common.common_configs import FILEPATH_MODELS_DEFAULT, REGEX_MODELS_DEFAULT
from workbench_train.common import Targets
from workbench_utils.export import get_filepath_from_directory, load_pipeline

router = APIRouter()

logger = logging.getLogger(__name__)

model = load_pipeline(get_filepath_from_directory(FILEPATH_MODELS_DEFAULT, REGEX_MODELS_DEFAULT))


@router.get("/predict/{target}", response_model=PredictionOutputModel, status_code=status.HTTP_200_OK)
async def make_prediction_target(
    prediction_input: Annotated[PredictionInputModel, Depends(PredictionInputModel)],
    target: Annotated[
        Targets,
        Path(
            ...,
            examples=[list(Targets)[0]],
            openapi_examples={
                "example1": {
                    "summary": "Predict compressive strength",
                    "value": Targets.COMPRESSIVE_STRENGTH,
                }
            },
        ),
    ],
):
    logger.debug(f"Making prediction for '{target}' with input: {prediction_input.model_dump()}")
    predicted_value = get_predicted_value(prediction_input, model)
    logger.debug(f"Predicted value for '{target}': {predicted_value:.2f}")

    return PredictionOutputModel(value=predicted_value, feature=target)
