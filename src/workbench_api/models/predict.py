import math
from typing import Optional

from fastapi import Query
from pydantic import BaseModel, model_validator

from workbench_api.common import DEFAULTS_COMPOSITION, TEMPLATE_TITLE_COMPOSITION
from workbench_train.common import Targets
from workbench_utils.strings import clean_text


class PredictionInputModel(BaseModel):

    cement: float = Query(**DEFAULTS_COMPOSITION, title=TEMPLATE_TITLE_COMPOSITION.format(clean_text("cement")))
    slag: float = Query(**DEFAULTS_COMPOSITION, title=TEMPLATE_TITLE_COMPOSITION.format(clean_text("slag")))
    fly_ash: float = Query(**DEFAULTS_COMPOSITION, title=TEMPLATE_TITLE_COMPOSITION.format(clean_text("fly_ash")))
    water: float = Query(**DEFAULTS_COMPOSITION, title=TEMPLATE_TITLE_COMPOSITION.format(clean_text("water")))
    superplasticizer: float = Query(
        **DEFAULTS_COMPOSITION, title=TEMPLATE_TITLE_COMPOSITION.format(clean_text("superplasticizer"))
    )
    coarse_aggregate: float = Query(
        **DEFAULTS_COMPOSITION, title=TEMPLATE_TITLE_COMPOSITION.format(clean_text("coarse_aggregate"))
    )
    fine_aggregate: float = Query(
        **DEFAULTS_COMPOSITION, title=TEMPLATE_TITLE_COMPOSITION.format(clean_text("fine_aggregate"))
    )
    age: int = Query(28, ge=0, le=365, title="Age", description="Age of the material in days")

    @model_validator(mode="after")
    def validate_sum(self):

        total = sum(self.model_dump(exclude=["age"]).values())
        if not math.isclose(total, 100, rel_tol=0.01):
            raise ValueError("The sum of all components must be equal to 100+/-1.")
        return self

    class PredictionOutputModel(BaseModel):
        value: float
        feature: Optional[Targets] = None
        version: Optional[str] = None


class PredictionOutputModel(BaseModel):

    value: float
    feature: Optional[Targets] = None
    version: Optional[str] = None
