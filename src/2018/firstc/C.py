"""
@created: Dec 29, 2017
@Edited: May 5, 2018
@author: Doron Veltzer
"""

import functools

import fractions
import math
import re
from collections import OrderedDict

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


# print debug output to standard error file (since we are using standard input and output)
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
        # error_file.write('Solving problem #{0}\n'.format(i + 1))
        # read input
        n = process_input_line(input_file)
        ws = process_input_line(input_file)

        # print input
        # error_file.write('input {0} sized weights {1}\n'.format(n, ws))
        # check input

        # calculate output
        stacks = [(0, 0)]

        for j in range(n):
            next_stacks = stacks[:]
            for w, l in stacks:
                if w <= 6 * ws[j]:
                    # remove tuples where w1 > w2 and l1 < l2
                    w1, l1 = ws[j] + w, l + 1
                    # error_file.write('Trying {0}, {1}\n'.format(w1, l1))
                    for w2, l2 in stacks:
                        if w2 <= w1 and l2 >= l1:
                            # error_file.write('Found {0}, {1}\n'.format(w2, l2))
                            # error_file.write('While adding {0}, {1}\n'.format(w1, l1))
                            break
                        if w2 >= w1 and l2 <= l1:
                            # error_file.write('Removing {0}, {1}\n'.format(w2, l2))
                            next_stacks.remove((w2, l2))
                    else:
                        # error_file.write('Added {0}, {1}\n'.format(w1, l1))
                        next_stacks.append((w1, l1))
            stacks = next_stacks

        # set output
        output = str(max([l for _, l in stacks]))

        # print output
        output_file.write('Case #{}: {}\n'.format(i + 1, output))
        output_file.flush()


if __name__ == "__main__":
    solve(sys.stdin, sys.stdout, sys.stderr)
