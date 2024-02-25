from workbench_components.workbench_logic.workbench_logic import WorkbenchLogic
from workbench_process.process_data import ProcessData
from workbench_process.process_settings import ProcessSettings


class ProcessLogic(WorkbenchLogic):

    def run(
        self,
        data: ProcessData,
        config: ProcessSettings,
    ):  # pylint: disable=unused-argument
        self.log_info(self.run, "Running process")
        return True
