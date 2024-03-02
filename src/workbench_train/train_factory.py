"""Factory class for Train objects."""

from workbench_components.workbench_factory import WorkbenchFactory, WorkbenchFactoryError
from workbench_train.common import STEP_NAME
from workbench_train.train_data import TrainData
from workbench_train.train_logic import TrainLogic
from workbench_train.train_settings import TrainSettings


class TrainFactory(WorkbenchFactory):
    """Factory class for Train objects."""

    _items: dict[str, tuple[TrainLogic, TrainData, TrainSettings]] | None = None

    def create_instance(self, name: str) -> tuple[TrainLogic, TrainData, TrainSettings]:
        """Create an instance of an item from the factory.

        Args:
            name (str): The name of the item to be created.

        Returns:
            tuple[TrainLogic, TrainData, TrainSettings]: The created item.
        """
        self.log_info(method=self.create_instance, message=f"Creating instance of {name}.")

        if self.contains(name=name):
            return tuple(item() for item in self._items[name])

        raise WorkbenchFactoryError(f"Item {name} not found in factory.")


factory_train = TrainFactory()
factory_train.register(STEP_NAME, (TrainLogic, TrainData, TrainSettings))
