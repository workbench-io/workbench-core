from workbench_train.train_data import TrainData
from workbench_train.train_logic import TrainLogic
from workbench_train.train_settings import TrainSettings


class TestTrain:

    def test_run_should_return_true(
        self,
        train_data: TrainData,
        train_settings: TrainSettings,
    ):
        train = TrainLogic()
        result = train.run(train_data, train_settings)

        assert isinstance(result, bool)
        assert result
