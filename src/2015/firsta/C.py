'''
Created on April 30, 2016

@author: doronv
'''

# standard python package imports
import numpy as np
import fractions as fr
import math as ma
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
        N = processInputLine(inputFile)
        OutputLine = 'Case #' + str(t + 1) + ': ' 
        if t < T - 1: OutputLine += '\r\n'
        outputFile.write(OutputLine)