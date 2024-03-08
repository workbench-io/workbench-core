import os
from pathlib import Path

import joblib
from sklearn.pipeline import Pipeline


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


def remove_old_pipelines(path_models: Path) -> None:
    """
    Removes old model pipelines
    """
    for model_file in path_models.glob("*.pkl"):
        model_file.unlink()
