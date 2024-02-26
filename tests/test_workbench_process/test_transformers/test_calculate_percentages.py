import numpy as np
import pandas as pd

from workbench_process.process_data import ProcessData
from workbench_process.process_settings import ProcessSettings
from workbench_process.transformers.calculate_percentages import CalculatePercentages


class TestCalculatePercentages:
    def test_transform_returns_true(
        self,
        concrete_compressive_strength_after_rename_columns: pd.DataFrame,
        process_data: ProcessData,
        process_settings: ProcessSettings,
    ):

        process_data.compressive_strength = concrete_compressive_strength_after_rename_columns
        result = CalculatePercentages().transform(process_data, process_settings)

        assert result is True

    def test_transform_sum_of_components_should_add_to_100(
        self,
        concrete_compressive_strength_after_rename_columns: pd.DataFrame,
        process_data: ProcessData,
        process_settings: ProcessSettings,
    ):

        process_data.compressive_strength = concrete_compressive_strength_after_rename_columns
        CalculatePercentages().transform(process_data, process_settings)

        assert np.allclose(
            process_data.compressive_strength[process_settings.model.features.composition].sum(axis=1),
            pd.Series([100.0] * len(process_data.compressive_strength)),
        )
