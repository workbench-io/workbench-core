"""Factory class for Train objects."""

# pylint: disable=protected-access

from workbench_train.train_data import TrainData
from workbench_train.train_factory import TrainFactory
from workbench_train.train_logic import TrainLogic
from workbench_train.train_settings import TrainSettings
from workbench_utils.common import WorkbenchSteps


class TestTrainFactory:

    def test___init__(self):
        train_factory = TrainFactory()

        assert not train_factory._items

    def test_register(self):
        train_factory = TrainFactory()
        train_factory.register(WorkbenchSteps.TRAIN, (TrainLogic, TrainData, TrainSettings))

        assert train_factory._items[WorkbenchSteps.TRAIN] == (TrainLogic, TrainData, TrainSettings)

    def test_create_instance_returns_tuple_with_train_objects(self):
        train_factory = TrainFactory()
        train_factory.register(WorkbenchSteps.TRAIN, (TrainLogic, TrainData, TrainSettings))

        result = train_factory.create_instance(name=WorkbenchSteps.TRAIN)

        assert isinstance(result, tuple)
        assert len(result) == 3
        assert isinstance(result[0], TrainLogic)
        assert isinstance(result[1], TrainData)
        assert isinstance(result[2], TrainSettings)
