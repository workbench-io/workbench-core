from typing import Any, Callable

from pydantic import BaseModel
from sqlalchemy import Engine
from sqlmodel import Session, SQLModel

from workbench_components.workench_repository.workbench_repository import WorkbenchRepository


class SQLRepository(WorkbenchRepository):

    def __init__(self, fn_connection: Callable[[None], Any], *args, **kwargs) -> None:
        super().__init__()
        self.engine: Engine = fn_connection(*args, **kwargs)

    def add(self, item: SQLModel) -> BaseModel:  # pylint: disable=arguments-differ
        with Session(self.engine) as session:
            session.add(item)
            session.commit()

    def get(self, db_id: int) -> BaseModel:
        pass

    def get_latest(self) -> BaseModel:
        pass

    def get_all(self) -> list[BaseModel]:
        pass

    def update(self, db_id: int, new_item: BaseModel) -> BaseModel:
        pass

    def delete(self, db_id: int) -> None:
        pass
