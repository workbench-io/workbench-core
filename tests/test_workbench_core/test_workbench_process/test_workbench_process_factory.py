from workbench_core.workbench_process.workbench_process import WorkbenchProcess
from workbench_core.workbench_process.workbench_process_factory import WorkbenchProcessFactory


class TestWorkbenchProcessFactory:

    def test_register(self, workbench_process_factory: WorkbenchProcessFactory, data_transformer: WorkbenchProcess):
        workbench_process_factory.register(name="name", item=data_transformer)

        assert workbench_process_factory._items["name"] == data_transformer  # pylint: disable=protected-access

    def test_create(self, workbench_process_factory: WorkbenchProcessFactory, data_transformer: WorkbenchProcess):

        workbench_process_factory.register(name="name", item=data_transformer)
        result = workbench_process_factory.create(name="name")

        assert result == data_transformer

    def test_create_instance(
        self, workbench_process_factory: WorkbenchProcessFactory, data_transformer: WorkbenchProcess
    ):

        workbench_process_factory.register(name="name", item=data_transformer)
        result = workbench_process_factory.create_instance(name="name")

        assert result.__class__.__qualname__ == data_transformer.__qualname__
