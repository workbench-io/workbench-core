from pathlib import Path
from typing import Any, Optional

from pydantic import BaseModel, Field

from workbench_components.common.common_configs import ENCODING


class OptimizationResult(BaseModel):
    """Class to store the result of an optimization process."""

    best_value: float
    best_solution: dict[str, float] = Field(default_factory=dict)
    metadata: Optional[dict[str, Any]] = None

    def save(self, filepath: Path, *args, **kwargs) -> None:
        """
        Save the model's results as a JSON file.

        Args:
            filepath (Path): The path to save the JSON file.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            None
        """

        results_json = self.model_dump_json(*args, **kwargs)

        with open(filepath, "w", encoding=ENCODING) as file:
            file.write(results_json)
