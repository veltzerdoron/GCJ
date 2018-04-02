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


def solve(input_file, output_file, error_file):
    # read case number
    t = process_input_line(input_file)

    # iterate on all cases
    for i in range(t):
        error_file.write('Solving problem #{}\n'.format(i + 1))
        # read input
        D, I, M, N = process_input_line(input_file)

        As = process_input_line(input_file, input_type=int, input_number=N, force_list=True)

        # print input

        # check input
        assert len(As) == N

        # calculate output
        tab = [0] * 256
        otab = [0] * 256
        for j in range(N):
            otab, tab = tab, otab
            for k in range(256):
                cur = otab[k] + D
                for l in range(256):
                    new = otab[l] + abs(As[j] - k)
                    if l != k:
                        if M == 0:
                            continue
                        new += (abs(l - k) - 1) // M * i
                    cur = min(cur, new)
                tab[k] = cur

        output = str(min(tab[k] for k in range(256)))

        # print output
        output_file.write('Case #{}: {}\n'.format(i + 1, output))
        output_file.flush()


if __name__ == "__main__":
    solve(sys.stdin, sys.stdout, sys.stderr)
