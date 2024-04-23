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

    ALL_OPTIONS_STRING = [SINGLE_POINT_ARITHMETIC_STRING]


class MutationMechods(Enum):
    EDGE = 0
    SINGLE_POINT = 1
    DOUBLE_POINT = 2
    EDGE_STRING = 'Brzegowa'
    SINGLE_POINT_STRING = '1 punktowa'
    DOUBLE_POINT_STRING = '2 punktowa'

    ALL_OPTIONS_STRING = [SINGLE_POINT_STRING, DOUBLE_POINT_STRING, EDGE_STRING]


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
