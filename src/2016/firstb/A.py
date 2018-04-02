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
        # read input string S
        S = processInputLine(inputFile, ' ', None, str)[0]
        #"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", 
        #"SIX", "SEVEN", "EIGHT", "NINE"
        zero = S.count('Z')
        two = S.count('W')
        four = S.count('U')
        six = S.count('X')
        eight = S.count('G')
        one = S.count('O') - two - four - zero
        five = S.count('F') - four
        seven = S.count('S') - six
        three = S.count('H') - eight
        nine = S.count('I') - six - five - eight

        OutputLine = 'Case #' + str(t + 1) + ': '
        OutputLine += '0' * zero + '1' * one + '2' * two + '3' * three + '4' * four + '5' * five + '6' * six + '7' * seven + '8' * eight + '9' * nine
        if t < T - 1: OutputLine += '\r\n'
        outputFile.write(OutputLine)