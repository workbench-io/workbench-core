from typing import Optional

from pydantic import BaseModel, Field


class PredictionInputModel(BaseModel):

    cement: float = Field(..., ge=0, le=100)
    slag: float = Field(..., ge=0, le=100)
    fly_ash: float = Field(..., ge=0, le=100)
    water: float = Field(..., ge=0, le=100)
    superplasticizer: float = Field(..., ge=0, le=100)
    coarse_aggregate: float = Field(..., ge=0, le=100)
    fine_aggregate: float = Field(..., ge=0, le=100)
    age: Optional[int] = Field(28, ge=0, le=100)


class PredictionOutputtModel(BaseModel):

    prediction: float
    version: int | None = None
