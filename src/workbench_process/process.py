from workbench_components.workbench_process.workbench_process import WorkbenchProcess
from workbench_process.process_config import ProcessConfig
from workbench_process.process_data import ProcessData


class Process(WorkbenchProcess):

    def run(
        self,
        data: ProcessData,
        config: ProcessConfig,
    ):  # pylint: disable=unused-argument
        self.log_info(self.run, "Running process")
        return True
