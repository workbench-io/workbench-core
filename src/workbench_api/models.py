from typing import Optional

from pydantic import BaseModel, Field

from workbench_train.common import Targets


class PredictionInputModel(BaseModel):

    cement: float = Field(..., ge=0, le=100)
    slag: float = Field(..., ge=0, le=100)
    fly_ash: float = Field(..., ge=0, le=100)
    water: float = Field(..., ge=0, le=100)
    superplasticizer: float = Field(..., ge=0, le=100)
    coarse_aggregate: float = Field(..., ge=0, le=100)
    fine_aggregate: float = Field(..., ge=0, le=100)
    age: Optional[int] = Field(28, ge=0, le=365)


class PredictionOutputModel(BaseModel):

    value: float
    feature: Optional[Targets] = None
    version: Optional[int] = None
