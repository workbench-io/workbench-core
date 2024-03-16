from pydantic import BaseModel


class BaseOutputModel(BaseModel):
    id: int
