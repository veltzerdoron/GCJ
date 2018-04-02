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

def MUP(P, R, S):
    if P == 0:
        if R == 1 and S == 1: 
            return "RS"
        else:
            return None
    if R == 0:
        if P == 1 and S == 1: 
            return "PS"
        else:
            return None
    if S == 0:
        if R == 1 and P == 1: 
            return "PR"
        else:
            return None

    P2 = P / 2
    P_2 = P % 2
    R2 = R / 2
    R_2 = R % 2
    S2 = S / 2
    S_2 = S % 2

    if P_2 == 0:
        first = MUP(P2, R2 + R_2, S2)
        second = MUP(P2, R2, S2 + S_2)
    elif R_2 == 0:
        first = MUP(P2 + P_2, R2, S2)
        second = MUP(P2, R2, S2 + S_2)
    elif S_2 == 0:
        first = MUP(P2 + P_2, R2, S2)
        second = MUP(P2, R2 + R_2, S2)

    # I could have returned none if all remainders are zero instead
    if first is None or second is None or first == second:
        return None 
    else:
        return first + second

def solve(inputFile, outputFile):
    # read case number
    T = processInputLine(inputFile)

    # iterate on all cases
    for t in range(T):
        # read input N, R, P, S
        _, R, P, S = processInputLine(inputFile)

        result = MUP(P, R, S)
        if result is None:
            O = "IMPOSSIBLE"
        else:
            O = result

        # generate output line
        outputLine = "Case #" + str(t + 1) + ": " + O 
        if t < T - 1: 
            outputLine += "\r\n"
        outputFile.write(outputLine)
        print (outputLine)