from pydantic import BaseModel


class ZipFileModel(BaseModel):
    path: str
    pattern: str
    columns: dict[str, str]


class SourcesModel(BaseModel):
    compressive_strength: ZipFileModel


class ProcessSettingsModel(BaseModel):
    sources: SourcesModel
