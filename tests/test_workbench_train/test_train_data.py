from workbench_train.train_data import TrainData


class TestTrainData:

    def test_train_data(self):
        train_data = TrainData()

        assert isinstance(train_data, TrainData)
