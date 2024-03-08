from workbench_components.workbench_logic.workbench_logic import WorkbenchLogic
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings
from workbench_train.transformers.create_model_objects import CreateModelObjects
from workbench_train.transformers.create_preprocessor import CreatePreprocessor
from workbench_train.transformers.export_model import ExportModel
from workbench_train.transformers.select_best_model import SelectBestModel
from workbench_train.transformers.split_train_test_set import SplitTrainTestSet
from workbench_train.transformers.train_models import TrainModels


class TrainLogic(WorkbenchLogic):

    def run(
        self,
        data: TrainData,
        settings: TrainSettings,
    ):
        self.log_info(self.run, "Running train")

        SplitTrainTestSet().transform(data, settings)
        CreatePreprocessor().transform(data, settings)
        CreateModelObjects().transform(data, settings)
        TrainModels().transform(data, settings)
        SelectBestModel().transform(data, settings)
        ExportModel().transform(data, settings)

        self.log_info(self.run, "Train complete")

        return True
