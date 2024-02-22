from workbench_process.process_data import ProcessData


class TestProcessData:

    def test_process_data(self):
        process_data = ProcessData()

        assert isinstance(process_data, ProcessData)
        assert process_data.compressive_strength is not None
        assert process_data.compressive_strength.empty
        assert process_data.compressive_strength.shape == (0, 0)
