import copy
import math
import random
import time

from Consts.enums import MinMax, CrossingMechods, SelectionMechods, MutationMechods, FunctionsOptions, \
    InversionMethods as InversionMethodsEnum
from Helpers.crossingMethods import SingleArithmeticalCrossover
from Helpers.functions import rastrigin, schwefel
from Helpers.inversionMethod import InversionMethod
from Helpers.mutationMethods import EdgeMutation, SinglePointMutation, TwoPointMutation
from Helpers.parents import initPopulation
import numpy as np

from Helpers.plotsNFiles import make_plot, save_to_file
from Helpers.selectionMethods import BestSelection, RouletteWheelSelection, TournamentSelection


class Model:
    end_population = []
    start_time = 0
    end_time = 0
    stddev_values = []
    avg_values = []
    best_spec = []
    best_values = []

    def __init__(self,
                 number_of_epoch: int,
                 size_of_population: int,
                 number_of_parents: int,
                 elitism_rate: float,
                 crossing_probability: int,
                 crossing_function: CrossingMechods,
                 mutation_function: MutationMechods,
                 selection_function: SelectionMechods,
                 mutation_prob: float,
                 inversion_function: InversionMethodsEnum,
                 inversion_prob: float,
                 number_of_dimensions: int,
                 func: FunctionsOptions,
                 title,
                 direction: MinMax,
                 tournament_size: int,
                 q: int):
        self.number_of_epoch = number_of_epoch
        self.size_of_population = size_of_population
        self.number_of_parents = number_of_parents
        self.elitism_rate = elitism_rate
        self.crossing_probability = crossing_probability
        self.crossing_function = crossing_function
        self.mutation_function = mutation_function
        self.selection_function = selection_function
        self.mutation_prob = mutation_prob
        self.inversion_prob = inversion_prob
        self.number_of_dimensions = number_of_dimensions
        self.func = func
        self.title = title
        self.init_population = initPopulation(number_of_dimensions, size_of_population)
        self.direction = direction

        self.func = rastrigin(number_of_dimensions) if func == FunctionsOptions.RASTRIGIN else schwefel(
            number_of_dimensions)

        match selection_function:
            case SelectionMechods.BEST:
                selection = BestSelection(number_of_dimensions)
                self.selection_function = selection.select if self.direction == MinMax.MIN else selection.maxSelect
            case SelectionMechods.ROULETTE:
                selection = RouletteWheelSelection(number_of_dimensions)
                self.selection_function = selection.select
            case SelectionMechods.TOURNAMENT:
                selection = TournamentSelection(tournament_size, number_of_dimensions)
                self.selection_function = selection.select if self.direction == MinMax.MIN else selection.maxSelect
                self.selectionName = SelectionMechods.TOURNAMENT_STRING.value
        match crossing_function:
            case CrossingMechods.SINGLE_POINT_ARITHMETIC:
                self.crossing_function = SingleArithmeticalCrossover(0.2).crossover
        match mutation_function:
            case MutationMechods.EDGE:
                self.mutation_function = EdgeMutation(number_of_dimensions).mutate
            case MutationMechods.SINGLE_POINT:
                self.mutation_function = SinglePointMutation(number_of_dimensions).mutate
            case MutationMechods.DOUBLE_POINT:
                self.mutation_function = TwoPointMutation(number_of_dimensions).mutate
        match inversion_function:
            case InversionMethodsEnum.TWO_POINT:
                self.inversion_function = InversionMethod(number_of_dimensions).inverse

    @staticmethod
    def find_best_spec(fn, population, direction: MinMax):
        best_index = 0
        for i in range(1, len(population)):
            value1 = population[best_index]
            value2 = population[i]
            if ((fn(value1) > fn(value2) and direction == MinMax.MIN)
                    or
                    (fn(value1) < fn(value2) and direction == MinMax.MAX)):
                best_index = i
        return population[best_index]

    @staticmethod
    def worst_best_spec_index(fn, population, direction: MinMax) -> int:
        best_index = 0
        for i in range(1, len(population)):
            value1 = population[best_index]
            value2 = population[i]
            if ((fn(value1) < fn(value2) and direction == MinMax.MIN)
                    or
                    (fn(value1) > fn(value2) and direction == MinMax.MAX)):
                best_index = i
        return best_index

    def getStartString(self):
        return_string = ''
        best_spec = self.find_best_spec(self.func, self.init_population, self.direction)
        best_spec_copy = copy.deepcopy(best_spec)
        result = self.func(best_spec)
        return_string += '\nstart f('
        for val in best_spec_copy:
            return_string += f'{val:.4f}, '
        return_string = return_string[:-2]
        return_string += f') = {result:.4f}' + '\n'
        return return_string

    def getEndString(self):
        return_string = ''
        best_spec = self.find_best_spec(self.func, self.end_population, self.direction)
        best_spec_copy = copy.deepcopy(best_spec)
        result = self.func(best_spec)
        return_string += '\nend f('
        for val in best_spec_copy:
            return_string += f'{val:.4f}, '
        return_string = return_string[:-2]
        return_string += f') = {result:.4f}' + '\n'
        return_string += 'Czas: ' + f'{self.end_time - self.start_time:0.4f}' + ' sekund\n'
        return return_string

    def appendToAllArrays(self, all_res, population):
        self.avg_values.append(np.mean(all_res))
        self.stddev_values.append(np.std(all_res))
        self.best_spec.append(self.find_best_spec(self.func, population, self.direction))
        self.best_values.append(self.func(self.best_spec[-1]))

    def getBestAlive(self, population):
        best_values = np.array([self.func(individual) for individual in population])
        best_quantity = math.floor(len(population) * self.elitism_rate)
        zip = np.column_stack((best_values, population))
        sorted = zip[zip[:, 0].argsort()]
        return np.array(list(map(lambda x: x[1:], sorted[:best_quantity])))

    def fitness(self):
        self.best_values = []
        self.avg_values = []
        self.stddev_values = []
        self.best_spec = []
        self.start_time = time.perf_counter()
        population = self.init_population
        for _ in range(self.number_of_epoch):
            is_best_alive = False
            all_res = np.array([self.func(individual) for individual in population])
            self.appendToAllArrays(all_res, population)
            temp_population = self.selection_function(population, all_res, self.number_of_parents)

            while len(temp_population) < self.size_of_population:
                if random.random() >= self.crossing_probability:
                    temp_population = np.append(temp_population, self.crossing_function(temp_population), axis=0)

            best_old_spec = self.getBestAlive(population)
            best_old_spec = copy.deepcopy(best_old_spec)
            best_new_spec = self.find_best_spec(self.func, temp_population, self.direction)

            for spec_index in range(self.size_of_population):
                spec = temp_population[spec_index]
                if not is_best_alive and np.array_equal(spec, best_new_spec):
                    is_best_alive = True
                    continue
                for chrom_index in range(self.number_of_dimensions):
                    if random.random() >= self.mutation_prob:
                        temp_population[spec_index] = self.mutation_function(spec, self.mutation_prob)
            for i in range(len(temp_population)):
                temp_population[i] = self.inversion_function(temp_population[i], self.inversion_prob)

            temp_population = np.append(temp_population, best_old_spec, axis=0)
            population = temp_population

        self.end_population = population
        self.end_time = time.perf_counter()

    def getChats(self):
        make_plot(self.best_values, 'best', self.title, 'log')
        save_to_file(self.best_values, self.best_spec, 'best')
        make_plot(self.avg_values, 'avg', self.title)
        make_plot(self.stddev_values, 'std', self.title)
