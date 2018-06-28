import numpy as np 
#import pandas as pd 
rd = np.random

class Individual:
    def __init__(self, par=None, generation=0, parents=[], sons=[]):
        self.code = id(self)
        self.par = par
        self.generation = generation
        self.parents = parents
        self.sons = sons

        if not self.par:
            self.par = [rd.random() for i in range(10)]
    

    def breed(self, other, mutation_rate, mash=3, auto_add=False):
        
        dna1 = self.par
        dna2 = other.par

        dna3 = []
        dna4 = []

        #nodes = [int((i+1)*len(dna1)/mash) for i in range(mash)]
        #for n, node in enumerate(nodes):
        #    if n % 0 == 0:
        #        dna3.extend(dna1[])

        node = [3,7]

        dna3 = dna1[:node[0]] + dna2[node[0]:node[1]] + dna1[node[1]:]
        dna4 = dna2[:node[0]] + dna1[node[0]:node[1]] + dna2[node[1]:]

        s1 = Individual(dna3, max([self.generation, other.generation])+1, [self, other])
        s2 = Individual(dna4, max([self.generation, other.generation])+1, [self, other])

        s1.mutate(mutation_rate)
        s2.mutate(mutation_rate)

        self.sons = [s1, s2]
        other.sons = [s1, s2]

        if not auto_add:
            return self.sons
        else:
            raise EnvironmentError('Feature not implemented yet')
    

    def mutate(self, chance):
        if chance > 1:
            chance = chance/100
        
        
        for n, i in enumerate(self.par):
            if rd.rand() < chance:    
                i = rd.rand()
                self.par[n] = i
        
        return

        #self.par = [rd.random() for i in self.par if rd.random()<chance]
            
        


class Environment:
    def __init__(self, start_population=[]):
        self.start_population = start_population
        self.curr_pop = start_population