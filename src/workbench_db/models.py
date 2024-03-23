from typing import Optional

from sqlmodel import Field, SQLModel


class Optimization(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    value: float
    solution: str
    inputs: str


class Prediction(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    value: float
    feature: str
    inputs: str
    version: str | None = None
