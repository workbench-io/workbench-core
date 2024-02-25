import pandas as pd

from workbench_process.common import Source
from workbench_process.process_data import ProcessData
from workbench_process.process_logic import ProcessLogic
from workbench_process.process_settings import ProcessSettings


class TestProcess:

    def test_run_should_return_true(
        self,
        process_data: ProcessData,
        process_settings: ProcessSettings,
    ):
        process = ProcessLogic()
        result = process.run(process_data, process_settings)

        assert isinstance(result, bool)
        assert result

    def test_run_should_add_sources_to_process_data_object(
        self,
        process_data: ProcessData,
        process_settings: ProcessSettings,
    ):
        process = ProcessLogic()
        process.run(process_data, process_settings)

        for source in Source:
            source_data = process_data.get_data(source)

            assert source_data is not None
            assert not source_data.empty
            assert isinstance(source_data, pd.DataFrame)

    def test_run_should_transform_the_data(
        self,
        process_data: ProcessData,
        process_settings: ProcessSettings,
    ):
        process = ProcessLogic()
        process.run(process_data, process_settings)

        for source in Source:
            source_data = process_data.get_data(source)

            (source_data.columns == process_settings.model.sources.compressive_strength.columns.values()).all()
