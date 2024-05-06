import copy
import random

import numpy as np


class MutationMethod:
    def mutate(self, individual, mutation_rate):
        pass


class UniformMutation(MutationMethod):
    def __init__(self, number_of_dimensions, start_value, end_value):
        self.number_of_dimensions = number_of_dimensions
        if start_value > end_value:
            self.start_value = end_value
            self.end_value = start_value
        else:
            self.start_value = start_value
            self.end_value = end_value

    def mutate(self, individual, mutation_rate):
        mutated_individual = individual.copy()

        for i in range(self.number_of_dimensions):
            if random.random() < mutation_rate:
                mutated_random_index = random.randint(0, len(mutated_individual) - 1)
                mutation_value = random.uniform(self.start_value, self.end_value)
                mutated_individual[mutated_random_index] = mutation_value
                mutated_individual[i] = min(max(mutated_individual[i], self.start_value), self.end_value)

            else:
                mutated_individual[i] = individual[i]
        return mutated_individual


class GaussMutation(MutationMethod):
    def __init__(self, number_of_dimensions, mean, sigma, start_value, end_value):
        self.number_of_dimensions = number_of_dimensions
        self.mean = mean
        self.sigma = sigma
        if start_value > end_value:
            self.start_value = end_value
            self.end_value = start_value
        else:
            self.start_value = start_value
            self.end_value = end_value

    def mutate(self, individual, mutation_rate):
        mutated_individual = individual.copy()
        for i in range(self.number_of_dimensions):
            if random.random() < mutation_rate:
                mutation_value = random.gauss(self.mean, self.sigma)
                mutated_individual[i] += mutation_value
                mutated_individual[i] = min(max(mutated_individual[i], self.start_value), self.end_value)
            else:
                mutated_individual[i] = individual[i]
        return mutated_individual

