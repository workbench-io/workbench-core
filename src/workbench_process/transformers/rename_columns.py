from workbench_components.workbench_data.workbench_data import WorkbenchData
from workbench_components.workbench_settings.workbench_settings import WorkbenchSettings
from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_process.common import Source


class RenameColumns(WorkbenchTransformer):
    """Rename columns in a DataFrame."""

    def transform(self, data: WorkbenchData, settings: WorkbenchSettings) -> bool:  # pylint: disable=unused-argument
        """Renames columns in a DataFrame."""

        for source in Source:
            self.log_debug(self.transform, f"Renaming columns for {source.value}")

            source_data = getattr(settings.model.sources, source.value, None)
            if source_data is None:
                self.log_debug(self.transform, f"No column map found for {source.value}")
                continue

            column_mapping = {value: key for key, value in source_data.columns.items()}
            self.log_debug(self.transform, f"Using column map:{column_mapping}")

            data_renamed = data.get_data(source).rename(columns=column_mapping)
            data.set_data(source, data_renamed)

        return True
