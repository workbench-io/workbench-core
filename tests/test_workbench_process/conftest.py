import json
from pathlib import Path

import pytest

from workbench_process.process_config import ProcessConfig
from workbench_process.process_config_model import ProcessConfigModel
from workbench_process.process_data import ProcessData

URL = "https://archive.ics.uci.edu/static/public/165/concrete+compressive+strength.zip"

dir_resources = Path(__file__).parent.joinpath("resources")
dir_configs_example = dir_resources.joinpath("configs_example.json")


@pytest.fixture(scope="session")
def configs_path() -> Path:
    return dir_configs_example


@pytest.fixture(scope="session")
def config_dict() -> dict:
    with open(dir_configs_example, "r", encoding="utf-8") as file:
        return json.load(file)


@pytest.fixture(scope="session")
def configs_model() -> ProcessConfigModel:
    config_dict_ = json.load(dir_configs_example)
    return ProcessConfigModel(**config_dict_)


@pytest.fixture(scope="session")
def process_config() -> ProcessConfig:
    process_config_ = ProcessConfig()
    process_config_.load_configs(dir_configs_example)
    return process_config_


@pytest.fixture
def process_data() -> ProcessData:
    return ProcessData()


@pytest.fixture
def filepath_compressive_strength() -> Path:
    return dir_resources.joinpath("concrete+compressive+strength.zip")
