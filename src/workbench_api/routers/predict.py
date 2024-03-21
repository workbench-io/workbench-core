import logging
from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, Path, Response, status

from workbench_api.data.repository import ListRepository, ListRepositoryError, get_predictions_repository
from workbench_api.enums import RoutersPath
from workbench_api.models.predict import PredictionInputModel, PredictionOutputModel, PredictionUpdateModel
from workbench_api.utils import get_predicted_value
from workbench_components.common.common_configs import FILEPATH_MODELS_DEFAULT, REGEX_MODELS_DEFAULT
from workbench_train.common import Targets
from workbench_utils.export import get_filepath_from_directory, load_pipeline

router = APIRouter(prefix=RoutersPath.PREDICT.value)

logger = logging.getLogger(__name__)

model = load_pipeline(get_filepath_from_directory(FILEPATH_MODELS_DEFAULT, REGEX_MODELS_DEFAULT))


@router.post("/{target}", response_model=PredictionOutputModel, status_code=status.HTTP_201_CREATED)
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
    repo: Annotated[ListRepository, Depends(get_predictions_repository)],
):

    logger.debug(f"Making prediction for '{target}' with input: {prediction_input.model_dump()}")
    predicted_value = get_predicted_value(prediction_input, model)
    logger.debug(f"Predicted value for '{target}': {predicted_value:.2f}")

    db_id = repo.get_next_id()

    result = PredictionOutputModel(
        id=db_id,
        value=predicted_value,
        feature=target,
        prediction_input=prediction_input,
    )

    repo.add(db_id, result)

    return result


@router.get("/{target}", status_code=status.HTTP_200_OK)
async def get_all_predictions(
    repo: Annotated[ListRepository, Depends(get_predictions_repository)],
) -> list[PredictionOutputModel]:
    return repo.get_all()


@router.get("/{target}/latest", status_code=status.HTTP_200_OK, response_model=PredictionOutputModel)
async def get_last_prediction(
    repo: Annotated[ListRepository, Depends(get_predictions_repository)],
) -> PredictionOutputModel:

    result = repo.get_latest()

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No previous entry in database was found",
        )
    return result


@router.get("/{target}/{db_id}", status_code=status.HTTP_200_OK, response_model=PredictionOutputModel)
async def get_prediction(
    db_id: int,
    repo: Annotated[ListRepository, Depends(get_predictions_repository)],
) -> PredictionOutputModel:
    result = repo.get(db_id)

    if result:
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {db_id} not found",
    )


@router.delete("/{target}/{db_id}", response_model=PredictionOutputModel)
async def delete_prediction(
    db_id: int,
    repo: Annotated[ListRepository, Depends(get_predictions_repository)],
) -> PredictionOutputModel:

    try:
        repo.delete(db_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except ListRepositoryError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {db_id} not found",
        ) from error


@router.put("/{target}/{db_id}", status_code=status.HTTP_201_CREATED, response_model=PredictionUpdateModel)
async def update_prediction(
    db_id: int,
    prediction_update: Annotated[
        PredictionUpdateModel,
        Body(...),
    ],
    repo: Annotated[ListRepository, Depends(get_predictions_repository)],
):

    try:
        result = repo.update(db_id, prediction_update)
        return result
    except ListRepositoryError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {db_id} not found",
        ) from error
