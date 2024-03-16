import logging
from typing import Annotated

from fastapi import APIRouter, Body, Depends, status
from sklearn.base import BaseEstimator

from workbench_api.models.optimize import OptimizeInputModel, OptimizeOutputModel
from workbench_api.utils import get_model
from workbench_optimize.optimize_factory import factory_optimize
from workbench_train.common import Targets
from workbench_utils.enums import WorkbenchSteps

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/optimize", status_code=status.HTTP_200_OK, response_model=OptimizeOutputModel)
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

    return OptimizeOutputModel(**data.results.model_dump())
