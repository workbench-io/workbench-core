import pandas as pd

from workbench_api.models import PredictionInputModel


def get_predicted_value(prediction_input: PredictionInputModel, model) -> float:
    """
    Makes a prediction based on the given prediction input.

    Parameters:
    prediction_input (PredictionInputModel): The prediction input model containing the necessary data.
    model: The predictive model used for making the prediction.

    Returns:
    float: The predicted value.

    """
    prediction_input_df = pd.DataFrame([prediction_input.model_dump()])
    return model.predict(prediction_input_df).ravel()[0]
