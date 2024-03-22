from pathlib import Path

from sqlalchemy import Engine
from sqlmodel import SQLModel, create_engine

from workbench_api.enums import Routers
from workbench_api.models.optimize import OptimizationOutputModel
from workbench_api.models.predict import PredictionOutputModel

predictions: list[PredictionOutputModel] = []
optimizations: list[OptimizationOutputModel] = []

databases: dict[Routers, list[object]] = {
    Routers.PREDICT: predictions,
    Routers.OPTIMIZE: optimizations,
}


def get_database(name: Routers) -> list[object]:
    """
    Retrieves the specified database by name.

    Args:
        name (Routers): The name of the database to retrieve.

    Returns:
        list[object]: The database corresponding to the specified name.

    Raises:
        KeyError: If the specified name is not a valid database name.

    """
    if name in Routers:
        return databases[name]

    raise KeyError(f"Invalid database name: {name}")


def get_database_url(filepath_db: str) -> str:

    sqlite_url = f"sqlite:///{filepath_db}"
    return sqlite_url


def get_database_engine(db_url: str, *args, **kwargs) -> Engine:
    engine = create_engine(db_url, *args, **kwargs)
    return engine


def create_db_and_tables(engine: Engine, filepath_db: Path | None = None):

    if filepath_db is not None and filepath_db.exists():
        filepath_db.unlink()

    SQLModel.metadata.create_all(engine)
