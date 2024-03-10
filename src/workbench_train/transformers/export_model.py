from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_train.common import EXPORTED_MODEL_FILENAME_TEMPLATE
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings
from workbench_utils.export import remove_old_pipelines, save_pipeline


class ExportModelError(Exception):
    """Export model error"""


class ExportModel(WorkbenchTransformer):
    """Export the best model"""

    def transform(self, data: TrainData, settings: TrainSettings) -> bool:
        """Export the best model"""

        self.log_info(self.transform, "Exporting the best model")

        if data.model_selection is None:
            self.log_error(self.transform, "No model available to export in TrainData object")
            raise ExportModelError("No model available to export in TrainData object")

        if settings.model.exporting.remove_previous and settings.model.exporting.path.exists():
            self.log_info(self.transform, f"Removing previous models in {settings.model.exporting.path.absolute()}")
            remove_old_pipelines(settings.model.exporting.path)

        for model_name in data.model_selection:
            if not settings.model.exporting.path.exists():
                settings.model.exporting.path.mkdir(parents=True, exist_ok=True)

            filepath_model = settings.model.exporting.path / EXPORTED_MODEL_FILENAME_TEMPLATE.format(
                model_name=model_name
            )
            save_pipeline(data.estimators[model_name], filepath_model)
            self.log_info(self.transform, f"'{model_name}' model exported to {filepath_model.absolute()}")

        self.log_info(self.transform, "Exporting the best model completed")

        return True
