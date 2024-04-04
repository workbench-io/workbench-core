import logging
from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, Response, status
from sklearn.base import BaseEstimator

from workbench_api.enums import RoutersPath
from workbench_api.models.optimize import OptimizationInputModel, OptimizationOutputModel, OptimizationUpdateModel
from workbench_api.utils import get_model
from workbench_db.db import get_optimizations_repository
from workbench_db.repositories.list_repository import ListRepository, ListRepositoryError
from workbench_optimize.optimize_factory import factory_optimize
from workbench_train.common import Targets
from workbench_utils.enums import WorkbenchSteps

router = APIRouter(prefix=RoutersPath.OPTIMIZE.value)

logger = logging.getLogger(__name__)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=OptimizationOutputModel)
async def run_optimization(
    inputs: Annotated[OptimizationInputModel, Body(...)],
    model: Annotated[BaseEstimator, Depends(get_model)],
    repo: Annotated[ListRepository, Depends(get_optimizations_repository)],
) -> OptimizationOutputModel:

    logic, data, settings = factory_optimize.create_instance(name=WorkbenchSteps.OPTIMIZE)

    settings.load_settings_from_model(inputs)

    data.model = model

    logger.debug(f"Making optimization for '{Targets.COMPRESSIVE_STRENGTH}' with input: {settings.model.model_dump()}")
    logic.run(data, settings)
    logger.debug(f"Predicted value for '{Targets.COMPRESSIVE_STRENGTH}': {data.results}")

    db_id = repo.get_next_id()

    result = OptimizationOutputModel(
        id=db_id,
        inputs=inputs,
        **data.results.model_dump(),
    )

    logger.debug(f"Saving result to database {result} with id {db_id}")
    repo.add(result)

    return result


@router.get("", status_code=status.HTTP_200_OK)
async def get_all_optimizations(
    repo: Annotated[ListRepository, Depends(get_optimizations_repository)],
) -> list[OptimizationOutputModel]:
    return repo.get_all()


@router.get("/latest", status_code=status.HTTP_200_OK, response_model=OptimizationOutputModel)
async def get_last_optimization(
    repo: Annotated[ListRepository, Depends(get_optimizations_repository)],
) -> OptimizationOutputModel:

    result = repo.get_latest()

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No previous entry in database was found",
        )
    return result


@router.get("/{db_id}", status_code=status.HTTP_200_OK, response_model=OptimizationOutputModel)
async def get_optimization(
    db_id: int,
    repo: Annotated[ListRepository, Depends(get_optimizations_repository)],
) -> OptimizationOutputModel:
    result = repo.get(db_id)

    if result:
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {db_id} not found",
    )


@router.delete("/{db_id}", response_model=OptimizationOutputModel)
async def delete_optimization(
    db_id: int,
    repo: Annotated[ListRepository, Depends(get_optimizations_repository)],
) -> OptimizationOutputModel:

    try:
        repo.delete(db_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except ListRepositoryError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {db_id} not found",
        ) from error


@router.put("/{db_id}", status_code=status.HTTP_201_CREATED, response_model=OptimizationOutputModel)
async def update_optimization(
    db_id: int,
    optimization_update: Annotated[
        OptimizationUpdateModel,
        Body(...),
    ],
    repo: Annotated[ListRepository, Depends(get_optimizations_repository)],
):

    try:
        result = repo.update(db_id, optimization_update)
        return result
    except ListRepositoryError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {db_id} not found",
        ) from error
