from pathlib import Path

import pandas as pd

from workbench_process.common import Source
from workbench_process.process_config import ProcessConfig
from workbench_process.process_data import ProcessData
from workbench_process.sources.source_compressive_strength import SourceCompressiveStrength


class TestSourceCompressiveStrength:

    def test_source_should_instantiate(self) -> None:
        source = SourceCompressiveStrength()

        assert source is not None
        assert isinstance(source, SourceCompressiveStrength)

    def test_load_should_return_true(
        self,
        filepath_compressive_strength: Path,
        process_data: ProcessData,
        process_config: ProcessConfig,
    ) -> None:
        source = SourceCompressiveStrength()
        result = source.load(filepath_compressive_strength, process_data, process_config)

        assert result is True

    def test_load_should_add_dataframe_as_attribute_to_data_object(
        self,
        filepath_compressive_strength: Path,
        process_data: ProcessData,
        process_config: ProcessConfig,
    ) -> None:
        source = SourceCompressiveStrength()

        source.load(filepath_compressive_strength, process_data, process_config)

        assert hasattr(process_data, Source.COMPRESSIVE_STRENGTH)

    def test_load_should_add_non_empty_dataframe_as_attribute_to_data_object(
        self,
        filepath_compressive_strength: Path,
        process_data: ProcessData,
        process_config: ProcessConfig,
    ) -> None:
        source = SourceCompressiveStrength()

        source.load(filepath_compressive_strength, process_data, process_config)

        data_attribute = getattr(process_data, Source.COMPRESSIVE_STRENGTH)

        assert isinstance(data_attribute, pd.DataFrame)
        assert not data_attribute.empty
        assert data_attribute.shape == (1030, 9)
