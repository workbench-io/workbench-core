import logging
from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, Response, status
from sklearn.base import BaseEstimator

from workbench_api.data.repository import ListRepository, get_optimizations_repository
from workbench_api.enums import RoutersPath
from workbench_api.models.optimize import OptimizeInputModel, OptimizeOutputModel
from workbench_api.utils import get_model
from workbench_optimize.optimize_factory import factory_optimize
from workbench_train.common import Targets
from workbench_utils.enums import WorkbenchSteps

router = APIRouter(prefix=RoutersPath.OPTIMIZE.value)

logger = logging.getLogger(__name__)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=OptimizeOutputModel)
async def run_optimization(
    optimization_input: Annotated[OptimizeInputModel, Body(...)],
    model: Annotated[BaseEstimator, Depends(get_model)],
    repo: Annotated[ListRepository, Depends(get_optimizations_repository)],
) -> OptimizeOutputModel:

    logic, data, settings = factory_optimize.create_instance(name=WorkbenchSteps.OPTIMIZE)

    settings.load_settings_from_model(optimization_input)

    data.model = model

    logger.debug(f"Making optimization for '{Targets.COMPRESSIVE_STRENGTH}' with input: {settings.model.model_dump()}")
    logic.run(data, settings)
    logger.debug(f"Predicted value for '{Targets.COMPRESSIVE_STRENGTH}': {data.results}")

    db_id = repo.get_next_id()

    result = OptimizeOutputModel(
        id=db_id,
        optimization_input=optimization_input,
        **data.results.model_dump(),
    )

    logger.debug(f"Saving result to database {result} with id {db_id}")
    repo.add(db_id, result)

    return result


@router.get("", status_code=status.HTTP_200_OK)
async def get_all_optimizations(
    repo: Annotated[ListRepository, Depends(get_optimizations_repository)],
) -> list[OptimizeOutputModel]:
    return repo.get_all()


@router.get("/latest", status_code=status.HTTP_200_OK, response_model=OptimizeOutputModel)
async def get_last_optimization(
    repo: Annotated[ListRepository, Depends(get_optimizations_repository)],
) -> OptimizeOutputModel:

    result = repo.get_latest()

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No previous entry in database was found",
        )
    return result


@router.get("/{db_id}", status_code=status.HTTP_200_OK, response_model=OptimizeOutputModel)
async def get_optimization(
    db_id: int,
    repo: Annotated[ListRepository, Depends(get_optimizations_repository)],
) -> OptimizeOutputModel:
    result = repo.get(db_id)

    if result:
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {db_id} not found",
    )


@router.delete("/{db_id}", response_model=OptimizeOutputModel)
async def delete_optimization(
    db_id: int,
    repo: Annotated[ListRepository, Depends(get_optimizations_repository)],
) -> OptimizeOutputModel:

    try:
        repo.delete(db_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except IndexError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {db_id} not found",
        ) from error
