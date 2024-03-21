import os
from pathlib import Path

import joblib
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline


def get_filepath_from_directory(directory: Path, regex: str) -> Path:
    """Get the file path from a directory using a regex"""
    return list(directory.glob(regex))[0]


def save_pipeline(pipeline_to_persist: Pipeline, filepath: os.PathLike) -> None:
    """Saves the pipeline to a pkl file

    Args:
        pipeline_to_persist (Pipeline): pipeline to save
        filepath (os.PathLike): file path to save the file
    """
    joblib.dump(pipeline_to_persist, filepath)


def load_pipeline(filepath: os.PathLike) -> Pipeline:
    """Load a pipeline saved as a pkl file

    Args:
        filepath (os.PathLike): file path of file

    Returns:
        Pipeline: a scikit-learn Pipeline object
    """
    trained_model = joblib.load(filename=filepath)
    return trained_model


def remove_old_pipelines(path_models: Path, regex: str = "*.pkl") -> None:
    """
    Removes old model pipelines
    """
    for model_file in path_models.glob(regex):
        model_file.unlink()


def load_estimator_from_directory(directory: Path, regex: str = "*.pkl") -> BaseEstimator:
    """
    Loads a machine learning model from a directory.

    Args:
        directory (Path): The directory where the model file is located.
        regex (str, optional): The regular expression pattern to match the model file. Defaults to "*.pkl".

    Returns:
        BaseEstimator: The loaded machine learning model.

    Raises:
        FileNotFoundError: If the model file is not found at the specified directory.

    """
    filepath = get_filepath_from_directory(directory, regex)

    if filepath.exists():
        model = load_pipeline(filepath)
    else:
        raise FileNotFoundError(f"Model file not found at {filepath}")

    return model
