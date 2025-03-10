from workbench_components.workbench_logic.workbench_logic import WorkbenchLogic
from workbench_components.workbench_source.workbench_source import WorkbenchSource
from workbench_process.common import Source
from workbench_process.process_data import ProcessData
from workbench_process.process_settings import ProcessSettings
from workbench_process.sources.source_factory import factory_source
from workbench_process.transformers.calculate_percentages import CalculatePercentages
from workbench_process.transformers.rename_columns import RenameColumns
from workbench_process.transformers.split_features_and_targets import SplitFeaturesAndTargets
from workbench_utils.enums import WorkbenchSteps
from workbench_utils.strings import STRING_LOGIC_END, STRING_LOGIC_START


class ProcessLogic(WorkbenchLogic):

    def run(
        self,
        data: ProcessData,
        settings: ProcessSettings,
    ):
        self.log_info(self.run, STRING_LOGIC_START.format(step=WorkbenchSteps.OPTIMIZE))

        self._load_sources(data, settings)
        self._perform_transformations(data, settings)

        self.log_info(self.run, STRING_LOGIC_END.format(step=WorkbenchSteps.OPTIMIZE))

        return True

    def _load_sources(self, data: ProcessData, settings: ProcessSettings):

        for source in Source:
            self.log_info(self.run, f"Processing source: {source}")
            source: WorkbenchSource = factory_source.create_instance(name=source)
            source.load(data, settings)
            self.log_info(self.run, f"Source {source} processed")

    def _perform_transformations(self, data: ProcessData, settings: ProcessSettings):

        self.log_info(self._perform_transformations, "Performing transformations")

        RenameColumns().transform(data, settings)
        CalculatePercentages().transform(data, settings)
        SplitFeaturesAndTargets().transform(data, settings)

        self.log_info(self._perform_transformations, "Transformations complete")
