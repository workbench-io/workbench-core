from pathlib import Path

ENCODING = "utf-8"

DEFAULT_LOG_FILEPATH = Path(__file__).parent.parent.parent.parent.parent.joinpath("logs/logs.log").resolve()
