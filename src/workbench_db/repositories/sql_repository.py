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

            return item

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

    def update(self, model: SQLModel, db_id: int, new_item: SQLModel) -> SQLModel:  # pylint: disable=arguments-differ

        with Session(self._engine) as session:
            item: SQLModel = session.get(model, db_id)
            item_updated = item.model_copy(update=new_item.model_dump(exclude_unset=True, exclude_none=True))

            session.add(item_updated)
            session.commit()
            session.refresh(item_updated)
            return item_updated

    def delete(self, model: SQLModel, db_id: int) -> SQLModel:  # pylint: disable=arguments-differ

        with Session(self._engine) as session:

            item: SQLModel = session.get(model, db_id)

            session.delete(item)
            session.commit()

            return item
