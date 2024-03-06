from pydantic import BaseModel


class SourceFileModel(BaseModel):
    """Model for the data source file."""

    path: str
    pattern: str
    columns: dict[str, str]


class SourcesModel(BaseModel):
    """Model for the sources of data."""

    compressive_strength: SourceFileModel


class FeaturesModel(BaseModel):
    """Model for the features of the data."""

    targets: list[str]
    ignore: list[str]
    numerical: list[str]
    categorical: list[str]
    discrete: list[str]
    text: list[str]
    date: list[str]
    id: list[str]
    geo: list[str]
    composition: list[str]

    @property
    def all_features(self) -> set[str]:
        return set(
            self.numerical
            + self.categorical
            + self.discrete
            + self.text
            + self.date
            + self.id
            + self.geo
            + self.composition
        )


class ProcessSettingsModel(BaseModel):
    """Model for the settings of the process step."""

    sources: SourcesModel
    features: FeaturesModel
