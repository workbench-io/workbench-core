import logging
import pathlib

from fastapi import APIRouter, status

from workbench_api.models.optimize import OptimizeOutputModel
from workbench_optimize.optimize_factory import factory_optimize
from workbench_train.common import Targets
from workbench_utils.common import WorkbenchSteps

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/optimize", status_code=status.HTTP_200_OK, response_model=OptimizeOutputModel)
async def run_optimization():

    optimize_logic, optimize_data, optimize_settings = factory_optimize.create_instance(name=WorkbenchSteps.OPTIMIZE)
    optimize_settings.load_settings_from_file(
        pathlib.Path(
            "/Users/jean/learn/workbench/workbench-core/tests/test_workbench_optimize/resources/workbench_settings.json"
        )
    )

    logger.debug(
        f"Making optimization for '{Targets.COMPRESSIVE_STRENGTH}' with input: {optimize_settings.model.model_dump()}"
    )
    optimize_logic.run(optimize_data, optimize_settings)
    logger.debug(f"Predicted value for '{Targets.COMPRESSIVE_STRENGTH}': {optimize_data.results}")

    return OptimizeOutputModel(**optimize_data.results.model_dump())
