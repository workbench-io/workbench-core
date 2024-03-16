from pathlib import Path

ENCODING = "utf-8"

FILEPATH_LOGS_DEFAULT = Path(__file__).parent.parent.parent.parent.joinpath("logs/logs.log").resolve()
FILEPATH_MODELS_DEFAULT = Path(__file__).parent.parent.parent.parent.joinpath("output/models").resolve()

REGEX_MODELS_DEFAULT = "*.pkl"
