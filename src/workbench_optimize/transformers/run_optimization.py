import pygad

from workbench_components.workbench_transformer.workbench_transformer import WorkbenchTransformer
from workbench_optimize.optimize_data import OptimizeData
from workbench_optimize.optimize_settings import OptimizeSettings
from workbench_utils.composition import convert_to_percentage, create_composition_dataframe_from_percentages_list
from workbench_utils.export import load_pipeline

DEFAULT_AGE = 28


class RunOptimizationError(Exception):
    """Run optimization error"""


class RunOptimization(WorkbenchTransformer):
    """Run optimization logic"""

    def transform(self, data: OptimizeData, settings: OptimizeSettings) -> bool:
        """Run optimization logic"""

        self.log_info(self.transform, "Starting optimization logic")

        global model  # pylint: disable=global-variable-undefined
        model = load_pipeline(settings.model.path_model)
        optimizer = self._create_optimizer_instance(settings)
        optimizer.run()

        self.log_info(self.transform, "Optimization logic completed")

        return True

    @staticmethod
    def _fitness_func(ga_instance: pygad.GA, solution, solution_idx: int):  # pylint: disable=unused-argument

        percentages_list = convert_to_percentage(solution)
        solution_df = create_composition_dataframe_from_percentages_list(percentages_list, age=DEFAULT_AGE)
        prediction = model.predict(solution_df)[0][0]

        return prediction

    def _create_optimizer_instance(self, settings: OptimizeSettings) -> pygad.GA:
        """Create optimizer instance"""
        ga_instance = pygad.GA(
            fitness_func=self._fitness_func,
            **settings.model.genetic_algorithm.model_dump(),
        )

        return ga_instance

    def _run_optimization(self, name: str, data: OptimizeData, settings: OptimizeSettings):
        """Run optimization logic"""

    def _save_results(self, name: str, data: OptimizeData, settings: OptimizeSettings):
        """Save results from optimization"""
