'''
@author: doronv
'''

import numpy as np
import re

M = [[ 0,  0,  0,  0,  0 ],
     [ 0,  1,  2,  3,  4 ],
     [ 0,  2, -1,  4, -3 ],
     [ 0,  3, -4, -1,  2 ],
     [ 0,  4,  3, -2, -1 ]]

def mul(a, b):
    sign = 1 if a * b > 0 else -1
    return sign * M[abs(a)][abs(b)]

def power(a, n):
    if n == 1: return a
    if n % 2 == 0: return power(mul(a, a), n // 2)
    return mul(a, power(mul(a, a), (n - 1) // 2))

def multiply_all(ijk, L, X):
    value = 1
    for i in xrange(L):
        value = mul(value, ijk[i])
    return power(value, X) # computes value^X

def construct_first_two(ijk, L, X):
    i_value = 1
    j_value = 1
    for i in xrange(X):
        for j in xrange(L):
            if i_value != 2:
                i_value = mul(i_value, ijk[j])
            elif j_value != 3:
                j_value = mul(j_value, ijk[j])
    return i_value == 2 and j_value == 3

def solve(inputFile, outputFile):
    # read case number
    T = int(inputFile.readline())
    
    # iterate on all cases
    for t in range(T):
        lineSplit = inputFile.readline().rstrip().split(' ')
        L = int(lineSplit[0])
        X = int(lineSplit[1])

        ijk = [(ord(v) - ord('i') + 2) for v in inputFile.readline()]

        ok1 = multiply_all(ijk, L, X) == -1
        ok2 = construct_first_two(ijk, L, min(8, X))

        # Output case result
        OutputLine = 'Case #' + str(t + 1) + ': ' 
        OutputLine += "YES" if ok1 and ok2 else "NO"
        if t < T - 1: OutputLine += '\r\n'
        outputFile.write(OutputLine)
