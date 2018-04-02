'''
Created on April 30, 2016

@author: doronv
'''

# standard python package imports
import numpy as np
import fractions as fr
import math as ma
import re
import hopcroftkarp

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


# solution
def solve(inputFile, outputFile):
    # read case number
    T = int(inputFile.readline())

    # iterate on all cases
    for t in range(T):
        # read input N
        N = processInputLine(inputFile)

        # read topic names and build graph G
        Us = set()
        Vs = set()
        G = {}
        for n in range(N):
            u, v = processInputLine(inputFile, str)
            u = "1" + u
            v = "2" + v
            Us.add(u)
            Vs.add(v)
            if u not in G:
                G[u] = set()
            G[u].add(v)

        match = hopcroftkarp.HopcroftKarp(G).maximum_matching()
        r = len(match) / 2

        O = str(N + r - len(Us) - len(Vs))

        outputLine = "Case #" + str(t + 1) + ": " + O 
        if t < T - 1: 
            outputLine += "\r\n"
        outputFile.write(outputLine)