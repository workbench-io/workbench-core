import logging
from typing import Optional

from sqlmodel import Field, SQLModel

from workbench_components.workbench_configs import workbench_configs
from workbench_db.db import create_db_and_tables, get_database_engine

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Optimization(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    value: float
    solution: str
    inputs: str


class Prediction(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    value: float
    feature: str
    inputs: str
    version: str | None = None


if __name__ == "__main__":

    logger.info("Creating database engine")
    engine = get_database_engine(workbench_configs.database_url)

    logger.info("Creating database and tables")
    create_db_and_tables(engine, workbench_configs.database_url)
    logger.info("Database and tables created")
