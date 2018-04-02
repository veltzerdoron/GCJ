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


def solve(input_file, output_file, error_file):
    # read case number
    t = process_input_line(input_file)

    # iterate on all cases
    for i in range(t):
        # read input
        n, k = process_input_line(input_file)
        gs = [process_input_line(input_file, input_mapping=identity) for _ in range(n)]

        # print input
        # error_file.write("{} {} \n".format(n, k))
        # for g in gs:
        #     error_file.write(''.join(g) + '\n')

        # check input

        # output
        # "rotate" board
        rs = []
        for g in gs:
            r, n_subs = re.subn(r"\.", '', g)
            rs.append('.' * n_subs + r)

        # for r in rs:
        #     error_file.write(''.join(r) + '\n')

        # calculate winners
        winners = set()
        for color in ('R', 'B'):
            if color in winners:
                break
            for x in range(n):
                if color in winners:
                    break
                for y in range(n):
                    if color in winners:
                        break
                    # error_file.write('at : {},{}\n'.format(x, y))
                    if rs[x][y] != color:
                        continue
                    for dx, dy in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                        if color in winners:
                            break
                        if 0 <= x + (k - 1) * dx < n and 0 <= y + (k - 1) * dy < n:
                            for d in range(1, k):
                                # error_file.write('checking : {},{}\n'.format(x + d * dx, y + d * dy))
                                if rs[x + d * dx][y + d * dy] != color:
                                    break
                            else:
                                winners.add(color)
                                # error_file.write('found winner {}\n'.format(color))
                                break
        # error_file.write(str(winners))
        # set output
        if 'R' in winners:
            if 'B' in winners:
                output = "Both"
            else:
                output = "Red"
        else:
            if 'B' in winners:
                output = "Blue"
            else:
                output = "Neither"

        # print output
        output_line = 'Case #' + str(i + 1) + ': ' + output + '\n'
        output_file.write(output_line)
        output_file.flush()


if __name__ == "__main__":
    solve(sys.stdin, sys.stdout, sys.stderr)
