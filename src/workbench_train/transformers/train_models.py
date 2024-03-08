import warnings
from typing import Callable

import numpy as np
from sklearn.compose import TransformedTargetRegressor
from sklearn.metrics import (
    make_scorer,
    max_error,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    root_mean_squared_error,
)
from sklearn.model_selection import RandomizedSearchCV
from sklearn.pipeline import Pipeline
from sklearn.utils import parallel_backend

from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_train.common import Metrics
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings
from workbench_utils.warning import filter_warnings

filter_warnings()

METRIC_TO_SCORER_MAP: dict[str, Callable] = {
    Metrics.MSE: make_scorer(
        score_func=mean_squared_error,
        squared=True,
        greater_is_better=False,
    ),
    Metrics.RMSE: make_scorer(
        score_func=root_mean_squared_error,
        greater_is_better=False,
    ),
    Metrics.MAE: make_scorer(
        score_func=mean_absolute_error,
        greater_is_better=False,
    ),
    Metrics.MAX_ERROR: make_scorer(
        score_func=max_error,
        greater_is_better=False,
    ),
    Metrics.R2: make_scorer(
        score_func=r2_score,
        greater_is_better=True,
    ),
}


class TrainModels(WorkbenchTransformer):
    """Trains models by performing cross validation on the pipeline"""

    def transform(self, data: TrainData, settings: TrainSettings) -> bool:
        """Trains models by performing cross validation on the pipeline"""

        self.log_info(self.transform, "Training models")

        self._train_models(data, settings)

        self.log_info(self.transform, "Training of models completed")

        return True

    def _train_models(self, data: TrainData, settings: TrainSettings) -> None:

        with parallel_backend("multiprocessing"):
            with warnings.catch_warnings():
                filter_warnings()

                for model_name, model_data in data.model_objects.items():

                    self.log_debug(self._train_models, f"Fitting '{model_name}' model")

                    pipeline = self._get_pipeline(data, model_data["model"])

                    rs = RandomizedSearchCV(
                        estimator=pipeline,
                        param_distributions=model_data["params"],
                        scoring=self._get_scorers(settings),
                        n_iter=settings.model.training.search_iterations,
                        cv=settings.model.training.cross_validation.folds,
                        refit=settings.model.training.cross_validation.metric,
                        n_jobs=settings.model.training.n_jobs,
                        random_state=settings.model.seed,
                    )

                    rs.fit(data.x_train, data.y_train)

                    test_set_scores = self._get_test_set_scores(rs, data)
                    data.results[model_name] = test_set_scores
                    data.estimators[model_name] = rs

                    self.log_debug(
                        self._train_models, f"Results for '{model_name}': {test_set_scores}", extra=test_set_scores
                    )

    def _get_scorers(self, settings: TrainSettings) -> dict[str, Callable]:
        scorers_subset = {
            metric: scorer
            for metric, scorer in METRIC_TO_SCORER_MAP.items()
            if metric in settings.model.training.cross_validation.scores
        }

        return scorers_subset

    def _get_pipeline(self, data: TrainData, regressor) -> Pipeline:

        pipeline = Pipeline(
            steps=[
                ("preprocessor", data.preprocessor),
                (
                    "model",
                    TransformedTargetRegressor(
                        regressor=regressor,
                        func=np.log1p,
                        inverse_func=np.expm1,
                    ),
                ),
            ]
        )

        return pipeline

    def _get_test_set_scores(self, model, data: TrainData) -> dict[str, float]:
        y_pred = model.predict(data.x_test)

        test_set_scores = {
            Metrics.MSE: mean_squared_error(data.y_test, y_pred),
            Metrics.RMSE: root_mean_squared_error(data.y_test, y_pred),
            Metrics.MAE: mean_absolute_error(data.y_test, y_pred),
            Metrics.MAX_ERROR: max_error(data.y_test, y_pred),
            Metrics.R2: r2_score(data.y_test, y_pred),
        }

        return test_set_scores
