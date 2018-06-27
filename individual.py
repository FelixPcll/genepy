import numpy as np 
import pandas as pd 
rd = np.random

class Individual:
    def __init__(self, code, par=None, generation=0, parents=None, sons=None):
        self.code = code
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

        #nodes = [(i+1)*int(len(dna1)/mash) for i in range(mash)]
        #for n, node in enumerate(nodes):
        #    if n % 0 == 0:
        #        dna3.extend(dna1[])

        node = [3,7]

        dna3.extend( dna1[:node[0]] + dna2[node[0]:node[1]] + dna1[node[1]:] )
        dna4.extend( dna2[:node[0]] + dna1[node[0]:node[1]] + dna2[node[1]:] )

        if not auto_add:
            return dna3, dna4
