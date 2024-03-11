from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class OptimizationResult:
    """Class to store the result of an optimization process."""

    best_value: float
    best_solution: dict[str, float] = field(default_factory=dict)
    metadata: Optional[dict[str, Any]] = None
