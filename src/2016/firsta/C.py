'''
Created on Apr 16, 2016

@author: doronv
'''

# standard python package imports
import numpy as np
import fractions as fr
import collections as co
import math as ma
import re

# read line from file split it according to separator and convert it to type
def processInputLine(inputFile, inputType = int, inputNumber = None, inputSeparator = " "):
    inputLine = inputFile.readline().rstrip()
    if inputNumber == None:
        inputVector = inputLine.split(inputSeparator)
    else:
        inputVector = inputLine.split(inputSeparator, inputNumber)
    outputVector = map(inputType, inputVector)
    if len(outputVector) == 1:
        return outputVector[0]
    else:
        return outputVector

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

def solve(inputFile, outputFile):
    # read case number
    T = processInputLine(inputFile)

    # iterate on all cases
    for t in range(T):
        # read N
        N = processInputLine(inputFile)
        # read BFF
        BFF = processInputLine(inputFile, lambda x: int(x) - 1)

        # count regular circles
        CMax = 0
        for i in range(N):
            # find circle starting at i
            x = i
            visited = [False for i in range(N)]
            while not visited[x] :
                visited[x] = True
                x = BFF[x]

            #find circle length
            C = 0
            visited = [False for i in range(N)]
            while not visited[x] :
                C = C + 1
                visited[x] = True
                x = BFF[x]

            if C > CMax:
                CMax = C

        # build maximal chains to power couples
        d = [0 for j in range(N)]
        d_ = [0 for j in range(N)]
        for _ in range(N):
            for i in range(N):
                j = BFF[i]
                # check that this is not a power couple
                if BFF[j] != i:
                    d_[j] = max(d[j], d[i] + 1)
            d = d_

        # get power couples possibility
        PCMax = 0
        for i in range(N):
            # if i and BFF[i] are a power couple
            j = BFF[i]
            # count every PC component once
            if BFF[j] == i and i < j:
                C = 2 + d[i] + d[j]
                PCMax += C

        # maximum of the two cases
        O = max(CMax, PCMax)

        O = max(CMax, PCMax)

        # Output case result
        outputLine = "Case #" + str(t + 1) + ": " + str(O)
        if t < T - 1: outputLine += "\r\n"
        outputFile.write(outputLine)