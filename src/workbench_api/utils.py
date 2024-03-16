import pandas as pd
from sklearn.base import BaseEstimator

from workbench_api.models.predict import PredictionInputModel
from workbench_components.common.common_configs import FILEPATH_MODELS_DEFAULT, REGEX_MODELS_DEFAULT
from workbench_utils.export import load_estimator_from_directory


def get_predicted_value(prediction_input: PredictionInputModel, model: BaseEstimator) -> float:
    """
    Makes a prediction based on the given prediction input.

    Parameters:
    prediction_input (PredictionInputModel): The prediction input model containing the necessary data.
    model (BaseEstimator): The predictive model used for making the prediction.

    Returns:
    float: The predicted value.
    """
    prediction_input_df = pd.DataFrame([prediction_input.model_dump()])
    return model.predict(prediction_input_df)[0][0]


def get_model() -> BaseEstimator:
    """
    Loads and returns a machine learning model.

    Returns:
        The loaded machine learning model.

    Raises:
        FileNotFoundError: If the model file is not found.
    """
    model = load_estimator_from_directory(FILEPATH_MODELS_DEFAULT, REGEX_MODELS_DEFAULT)
    return model


def get_id(db: dict[int, dict]) -> int:
    """
    Returns the next available id for a given database.

    Parameters:
    db (dict[int, dict]): The database for which to get the next available id.

    Returns:
    int: The next available id.
    """
    return len(db) + 1
