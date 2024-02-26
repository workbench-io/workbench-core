from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_process.common import Source
from workbench_process.process_data import ProcessData
from workbench_process.process_settings import ProcessSettings


class RenameColumns(WorkbenchTransformer):
    """Rename columns in a DataFrame."""

    def transform(self, data: ProcessData, settings: ProcessSettings) -> bool:
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
