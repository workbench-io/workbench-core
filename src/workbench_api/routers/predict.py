import logging
from typing import Annotated

from fastapi import APIRouter, Body, HTTPException, Path, Response, status

from workbench_api.data import db
from workbench_api.models.predict import PredictionInputModel, PredictionOutputModel
from workbench_api.utils import get_db_entry_by_id, get_id, get_predicted_value
from workbench_components.common.common_configs import FILEPATH_MODELS_DEFAULT, REGEX_MODELS_DEFAULT
from workbench_train.common import Targets
from workbench_utils.export import get_filepath_from_directory, load_pipeline

router = APIRouter()

logger = logging.getLogger(__name__)

model = load_pipeline(get_filepath_from_directory(FILEPATH_MODELS_DEFAULT, REGEX_MODELS_DEFAULT))


@router.post("/predict/{target}", response_model=PredictionOutputModel, status_code=status.HTTP_201_CREATED)
async def make_prediction_target(
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
    prediction_input: Annotated[
        PredictionInputModel,
        Body(
            ...,
            examples=[
                {
                    "water": 8.33,
                    "coarse_aggregate": 42.23,
                    "slag": 0.0,
                    "cement": 12.09,
                    "superplasticizer": 0.0,
                    "fine_aggregate": 37.35,
                    "fly_ash": 0.0,
                    "age": 28,
                }
            ],
        ),
    ],
):

    logger.debug(f"Making prediction for '{target}' with input: {prediction_input.model_dump()}")
    predicted_value = get_predicted_value(prediction_input, model)
    logger.debug(f"Predicted value for '{target}': {predicted_value:.2f}")

    db_id = get_id(db.predictions)

    result = PredictionOutputModel(
        id=db_id,
        value=predicted_value,
        feature=target,
        prediction_input=prediction_input,
    )

    db.predictions.append(result)

    return result


@router.get("/predict/{target}", status_code=status.HTTP_200_OK)
async def get_all_predictions() -> list[PredictionOutputModel]:
    return db.predictions


@router.get("/predict/{target}/latest", status_code=status.HTTP_200_OK, response_model=PredictionOutputModel)
async def get_last_prediction() -> PredictionOutputModel:

    try:
        result = db.predictions[-1]
        return result
    except IndexError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No previous entry in database was found",
        ) from error


@router.get("/predict/{target}/{db_id}", status_code=status.HTTP_200_OK, response_model=PredictionOutputModel)
async def get_prediction(db_id: int) -> PredictionOutputModel:
    result = get_db_entry_by_id(db.predictions, db_id)

    if result:
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {db_id} not found",
    )


@router.delete("/predict/{target}/{db_id}", response_model=PredictionOutputModel)
async def delete_prediction(db_id: int) -> PredictionOutputModel:

    try:
        db.predictions.pop(db_id - 1)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except IndexError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {db_id} not found",
        ) from error
