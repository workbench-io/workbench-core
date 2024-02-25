from workbench_components.workbench_logic.workbench_logic import WorkbenchLogic
from workbench_components.workbench_source.workbench_source import WorkbenchSource
from workbench_process.common import Source
from workbench_process.process_data import ProcessData
from workbench_process.process_settings import ProcessSettings
from workbench_process.sources.source_factory import factory_source


class ProcessLogic(WorkbenchLogic):

    def run(
        self,
        data: ProcessData,
        settings: ProcessSettings,
    ):
        self.log_info(self.run, "Running process")

        self._load_sources(data, settings)

        self.log_info(self.run, "Process complete")

        return True

    def _load_sources(self, data: ProcessData, settings: ProcessSettings):

        for source in Source:
            self.log_info(self.run, f"Processing source: {source}")
            source: WorkbenchSource = factory_source.create_instance(name=source)
            source.load(data, settings)
            self.log_info(self.run, f"Source {source} processed")
