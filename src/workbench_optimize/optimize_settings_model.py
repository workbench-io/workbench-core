from pydantic import BaseModel


class OptimizeSettingsModel(BaseModel):
    """Model for the settings of the train step."""

    seed: int
    verbose: bool
