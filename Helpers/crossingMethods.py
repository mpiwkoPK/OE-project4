import numpy as np


class CrossoverMethod:
    def crossover(self, population):
        pass


class SingleArithmeticalCrossover(CrossoverMethod):
    def __init__(self, alpha):
        self.alpha = alpha

    def crossover(self, pop: np.ndarray):
        n_pop, n_dim = pop.shape
        parents = pop[np.random.choice(n_pop, 2, replace=False)]
        gen_idx = np.random.randint(0, n_dim)
        p1_gen = parents[0, gen_idx]
        p2_gen = parents[1, gen_idx]
        child1 = parents[0]
        child2 = parents[1]
        child1[gen_idx] = (1 - self.alpha) * p1_gen + self.alpha * p2_gen
        child2[gen_idx] = (1 - self.alpha) * p2_gen + self.alpha * p1_gen

        return np.array([child1, child2])


class ArithmeticalCrossover(CrossoverMethod):
    def __init__(self, alpha):
        self.alpha = alpha

    def crossover(self, pop: np.ndarray):
        n_pop, n_dim = pop.shape
        parents = pop[np.random.choice(n_pop, 2, replace=False)]
        child1 = np.array([(1 - self.alpha) * parents[0, x] + self.alpha * parents[0, x] for x in range(n_dim)])
        child2 = np.array([(1 - self.alpha) * parents[1, x] + self.alpha * parents[1, x] for x in range(n_dim)])
        return np.array([child1, child2])


class LinearCrossover(CrossoverMethod):
    def __init__(self, func):
        self.func = func

    def crossover(self, pop: np.ndarray, alpha=0.2):
        n_pop, n_dim = pop.shape
        parents = pop[np.random.choice(n_pop, 2, replace=False)]
        p1 = parents[0]
        p2 = parents[1]
        Z = np.array([p1[x] / 2 + p2[x] / 2 for x in range(n_dim)])
        V = np.array([p1[x] * 3 / 2 + p2[x] / (-2) for x in range(n_dim)])
        W = np.array([p1[x] / (-2) + p2[x] * 3 / 2 for x in range(n_dim)])
        values = [self.func(Z), self.func(W), self.func(V)]
        zip = np.column_stack((values, [Z, W, V]))
        sorted = zip[zip[:, 0].argsort()]
        best_linear = np.array([spec[1:] for spec in sorted[:2]])
        return best_linear


class BlendCrossoverAlfaBeta(CrossoverMethod):
    def crossover(self, pop: np.ndarray, alpha=0.2):
        n_pop, n_dim = pop.shape
        parents = pop[np.random.choice(n_pop, 2, replace=False)]
        child1 = np.empty_like(parents[0])
        child2 = np.empty_like(parents[0])

        alpha = np.random.uniform(low=0, high=1)
        beta = np.random.uniform(low=0, high=1)


        for i in range(len(parents[0])):
            x1 = parents[0][i]
            x2 = parents[1][i]
            distancia = abs(x1-x2)

            u1 = np.random.uniform(min(x1,x2)-alpha*distancia, max(x1,x2)+beta*distancia)
            u2 = np.random.uniform(min(x1,x2)-alpha*distancia, max(x1,x2)+beta*distancia)

            child1[i] = u1
            child2[i] = u2

        return np.array([child1, child2])


class AverageCrossover(CrossoverMethod):
    def crossover(self, pop: np.ndarray, alpha=0.2):
        n_pop, n_dim = pop.shape
        child = np.array([np.mean([values for values in pop[:, x]]) for x in range(n_dim)])
        return np.array([child])


class RandomCrossover(CrossoverMethod):
     def crossover(self, pop: np.ndarray):
        n_pop, n_dim = pop.shape
        parents = pop[np.random.choice(n_pop, 2, replace=False)]

        chromosome_Z = np.array([np.random.uniform() for i in range(n_dim)])
        chromosome_W = np.array([np.random.uniform() for i in range(n_dim)])

        crossover_point_X = np.random.randint(0, n_dim)
        crossover_point_Y = np.random.randint(0, n_dim)

        child1 = np.concatenate((parents[0][:crossover_point_X], chromosome_Z[crossover_point_X:]))
        child2 = np.concatenate((parents[1][:crossover_point_Y], chromosome_W[crossover_point_Y:]))

        return np.array([child1, child2])

class SimpleCrossover(CrossoverMethod):
    def __init__(self, alpha):
        self.alpha = alpha

    def crossover(self, pop: np.ndarray, alpha=0.2):
        n_pop, n_dim = pop.shape
        parents = pop[np.random.choice(n_pop, 2, replace=False)]

        crossing_point = np.random.randint(1, len(parents[0]))
        child1 = []
        child2 = []

        for i in range(0, crossing_point):
            child1.append(parents[0][i])
            child2.append(parents[1][i])
        for i in range(crossing_point, len(parents[0])):
            child1.append(alpha * parents[1][i] + (1 - alpha) * parents[0][i])
            child2.append(alpha * parents[0][i] + (1 - alpha) * parents[1][i])

        return np.array([child1, child2])


class BlendCrossoverAlfa(CrossoverMethod):
    def crossover(self, pop: np.ndarray):
        n_pop, n_dim = pop.shape
        alpha = np.random.uniform()
        parents = pop[np.random.choice(n_pop, 2, replace=False)]

        child1 = np.empty_like(parents[0])
        child2 = np.empty_like(parents[0])
        for i in range(len(parents[0])):
            x1 = parents[0][i]
            x2 = parents[1][i]
            distancia = abs(x1 - x2)
            u1 = np.random.uniform(min(x1, x2) - alpha * distancia, max(x1, x2) + alpha * distancia)
            u2 = np.random.uniform(min(x1, x2) - alpha * distancia, max(x1, x2) + alpha * distancia)

            child1[i] = u1
            child2[i] = u2

        return np.array([child1, child2])

#class AlphaBetaCrossover(CrossoverMethod):
