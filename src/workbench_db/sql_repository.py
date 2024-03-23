from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, select

from workbench_components.workench_repository.workbench_repository import WorkbenchRepository


class SQLRepository(WorkbenchRepository):

    def __init__(self, engine: Engine) -> None:
        super().__init__()
        self._engine: Engine = engine

    def add(self, item: SQLModel) -> SQLModel:  # pylint: disable=arguments-differ
        with Session(self._engine) as session:
            session.add(item)
            session.commit()
            session.refresh(item)

    def get(self, model: SQLModel, db_id: int) -> SQLModel:  # pylint: disable=arguments-differ
        with Session(self._engine) as session:
            return session.get(model, db_id)

    def get_latest(self, model: SQLModel) -> SQLModel:
        with Session(self._engine) as session:
            statement = select(model).order_by(model.id.desc())
            result = session.exec(statement).first()
            return result

    def get_all(self, model: SQLModel) -> list[SQLModel]:  # pylint: disable=arguments-differ
        with Session(self._engine) as session:
            statement = select(model)
            results = session.exec(statement).all()
            return results

    def update(self, db_id: int, new_item: SQLModel) -> SQLModel:
        pass

    def delete(self, db_id: int) -> None:
        pass
