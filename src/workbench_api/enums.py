from enum import StrEnum, auto


class Routers(StrEnum):
    """Enum for routers available for the API."""

    PREDICT = auto()
    OPTIMIZE = auto()


class RoutersPath(StrEnum):
    """Enum for routers path available for the API."""

    PREDICT = "/predict"
    OPTIMIZE = "/optimize"
