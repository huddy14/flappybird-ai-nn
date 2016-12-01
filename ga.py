import numpy as np
import random
from Bird import Bird
import operator as op

CROSS_RATE = .5
MUT_RATE = .8
BEST_RATE = .2
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
        self.sort_population_by_fitness()
        b = self.population[int(.8*len(self.population)):]
        for best in b:
            print('best fitness: {} \n best weights: {}'.format(best.fitness, best.net.weights))


    def mutate(self, bird):

        w = self.decode_weights(bird.net.weights)
        r = []
        for i in w:
            if random.random() < MUT_RATE:
                r.append(np.random.uniform(-5,5))
            else:
                r.append(i)
        mutated_weights = self.encode_weight(r)
        return Bird(mutated_weights)


    def crossover_best(self):
        print('popoulation:')
        for p in self.population:
            print(p.fitness)
        self.sort_population_by_fitness()
        l = len(self.population)

        # picking birds with highest fitness to be parents for new birds
        best = self.population[int(l*(1-BEST_RATE)):]
        print('best')
        for b in best:
            print(b.fitness)
        result = [Bird(w.net.weights) for w in best]

        #breeding with random parents - for specified cross rate
        for i in range(int(l*CROSS_RATE)):
            # taking 2 random and different ids to breed
            ids = random.sample(range(len(best)), 2)
            result.append(self.breed(best[ids[0]].net, best[ids[1]].net))

        return result

    def evolve(self):
        #grade the last generation before evolving
        #self.grade()

        #croosing over the best birds
        new_pop = self.crossover_best()

        #mutating the rest of population
        while len(new_pop) < POP_SIZE:
            # selecting random bird to mutate weights
            bird = self.population[random.randint(0, len(self.population) - 1)]
            new_pop.append(self.mutate(bird))

        self.population = new_pop
        return new_pop


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

