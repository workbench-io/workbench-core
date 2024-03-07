from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_train.common import METRIC_LOWER_IS_BETTER_MAP
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings


class SelectBestModel(WorkbenchTransformer):
    """Select the best model from the trained models"""

    def transform(self, data: TrainData, settings: TrainSettings) -> bool:
        """Select the best model from the trained models"""

        self.log_info(self.transform, "Select the best model")

        if METRIC_LOWER_IS_BETTER_MAP[settings.model.selecting.metric]:
            models_sorted = sorted(data.results, key=lambda x: data.results[x][settings.model.selecting.metric])
        else:
            models_sorted = sorted(
                data.results, key=lambda x: data.results[x][settings.model.selecting.metric], reverse=True
            )

        data.model_selection = models_sorted[: settings.model.selecting.n_models]

        self.log_info(self.transform, "Selecting the best model completed")
        self.log_debug(self.transform, f"Model selection: {data.model_selection}")

        return True
