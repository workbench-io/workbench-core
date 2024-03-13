import logging
import pathlib

from fastapi import APIRouter, Depends, Path, status

from workbench_api.models import PredictionInputModel, PredictionOutputModel
from workbench_api.utils import get_predicted_value
from workbench_train.common import Targets
from workbench_utils.export import get_filepath_from_directory, load_pipeline

DIR_MODELS = pathlib.Path("./output/models")
DIR_MODELS_PATTERN = "*.pkl"

router = APIRouter()

logger = logging.getLogger(__name__)

model = load_pipeline(get_filepath_from_directory(DIR_MODELS, DIR_MODELS_PATTERN))


@router.get("/predict/{target}", response_model=PredictionOutputModel, status_code=status.HTTP_200_OK)
async def make_prediction_target(
    prediction_input: PredictionInputModel = Depends(),
    target: Targets = Path(..., example=list(Targets)[0]),
):
    logger.debug(f"Making prediction for '{target}' with input: {prediction_input.model_dump()}")
    predicted_value = get_predicted_value(prediction_input, model)
    logger.debug(f"Predicted value for '{target}': {predicted_value:.2f}")

    return PredictionOutputModel(value=predicted_value, feature=target)
