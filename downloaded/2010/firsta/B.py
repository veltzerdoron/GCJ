#!/usr/bin/env python

from __future__ import division

import collections
import itertools
import sys

class gcj:
    IN = sys.stdin
    number = 0

    @classmethod
    def case(cls):
        cls.number += 1
        return 'Case #%d:' % cls.number

    @classmethod
    def line(cls, type=str):
        line = cls.IN.readline()
        return type(line.strip('\n'))

    @classmethod
    def splitline(cls, type=str):
        line = cls.IN.readline()
        return [type(x) for x in line.split()]

def go():
    t = gcj.line(int)
    for _ in xrange(t):
        D, I, m, n = gcj.splitline(int)
        data = gcj.splitline(int)
        assert len(data) == n
        print gcj.case(), solve(D, I, m, data)

def solve(D, I, m, data):
    n = len(data)
    tab = [0] * 256
    otab = [0] * 256
    for i in xrange(n):
        otab, tab = tab, otab
        for j in xrange(256):
            cur = otab[j] + D
            for k in xrange(256):
                new = otab[k] + abs(data[i] - j)
                if k != j:
                    if m == 0:
                        continue
                    new += (abs(k - j) - 1) // m * I
                cur = min(cur, new)
            tab[j] = cur
    return min(tab[i] for i in xrange(256))

go()
