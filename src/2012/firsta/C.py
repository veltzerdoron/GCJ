'''
@author: doronv
'''

import math


def solve(inputFile, outputFile):
    # read case number
    T = int(inputFile.readline())
    
    # iterate on all cases
    for t in range(T):

        # Output case result
        OutputLine = 'Case #' + str(t + 1) + ': ' # output here
        if t < T - 1: OutputLine += '\r\n'
        outputFile.write(OutputLine)
