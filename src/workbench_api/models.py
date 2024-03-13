from typing import Optional

from fastapi import Query
from pydantic import BaseModel

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


class PredictionOutputModel(BaseModel):

    value: float
    feature: Optional[Targets] = None
    version: Optional[str] = None
