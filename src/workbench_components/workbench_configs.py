from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

ENCODING_DEFAULT = "utf-8"


class WorkbenchConfigs(BaseSettings):

    env_state: Literal["dev", "test", "prod"] = "dev"
    logs_filepath: Path
    models_filepath: Path
    database_filepath: Path
    models_regex: str = "*.pkl"
    encoding: str = ENCODING_DEFAULT

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding=ENCODING_DEFAULT)


workbench_configs = WorkbenchConfigs()
