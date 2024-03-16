from typing import Literal, Optional, Union

from pydantic import BaseModel, Field


class OptimizeInputModel(BaseModel):
    """Model for the settings of the train step."""

    num_genes: Optional[int] = Field(7, ge=1)
    num_generations: Optional[int] = Field(10, ge=1)
    sol_per_pop: Optional[int] = Field(10, ge=1)
    num_parents_mating: Optional[int] = Field(5, ge=1)
    keep_parents: Optional[Literal[-1, 0] | int] = 0
    init_range_low: Optional[int | float] = 0
    init_range_high: Optional[int | float] = 100
    gene_space: Optional[Union[dict[str, int], list[int], list[dict[str, int]]]] = {"low": 0, "high": 100}
    parent_selection_type: Optional[
        Literal["sss", "rws", "sus", "random", "tournament", "tournament_nsga2", "nsga2", "rank"]
    ] = "sss"
    crossover_type: Optional[Literal["single_point", "two_points", "uniform", "scattered"] | None] = "single_point"
    crossover_probability: Optional[float] = Field(0.2, ge=0, le=1)
    mutation_type: Optional[Literal["random", "swap", "scramble", "inversion", "adaptive"] | None] = "random"
    mutation_probability: Optional[float] = Field(0.2, ge=0, le=1)
    random_seed: Optional[int | None] = 1


class OptimizeOutputModel(BaseModel):

    best_value: float
    best_solution: dict[str, float]
