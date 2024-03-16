from typing import Literal, Union

from pydantic import BaseModel, Field


class OptimizeSettingsModel(BaseModel):
    """Model for the settings of the train step."""

    num_genes: int = Field(..., ge=1)
    num_generations: int = Field(..., ge=1)
    sol_per_pop: int = Field(..., ge=1)
    num_parents_mating: int = Field(..., ge=1)
    keep_parents: Literal[-1, 0] | int
    init_range_low: int
    init_range_high: int
    gene_space: Union[dict[str, int], list[int], list[dict[str, int]]]
    parent_selection_type: Literal["sss", "rws", "sus", "random", "tournament", "tournament_nsga2", "nsga2", "rank"]
    crossover_type: Literal["single_point", "two_points", "uniform", "scattered"] | None
    crossover_probability: float = Field(..., ge=0, le=1)
    mutation_type: Literal["random", "swap", "scramble", "inversion", "adaptive"] | None
    mutation_probability: float = Field(..., ge=0, le=1)
    random_seed: int | None
