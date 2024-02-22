from pydantic import BaseModel


class SourcesModel(BaseModel):
    compressive_strength: str


class ProcessConfigModel(BaseModel):

    sources: SourcesModel
