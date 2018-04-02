"""
@created: on Dec 29, 2017

@author: Doron Veltzer
"""

import functools

import numpy as np
import fractions
import math
import re

import sys


# read line from file split it according to separator and convert it to type
def process_input_line(input_file, 
                       input_type=int,
                       input_number=None,
                       force_list=False,
                       separator=' '):
    input_line = input_file.readline().rstrip()
    if input_number is None:
        input_vector = input_line.split(separator)
    else:
        input_vector = input_line.split(separator, input_number)
    output_vector = list(map(input_type, input_vector))
    if len(output_vector) == 1 and not force_list:
        return output_vector[0]
    else:
        return output_vector


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


# define useful constants
phi = (1 + 5 ** .5) / 2


def solve(input_file, output_file, error_file):
    # read case number
    t = process_input_line(input_file)

    # iterate on all cases
    for i in range(t):
        error_file.write('Solving problem #{}\n'.format(i + 1))
        # read input

        a1, a2, b1, b2 = process_input_line(input_file)

        # calculate output
        output = 0
        for a in range(a1, a2 + 1):
            phi_high = ma.ceil(phi * a)
            phi_low = ma.floor(a / phi)
            output += max(0, min(phi_low, b2) - b1 + 1)
            output += max(0, b2 - max(b1, phi_high) + 1)

        # print output
        output_file.write('Case #{}: {}\n'.format(i + 1, output))
        output_file.flush()


if __name__ == "__main__":
    solve(sys.stdin, sys.stdout, sys.stderr)
