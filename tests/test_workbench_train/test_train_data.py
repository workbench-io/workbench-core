import pandas as pd
from pandas.testing import assert_frame_equal

from workbench_process.process_data import ProcessData
from workbench_train.train_data import TrainData


class TestTrainData:

    def test_train_data(self):
        train_data = TrainData()

        assert isinstance(train_data, TrainData)

    def test_train_data_from_process_data_loads_data_from_process_data_object(self):

        process_data = ProcessData()
        process_data.compressive_strength = pd.DataFrame({"A": [1, 2, 3]})

        train_data = TrainData()
        train_data.from_process_data(process_data)

        assert_frame_equal(train_data.processed, pd.DataFrame({"A": [1, 2, 3]}))
