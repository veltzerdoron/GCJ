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
from boto.dynamodb.condition import NULL

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

dirs = {
    "<" : (0, -1), 
    ">" : (0, 1),
    "^" : (-1, 0),
    "v" : (1, 0)}

def checkRun(M, r, c, d):
    while True: 
        r += d[0]
        c += d[1]
        if r < 0 or r >= len(M) or c < 0 or c >= len(M[0]):
            break
        if M[r][c] in dirs:
            return False
    return True

def solve(inputFile, outputFile):
    # read case number
    T = processInputLine(inputFile)

    # iterate on all cases
    for t in range(T):
        # read input R C
        R, C = processInputLine(inputFile)
        M = [""] * R
        for r in xrange(R):
            M[r] = processInputLine(inputFile, str)

        count = 0
        for r in xrange(R):
            for c in xrange(C):
                if M[r][c] in dirs:
                    if checkRun(M, r, c, dirs[M[r][c]]):
                        for d in dirs.keys():
                            if not checkRun(M, r, c, dirs[d]):
                                count += 1
                                break
                        else:
                            count = None
                            break

        if count is None:
            O = "IMPOSSIBLE"
        else:
            O = str(count)

        # generate output line
        outputLine = "Case #" + str(t + 1) + ": " + O 
        if t < T - 1: 
            outputLine += "\r\n"
        outputFile.write(outputLine)
        print (outputLine)