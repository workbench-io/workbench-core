import pandas as pd

from workbench_process.common import Source
from workbench_process.process_data import ProcessData
from workbench_process.process_settings import ProcessSettings
from workbench_process.sources.source_compressive_strength import SourceCompressiveStrength


class TestSourceCompressiveStrength:

    def test_source_should_instantiate(self) -> None:
        source = SourceCompressiveStrength()

        assert source is not None
        assert isinstance(source, SourceCompressiveStrength)

    def test_load_should_return_true(
        self,
        process_data: ProcessData,
        process_settings: ProcessSettings,
    ) -> None:
        source = SourceCompressiveStrength()
        result = source.load(process_data, process_settings)

        assert result is True

    def test_load_should_add_dataframe_as_attribute_to_data_object(
        self,
        process_data: ProcessData,
        process_settings: ProcessSettings,
    ) -> None:
        source = SourceCompressiveStrength()

        source.load(process_data, process_settings)

        assert hasattr(process_data, Source.COMPRESSIVE_STRENGTH)

    def test_load_should_add_non_empty_dataframe_as_attribute_to_data_object(
        self,
        process_data: ProcessData,
        process_settings: ProcessSettings,
    ) -> None:
        source = SourceCompressiveStrength()

        source.load(process_data, process_settings)

        data_attribute = getattr(process_data, Source.COMPRESSIVE_STRENGTH)

        assert isinstance(data_attribute, pd.DataFrame)
        assert not data_attribute.empty
        assert data_attribute.shape == (1030, 9)
