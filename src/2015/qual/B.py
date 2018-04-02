'''
@author: doronv
'''

import numpy as np
import re

def solve(inputFile, outputFile):
    # read case number
    T = int(inputFile.readline())
    
    # iterate on all cases
    for t in range(T):
        #read D and Pans 
        D = int(inputFile.readline())
        Ps = map(int, list(inputFile.readline().split(' ')))

        time = 1000000000
        for i in range(1, 1001):
            cur = i
            for p in Ps:
                cur += (p - 1) / i
            time = min(time, cur)

        O = str(time)
        # Output case result
        outputLine = 'Case #' + str(t + 1) + ': ' + O 
        if t < T - 1: outputLine += '\r\n'
        outputFile.write(outputLine)
