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
        # read input N
        _ = processInputLine(inputFile)

        Pis = processInputLine(inputFile)

        SPis = sorted(enumerate(Pis), key=lambda x:x[1], reverse=True)

        O = ""
        
        # reduce the biggest one
        if len(Pis) > 1:
            for i in xrange(SPis[0][1] - SPis [1][1]):
                O += chr(ord("A") + SPis[0][0]) + " "
        else:
            raise Exception("This cannot be!!!")

        for i in xrange(2, len(Pis)):
            P, Pj = SPis[i]
            for _ in xrange(Pj):
                O += chr(ord("A") + P) + " "

        for i in xrange(SPis[1][1]):
            O += chr(ord('A') + SPis[0][0]) + chr(ord('A') + SPis[1][0]) + " "

        # generate output line
        outputLine = "Case #" + str(t + 1) + ": " + O 
        if t < T - 1: 
            outputLine += "\r\n"
        outputFile.write(outputLine)
        print (outputLine)