import os
import shutil
from pathlib import Path

import pytest

from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings
from workbench_train.transformers.export_model import ExportModel


class Model1:
    pass


class Model2:
    pass


class TestExportModel:
    def test_transform_returns_true(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
        tmp_path: Path,
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
            temp_dir = tmp_path / "models_dir"
            temp_dir.mkdir(parents=True, exist_ok=True)

            result = ExportModel().transform(train_data, train_settings)

            assert result

            assert train_settings.model.exporting.path.exists()
            assert train_settings.model.exporting.path.joinpath("model_2.pkl").exists()
            assert not train_settings.model.exporting.path.joinpath("model_1.pkl").exists()

        finally:
            shutil.rmtree(tmp_path)
            os.chdir(original_directory)

    @pytest.mark.parametrize(
        ["model_selection", "expected_files", "not_expected_files"],
        [
            (["model_2"], ["model_2.pkl"], ["model_1.pkl"]),
            (["model_1"], ["model_1.pkl"], ["model_2.pkl"]),
            (["model_1", "model_2"], ["model_1.pkl", "model_2.pkl"], []),
        ],
    )
    def test_transform_saves_files_of_model_to_be_exported(
        self,
        model_selection: list[str],
        expected_files: list[str],
        not_expected_files: list[str],
        train_data: TrainData,
        train_settings: TrainSettings,
        tmp_path: Path,
    ):  # pylint: disable=too-many-arguments

        train_settings.model.exporting.path = tmp_path / "models"
        train_settings.model.exporting.path.mkdir(parents=True, exist_ok=True)

        train_data.estimators = {
            "model_1": Model1,
            "model_2": Model2,
        }
        train_data.results = {
            "model_1": {"rmse": 5.0},
            "model_2": {"rmse": 1.0},
        }

        train_data.model_selection = model_selection

        try:
            temp_dir = tmp_path / "models_dir"
            temp_dir.mkdir(parents=True, exist_ok=True)

            ExportModel().transform(train_data, train_settings)

            for file in expected_files:
                assert train_settings.model.exporting.path.joinpath(file).exists()
            for file in not_expected_files:
                assert not train_settings.model.exporting.path.joinpath(file).exists()

        finally:
            shutil.rmtree(tmp_path)
