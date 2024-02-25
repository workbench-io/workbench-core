import pytest

from workbench_process.common import Source
from workbench_process.process_data import ProcessData


class TestProcessData:

    def test_process_data(self):
        process_data = ProcessData()

        assert isinstance(process_data, ProcessData)

    @pytest.mark.parametrize(
        "attribute",
        [
            Source.COMPRESSIVE_STRENGTH,
        ],
    )
    def test_process_data_source_attributes(self, attribute: str):
        process_data = ProcessData()

        source_attribute = getattr(process_data, attribute)

        assert source_attribute is not None
        assert source_attribute.empty
        assert source_attribute.shape == (0, 0)
