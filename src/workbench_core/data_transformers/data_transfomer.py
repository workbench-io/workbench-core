"""Base class for data transformers"""


class DataTransformer:
    """Base class for data transformers"""

    def transform(self, data) -> bool:  # pylint: disable=unused-argument
        """Transform data and return True if successful, False otherwise."""
        return True
