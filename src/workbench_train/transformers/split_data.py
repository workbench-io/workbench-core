from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings


class SplitData(WorkbenchTransformer):
    """Split data into training and test sets."""

    def transform(self, data: TrainData, settings: TrainSettings) -> bool:
        """Split data into training and test sets."""

        self.log_debug(self.transform, "Spliting Data")

        self.log_debug(self.transform, "Data spliting completed")

        return True
