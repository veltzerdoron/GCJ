import math


def solve(p, cookies):
    # hypothesis: if it's possible to exceed, it's possible to get exact
    # if it's not, just add all hi's
    # no rigorous justification, just feel like that's probably the solution
    total_perim = sum(2 * (w + h) for (w, h) in cookies)
    p_cut = (p - total_perim) / 2.0
    cut_ranges = [(min(w, h), math.hypot(w, h)) for (w, h) in cookies]
    # update: lol that didn't work. maybe if the factor in question were 2 instead of sqrt(2)...
    # in case of two squares,
    # range of cutting both is (2, 2 sqrt(2))
    # range of cutting one is (1, sqrt(2))
    # these ranges are disjoint
    # we could consider each cookie in turn to augment valid ranges??

    possible_ranges = [(0, 0)]
    for clo, chi in cut_ranges:
        # compute possible ranges with or without this cookie
        prev_possible_ranges = possible_ranges
        possible_ranges = []
        for plo, phi in prev_possible_ranges:
            possible_ranges.append((plo, phi))
            possible_ranges.append((plo + clo, phi + chi))
        possible_ranges.sort()

        # coalesce resulting intervals
        prev_possible_ranges = possible_ranges
        possible_ranges = []
        for plo, phi in prev_possible_ranges:
            if not possible_ranges:
                possible_ranges.append((plo, phi))
            else:
                lo, hi = possible_ranges[-1]
                if hi < plo:
                    possible_ranges.append((plo, max(hi, phi)))
                else:
                    possible_ranges[-1] = (lo, max(hi, phi))

    # is p_cut in possible_ranges?
    best = None
    for lo, hi in possible_ranges:
        if best is None:
            best = hi
            continue
        if p_cut < lo:
            break
        elif lo <= p_cut <= hi:
            best = p_cut
            break
        elif hi < p_cut:
            best = hi

    return best * 2 + total_perim


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        fp = open(sys.argv[1])
    else:
        fp = sys.stdin


    def readline():
        return fp.readline().strip()


    num_cases = int(readline())
    for i in xrange(num_cases):
        n, p = readline().split()
        n = int(n)
        p = float(p)
        cookies = []
        for j in xrange(n):
            cookies.append(map(float, readline().split()))
        print
        "Case #%d: %.12f" % (i + 1, solve(p, cookies))