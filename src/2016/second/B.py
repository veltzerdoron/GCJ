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
import itertools as it

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

def PTie(SKPis, K):
    PPrev = [1] + [0] * (K)
    for i in xrange(K):
        PNext = [0] * (K + 1)
        for j in xrange(i + 1):
            PNext[j] += PPrev[j] * (1 - SKPis[i])
            PNext[j + 1] +=  PPrev[j] * SKPis[i]
        PPrev = PNext
    return PPrev[K / 2]

def solve(inputFile, outputFile):
    # read case number
    T = processInputLine(inputFile)

    # iterate on all cases
    for t in range(T):
        # read input N & K
        _, K = processInputLine(inputFile)
        Pis = processInputLine(inputFile, float)

        SPis = sorted(Pis)

        P = 0
        for i in xrange(K + 1):
            P_ = PTie(SPis[0 : i] + SPis[- K + i:], K)

            if P < P_:
                iMin = i
                P = P_

        if iMin == 0 or iMin == K:
            print "EXTREME EXAMPLE : " + str(SPis) + " K : " + str(K)
        O = str(P)

        # generate output line
        outputLine = "Case #" + str(t + 1) + ": " + str(O) 
        if t < T - 1: 
            outputLine += "\r\n"
        outputFile.write(outputLine)
        print (outputLine)