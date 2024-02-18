from workbench_core.workbench_config.workbench_config import WorkbenchConfig
from workbench_core.workbench_config.workbench_config_factory import WorkbenchConfigFactory


class TestWorkbenchConfigFactory:

    def test_register(self, workbench_config_factory: WorkbenchConfigFactory, workbench_config: WorkbenchConfig):
        workbench_config_factory.register(name="name", item=workbench_config)

        assert workbench_config_factory._items["name"] == workbench_config  # pylint: disable=protected-access

    def test_create(self, workbench_config_factory: WorkbenchConfigFactory, workbench_config: WorkbenchConfig):

        workbench_config_factory.register(name="name", item=workbench_config)
        result = workbench_config_factory.create(name="name")

        assert result == workbench_config

    def test_create_instance(self, workbench_config_factory: WorkbenchConfigFactory, workbench_config: WorkbenchConfig):

        workbench_config_factory.register(name="name", item=workbench_config)
        result = workbench_config_factory.create_instance(name="name")

        assert result.__class__.__qualname__ == workbench_config.__qualname__
