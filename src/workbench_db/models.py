from typing import Optional

from sqlmodel import Field, SQLModel


class OptimizationsTable(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    value: float
    solution: dict
    inputs: dict


class PredictionsTable(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    value: float
    feature: str
    inputs: dict
    version: str | None = None
