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

    BMax = 50
    maxMs = [0 for _ in xrange(BMax)]
    maxMs[1] = 1 
    for b in xrange (2, BMax):
        for i in xrange(b):
            maxMs[b] += maxMs[i]

    # iterate on all cases
    for t in range(T):
        # read input B and M
        B, M = processInputLine(inputFile)

        O = ""

        if M > ma.pow(2, B - 2):
            O += "IMPOSSIBLE"
        else:
            O += "POSSIBLE" + "\r\n"
            if M == ma.pow(2, B - 2):
                MBIN = "1"
                M -= 1
            else:
                MBIN = "0"
            for _ in xrange(B - 1):
                if M % 2 == 1:
                    MBIN = "1" + MBIN
                else:
                    MBIN = "0" + MBIN 
                M /= 2
            O += MBIN + "\r\n"

            for i in xrange(1, B):
                for j in xrange(0, i + 1): 
                    O += "0"
                for j in xrange(i + 1, B): 
                    O += "1"
                if i < B - 1:
                    O += "\r\n"

        # generate output line
        outputLine = "Case #" + str(t + 1) + ": " + O 
        if t < T - 1: 
            outputLine += "\r\n"
        outputFile.write(outputLine)
        #print (outputLine)