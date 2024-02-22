# from workbench_process.process import Process
# from workbench_process.process_config import ProcessConfig
# from workbench_process.process_data import ProcessData


from workbench_process.process import Process
from workbench_process.process_config import ProcessConfig
from workbench_process.process_data import ProcessData


class TestProcess:

    def test_run_should_return_true(self, process_data: ProcessData, process_config: ProcessConfig):
        process = Process()
        result = process.run(process_data, process_config)

        assert isinstance(result, bool)
        assert result
