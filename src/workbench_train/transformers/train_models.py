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

from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_train.train_data import TrainData
from workbench_train.train_settings import TrainSettings

METRIC_TO_SCORER_MAP: dict[str, Callable] = {
    "mse": make_scorer(
        score_func=mean_squared_error,
        squared=True,
        greater_is_better=False,
    ),
    "rmse": make_scorer(
        score_func=root_mean_squared_error,
        greater_is_better=False,
    ),
    "mae": make_scorer(
        score_func=mean_absolute_error,
        greater_is_better=False,
    ),
    "max_error": make_scorer(
        score_func=max_error,
        greater_is_better=False,
    ),
    "r2": make_scorer(
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

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            for model_name, model_data in data.model_objects.items():

                self.log_debug(self._train_models, f"Fitting '{model_name}' model")

                pipeline = self._get_pipeline(data, model_data["model"])

                # Hyperparameter tuning with k-fold cross-validation
                rs = RandomizedSearchCV(
                    estimator=pipeline,
                    param_distributions=model_data["params"],
                    n_iter=settings.model.training.search_iterations,
                    random_state=settings.model.seed,
                    cv=settings.model.training.cross_validation.folds,
                    scoring=self._get_scorers(settings),
                    refit=settings.model.training.cross_validation.metric,
                    return_train_score=False,
                    n_jobs=settings.model.training.n_jobs,
                )

                rs.fit(data.x_train, data.y_train)

                test_set_scores = self._get_test_set_scores(rs, data)
                data.results[model_name] = test_set_scores

                self.log_debug(
                    self._train_models, f"Results for {model_name}: {test_set_scores}", extra=test_set_scores
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
            "mse": mean_squared_error(data.y_test, y_pred),
            "rmse": root_mean_squared_error(data.y_test, y_pred),
            "mae": mean_absolute_error(data.y_test, y_pred),
            "max_error": max_error(data.y_test, y_pred),
            "r2": r2_score(data.y_test, y_pred),
        }

        return test_set_scores
