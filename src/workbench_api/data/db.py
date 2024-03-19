from workbench_api.enums import Routers
from workbench_api.models.optimize import OptimizeOutputModel
from workbench_api.models.predict import PredictionOutputModel

predictions: list[PredictionOutputModel] = []
optimizations: list[OptimizeOutputModel] = []


def get_db(name: Routers) -> list[object]:

    if name in Routers:
        if name == Routers.PREDICT:
            return predictions
        return optimizations

    raise ValueError(f"Invalid database name: {name}")
