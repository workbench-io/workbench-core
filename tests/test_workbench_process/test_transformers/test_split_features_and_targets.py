import pandas as pd
import pytest

from workbench_process.process_data import ProcessData
from workbench_process.process_settings import ProcessSettings
from workbench_process.transformers.split_features_and_targets import SplitFeaturesAndTargets


class TestSplitFeaturesAndTargets:
    def test_transform_returns_true(
        self,
        process_data: ProcessData,
        process_settings: ProcessSettings,
    ):

        result = SplitFeaturesAndTargets().transform(process_data, process_settings)

        assert result is True

    @pytest.mark.xfail(reason="Not implemented.")
    def test_transform_split_features_and_targets_into_separate_attributes(
        self,
        process_data: ProcessData,
        process_settings: ProcessSettings,
        concrete_compressive_strength_after_calculate_percentages: pd.DataFrame,
    ):

        process_data.compressive_strength = concrete_compressive_strength_after_calculate_percentages

        SplitFeaturesAndTargets().transform(process_data, process_settings)

        assert False
