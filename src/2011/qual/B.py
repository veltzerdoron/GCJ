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
                       input_type_array=None,
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
        error_file.write('Solving problem #{}\n'.format(i + 1))
        # read input
        game = process_input_line(input_file, str)
        c = int(game[0])
        combines = [None] * c
        for j in range(c):
            combines[j] = [sorted(game[j + 1][0:2]), game[j + 1][2]]
        d = int(game[c + 1])
        opposed = [None] * d
        for j in range(d):
            opposed[j] = game[c + j + 2]
        n = int(game[-2])
        s = game[-1]       
 
        # print input
        #eprint(c, combines, d, opposed, n, s)

        # check input

        # calculate output
        sj = ""
        for j in range(n):
            sj += s[j]
            # try combines
            combining = True
            while combining:
                for k in range(len(sj) - 1):
                    for combine in combines:
                        if sorted(sj[k:k + 2]) == combine[0]:
                            # combine
                            sj = sj[:k] + combine[1] + sj[k + 2:]
                            combining = True
                            break
                    else:
                        combining = False
                    if combining:
                        break
                else:
                    combining = False
            # try opposed
            for oppose in opposed:
                if all(ch in sj for ch in oppose):
                    sj = ""
                    break
        

        # set output
        output = '[' + ', '.join(sj) + ']'

        # print output
        output_file.write('Case #{}: {}\n'.format(i + 1, output))
        output_file.flush()


if __name__ == "__main__":
    solve(sys.stdin, sys.stdout, sys.stderr)
