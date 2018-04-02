'''
Created on May 8, 2016

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
        # read input J P S and K
        J, P, S, K = processInputLine(inputFile)

        O = ""
        R = min(S, K)
        O += str(J * P * R) + "\r\n"
        for j in xrange(1, J + 1):
            i = 0
            for p in xrange(1, P +1):
                for r in xrange(1, R + 1):
                    O += str(j) + " " + str(p) + " " + str((i + j) % S + 1) + " "
                    i += 1
                    if j < J or p < P or r < R:
                        O += "\r\n"

        # generate output line
        outputLine = "Case #" + str(t + 1) + ": " + O
        if t < T - 1: 
            outputLine += "\r\n"
        outputFile.write(outputLine)
        print (outputLine)