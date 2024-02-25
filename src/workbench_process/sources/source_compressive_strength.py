import os
import tempfile
from pathlib import Path
from zipfile import ZipFile

import pandas as pd
import wget

from workbench_components.workbench_source.workbench_source import WorkbenchSource
from workbench_process.common import Source
from workbench_process.process_data import ProcessData
from workbench_process.process_settings import ProcessSettings


class SourceCompressiveStrength(WorkbenchSource):
    """Source for compressive strength data."""

    def __init__(self):
        super().__init__()

    def load(
        self,
        data: ProcessData,
        settings: ProcessSettings,
    ) -> bool:

        source = settings.model.sources.compressive_strength.path

        self.log_info(self.load, f"Loading data from {source}")

        df = self._get_data(settings)
        data.set_data(Source.COMPRESSIVE_STRENGTH, df)

        self.log_info(self.load, f"Loaded data for {Source.COMPRESSIVE_STRENGTH}")

        return True

    def _get_data(
        self,
        settings: ProcessSettings,
    ) -> pd.DataFrame:

        source = settings.model.sources.compressive_strength.path

        with tempfile.TemporaryDirectory() as temp_dir:
            if isinstance(source, str) and source.startswith("http"):
                filepath = os.path.join(temp_dir, "downloaded_file.zip")
                wget.download(source, out=filepath)
            elif isinstance(source, Path):
                filepath = str(source)

            with ZipFile(filepath, "r") as zip_file:
                zip_file.extractall(temp_dir)

            pattern = settings.model.sources.compressive_strength.pattern
            files = list(Path(temp_dir).glob(pattern))

            if not files:
                raise FileNotFoundError(f"No file found matching the pattern: {pattern}")

            selected_file = files[0]

            df = pd.read_excel(selected_file)

            return df
