from workbench_core.workbench_source.workbench_source import WorkbenchSource
from workbench_core.workbench_source.workbench_source_factory import WorkbenchSourceFactory


class TestWorkbenchSourceFactory:

    def test_register(self, workbench_source_factory: WorkbenchSourceFactory, workbench_source: WorkbenchSource):
        workbench_source_factory.register(name="name", item=workbench_source)

        assert workbench_source_factory._items["name"] == workbench_source  # pylint: disable=protected-access

    def test_create(self, workbench_source_factory: WorkbenchSourceFactory, workbench_source: WorkbenchSource):

        workbench_source_factory.register(name="name", item=workbench_source)
        result = workbench_source_factory.create(name="name")

        assert result == workbench_source

    def test_create_instance(self, workbench_source_factory: WorkbenchSourceFactory, workbench_source: WorkbenchSource):

        workbench_source_factory.register(name="name", item=workbench_source)
        result = workbench_source_factory.create_instance(name="name")

        assert isinstance(result, WorkbenchSource)
