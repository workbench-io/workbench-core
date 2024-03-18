import logging
from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, Response, status
from sklearn.base import BaseEstimator

from workbench_api import db
from workbench_api.models.optimize import OptimizeInputModel, OptimizeOutputModel
from workbench_api.utils import get_db_entry_by_id, get_id, get_model
from workbench_optimize.optimize_factory import factory_optimize
from workbench_train.common import Targets
from workbench_utils.enums import WorkbenchSteps

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/optimize", status_code=status.HTTP_201_CREATED, response_model=OptimizeOutputModel)
async def run_optimization(
    optimization_input: Annotated[OptimizeInputModel, Body(...)],
    model: BaseEstimator = Depends(get_model),
) -> OptimizeOutputModel:

    logic, data, settings = factory_optimize.create_instance(name=WorkbenchSteps.OPTIMIZE)

    settings.load_settings_from_model(optimization_input)

    data.model = model

    logger.debug(f"Making optimization for '{Targets.COMPRESSIVE_STRENGTH}' with input: {settings.model.model_dump()}")
    logic.run(data, settings)
    logger.debug(f"Predicted value for '{Targets.COMPRESSIVE_STRENGTH}': {data.results}")

    db_id = get_id(db.optimizations)

    result = OptimizeOutputModel(
        id=db_id,
        optimization_input=optimization_input,
        **data.results.model_dump(),
    )

    logger.debug(f"Saving result to database {result} with id {db_id}")
    db.optimizations.append(result)

    return result


@router.get("/optimize", status_code=status.HTTP_200_OK)
async def get_all_optimizations() -> list[OptimizeOutputModel]:
    return db.optimizations


@router.get("/optimize/latest", status_code=status.HTTP_200_OK, response_model=OptimizeOutputModel)
async def get_last_optimization() -> OptimizeOutputModel:

    try:
        result = db.optimizations[-1]
        return result
    except IndexError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No previous entry in database was found",
        ) from error


@router.get("/optimize/{db_id}", status_code=status.HTTP_200_OK, response_model=OptimizeOutputModel)
async def get_optimization(db_id: int) -> OptimizeOutputModel:
    result = get_db_entry_by_id(db.optimizations, db_id)

    if result:
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {db_id} not found",
    )


@router.delete("/optimize/{db_id}", response_model=OptimizeOutputModel)
async def delete_optimization(db_id: int) -> OptimizeOutputModel:

    try:
        db.optimizations.pop(db_id - 1)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except IndexError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {db_id} not found",
        ) from error
