"""
@created: Dec 29, 2017
@Edited: May 5, 2018
@author: Doron Veltzer
"""

import functools

import fractions
import math
import re
import random

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
        # interactive
        n = process_input_line(input_file)

        ls, favs = [True] * n, [0] * n
        for j in range(n):
            # print input
            read = process_input_line(input_file)
            if read == -1:
                exit()
            if read == 0:
                # print output
                output_file.write('{}\n'.format(-1))
            else:
                d, *fs = read
                # increment favorites
                for f in fs:
                    favs[f] += 1

                # get least favorite flavor
                cans = [favs[f] for f in fs if ls[f]]
                # error_file.write('Can loli #{0}\n'.format(cans))

                if cans:
                    mincans = [f for f in fs if favs[f] == min(cans) and ls[f]]
                    s = random.choice(mincans)

                    ls[s] = False
                    # error_file.write('Dealing loli #{0}\n'.format(s))
                    # print output
                    output_file.write('{}\n'.format(s))
                else:
                    # error_file.write('No loli for you!\n')
                    # print output
                    output_file.write('{}\n'.format(-1))

            # flush output
            output_file.flush()


if __name__ == "__main__":
    solve(sys.stdin, sys.stdout, sys.stderr)