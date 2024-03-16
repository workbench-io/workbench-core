"""Factory class for Process objects."""

# pylint: disable=protected-access

from workbench_process.process_data import ProcessData
from workbench_process.process_factory import ProcessFactory
from workbench_process.process_logic import ProcessLogic
from workbench_process.process_settings import ProcessSettings
from workbench_utils.enums import WorkbenchSteps


class TestProcessFactory:

    def test___init__(self):
        process_factory = ProcessFactory()

        assert not process_factory._items

    def test_register(self):
        process_factory = ProcessFactory()
        process_factory.register(WorkbenchSteps.PROCESS, (ProcessLogic, ProcessData, ProcessSettings))

        assert process_factory._items[WorkbenchSteps.PROCESS] == (ProcessLogic, ProcessData, ProcessSettings)

    def test_create_instance_returns_tuple_with_process_objects(self):
        process_factory = ProcessFactory()
        process_factory.register(WorkbenchSteps.PROCESS, (ProcessLogic, ProcessData, ProcessSettings))

        result = process_factory.create_instance(name=WorkbenchSteps.PROCESS)

        assert isinstance(result, tuple)
        assert len(result) == 3
        assert isinstance(result[0], ProcessLogic)
        assert isinstance(result[1], ProcessData)
        assert isinstance(result[2], ProcessSettings)
