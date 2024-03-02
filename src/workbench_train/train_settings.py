from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings
from workbench_train.train_settings_model import TrainSettingsModel


class TrainSettings(WorkbenchSettings):
    """Settings for data training step."""

    _settings_model: TrainSettingsModel = TrainSettingsModel
