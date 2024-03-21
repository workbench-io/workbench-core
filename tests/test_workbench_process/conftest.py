import json
from pathlib import Path

import pandas as pd
import pytest

from workbench_components.workbench_configs import workbench_configs
from workbench_process.process_data import ProcessData
from workbench_process.process_settings import ProcessSettings
from workbench_process.process_settings_model import ProcessSettingsModel

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


@pytest.fixture
def concrete_compressive_strength_raw() -> pd.DataFrame:
    df = pd.DataFrame(
        {
            "Cement (component 1)(kg in a m^3 mixture)": [540.0, 540.0, 332.5],
            "Blast Furnace Slag (component 2)(kg in a m^3 mixture)": [0.0, 0.0, 142.5],
            "Fly Ash (component 3)(kg in a m^3 mixture)": [0.0, 0.0, 0.0],
            "Water  (component 4)(kg in a m^3 mixture)": [162.0, 162.0, 228.0],
            "Superplasticizer (component 5)(kg in a m^3 mixture)": [2.5, 2.5, 0.0],
            "Coarse Aggregate  (component 6)(kg in a m^3 mixture)": [1040.0, 1055.0, 932.0],
            "Fine Aggregate (component 7)(kg in a m^3 mixture)": [676.0, 676.0, 594.0],
            "Age (day)": [28, 28, 270],
            "Concrete compressive strength(MPa, megapascals) ": [79.9, 61.8, 40.2],
        },
        index=[0, 1, 2],
    )

    return df


@pytest.fixture
def concrete_compressive_strength_after_rename_columns() -> pd.DataFrame:
    df = pd.DataFrame(
        {
            "cement": [540.0, 540.0, 332.5],
            "slag": [0.0, 0.0, 142.5],
            "fly_ash": [0.0, 0.0, 0.0],
            "water": [162.0, 162.0, 228.0],
            "superplasticizer": [2.5, 2.5, 0.0],
            "coarse_aggregate": [1040.0, 1055.0, 932.0],
            "fine_aggregate": [676.0, 676.0, 594.0],
            "age": [28, 28, 270],
            "compressive_strength": [79.9, 61.8, 40.2],
        },
        index=[0, 1, 2],
    )

    return df


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
