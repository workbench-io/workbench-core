from workbench_api.enums import Routers
from workbench_api.models.optimize import OptimizationOutputModel
from workbench_api.models.predict import PredictionOutputModel

predictions: list[PredictionOutputModel] = []
optimizations: list[OptimizationOutputModel] = []

databases: dict[Routers, list[object]] = {
    Routers.PREDICT: predictions,
    Routers.OPTIMIZE: optimizations,
}


def get_database(name: Routers) -> list[object]:
    """
    Retrieves the specified database by name.

    Args:
        name (Routers): The name of the database to retrieve.

    Returns:
        list[object]: The database corresponding to the specified name.

    Raises:
        KeyError: If the specified name is not a valid database name.

    """
    if name in Routers:
        return databases[name]

    raise KeyError(f"Invalid database name: {name}")
