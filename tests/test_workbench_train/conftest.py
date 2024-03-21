import json
from pathlib import Path
from random import choices

import numpy as np
import pandas as pd
import pytest

from workbench_components.workbench_configs import workbench_configs
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
    with open(dir_configs_example, "r", encoding=workbench_configs.encoding) as file:
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
def features_and_targets() -> tuple[pd.DataFrame, pd.DataFrame]:
    n_size = 50
    index = range(n_size)
    np.random.seed(1)

    features = pd.DataFrame(
        {
            "cement": np.random.uniform(0, 100, size=n_size),
            "slag": np.random.uniform(0, 100, size=n_size),
            "fly_ash": np.random.uniform(0, 100, size=n_size),
            "water": np.random.uniform(0, 100, size=n_size),
            "superplasticizer": np.random.uniform(0, 100, size=n_size),
            "coarse_aggregate": np.random.uniform(0, 100, size=n_size),
            "fine_aggregate": np.random.uniform(0, 100, size=n_size),
            "age": choices([1, 3, 7, 14, 28, 90, 120, 180, 270, 360, 365], k=n_size),
        },
        index=index,
    )

    targets = pd.DataFrame(
        {"compressive_strength": np.random.normal(35, 16, size=n_size)},
        index=index,
    )

    return features, targets
