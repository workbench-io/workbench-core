from pydantic import BaseModel


class OptimizeInputModel(BaseModel):
    pass


class OptimizeOutputModel(BaseModel):

    best_value: float
    best_solution: dict[str, float]
