from workbench_components.workbench_logic.workbench_logic import WorkbenchLogic
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings
from workbench_train.transformers.split_train_test_set import SplitTrainTestSet


class TrainLogic(WorkbenchLogic):

    def run(
        self,
        data: TrainData,
        settings: TrainSettings,
    ):
        self.log_info(self.run, "Running train")

        SplitTrainTestSet().transform(data, settings)

        self.log_info(self.run, "Train complete")

        return True
