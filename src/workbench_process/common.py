from enum import StrEnum, auto

STEP_NAME = "process"


class Source(StrEnum):
    """Enum for sources."""

    COMPRESSIVE_STRENGTH = auto()
