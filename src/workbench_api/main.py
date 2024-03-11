import pathlib

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from workbench_api.models import PredictionInputModel, PredictionOutputtModel
from workbench_api.utils import get_predicted_value
from workbench_train.common import Targets
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


@app.get("/predict/")
async def make_prediction(
    prediction_input: PredictionInputModel,
):
    predicted_value = get_predicted_value(prediction_input, model)
    return PredictionOutputtModel(prediction=predicted_value)


@app.get("/predict/{target}")
async def make_prediction_target(
    prediction_input: PredictionInputModel,
    target: Targets,
):
    predicted_value = get_predicted_value(prediction_input, model)

    if target:
        return PredictionOutputtModel(value=predicted_value, feature=target)

    return PredictionOutputtModel(value=predicted_value)
