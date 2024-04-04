import logging
import pathlib
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import http_exception_handler
from fastapi.responses import HTMLResponse

from workbench_api.routers import optimize, predict
from workbench_components.workbench_configs import workbench_configs
from workbench_components.workbench_logging.logging_configs import setup_logging
from workbench_db.db import check_sql_model, create_db_and_tables, extract_path_from_db_url, get_database_engine
from workbench_db.models import Optimization, Prediction

dir_html = pathlib.Path(__file__).parent.joinpath("www")

logger = logging.getLogger(__name__)


def create_db_if_not_exist() -> None:
    db_path = extract_path_from_db_url(workbench_configs.database_url)

    if not db_path.exists():
        logger.info("Creating database engine")
        engine = get_database_engine(workbench_configs.database_url)

        logger.info("Creating database and tables")

        if check_sql_model(Optimization) and check_sql_model(Prediction):
            create_db_and_tables(engine, workbench_configs.database_url)
            logger.info("Database and tables created")


@asynccontextmanager
async def lifespan(app: FastAPI):  # pylint: disable=unused-argument, redefined-outer-name
    setup_logging()
    logger.info("Logging started")
    create_db_if_not_exist()
    yield
    logger.info("Logging Over")


app = FastAPI(title="Workbench API", debug=True, lifespan=lifespan)
app.include_router(predict.router, tags=["Prediction"])
app.include_router(optimize.router, tags=["Optimization"])


@app.get("/")
async def root() -> HTMLResponse:
    with open(dir_html.joinpath("root.html"), "r", encoding=workbench_configs.encoding) as file:
        body = file.read()

    return HTMLResponse(content=body)


@app.exception_handler(HTTPException)
async def http_exception_handle_logging(request, exc):
    logger.error(f"HTTPException: {exc.status_code} {exc.detail}")
    return await http_exception_handler(request, exc)
