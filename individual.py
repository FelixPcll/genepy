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
    
