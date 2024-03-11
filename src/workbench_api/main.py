import pathlib
from typing import Optional

from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse

from workbench_api.models import PredictionInputModel, PredictionOutputtModel
from workbench_api.utils import get_predicted_value
from workbench_utils.export import get_filepath_from_directory, load_pipeline

DIR_MODELS = pathlib.Path("./output/models")
DIR_MODELS_PATTERN = "*.pkl"

model = load_pipeline(get_filepath_from_directory(DIR_MODELS, DIR_MODELS_PATTERN))

app = FastAPI(
    title="Workbench API",
    openapi_url="/api/v1/openapi.json",
    debug=True,
)


@app.get("/")
async def root() -> HTMLResponse:
    """Basic HTML response."""

    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to the Workbench API</h1>"
        "<div>"
        "<p>"
        "For making a predictions use <a href='/predict'>/predict</a>"
        "</p>"
        "<div>"
        "For the documentation go to: <a href='/docs'>/docs</a>"
        "</div>"
        "</body>"
        "</html>"
    )

    return HTMLResponse(content=body)


# pylint: disable=too-many-arguments
@app.get("/predict/")
async def make_prediction(
    cement: float = Query(..., ge=0, le=100),
    slag: float = Query(..., ge=0, le=100),
    fly_ash: float = Query(..., ge=0, le=100),
    water: float = Query(..., ge=0, le=100),
    superplasticizer: float = Query(..., ge=0, le=100),
    coarse_aggregate: float = Query(..., ge=0, le=100),
    fine_aggregate: float = Query(..., ge=0, le=100),
    age: Optional[int] = Query(28, ge=0, le=100),
) -> PredictionOutputtModel:

    values = PredictionInputModel(
        cement=cement,
        slag=slag,
        fly_ash=fly_ash,
        water=water,
        superplasticizer=superplasticizer,
        coarse_aggregate=coarse_aggregate,
        fine_aggregate=fine_aggregate,
        age=age,
    )

    predicted_value = get_predicted_value(values, model)
    return PredictionOutputtModel(prediction=predicted_value)
