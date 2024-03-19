"""Factory class for Optimize objects."""

from workbench_components.workbench_factory import WorkbenchFactory, WorkbenchFactoryError
from workbench_optimize.optimize_data import OptimizeData
from workbench_optimize.optimize_logic import OptimizeLogic
from workbench_optimize.optimize_settings import OptimizeSettings
from workbench_utils.enums import WorkbenchSteps


class OptimizeFactory(WorkbenchFactory):
    """Factory class for Optimize objects."""

    _items: dict[str, tuple[OptimizeLogic, OptimizeData, OptimizeSettings]] | None = None

    def create_instance(
        self, name: str, *args, **kwargs
    ) -> tuple[OptimizeLogic, OptimizeData, OptimizeSettings]:  # pylint: disable=unused-argument
        """Create an instance of an item from the factory.

        Args:
            name (str): The name of the item to be created.

        Returns:
            tuple[OptimizeLogic, OptimizeData, OptimizeSettings]: The created item.
        """
        self.log_info(method=self.create_instance, message=f"Creating instance of {name}.")

        if self.contains(name=name):
            return tuple(item() for item in self._items[name])

        raise WorkbenchFactoryError(f"Item {name} not found in factory.")


factory_optimize = OptimizeFactory()
factory_optimize.register(WorkbenchSteps.OPTIMIZE, (OptimizeLogic, OptimizeData, OptimizeSettings))
