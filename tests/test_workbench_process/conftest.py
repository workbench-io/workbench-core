import json
from pathlib import Path

import pytest

from workbench_components.common.common_configs import ENCODING
from workbench_process.process_config_model import ProcessSettingsModel
from workbench_process.process_data import ProcessData
from workbench_process.process_settings import ProcessSettings

URL = "https://archive.ics.uci.edu/static/public/165/concrete+compressive+strength.zip"

dir_resources = Path(__file__).parent.joinpath("resources")
dir_configs_example = dir_resources.joinpath("configs_example.json")


@pytest.fixture(scope="session")
def configs_path() -> Path:
    return dir_configs_example


@pytest.fixture(scope="session")
def config_dict() -> dict:
    with open(dir_configs_example, "r", encoding=ENCODING) as file:
        return json.load(file)


@pytest.fixture(scope="session")
def configs_model() -> ProcessSettingsModel:
    config_dict_ = json.load(dir_configs_example)
    return ProcessSettingsModel(**config_dict_)


@pytest.fixture(scope="session")
def process_settings() -> ProcessSettings:
    process_config_ = ProcessSettings()
    process_config_.load_settings_from_file(dir_configs_example)
    return process_config_


@pytest.fixture
def process_data() -> ProcessData:
    return ProcessData()


@pytest.fixture
def filepath_compressive_strength() -> Path:
    return dir_resources.joinpath("concrete+compressive+strength.zip")
