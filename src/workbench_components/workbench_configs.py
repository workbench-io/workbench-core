from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

ENCODING = "utf-8"

FILEPATH_LOGS_DEFAULT = Path(__file__).parent.parent.parent.joinpath("logs/logs.log").resolve()
FILEPATH_MODELS_DEFAULT = Path(__file__).parent.parent.parent.joinpath("output/models").resolve()

REGEX_MODELS_DEFAULT = "*.pkl"


class WorkbenchConfigs(BaseSettings):

    env_state: Literal["dev", "test", "prod"] = "dev"
    logs_filepath: Path
    models_filepath: Path
    models_regex: str = "*.pkl"
    encoding: str = ENCODING

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding=ENCODING)


workbench_configs = WorkbenchConfigs()
