import json
from pathlib import Path

import pytest

from workbench_components.common.common_configs import ENCODING
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings
from workbench_train.train_settings_model import TrainSettingsModel

dir_resources = Path(__file__).parent.joinpath("resources")
dir_configs_example = dir_resources.joinpath("workbench_settings.json")


@pytest.fixture(scope="session")
def configs_path() -> Path:
    return dir_configs_example


@pytest.fixture(scope="session")
def config_dict() -> dict:
    with open(dir_configs_example, "r", encoding=ENCODING) as file:
        return json.load(file)


@pytest.fixture(scope="session")
def configs_model() -> TrainSettingsModel:
    config_dict_ = json.load(dir_configs_example)
    return TrainSettingsModel(**config_dict_)


@pytest.fixture(scope="session")
def train_settings() -> TrainSettings:
    train_config_ = TrainSettings()
    train_config_.load_settings_from_file(dir_configs_example)
    return train_config_


@pytest.fixture
def train_data() -> TrainData:
    return TrainData()
