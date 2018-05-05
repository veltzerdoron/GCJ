import sys
import collections

Cashier = collections.namedtuple("Cashier", ["m", "s", "p"])

tc = int(sys.stdin.readline())


def find_min_time(nr, nb, cs):
    l = 0
    r = int(10**18 * 2)
    while l < r:
        mt = (l + r) // 2
        mc = []
        css = []
        for c in cs:
            if c.p >= mt:
                continue
            css.append(c)
        for c in css:
            mc.append(min(c.m, (mt - c.p) // c.s))
        mc.sort()
        mc.reverse()
        if sum(mc[:nr]) >= nb:
            r = mt
        else:
            l = mt + 1
    return l


for tn in range(tc):
    r, b, c = map(int, sys.stdin.readline().split())
    cs = []
    for _ in range(c):
        m, s, p = map(int, sys.stdin.readline().split())
        cs.append(Cashier(m, s, p))
    print("Case #%d: %d" % (tn + 1, find_min_time(r, b, cs)))

CLOSE