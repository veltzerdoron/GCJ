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
        print('Solving problem #{}'.format(i + 1), file=error_file)
        # read input
        n = process_input_line(input_file)
        elements = process_input_line(input_file, force_list=True)

        # print input
        # check input

        # calculate output
        in_place = 0
        for j, element in enumerate(elements):
            if j == element - 1:
                in_place += 1
        # set output
        output = "{0:.6f}".format(n - in_place)

        # print output
        print('Case #{}: {}'.format(i + 1, output), file=output_file)
        output_file.flush()


if __name__ == "__main__":
    solve(sys.stdin, sys.stdout, sys.stderr)
