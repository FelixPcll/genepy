import numpy as np
# import pandas as pd
rd = np.random


class Individual:
    def __init__(self, par=None, generation=0, parents=[], sons=[]):

        self.code = id(self)
        self.par = par
        self.generation = generation
        self.parents = parents
        self.sons = sons
        self.score = 0

        if not self.par:
            self.par = list(rd.rand(10))

    def breed(self, other, mutation_rate, mash=3, auto_add=False):
        dna1 = self.par
        dna2 = other.par

        dna3 = []
        dna4 = []
        # nodes = [int((i+1)*len(dna1)/mash) for i in range(mash)][:-1]

        # for n, node in enumerate(nodes):
        #    if n % 2 == 0:
        #        f1 = dna1
        #        f2 = dna2
        #    elif n % 2 == 1:
        #        f1 = dna2
        #        f2 = dna1
        #
        #    for b in range(len(dna1)):

        node = [3, 7]

        dna3 = dna1[:node[0]] + dna2[node[0]:node[1]] + dna1[node[1]:]
        dna4 = dna2[:node[0]] + dna1[node[0]:node[1]] + dna2[node[1]:]

        s1 = Individual(par=dna3, parents=[self, other],
                        generation=max([self.generation, other.generation])+1)
        s2 = Individual(par=dna4, parents=[self, other],
                        generation=max([self.generation, other.generation])+1)

        s1.mutate(mutation_rate)
        s2.mutate(mutation_rate)

        self.sons = [s1, s2]
        other.sons = [s1, s2]

        if not auto_add:
            return self.sons
        else:
            raise EnvironmentError('Feature not implemented yet')

    def mutate(self, chance):
        for n, _ in enumerate(self.par):
            if rd.rand() < chance:
                self.par[n] = rd.rand()

        return

        # self.par = [rd.random() for i in self.par if rd.random()<chance]


class Environment:
    def __init__(self, start_population=[]):
        self.start_population = start_population
        self.curr_pop = start_population

    def preasure(self, individual, feature=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]):
        res = 0
        for n, f in enumerate(feature):
            res += (1-(f - individual.par[n])**2)

        individual.score = res
        return

    def evolve(self, keep=2, feature=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               mutate=True):
        for ind in self.curr_pop:
            self.preasure(ind, feature=feature)

        k = list(map(lambda x: x.score, self.curr_pop))
        k = [i/sum(k) for i in k]

        new_gen = rd.choice(self.curr_pop, size=keep,
                            replace=False, p=k)

        if not mutate:
            self.curr_pop = []
            self.curr_pop.extend(new_gen)
            return self.curr_pop
        else:
            self.curr_pop = []
            new_gen = list(new_gen)
            self.curr_pop.extend(new_gen)
            while len(new_gen) > 1:
                k = list(map(lambda x: x.score, new_gen))
                k = [i/sum(k) for i in k]

                pair = rd.choice(new_gen, size=2, replace=False, p=k)
                puppy = pair[0].breed(pair[1], mutation_rate=mutate)
                for p in puppy:
                    self.preasure(p, feature=feature)
                self.curr_pop.extend(puppy)
                for i in pair:
                    new_gen.remove(i)
            if len(new_gen) == 1:
                self.curr_pop.extend(new_gen)

            while len(self.curr_pop) < len(self.start_population):
                k = list(map(lambda x: x.score, self.curr_pop))
                k = [i/sum(k) for i in k]

                pair = rd.choice(self.curr_pop, size=2, replace=False, p=k)
                puppy = pair[0].breed(pair[1], mutation_rate=mutate)
                for p in puppy:
                    self.preasure(p, feature=feature)
                self.curr_pop.extend(puppy)
            return

    def gen_population(self, n):
        self.start_population = []
        self.curr_pop = []
        for j in range(n):
            j = Individual()
            self.start_population.append(j)
        self.curr_pop.extend(self.start_population)
