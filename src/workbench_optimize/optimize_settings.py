from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings
from workbench_optimize.optimize_settings_model import OptimizeSettingsModel


class OptimizeSettings(WorkbenchSettings):
    """Settings for data optimizeing step."""

    _settings_model: OptimizeSettingsModel = OptimizeSettingsModel
