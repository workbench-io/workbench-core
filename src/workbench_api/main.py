import logging
import pathlib
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import http_exception_handler
from fastapi.responses import HTMLResponse

from workbench_api.routers import optimize, predict
from workbench_components.common.common_configs import ENCODING
from workbench_components.workbench_logging.logging_configs import setup_logging

dir_html = pathlib.Path(__file__).parent.joinpath("www")

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):  # pylint: disable=unused-argument, redefined-outer-name
    setup_logging()
    logger.info("Logging started")
    yield


app = FastAPI(title="Workbench API", openapi_url="/api/v1/openapi.json", debug=True, lifespan=lifespan)
app.include_router(predict.router, tags=["Prediction"])
app.include_router(optimize.router, tags=["Optimization"])


@app.get("/")
async def root() -> HTMLResponse:
    with open(dir_html.joinpath("root.html"), "r", encoding=ENCODING) as file:
        body = file.read()

    return HTMLResponse(content=body)


@app.exception_handler(HTTPException)
async def http_exception_handle_logging(request, exc):
    logger.error(f"HTTPException: {exc.status_code} {exc.detail}")
    return await http_exception_handler(request, exc)
