from typing import Optional

from sqlmodel import Field, SQLModel


class PredictionBase(SQLModel):

    value: float
    feature: str
    inputs: str
    version: str | None = None


class Prediction(PredictionBase, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)


class OptimizationBase(SQLModel):

    value: float
    solution: str
    inputs: str


class Optimization(OptimizationBase, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
