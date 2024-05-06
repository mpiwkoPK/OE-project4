import numpy as np


class CrossoverMethod:
    def crossover(self, population):
        pass


class SingleArithmeticalCrossover(CrossoverMethod):
    def __init__(self, alpha):
        self.alpha = alpha

    def crossover(self, pop: np.ndarray, alpha=0.2):
        n_pop, n_dim = pop.shape
        parents = pop[np.random.choice(n_pop, 2, replace=False)]
        gen_idx = np.random.randint(0, n_dim)
        p1_gen = parents[0, gen_idx]
        p2_gen = parents[1, gen_idx]
        child1 = parents[0]
        child2 = parents[1]
        child1[gen_idx] = (1 - alpha) * p1_gen + alpha * p2_gen
        child2[gen_idx] = (1 - alpha) * p2_gen + alpha * p1_gen

        return np.array([child1, child2])

class ArithmeticalCrossover(CrossoverMethod):
    def __init__(self, alpha):
        self.alpha = alpha

    def crossover(self, pop: np.ndarray, alpha=0.2):
        n_pop, n_dim = pop.shape
        parents = pop[np.random.choice(n_pop, 2, replace=False)]
        gen_idx = np.random.randint(0, n_dim)
        p1_gen = parents[0, gen_idx]
        p2_gen = parents[1, gen_idx]
        child1 = parents[0]
        child2 = parents[1]

        child1[gen_idx] = (1 - alpha) * p1_gen + alpha * p2_gen
        child2[gen_idx] = (1 - alpha) * p2_gen + alpha * p1_gen

        return np.array([child1, child2])


class LinearCrossover(CrossoverMethod):
    def __init__(self, alpha):
        self.alpha = alpha

    def crossover(self, pop: np.ndarray, alpha=0.2):
        n_pop, n_dim = pop.shape
        parents = pop[np.random.choice(n_pop, 2, replace=False)]
        gen_idx = np.random.randint(0, n_dim)
        p1_gen = parents[0, gen_idx]
        p2_gen = parents[1, gen_idx]
        child1 = parents[0]
        child2 = parents[1]
        child1[gen_idx] = (1 - alpha) * p1_gen + alpha * p2_gen
        child2[gen_idx] = (1 - alpha) * p2_gen + alpha * p1_gen

        return np.array([child1, child2])


class BlendCrossoverAlfaBeta(CrossoverMethod):
    def __init__(self, probability):
        self.probability = probability

    def crossover(self, pop: np.ndarray, alpha=0.2):
        n_pop, n_dim = pop.shape
        parents = pop[np.random.choice(n_pop, 2, replace=False)]
        print("RODZIC: ", parents)
        child1 = np.empty_like(parents[0])
        child2 = np.empty_like(parents[0]) 
    
        if np.random.uniform() < self.probability:
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

        print("DZIECKO1: ", child1)
        print("DZIECKO2: ", child2)

        return np.array([child1, child2])


class AverageCrossover(CrossoverMethod):
    def __init__(self, alpha):
        self.alpha = alpha

    def crossover(self, pop: np.ndarray, alpha=0.2):
        n_pop, n_dim = pop.shape
        parents = pop[np.random.choice(n_pop, 2, replace=False)]
        gen_idx = np.random.randint(0, n_dim)
        p1_gen = parents[0, gen_idx]
        p2_gen = parents[1, gen_idx]
        child1 = parents[0]
        child2 = parents[1]
        child1[gen_idx] = (1 - alpha) * p1_gen + alpha * p2_gen
        child2[gen_idx] = (1 - alpha) * p2_gen + alpha * p1_gen

        return np.array([child1, child2])


class RandomCrossover(CrossoverMethod):
    def __init__(self, alpha):
        self.alpha = alpha

    def crossover(self, pop: np.ndarray, alpha=0.2):
        n_pop, n_dim = pop.shape
        parents = pop[np.random.choice(n_pop, 2, replace=False)]
        gen_idx = np.random.randint(0, n_dim)
        p1_gen = parents[0, gen_idx]
        p2_gen = parents[1, gen_idx]
        child1 = parents[0]
        child2 = parents[1]
        child1[gen_idx] = (1 - alpha) * p1_gen + alpha * p2_gen
        child2[gen_idx] = (1 - alpha) * p2_gen + alpha * p1_gen

        return np.array([child1, child2])


class SimpleCrossover(CrossoverMethod):
    def __init__(self, alpha):
        self.alpha = alpha

    def crossover(self, pop: np.ndarray, alpha=0.2):
        n_pop, n_dim = pop.shape
        parents = pop[np.random.choice(n_pop, 2, replace=False)]
        print(parents)

        crossing_point = np.random.randint(1, len(parents[0]))
        child1 = []
        child2 = []

        for i in range(0, crossing_point):
            child1.append(parents[0][i])
            child2.append(parents[1][i])
        for i in range(crossing_point, len(parents[0])):
            child1.append(alpha * parents[1][i] + (1 - alpha) * parents[0][i])
            child2.append(alpha * parents[0][i] + (1 - alpha) * parents[1][i])
         
        print("DZIECKO1: ", child1)
        print("DZIECKO2: ", child2)
        return np.array([child1, child2])
    
class BlendCrossoverAlfa(CrossoverMethod):
    def __init__(self, probability):
        self.probability = probability

    def crossover(self, pop: np.ndarray):
        n_pop, n_dim = pop.shape
        alpha = np.random.uniform()
        parents = pop[np.random.choice(n_pop, 2, replace=False)]
        print("RODZICE: ", parents)
        
        child1 = np.empty_like(parents[0])
        child2 = np.empty_like(parents[0])
        if alpha < self.probability:
            
            
            for i in range(len(parents[0])):
                x1 = parents[0][i]
                x2 = parents[1][i]
                distancia = abs(x1-x2)
                u1 = np.random.uniform(min(x1,x2)-alpha*distancia, max(x1,x2)+alpha*distancia)
                u2 = np.random.uniform(min(x1,x2)-alpha*distancia, max(x1,x2)+alpha*distancia)

                child1[i] = u1
                child2[i] = u2
        print("dziecko1: ", child1)
        print("dziecko2: ", child2)

        return np.array([child1, child2])




    
#class AlphaBetaCrossover(CrossoverMethod):
