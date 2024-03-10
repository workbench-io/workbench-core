from enum import StrEnum, auto


class WorkbenchSteps(StrEnum):
    """
    Steps in Workbench.

    - PROCESS: Loading and processing data.
    - TRAIN: Training the model.
    """

    PROCESS = auto()
    TRAIN = auto()
    OPTIMIZE = auto()
