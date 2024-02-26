import pandas as pd

from workbench_process.process_data import ProcessData
from workbench_process.process_settings import ProcessSettings
from workbench_process.transformers.rename_columns import RenameColumns


class TestRenameColumns:
    def test_transform_returns_true(
        self,
        concrete_compressive_strength_raw: pd.DataFrame,
        process_data: ProcessData,
        process_settings: ProcessSettings,
    ):

        process_data.compressive_strength = concrete_compressive_strength_raw
        result = RenameColumns().transform(process_data, process_settings)

        assert result is True

    def test_transform_changes_the_column_names(
        self,
        concrete_compressive_strength_raw: pd.DataFrame,
        concrete_compressive_strength_after_rename_columns: pd.DataFrame,
        process_data: ProcessData,
        process_settings: ProcessSettings,
    ):

        process_data.compressive_strength = concrete_compressive_strength_raw
        RenameColumns().transform(process_data, process_settings)

        assert (
            process_data.compressive_strength.columns == concrete_compressive_strength_after_rename_columns.columns
        ).all()
        assert process_data.compressive_strength.equals(concrete_compressive_strength_after_rename_columns)
