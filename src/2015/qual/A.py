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
        #read Smax and Sn list
        lineSplit = inputFile.readline().rstrip().split(' ')
        Smax = int(lineSplit[0])
        Sn = map(int, list(lineSplit[1]))

        SSn = np.cumsum(Sn)
        needed = SSn - range(Smax + 1) - 1
        O = - min(np.append(needed[needed < 0], 0))

        # Output case result
        OutputLine = 'Case #' + str(t + 1) + ': ' + str(O)
        if t < T - 1: OutputLine += '\r\n'
        outputFile.write(OutputLine)