from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings
from workbench_process.process_settings_model import ProcessSettingsModel


class ProcessSettings(WorkbenchSettings):
    """Settings for data processing step."""

    _settings_model: ProcessSettingsModel = ProcessSettingsModel
