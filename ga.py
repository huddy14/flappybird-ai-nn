import numpy as np
import random
from Bird import Bird
import operator as op

CROSS_RATE = .8
MUT_RATE = .6
BEST_RATE = .3
POP_SIZE = 50

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
        if random.random() < MUT_RATE:
            w = self.decode_weights(bird.net.weights)
            r = []
            for i in w:
                if random.random() < 0.5:
                    r.append(random.triangular(-1,1) * i)
                else:
                    r.append(i)
            mutated_weights = self.encode_weight(r)
            return Bird(mutated_weights)

        else: return Bird(bird.net.weights)


    def crossover(self):
        print('popoulation:')
        for p in self.population:
            print(p.fitness)
        self.sort_population_by_fitness()


        l = len(self.population)

        # picking birds with highest fitness to be parents for new birds
        best = self.population[int(l*(1-BEST_RATE)):]
        # picking 2 best performing birds to add unchanged to the population
        leaders = [Bird(best[-1].net.weights),Bird(best[-2].net.weights)]
        print('best')
        for b in best:
            print(b.fitness)
        result = leaders

        #breeding with random parents - for specified cross rate
        while len(result) < POP_SIZE:
            # taking 2 random and different ids to breed
            ids = random.sample(range(len(best)), 2)
            new_bird = self.breed(best[ids[0]].net, best[ids[1]].net)

            #mutating by MUTE_RATE
            new_bird = self.mutate(new_bird)
            result.append(new_bird)

        self.population = result
        return result

    # def evolve(self):
    #     #grade the last generation before evolving
    #     #self.grade()
    #
    #     self.sort_population_by_fitness()
    #     l = len(self.population)
    #     best = self.population[int(l*(1-BEST_RATE)):]
    #     #croosing over the best birds
    #     new_pop = self.crossover_best()
    #
    #     #mutating the rest of population
    #     while len(new_pop) < POP_SIZE:
    #         # selecting random bird to mutate weights
    #         bird = best[random.randint(0, len(best) - 1)]
    #         new_pop.append(self.mutate(bird))
    #
    #     self.population = new_pop
    #     return new_pop


    def breed(self,n1,n2):
        W1 = self.decode_weights(n1.weights)
        W2 = self.decode_weights(n2.weights)

        m = int(len(W1)/2)
        r_gens = random.randint(1,m*2)
        new_weights = self.encode_weight(W1[:r_gens] + W2[r_gens:])
#        new_weights = self.encode_weight([.5 * (w1+w2) for w1,w2 in zip(W1,W2)])
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

