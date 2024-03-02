from workbench_components.workbench_logic.workbench_logic import WorkbenchLogic
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings


class TrainLogic(WorkbenchLogic):

    def run(
        self,
        data: TrainData,
        settings: TrainSettings,
    ):  # pylint: disable=unused-argument
        self.log_info(self.run, "Running train")

        self.log_info(self.run, "Train complete")

        return True
