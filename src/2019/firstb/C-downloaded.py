def readline():
    return input()
def readint():
    return int(input())
def readfloat():
    return float(input())
def readints():
    xs = input().split()
    return [int(x) for x in xs]
def readfloats():
    xs = input().split()
    return [float(x) for x in xs]
def printcase(casenum, x):
    print('Case #{:d}: {}'.format(casenum, x))
def run(main):
    t = readint()
    for casenum in range(1, t + 1):
        main(casenum)

def search(subs, subs_valid, v, equal = False):
    low = 0
    high = subs_valid

    if equal:
        while low < high:
            mid = (low + high) // 2
            if subs[mid] >= v:
                low = mid + 1
            else:
                high = mid
    else:
        while low < high:
            mid = (low + high) // 2
            if subs[mid] > v:
                low = mid + 1
            else:
                high = mid

    return low

def main(casenum):
    n, k = readints()
    cs = readints()
    ds = readints()


    memo_right = [None] * n
    memo_left = [None] * n

    c_subs = [None] * (n + 1)
    c_subs_ind = [None] * (n + 1)
    c_subs_valid = 0

    d_subs = [None] * (n + 1)
    d_subs_ind = [None] * (n + 1)
    d_subs_valid = 0

    # Scan from left to right
    for i in range(n):
        c = cs[i]
        d = ds[i]

        lc = search(c_subs, c_subs_valid, c, True)
        c_subs[lc] = c
        c_subs_ind[lc] = i
        c_subs_valid = lc + 1

        if lc > 0:
            lc_ind = c_subs_ind[lc - 1] + 1
        else:
            lc_ind = 0

        ld = search(d_subs, d_subs_valid, d)
        d_subs[ld] = d
        d_subs_ind[ld] = i
        d_subs_valid = ld + 1

        if d > c + k:
            memo_left[i] = None
            continue

        ld_low = search(d_subs, d_subs_valid, c - k, True)
        ld_high = search(d_subs, d_subs_valid, c + k + 1, True)

        if ld_low > 0:
            ld_low_ind = d_subs_ind[ld_low - 1]
        else:
            ld_low_ind = -1
        if ld_high > 0:
            ld_high_ind = d_subs_ind[ld_high - 1] + 1
        else:
            ld_high_ind = 0

        l_high_ind = max(lc_ind, ld_high_ind)
        l_low_ind = max(ld_low_ind, l_high_ind - 1)

        memo_left[i] = (l_high_ind, l_low_ind)

    # Scan from right to left
    c_subs_valid = 0
    d_subs_valid = 0

    for i_ in range(n):
        i = n - i_ - 1

        c = cs[i]
        d = ds[i]

        rc = search(c_subs, c_subs_valid, c)
        c_subs[rc] = c
        c_subs_ind[rc] = i
        c_subs_valid = rc + 1

        if rc > 0:
            rc_ind = c_subs_ind[rc - 1] - 1
        else:
            rc_ind = n - 1

        rd = search(d_subs, d_subs_valid, d)
        d_subs[rd] = d
        d_subs_ind[rd] = i
        d_subs_valid = rd + 1

        if d > c + k:
            memo_right[i] = None
            continue

        rd_low = search(d_subs, d_subs_valid, c - k, True)
        rd_high = search(d_subs, d_subs_valid, c + k + 1, True)

        if rd_low > 0:
            rd_low_ind = d_subs_ind[rd_low - 1]
        else:
            rd_low_ind = n
        if rd_high > 0:
            rd_high_ind = d_subs_ind[rd_high - 1] - 1
        else:
            rd_high_ind = n - 1

        r_high_ind = min(rc_ind, rd_high_ind)
        r_low_ind = min(rd_low_ind, r_high_ind + 1)

        memo_right[i] = (r_high_ind, r_low_ind)

    # print('                ', casenum)
    count = 0
    for i in range(n):
        ml = memo_left[i]
        mr = memo_right[i]
        if ml is None or mr is None:
            # print('                ', i, None)
            continue

        la, lb = ml
        ra, rb = mr

        s = (i + 1 - la) * (ra + 1 - i) - (i - lb) * (rb - i)
        # print('                ', i, s, la, lb, ra, rb)
        count += s

    printcase(casenum, count)

run(main)
