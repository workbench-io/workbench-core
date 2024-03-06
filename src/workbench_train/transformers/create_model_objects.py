# Contains model object and the parameters to be used for hyperparameter tuning

import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import ElasticNet, Lasso
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR

from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings

MODEL_TO_MODEL_REGRESSOR_MAP = {
    "pls": {
        "model": PLSRegression(max_iter=1000),
        "params": {
            "model__regressor__n_components": range(1, 5),
        },
    },
    "lasso": {
        "model": Lasso(
            random_state=1,
        ),
        "params": {
            "model__regressor__max_iter": [250, 500, 1000],
            "model__regressor__alpha": np.logspace(-6, 6, 13),
        },
    },
    "elasticnet": {
        "model": ElasticNet(
            random_state=1,
            max_iter=1000,
        ),
        "params": {
            "model__regressor__alpha": np.logspace(-6, 6, 13),
            "model__regressor__l1_ratio": [0.1, 0.25, 0.5, 0.75, 0.9],
        },
    },
    "svr": {
        "model": SVR(verbose=False),
        "params": {
            "model__regressor__kernel": ["linear", "poly", "rbf"],
            "model__regressor__degree": [2, 3, 4],
            "model__regressor__C": np.logspace(-3, 3, 7),
            "model__regressor__tol": np.logspace(-3, -1, 3),
            "model__regressor__epsilon": np.logspace(-2, 2, 5),
        },
    },
    "random_forest": {
        "model": RandomForestRegressor(
            criterion="squared_error",
            n_jobs=-1,
            random_state=1,
            verbose=False,
        ),
        "params": {
            "model__regressor__n_estimators": [100, 250, 500],
            "model__regressor__max_depth": [3, 5, 10, None],
            "model__regressor__max_features": [0.3, 0.5, 0.7, None],
            "model__regressor__min_samples_leaf": [5, 10, 25, 50],
        },
    },
    "gbm": {
        "model": GradientBoostingRegressor(
            loss="squared_error",
            random_state=1,
            verbose=False,
        ),
        "params": {
            "model__regressor__n_estimators": [50, 100],
            "model__regressor__learning_rate": np.logspace(-3, 3, num=5),
            "model__regressor__max_depth": [3, 5, 10],
            "model__regressor__max_features": [0.3, 0.7, None],
            "model__regressor__min_samples_leaf": [1, 10],
            "model__regressor__min_samples_split": [2],
        },
    },
    "neural_network": {
        "model": MLPRegressor(
            solver="adam",
            n_iter_no_change=10,
            random_state=1,
            verbose=False,
        ),
        "params": {
            "model__regressor__activation": ["relu", "logistic", "tanh"],
            "model__regressor__max_iter": [250, 500, 1000, 2000],
            "model__regressor__hidden_layer_sizes": [(5,), (10,), (20,), (3, 3), (5, 5), (5, 2), (3, 2), (4, 2)],
            "model__regressor__learning_rate_init": np.logspace(-3, 3, 7),
        },
    },
}


class CreateModelObjects(WorkbenchTransformer):
    """Create a dictionary of selected model objects and parameters to tune during cross-validation"""

    def transform(self, data: TrainData, settings: TrainSettings) -> bool:
        """Create a dictionary of selected model objects and parameters to tune during cross-validation"""

        self.log_info(self.transform, "Creating pre-processor")
        data.model_objects = self._create_objects(settings)

        return True

    def _create_objects(self, settings: TrainSettings) -> dict[str, dict]:

        models_data = {}

        for model_name in settings.model.training.models:
            if model_name in MODEL_TO_MODEL_REGRESSOR_MAP:
                self.log_debug(
                    self._create_objects,
                    f"Adding {model_name} to model selection",
                )

                models_data[model_name] = MODEL_TO_MODEL_REGRESSOR_MAP[model_name]

        return models_data
