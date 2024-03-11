from pathlib import Path
from typing import Union

from pydantic import BaseModel


class GeneticAlgorithmSettingsModel(BaseModel):
    """Settings for the genetic algorithm."""

    num_genes: int
    num_generations: int
    sol_per_pop: int
    num_parents_mating: int
    keep_parents: int
    init_range_low: int
    init_range_high: int
    mutation_percent_genes: int
    gene_space: Union[dict[str, int], list[int], list[dict[str, int]]]
    parent_selection_type: str
    crossover_type: str
    mutation_type: str
    random_seed: int


class OptimizeSettingsModel(BaseModel):
    """Model for the settings of the train step."""

    verbose: bool
    path_model: Path
    genetic_algorithm: GeneticAlgorithmSettingsModel
