from typing import Optional

from fastapi import Query
from pydantic import BaseModel

from workbench_train.common import Targets


class PredictionInputModel(BaseModel):

    cement: float = Query(default=0, ge=0, le=100)
    slag: float = Query(default=0, ge=0, le=100)
    fly_ash: float = Query(default=0, ge=0, le=100)
    water: float = Query(default=0, ge=0, le=100)
    superplasticizer: float = Query(default=0, ge=0, le=100)
    coarse_aggregate: float = Query(default=0, ge=0, le=100)
    fine_aggregate: float = Query(default=0, ge=0, le=100)
    age: Optional[int] = Query(28, ge=0, le=365)


class PredictionOutputModel(BaseModel):

    value: float
    feature: Optional[Targets] = None
    version: Optional[int] = None
