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
        n, *instructions = process_input_line(input_file, str)
        n = int(n)
        robots = [None] * n
        buttons = [None] * n
        for j in range(n):
            robots[j] = instructions[j * 2]
            buttons[j] = int(instructions[j * 2 + 1])
        
        # print input
        #eprint(n, robot, button)

        # check input

        # calculate output
        O, B, time, spare, last = 1, 1, 0, 0, None
        for button, robot in zip(buttons, robots):
            if robot == 'O':
                delta = abs(button - O)
                if last == 'O':
                    time += delta + 1
                    spare += delta + 1
                else:
                    time += max(delta - spare, 0) + 1
                    spare = max(delta - spare, 0) + 1
                O = button
            if robot == 'B':
                delta = abs(button - B)
                if last == 'B':
                    time += delta + 1
                    spare += delta + 1
                else:
                    time += max(delta - spare, 0) + 1
                    spare = max(delta - spare, 0) + 1
                B = button
            last = robot
        # set output
        output = str(time)

        # print output
        output_file.write('Case #{}: {}\n'.format(i + 1, output))
        output_file.flush()


if __name__ == "__main__":
    solve(sys.stdin, sys.stdout, sys.stderr)
