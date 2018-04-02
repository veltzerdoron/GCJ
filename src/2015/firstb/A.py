'''
@author: doronv
'''

import numpy as np
import math
import re

# read line from file split it according to separator and convert it to type
def processInputLine(inputFile, inputSeparator = ' ', inputNumber = None, inputType = int):
    inputLine = inputFile.readline()
    if inputNumber == None:
        inputVector = inputLine.rstrip().split(inputSeparator)
    else:
        inputVector = inputLine.rstrip().split(inputSeparator, inputNumber)
    return map(inputType, inputVector)

def GCD(a, b):
    a = abs(a)
    b = abs(b)
    while a:
        a, b = b % a, a
    return b
def LCM(a, b):
        return (a * b) // GCD(a, b)
def GCDList(v):
    return reduce(GCD, v)
def LCMList(v):
    return reduce(LCM, v)

# solution
def solve(inputFile, outputFile):
    # read case number
    T = int(inputFile.readline())

    # iterate on all cases
    for t in range(T):
        # read input N
        N = processInputLine(inputFile)[0]
        
        steps = 1
        current = 1
        L = len(str(N))

        while len(str(current)) != len(str(N)):
            K = len(str(current))
            if K == 1:
                current = 10
                steps = 10
            else:
                current = current * 10
                steps += 10 ** (K // 2) + 10 ** (K - K // 2) - 1
    
        if current != N and L > 1 and str(N)[-1] == '0':
            N -= 1
            steps += 1
    
        if L > 1:
            V = str(N)[:L // 2]
            V = V[::-1]
            if int(V) > 1:
                steps += int(V) + 1
                current = int(V[::-1] + '0' * (L - L // 2))
                current += 1
        steps += N - current
        # Output case result
        OutputLine = 'Case #' + str(t + 1) + ': ' + str(steps)
        if t < T - 1: OutputLine += '\r\n'
        outputFile.write(OutputLine)
