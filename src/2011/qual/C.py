"""
@created: Dec 29, 2017
@Edited: Feb 27, 2018
@author: Doron Veltzer
"""

import functools

import numpy as np
import fractions
import math
import re

import sys


# define useful methods
# read line from file split it according to separator and convert it to type
def process_input_line(input_file, 
                       input_mapping=int,
                       input_number=None,
                       force_list=False,
                       separator=' '):
    input_line = input_file.readline().rstrip()
    if input_number is None:
        input_vector = input_line.split(separator)
    else:
        input_vector = input_line.split(separator, input_number)
    output_vector = list(map(input_mapping, input_vector))
    if len(output_vector) == 1 and not force_list:
        return output_vector[0]
    else:
        return output_vector


#print debug output to standard error file (since we are using standard input and output)
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while a:
        a, b = b % a, a
    return b


def lcm(a, b):
        return (a * b) // gcd(a, b)


def gcd_list(v):
    return functools.reduce(gcd, v)


def lcm_list(v):
    return functools.reduce(lcm, v)


def identity(x):
    return x


# define useful constants


def solve(input_file, output_file, error_file):
    # read case number
    t = process_input_line(input_file)

    # iterate on all cases
    for i in range(t):
        error_file.write('Solving problem #{}\n'.format(i + 1))
        # read input
        n = process_input_line(input_file)
        Cs = process_input_line(input_file, input_number=n)

        xor = 0
        for c in Cs:
            xor = xor ^ c
        # print input
        # check input

        # calculate output
        # set output
        if xor == 0:
            output = sum(Cs) - min(Cs)
        else:
            output = "NO" 

        # print output
        output_file.write('Case #{}: {}\n'.format(i + 1, output))
        output_file.flush()



if __name__ == "__main__":
    solve(sys.stdin, sys.stdout, sys.stderr)
