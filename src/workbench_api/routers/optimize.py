import logging
import pathlib

from fastapi import APIRouter, status

from workbench_api.models.optimize import OptimizeOutputModel
from workbench_optimize.optimize_factory import factory_optimize
from workbench_train.common import Targets
from workbench_utils.enums import WorkbenchSteps
from workbench_utils.export import load_estimator_from_directory

router = APIRouter()

logger = logging.getLogger(__name__)


PATH_OPTIMIZE_SETTINGS = (
    "/Users/jean/learn/workbench/workbench-core/tests/test_workbench_optimize/resources/workbench_settings.json"
)


@router.get("/optimize", status_code=status.HTTP_200_OK, response_model=OptimizeOutputModel)
async def run_optimization():

    logic, data, settings = factory_optimize.create_instance(name=WorkbenchSteps.OPTIMIZE)

    settings.load_settings_from_file(pathlib.Path(PATH_OPTIMIZE_SETTINGS))

    data.model = load_estimator_from_directory(settings.model.path_model)

    logger.debug(f"Making optimization for '{Targets.COMPRESSIVE_STRENGTH}' with input: {settings.model.model_dump()}")
    logic.run(data, settings)
    logger.debug(f"Predicted value for '{Targets.COMPRESSIVE_STRENGTH}': {data.results}")

    return OptimizeOutputModel(**data.results.model_dump())
