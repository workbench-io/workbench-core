import shutil
from pathlib import Path

import pandas as pd

from workbench_train.train_data import TrainData
from workbench_train.train_logic import TrainLogic
from workbench_train.train_settings import TrainSettings


class TestTrainLogic:

    def test_run_should_return_true(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
        features_and_targets: tuple[pd.DataFrame, pd.DataFrame],
        tmp_path: Path,
    ):

        try:
            train_data.features, train_data.targets = features_and_targets

            dir_models = tmp_path.joinpath("models")
            dir_models.mkdir(exist_ok=True, parents=True)

            train_settings.model.exporting.path = dir_models

            train = TrainLogic()

            result = train.run(train_data, train_settings)

            assert isinstance(result, bool)
            assert result

        finally:
            shutil.rmtree(tmp_path)
