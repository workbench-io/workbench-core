import json
from pathlib import Path

import pytest

from workbench_components.common.common_configs import ENCODING
from workbench_optimize.optimize_data import OptimizeData
from workbench_optimize.optimize_settings import OptimizeSettings
from workbench_optimize.optimize_settings_model import OptimizeSettingsModel

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
def configs_model() -> OptimizeSettingsModel:
    config_dict_ = json.load(dir_configs_example)
    return OptimizeSettingsModel(**config_dict_)


@pytest.fixture(scope="session")
def optimize_settings() -> OptimizeSettings:
    optimize_config_ = OptimizeSettings()
    optimize_config_.load_settings_from_file(dir_configs_example)
    return optimize_config_


@pytest.fixture
def optimize_data() -> OptimizeData:
    return OptimizeData()
