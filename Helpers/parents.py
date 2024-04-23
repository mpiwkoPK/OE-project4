from typing import Any

import numpy as np
from numpy import ndarray, dtype


def initPopulation(number_of_dimensions: int, population_size: int) -> ndarray[Any, dtype[Any]]:
    return np.array([np.random.sample(number_of_dimensions) for _ in range(population_size)])


