from pathlib import Path

from sqlalchemy import Engine

from workbench_api.enums import Routers
from workbench_db.db import extract_path_from_db_url, get_database, get_database_engine, get_database_url


def test_get_database():

    result = get_database(Routers.PREDICT)

    assert isinstance(result, list)
    assert len(result) == 0


def test_get_database_url():
    filepath_db = "/path/to/database.db"
    expected_url = "sqlite:////path/to/database.db"

    result = get_database_url(filepath_db)

    assert result == expected_url


def test_get_database_engine():
    db_url = "sqlite:///test.db"
    engine = get_database_engine(db_url)
    assert isinstance(engine, Engine)


def test_extract_path_from_db_url():
    db_url = "sqlite:////path/to/database/test.db"
    expected_path = "/path/to/database/test.db"

    result = extract_path_from_db_url(db_url)

    assert result == Path(expected_path)


def test_extract_path_from_db_url_for_in_memory_db():
    db_url = "sqlite:///:memory:"
    expected_path = ":memory:"

    result = extract_path_from_db_url(db_url)

    assert result == Path(expected_path)
