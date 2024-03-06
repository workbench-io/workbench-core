import json
from pathlib import Path

import pandas as pd
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


@pytest.fixture
def concrete_compressive_strength_after_calculate_percentages() -> pd.DataFrame:
    df = pd.DataFrame(
        {
            "cement": [22.309440198306135, 22.17203859577089, 14.917003140421714],
            "slag": [0.0, 0.0, 6.39300134589502],
            "fly_ash": [0.0, 0.0, 0.0],
            "water": [6.692832059491841, 6.651611578731266, 10.228802153432031],
            "superplasticizer": [0.1032844453625284, 0.10264832683227264, 0.0],
            "coarse_aggregate": [42.96632927081181, 43.31759392321905, 41.81247196052041],
            "fine_aggregate": [27.92811402602768, 27.75610757544652, 26.648721399730825],
            "age": [28, 28, 270],
            "compressive_strength": [79.98611076, 61.887365759999994, 40.269535256000005],
        },
        index=[0, 1, 2],
    )

    return df
