from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings
from workbench_components.workbench_settings.workbench_settings_factory import WorkbenchSettingsFactory


class TestWorkbenchSettingsFactory:

    def test_register(self, workbench_config_factory: WorkbenchSettingsFactory, workbench_settings: WorkbenchSettings):
        workbench_config_factory.register(name="name", item=workbench_settings)

        assert workbench_config_factory._items["name"] == workbench_settings  # pylint: disable=protected-access

    def test_create(self, workbench_config_factory: WorkbenchSettingsFactory, workbench_settings: WorkbenchSettings):

        workbench_config_factory.register(name="name", item=workbench_settings)
        result = workbench_config_factory.create(name="name")

        assert result == workbench_settings

    def test_create_instance(
        self, workbench_config_factory: WorkbenchSettingsFactory, workbench_settings: WorkbenchSettings
    ):

        workbench_config_factory.register(name="name", item=workbench_settings)
        result = workbench_config_factory.create_instance(name="name")

        assert result.__class__.__qualname__ == workbench_settings.__qualname__
