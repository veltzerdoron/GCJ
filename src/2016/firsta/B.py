'''
Created on Apr 16, 2016

@author: doronv
'''

# standard python package imports
import numpy as np
import fractions as fr
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
        # read lists
        Ls = [[0 for x in range(N)] for x in range(2 * N - 1)]
        for i in range(2 * N - 1):
            Ls[i] = processInputLine(inputFile)

        # count occurrences
        counts = dict()
        for i in range(2 * N - 1):
            for x in range(N):
                h = Ls[i][x]
                if (not h in counts.keys()):
                    counts[h] = sum(Ls[i].count(h) for i in range(2 * N - 1))

        missingLine = [0 for x in range(N)]
        x = 0
        # append all elements that occur an odd number of times
        for h in counts.keys():
            c = counts[h]
            if (c % 2 != 0):
                missingLine[x] = h
                x = x + 1

        # build output
        sortedMissingLine = sorted(missingLine)
        O = ""
        for x in range(N):
            O = O + str(sortedMissingLine[x])
            if x < N - 1:
                O += ' '

        # Output case result
        OutputLine = "Case #" + str(t + 1) + ": " + O
        if t < T - 1: OutputLine += "\r\n"
        outputFile.write(OutputLine)
