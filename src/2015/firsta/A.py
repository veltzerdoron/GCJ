'''
@author: doronv
'''

import numpy as np
import math
import re

def solve(inputFile, outputFile):
    # read case number
    T = int(inputFile.readline())
    
    # iterate on all cases
    for t in range(T):
        # read input N and Mjs
        N = int(inputFile.readline())
        Mjs = map(int, inputFile.readline().rstrip().split(' '))

        minEatens = [max(mi_1 - mi, 0) for mi_1, mi in zip(Mjs, Mjs[1:])]
        y = sum(minEatens)
        speed = max(minEatens)
        constEatens = [min(mj, speed) for mj in Mjs[:-1]]
        z = sum(constEatens)
        # Output case result
        OutputLine = 'Case #' + str(t + 1) + ': ' + str(y) + ' ' + str(z)
        if t < T - 1: OutputLine += '\r\n'
        outputFile.write(OutputLine)