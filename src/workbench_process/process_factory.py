"""Factory class for Process objects."""

from workbench_components.workbench_factory import WorkbenchFactory, WorkbenchFactoryError
from workbench_process.process_data import ProcessData
from workbench_process.process_logic import ProcessLogic
from workbench_process.process_settings import ProcessSettings
from workbench_utils.enums import WorkbenchSteps


class ProcessFactory(WorkbenchFactory):
    """Factory class for Process objects."""

    _items: dict[str, tuple[ProcessLogic, ProcessData, ProcessSettings]] | None = None

    def create_instance(
        self, name: str, *args, **kwargs
    ) -> tuple[ProcessLogic, ProcessData, ProcessSettings]:  # pylint: disable=unused-argument
        """Create an instance of an item from the factory.

        Args:
            name (str): The name of the item to be created.

        Returns:
            tuple[ProcessLogic, ProcessData, ProcessSettings]: The created item.
        """
        self.log_info(method=self.create_instance, message=f"Creating instance of {name}.")

        if self.contains(name=name):
            return tuple(item() for item in self._items[name])

        raise WorkbenchFactoryError(f"Item {name} not found in factory.")


factory_process = ProcessFactory()
factory_process.register(WorkbenchSteps.PROCESS, (ProcessLogic, ProcessData, ProcessSettings))
