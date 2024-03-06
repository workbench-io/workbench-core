from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_process.process_data import ProcessData
from workbench_process.process_settings import ProcessSettings


class SplitFeaturesAndTargets(WorkbenchTransformer):
    """Split features and target(s) into separate dataframes."""

    def transform(self, data: ProcessData, settings: ProcessSettings) -> bool:
        """Split features and target(s) into separate dataframes."""

        self.log_debug(self.transform, "Spliting features and targets")

        return True
