from pydantic import BaseModel
from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, select

from workbench_components.workench_repository.workbench_repository import WorkbenchRepository


class SQLRepository(WorkbenchRepository):

    def __init__(self, engine: Engine) -> None:
        super().__init__()
        self.engine: Engine = engine

    def add(self, item: SQLModel) -> BaseModel:  # pylint: disable=arguments-differ
        with Session(self.engine) as session:
            session.add(item)
            session.commit()
            session.refresh(item)

    def get(self, model: SQLModel, db_id: int) -> BaseModel:  # pylint: disable=arguments-differ
        with Session(self.engine) as session:
            return session.get(model, db_id)

    def get_latest(self) -> BaseModel:
        pass

    def get_all(self, model) -> list[BaseModel]:  # pylint: disable=arguments-differ
        with Session(self.engine) as session:
            statement = select(model)
            results = session.exec(statement).all()
            return results

    def update(self, db_id: int, new_item: BaseModel) -> BaseModel:
        pass

    def delete(self, db_id: int) -> None:
        pass
