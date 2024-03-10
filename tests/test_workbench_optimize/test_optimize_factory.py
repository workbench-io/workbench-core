"""Factory class for Optimize objects."""

# pylint: disable=protected-access

from workbench_optimize.optimize_data import OptimizeData
from workbench_optimize.optimize_factory import OptimizeFactory
from workbench_optimize.optimize_logic import OptimizeLogic
from workbench_optimize.optimize_settings import OptimizeSettings
from workbench_utils.common import WorkbenchSteps


class TestOptimizeFactory:

    def test___init__(self):
        optimize_factory = OptimizeFactory()

        assert not optimize_factory._items

    def test_register(self):
        optimize_factory = OptimizeFactory()
        optimize_factory.register(WorkbenchSteps.TRAIN, (OptimizeLogic, OptimizeData, OptimizeSettings))

        assert optimize_factory._items[WorkbenchSteps.TRAIN] == (OptimizeLogic, OptimizeData, OptimizeSettings)

    def test_create_instance_returns_tuple_with_optimize_objects(self):
        optimize_factory = OptimizeFactory()
        optimize_factory.register(WorkbenchSteps.TRAIN, (OptimizeLogic, OptimizeData, OptimizeSettings))

        result = optimize_factory.create_instance(name=WorkbenchSteps.TRAIN)

        assert isinstance(result, tuple)
        assert len(result) == 3
        assert isinstance(result[0], OptimizeLogic)
        assert isinstance(result[1], OptimizeData)
        assert isinstance(result[2], OptimizeSettings)
