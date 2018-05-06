"""
@created: Dec 29, 2017
@Edited: May 5, 2018
@author: Doron Veltzer
"""

import functools

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
        n, l = process_input_line(input_file)

        ws = [process_input_line(input_file, input_mapping=str) for _ in range(n)]
        # error_file.write('{0}\n'.format(ws))

        cs = [{ws[k][j] for k in range(n)} for j in range(l)]
        # error_file.write('{0}\n'.format(cs))

        def gen_word(j):
            if j == l:
                yield('')
            else:
                for c in cs[j]:
                    # error_file.write('char {0}\n'.format(c))
                    for suffix in gen_word(j + 1):
                        yield(c + suffix)

        # print input
        # check input

        # calculate output
        j = 0
        output = None
        for word in gen_word(0):
            # error_file.write('word {0}\n'.format(word))
            if word not in ws:
                # error_file.write('word {0}\n'.format(word))
                output = word
            j += 1
            if j > n:
                # error_file.write('none\n')
                output = '-'

        # print output
        # error_file.write('Output {0}\n'.format(output))
        output_file.write('Case #{0}: {1}\n'.format(i + 1, output))
        output_file.flush()


if __name__ == "__main__":
    solve(sys.stdin, sys.stdout, sys.stderr)
