import json
from pathlib import Path

import pytest

from workbench_process.process_config import ProcessConfig
from workbench_process.process_config_model import ProcessConfigModel
from workbench_process.process_data import ProcessData

DIR_RESOURCES = Path(__file__).parent.joinpath("resources")
DIR_CONFIGS_EXAMPLE = DIR_RESOURCES.joinpath("configs_example.json")


@pytest.fixture(scope="session")
def configs_path() -> Path:
    return DIR_CONFIGS_EXAMPLE


@pytest.fixture(scope="session")
def config_dict() -> dict:
    with open(DIR_CONFIGS_EXAMPLE, "r", encoding="utf-8") as file:
        return json.load(file)


@pytest.fixture(scope="session")
def configs_model() -> ProcessConfigModel:
    config_dict_ = json.load(DIR_CONFIGS_EXAMPLE)
    return ProcessConfigModel(**config_dict_)


@pytest.fixture(scope="session")
def process_config() -> ProcessConfig:
    process_config_ = ProcessConfig()
    process_config_.load_configs(DIR_CONFIGS_EXAMPLE)
    return process_config_


@pytest.fixture
def process_data() -> ProcessData:
    return ProcessData()
