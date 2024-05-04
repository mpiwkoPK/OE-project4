import copy
import random

import numpy as np


class MutationMethod:
    def mutate(self, individual, mutation_rate):
        pass

class UniformMutation(MutationMethod):
    def __init__(self, number_of_dimensions):
        self.number_of_dimensions = number_of_dimensions

    def mutate(self, individual, mutation_rate):
        mutated_individual = individual.copy()
        for i in range(self.number_of_dimensions):
            if random.random() < mutation_rate:
                mutation_value = random.uniform(-1, 1) 
                mutated_individual[i] += mutation_value
                mutated_individual[i] = max(min(mutated_individual[i], 1), -1) 
        return mutated_individual

class GaussMutation(MutationMethod):
    def __init__(self, number_of_dimensions, mean, sigma):
        self.number_of_dimensions = number_of_dimensions
        self.mean = mean
        self.sigma = sigma

    def mutate(self, individual, mutation_rate):
        mutated_individual = individual.copy()
        for i in range(self.number_of_dimensions):
            if random.random() < mutation_rate:
                mutation_value = random.gauss(self.mean, self.sigma)
                mutated_individual[i] += mutation_value
        return mutated_individual
