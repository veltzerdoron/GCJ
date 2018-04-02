'''
@author: doronv
'''

import numpy as np
import math
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
        # read input B & N
        B, N = processInputLine(inputFile)
        # read input Mks
        Mks = processInputLine(inputFile)

        cycle = LCMList(Mks)
        customerCycle = sum([cycle / Mk for Mk in Mks])
        N_ = N % customerCycle
        if N_ == 0:
            N_ = customerCycle
        Time = 0
        customer = 1
        working = [0] * B
        while customer <= N_:
            for i in xrange(B):
                if working[i] == 0:
                    # assign customer to barber i
                    customer += 1
                    working[i] = Mks[i] - 1
                    if customer > N_:
                        servingCustomerN = i + 1
                        break
                else:
                    working[i] -= 1
            Time += 1
        # Output case result
        OutputLine = 'Case #' + str(t + 1) + ': ' + str(servingCustomerN)
        if t < T - 1: OutputLine += '\r\n'
        outputFile.write(OutputLine)
