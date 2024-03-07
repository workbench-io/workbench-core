from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings


class SelectBestModel(WorkbenchTransformer):
    """Select the best model from the trained models"""

    def transform(self, data: TrainData, settings: TrainSettings) -> bool:
        """Select the best model from the trained models"""

        self.log_info(self.transform, "Select the best model")

        self.log_info(self.transform, "Selecting the best model completed")

        return True
