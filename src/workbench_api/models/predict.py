import math
from typing import Optional

from pydantic import BaseModel, Field, model_validator

# from workbench_api.common import DEFAULTS_COMPOSITION, TEMPLATE_TITLE_COMPOSITION
from workbench_api.common import DEFAULTS_COMPOSITION, TEMPLATE_TITLE_COMPOSITION
from workbench_optimize.common import DEFAULT_AGE
from workbench_train.common import Targets
from workbench_utils.strings import clean_text


class PredictionInputModel(BaseModel):
    """Input model for prediction."""

    cement: float = Field(**DEFAULTS_COMPOSITION, title=TEMPLATE_TITLE_COMPOSITION.format(clean_text("cement")))
    slag: float = Field(**DEFAULTS_COMPOSITION, title=TEMPLATE_TITLE_COMPOSITION.format(clean_text("slag")))
    fly_ash: float = Field(**DEFAULTS_COMPOSITION, title=TEMPLATE_TITLE_COMPOSITION.format(clean_text("fly_ash")))
    water: float = Field(**DEFAULTS_COMPOSITION, title=TEMPLATE_TITLE_COMPOSITION.format(clean_text("water")))
    superplasticizer: float = Field(
        **DEFAULTS_COMPOSITION, title=TEMPLATE_TITLE_COMPOSITION.format(clean_text("superplasticizer"))
    )
    coarse_aggregate: float = Field(
        **DEFAULTS_COMPOSITION, title=TEMPLATE_TITLE_COMPOSITION.format(clean_text("coarse_aggregate"))
    )
    fine_aggregate: float = Field(
        **DEFAULTS_COMPOSITION, title=TEMPLATE_TITLE_COMPOSITION.format(clean_text("fine_aggregate"))
    )
    age: int = Field(DEFAULT_AGE, ge=0, le=365, title="Age", description="Age of the material in days")

    @model_validator(mode="after")
    def validate_sum(self):

        total = sum(self.model_dump(exclude=["age"]).values())
        if not math.isclose(total, 100, rel_tol=0.01):
            raise ValueError("The sum of all components must be equal to 100+/-1.")
        return self


class PredictionOutputModel(BaseModel):
    """Output model for prediction."""

    id: int
    value: float
    feature: Targets
    inputs: PredictionInputModel
    version: Optional[str] = None


class PredictionUpdateModel(BaseModel):
    """Update model for prediction."""

    id: Optional[int] = None
    value: Optional[float] = None
    feature: Optional[Targets] = None
    inputs: Optional[PredictionInputModel] = None
    version: Optional[str] = None
