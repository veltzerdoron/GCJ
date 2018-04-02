'''
Created on April 30, 2016

@author: doronv
'''

# standard python package imports
import numpy as np
import fractions as fr
import math as ma
import re
from pybrain.rl.environments.mazes.tasks.maze4x3 import FourByThreeMaze
import six
from numpy import Infinity

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

C__ = ""
J__ = ""
minAbsDiff = np.Inf
minValC = np.Inf
minValJ = np.Inf

def compare(absDiff, valC, valJ):
    if (
            (absDiff < minAbsDiff) or
            (absDiff ==  minAbsDiff and valC < minValC) or
            (absDiff ==  minAbsDiff and valC == minValC and valJ < minValJ)
        ):
        return True
    return False

def checker(C, J):
    global C__
    global J__
    global minAbsDiff
    global minValC
    global minValJ
    valC = int(C)
    valJ = int(J)
    absDiff = np.abs(valC - valJ)
    if (compare(absDiff, valC, valJ)):
        C__ = C
        J__ = J
        minAbsDiff = absDiff
        minValC = valC
        minValJ = valJ

def getBest(C, J, i):
    if i == len(C):
        checker(C.replace("?", "0"), J.replace("?", "0"))
        return
    c = C[i]
    j = J[i]
    if c == "?" and j == "?":
        C_ = C[:i] + "0" + C[(i + 1):]
        J_ = J[:i] + "1" + J[(i + 1):]
        checker(C_.replace("?", "9"), J_.replace("?", "0"))
        C_ = C[:i] + "1" + C[(i + 1):]
        J_ = J[:i] + "0" + J[(i + 1):]
        checker(C_.replace("?", "0"), J_.replace("?", "9"))
        C_ = C[:i] + "0" + C[(i + 1):]
        J_ = J[:i] + "0" + J[(i + 1):]
        getBest(C_, J_, i + 1)
        return
    if c == "?":
        if j != "9":
            C_ = C[:i] + str(int(j) + 1) + C[(i + 1):]
            J_ = J[:i + 1] + J[i + 1:]
            checker(C_.replace("?", "0"), J_.replace("?", "9"))
        if j != "0":
            C_ = C[:i] + str(int(j) - 1) + C[(i + 1):]
            checker(C_.replace("?", "9"), J.replace("?", "0"))
        C_ = C[:i] + j + C[(i + 1):]
        getBest(C_, J, i + 1)
        return
    if j == "?":
        if c != "9":
            C_ = C[:i + 1] + C[i + 1:]
            J_ = J[:i] + str(int(c) + 1) + J[(i + 1):]
            checker(C_.replace("?", "9"), J_.replace("?", "0"))
        if c != "0":
            J_ = J[:i] + str(int(c) - 1) + J[i + 1:]
            checker(C.replace("?", "0"), J_.replace("?", "9"))
        J_ = J[:i] + c + J[i + 1:]
        getBest(C, J_, i + 1)
        return
    if int(c) > int(j):
        checker(C.replace("?", "0"), J.replace("?", "9"))
        return
    if int(c) < int(j):
        checker(C.replace("?", "9"), J.replace("?", "0"))
        return
    if int(c) == int(j):
        getBest(C, J, i + 1)
        return

# solution
def solve(inputFile, outputFile):
    global C__
    global J__
    global minAbsDiff
    global minValC
    global minValJ
    # read case number
    T = int(inputFile.readline())

    # iterate on all cases
    for t in range(T):
        C__ = ""
        J__ = ""
        minAbsDiff = np.Inf
        minValC = np.Inf
        minValJ = np.Inf
        # read input strings C & J
        C, J  = processInputLine(inputFile, ' ', None, str)

        getBest(C, J, 0)

        # construct output
        OutputLine = 'Case #' + str(t + 1) + ': ' + C__ + ' ' + J__
        if t < T - 1: OutputLine += '\r\n'
        outputFile.write(OutputLine)