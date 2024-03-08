import warnings

from sklearn.exceptions import ConvergenceWarning


def filter_warnings() -> None:
    """Filter warnings from scikit-learn."""
    warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")
    warnings.filterwarnings("ignore", category=ConvergenceWarning, module="sklearn")
    warnings.filterwarnings("ignore", category=RuntimeWarning, module="sklearn")
