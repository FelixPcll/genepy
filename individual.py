import numpy as np 
#import pandas as pd 
rd = np.random

class Individual:
    """
    Individual(par, generation, parents, sons)
    
    
    """
    def __init__(self, par=None, generation=0, parents=[], sons=[]):
        self.code = id(self)
        self.par = par
        self.generation = generation
        self.parents = parents
        self.sons = sons

        if not self.par:
            self.par = [rd.random() for i in range(10)]
    

    def breed(self, other, mash=3, auto_add=False):
        
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

        s1 = Individual(dna3, other.generation+1, [self, other])
        s2 = Individual(dna4, other.generation+1, [self, other])

        self.sons = [s1, s2]
        other.sons = [s1, s2]

        if not auto_add:
            return self.sons
        else:
            raise EnvironmentError('Feature not implemented yet')
    

