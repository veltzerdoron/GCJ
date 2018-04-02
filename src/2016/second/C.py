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

def position(v, R, C):
    # Map from outer cell number to a direction facing into the maze
    # and the position of the outer cell
    # 0-> downwards, 1-> leftwards, 2-> upwards, 3-> rightwards
    if v <= C:
        return 0, v - 1, -1
    v -= C
    if v <= R:
        return 1, C, v - 1
    v -= R
    if v <= C:
        return 2, C - v, R
    v -= C
    return 3, -1, R - v

def move(x, y, direction):
    return x + [0,-1, 0, 1][direction], y + [1 , 0, -1, 0][direction]

def solve(inputFile, outputFile):
    # read case number
    T = processInputLine(inputFile)

    # iterate on all cases
    for t in range(T):
        # read input R & C
        R, C = processInputLine(inputFile)
        permutation = processInputLine(inputFile)

        O = ""

        board = [[None] * C for _ in range(R)]
        size = 2 * (R + C)
        # prepare permutation by tupleing sort by length and standardizing direction 
        permutation = zip(permutation[::2], permutation[1::2])
        permutation.sort(key = lambda(a, b): min((b - a) % size, (a - b) % size))
        permutation = map(lambda(a, b): (b, a) if (a - b) % size > R + C else (a, b), permutation)
        for start, end in permutation:
            direction, x, y = position(start, R, C)
            x, y = move(x, y, direction)
            while 0 <= x < C and 0 <= y < R:
                if board[y][x] is None:
                    board[y][x] = "/\\"[direction & 1]
                direction ^= {"/": 1, "\\": 3}[board[y][x]]
                x, y = move(x, y, direction)
            if (x, y) != position(end, R, C)[1:]:
                O = "IMPOSSIBLE"
                break

        if O != "IMPOSSIBLE":
            O = "\n".join("".join(c or "/" for c in row) for row in board)
        # generate output line
        outputLine = "Case #" + str(t + 1) + ":\n" + O 
        if t < T - 1:
            outputLine += "\r\n"
        outputFile.write(outputLine)
        print (outputLine)