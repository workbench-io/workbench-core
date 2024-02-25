from workbench_process.process_data import ProcessData
from workbench_process.process_logic import ProcessLogic
from workbench_process.process_settings import ProcessSettings


class TestProcess:

    def test_run_should_return_true(self, process_data: ProcessData, process_settings: ProcessSettings):
        process = ProcessLogic()
        result = process.run(process_data, process_settings)

        assert isinstance(result, bool)
        assert result
