import os
import shutil

import pytest

from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings
from workbench_train.transformers.export_model import ExportModel


class Model1:
    pass


class Model2:
    pass


@pytest.mark.xfail
class TestExportModel:
    def test_transform_returns_true(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
        tmp_path,
    ):

        train_settings.model.exporting.path = tmp_path / "models"
        train_settings.model.exporting.path.mkdir(parents=True, exist_ok=True)

        train_data.results = {
            "model_1": {"rmse": 5.0},
            "model_2": {"rmse": 1.0},
        }

        train_data.estimators = {
            "model_1": Model1,
            "model_2": Model2,
        }

        train_data.model_selection = ["model_2"]

        original_directory = os.getcwd()

        try:
            temp_dir = tmp_path / "my_temp_dir"
            temp_dir.mkdir(parents=True, exist_ok=True)
            os.chdir(temp_dir)

            ExportModel().transform(train_data, train_settings)

            assert train_settings.model.exporting.path.exists()
            assert train_settings.model.exporting.path.joinpath("model_2.pkl").exists()
            assert not train_settings.model.exporting.path.joinpath("model_1.pkl").exists()

        finally:
            shutil.rmtree(tmp_path)
            os.chdir(original_directory)
