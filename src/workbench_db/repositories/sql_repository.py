from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, select

from workbench_components.workench_repository.workbench_repository import WorkbenchRepository
from workbench_db.models import Optimization, Prediction


class SQLRepository(WorkbenchRepository):

    _model: SQLModel

    def __init__(self, engine: Engine) -> None:
        super().__init__()
        self._engine: Engine = engine

    def add(self, item: SQLModel) -> SQLModel:
        with Session(self._engine) as session:
            session.add(item)
            session.commit()
            session.refresh(item)

            return item

    def get(self, db_id: int) -> SQLModel:
        with Session(self._engine) as session:
            return session.get(self._model, db_id)

    def get_latest(self) -> SQLModel:
        with Session(self._engine) as session:
            statement = select(self._model).order_by(self._model.id.desc())
            result = session.exec(statement).first()
            return result

    def get_all(self) -> list[SQLModel]:
        with Session(self._engine) as session:
            statement = select(self._model)
            results = session.exec(statement).all()
            return results

    def update(self, db_id: int, new_item: SQLModel) -> SQLModel:

        with Session(self._engine) as session:
            item: SQLModel = session.get(self._model, db_id)
            item_updated = item.model_copy(update=new_item.model_dump(exclude_unset=True, exclude_none=True))

            session.add(item_updated)
            session.commit()
            session.refresh(item_updated)
            return item_updated

    def delete(self, db_id: int) -> SQLModel:

        with Session(self._engine) as session:

            item: SQLModel = session.get(self._model, db_id)

            session.delete(item)
            session.commit()

            return item


class PredictionsRepository(SQLRepository):
    """Repository class for Prediction objects."""

    _model = Prediction


class OptimizationsRepository(SQLRepository):
    """Repository class for Optimization objects."""

    _model = Optimization
