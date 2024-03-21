import json
import shutil
from pathlib import Path

from workbench_optimize.common import OptimizationResult


class TestOptimizationResult:

    def test_save(self, tmp_path: Path):

        filepath = tmp_path / "test.json"

        try:
            OptimizationResult(value=1.0, solution={"a": 1.0}, metadata={"b": 2.0}).save(filepath)

            assert (filepath).exists()

            result = json.loads(filepath.read_text())
            assert result == {"value": 1.0, "solution": {"a": 1.0}, "metadata": {"b": 2.0}}

        finally:
            shutil.rmtree(tmp_path)
