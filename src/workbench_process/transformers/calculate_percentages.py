from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_process.common import Source
from workbench_process.process_data import ProcessData
from workbench_process.process_settings import ProcessSettings


class CalculatePercentages(WorkbenchTransformer):
    """Calculate percentages from quantities of components."""

    def transform(self, data: ProcessData, settings: ProcessSettings) -> bool:
        """Calculate percentages from quantities of components."""

        self.log_debug(self.transform, "Calculating percentages")

        df = data.get_data(Source.COMPRESSIVE_STRENGTH)
        df[settings.model.features.composition] = df[settings.model.features.composition].apply(
            lambda x: (x / sum(x)) * 100, axis=1
        )

        data.set_data(Source.COMPRESSIVE_STRENGTH, df)

        self.log_debug(self.transform, "Percentages calculated")

        return True
