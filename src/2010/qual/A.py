"""
Created on Dec 29, 2017

@author: Doron Veltzer
"""

import functools

# import numpy as np
# import fractions as fr
# import math as ma
# import re

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


def solve(input_file, output_file):
    # read case number
    t = process_input_line(input_file)

    # iterate on all cases
    for i in range(t):
        # read n and k
        n, k = process_input_line(input_file, int)

        if (k + 1) % 2**n == 0:
            output = "ON"
        else:
            output = "OFF"

        # Output case result
        output_line = 'Case #' + str(i + 1) + ': ' + output + '\n'
        output_file.write(output_line)
        output_file.flush()

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
