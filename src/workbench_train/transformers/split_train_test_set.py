from sklearn.model_selection import train_test_split

from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings


class SplitTrainTestSet(WorkbenchTransformer):
    """Split data into training and test sets."""

    def transform(self, data: TrainData, settings: TrainSettings) -> bool:
        """Split data into training and test sets."""

        self.log_info(self.transform, "Spliting Data")

        x_train, x_test, y_train, y_test = train_test_split(
            data.features,
            data.targets,
            test_size=settings.model.test_size,
            random_state=settings.model.seed,
        )

        data.x_train = x_train
        data.x_test = x_test
        data.y_train = y_train
        data.y_test = y_test

        self.log_info(self.transform, "Data spliting completed")
        self.log_debug(self.transform, f"train set size: {len(data.x_train)}; test set size: {len(data.x_test)}")

        return True
