from typing import Any, TypeVar

import pandas as pd
from sklearn.base import BaseEstimator

from workbench_api.models.predict import PredictionInputModel
from workbench_components.common.common_configs import FILEPATH_MODELS_DEFAULT, REGEX_MODELS_DEFAULT
from workbench_utils.export import load_estimator_from_directory

T = TypeVar("T")


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


def get_next_id(db: dict[int, Any] | list[Any]) -> int:
    """
    Returns the next available id for a given database.

    Parameters:
    db (dict[int, Any] | list[Any]): The database for which to get the next available id.

    Returns:
    int: The next available id.
    """
    return len(db) + 1


def get_db_entry_by_id(db: list[T], db_id: int) -> T:
    """
    Returns the database entry with the given id.

    Parameters:
    db (list[T]): The database from which to get the entry.
    db_id (int): The id of the entry to get.

    Returns:
    T: The entry with the given id.
    """

    result = [entry for entry in db if int(entry.id) == int(db_id)]

    if result:
        return result[0]
    return None


def get_index_of_db_entry_by_id(db: list[T], db_id: int) -> T:
    """
    Returns the index of the database entry with the given id.

    Parameters:
    db (list[T]): The database from which to get the entry.
    db_id (int): The id of the entry to get.

    Returns:
    T: The entry with the given id.
    """

    for index, entry in enumerate(db):
        if entry.id == db_id:
            return index

    return None


def create_list() -> list:
    return []
