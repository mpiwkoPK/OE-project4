import copy
import random

import numpy as np


class Inversion:
     def inverse(self, individual, inversion_probability):
        pass

class InversionMethod(Inversion):
    def __init__(self, number_of_dimensions):
        self.number_of_dimensions = number_of_dimensions

    def inverse(self, individual: np.ndarray, inversion_probability):
        inverted_individual = copy.copy(individual)
        if random.random() < inversion_probability:
            start = random.randint(0, inverted_individual.shape[0] - 2)
            end = random.randint(start, inverted_individual.shape[0] - 1)
            inverted_fragment = np.flip(inverted_individual[start:end + 1])
            if len(inverted_individual[:start]) != 0 and len(inverted_individual[end + 1:]) != 0:
                return np.append(np.append(inverted_individual[:start], inverted_fragment), inverted_individual[end + 1:])
        return individual
