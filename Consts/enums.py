from enum import Enum


class SelectionMechods(Enum):
    BEST = 0
    ROULETTE = 1
    TOURNAMENT = 2
    BEST_STRING = 'Najlepszych'
    ROULETTE_STRING = 'Koło ruletki'
    TOURNAMENT_STRING = 'Selekcja turniejowa'

    ALL_OPTIONS_STRING = [BEST_STRING, ROULETTE_STRING, TOURNAMENT_STRING]


class CrossingMechods(Enum):
    SINGLE_POINT_ARITHMETIC = 0
    SINGLE_POINT_ARITHMETIC_STRING = 'Krzyżowanie 1 arytmetyczne'
    ARITHMETIC = 1
    ARITHMETIC_STRING = 'Krzyżowanie arytmetyczne'
    LINEAR = 2
    LINEAR_STRING = 'Krzyżowanie linearne'
    BLEND_ALFA = 3
    BLEND_ALFA_STRING = 'Krzyżowanie mieszające typu alfa'
    BLEND_ALFA_BETA = 4
    BLEND_ALFA_BETA_STRING = 'Krzyżowanie mieszające typu alfa i beta'
    AVERAGE = 5
    AVERAGE_STRING = 'Krzyżowanie uśredniające'
    SIMPLE = 6
    SIMPLE_STRING = 'Krzyżowanie proste'
    RANDOM = 7
    RANDOM_STRING = 'Krzyżowanie przypadkowe'


    ALL_OPTIONS_STRING = [SINGLE_POINT_ARITHMETIC_STRING, ARITHMETIC_STRING, LINEAR_STRING, BLEND_ALFA_STRING, BLEND_ALFA_BETA_STRING, AVERAGE_STRING, SIMPLE_STRING, RANDOM_STRING]


class MutationMechods(Enum):
    UNIFORM = 0
    GAUSS = 1
    UNIFORM_STRING = 'Równomierna'
    GAUSS_STRING = 'Gaussa'

    ALL_OPTIONS_STRING = [ UNIFORM_STRING,GAUSS_STRING]


class InversionMethods(Enum):
    TWO_POINT = 0
    TWO_POINT_STRING = '2 punktowa'

    ALL_OPTIONS_STRING = [TWO_POINT_STRING]


class MinMax(Enum):
    MIN = 0
    MAX = 1


class FunctionsOptions(Enum):
    RASTRIGIN = 0
    SCHWEFEK = 1
