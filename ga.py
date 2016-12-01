import numpy as np
import random
from Bird import Bird
import operator as op

CROSS_RATE = .8
MUT_RATE = 0.8
POP_SIZE = 100

class GeneticAlgorithm():

    population = []

    def __init__(self):
        self.population = [Bird() for _ in range(POP_SIZE)]

    def individual(self):
        pass


    def create_population(self):
        pass

    def sort_population_by_fitness(self):
        self.population.sort(key=op.attrgetter('fitness'))

    def grade(self):
        pass

    def mutate(self):
        pass

    def crossover_best(self):
        print('popoulation:')
        for p in self.population:
            print(p.fitness)
        self.sort_population_by_fitness()
        l = len(self.population)
        best = self.population[int(l*CROSS_RATE):]
        print('best')
        for b in best:
            print(b.fitness)
        # taking 2 random and different ids to breed
        result = [Bird(w.net.weights) for w in best]

        while len(result) < POP_SIZE:
            mutate = random.randint(0,1)
            if mutate == 1:
                b = self.population[random.randint(0,len(self.population)-1)]
                w = self.decode_weights(b.net.weights)
                r = []
                for i in w:
                    if random.randint(0,1) == 1:
                        r.append(random.random())
                    else: r.append(i)
                r = self.encode_weight(r)
                result.append(Bird(r))
            else:
                ind = random.sample(range(len(best)), 2)
                result.append(self.breed(best[ind[0]].net, best[ind[1]].net))
        self.population = result
        return result

    def breed(self,n1,n2):
        W1 = self.decode_weights(n1.weights)
        W2 = self.decode_weights(n2.weights)

        m = int(len(W1)/2)

        new_weights = self.encode_weight(W1[:m] + W2[m:])
        return Bird(new_weights)


    def decode_weights(self,weigth):
        r1=[]
        for l in weigth:
            for w in l:
                for v in w:
                    r1.append(v)

        return r1

    def encode_weight(self,weights):
        W1 = np.reshape(weights[:4],(2,2))
        W2 = np.reshape(weights[4:],(2,1))
        return [W1,W2]

    def evolve(self):
        pass

print(random.randint(0,1))
# nn = Network()
# n1 = Network()
#
# g = GeneticAlgorithm()
# decoded = g.breed(nn,n1)
# print(decoded)
# print(g.encode_weight(decoded))