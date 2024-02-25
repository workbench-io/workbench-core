import os
import tempfile
from pathlib import Path
from typing import Union
from zipfile import ZipFile

import pandas as pd
import wget

from workbench_components.workbench_source.workbench_source import WorkbenchSource
from workbench_process.process_config import ProcessConfig
from workbench_process.process_data import ProcessData


class SourceCompressiveStrength(WorkbenchSource):
    """Source for compressive strength data."""

    def __init__(self):
        super().__init__()

    def load(
        self,
        source: Union[str, os.PathLike],
        data: ProcessData,
        config: ProcessConfig,
    ) -> bool:
        self.log_info(self.load, f"Loading data from {source}")

        with tempfile.TemporaryDirectory() as temp_dir:
            filepath = self._get_filepath(source)

            with ZipFile(filepath, "r") as zip_file:
                zip_file.extractall(temp_dir)

            pattern = config.configs.sources.compressive_strength.pattern
            files = list(Path(temp_dir).glob(pattern))

            if not files:
                raise FileNotFoundError(f"No file found matching the pattern: {pattern}")

            selected_file = files[0]

            df = pd.read_excel(selected_file)
            data.compressive_strength = df

        return True

    def _get_filepath(self, source: Union[str, os.PathLike]) -> str:
        if isinstance(source, str) and source.startswith("http"):
            with tempfile.TemporaryDirectory() as temp_dir:
                filepath = os.path.join(temp_dir, "downloaded_file.zip")
                wget.download(source, out=filepath)
                return filepath
        elif isinstance(source, Path):
            return str(source)
        else:
            return source
