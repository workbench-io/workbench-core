import pytest

from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings
from workbench_train.transformers.export_model import ExportModel


@pytest.mark.xfail
class TestExportModel:
    def test_transform_returns_true(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
    ):
        result = ExportModel().transform(train_data, train_settings)

        assert result is True
