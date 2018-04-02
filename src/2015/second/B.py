'''
Created on May 28, 2016

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
        # read input N V X
        N, V, X = processInputLine(inputFile)

        # read Ris & Cis
        Ris = [0] * N
        Cis = [0] * N
        for i in xrange(N):
            Ris[i], Cis[i] = processInputLine(inputFile)

        O = ""

        # generate output line
        outputLine = "Case #" + str(t + 1) + ": " + O 
        if t < T - 1: 
            outputLine += "\r\n"
        outputFile.write(outputLine)
        print (outputLine)