from enum import StrEnum, auto

STEP_NAME = "train"


class Source(StrEnum):
    """Enum for sources."""

    COMPRESSIVE_STRENGTH = auto()
