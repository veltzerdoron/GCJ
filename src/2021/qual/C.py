import numpy as np
import random


def cost(N, Ls):
    _Ls = Ls[:]
    res = 0
    for i in range(N - 1):
        j = np.argmin(_Ls[i:])
        _Ls[i:i + j + 1] = reversed(_Ls[i:i + j + 1])
        res += j + 1
    return res


T = int(input())
for t in range(T):
    # N = random.randint(2, 1000)
    N, C = map(int, input().split())
    s = int(N * (N + 1) / 2)
    # C = random.randint(N - 1, s - 1)
    if C < N - 1 or C >= s:
        print("Case #{n}: IMPOSSIBLE".format(n=t + 1))
    else:
        Ls = list(range(1, N + 1))
        _C = C
        reversals = set()
        for k in reversed(range(1, N)):
            if C > k + k - 1:
                C -= k + 1
                reversals.add(k)
            else:
                C -= 1
        for k in sorted(reversals):
            Ls[N - k - 1:] = reversed(Ls[N - k - 1:])

        # if cost(N, Ls) != _C:
        #     print("PROBLEM!!!")
        #     print(Ls, N, _C, cost(N, Ls))
        print("Case #{n}: {Ls}".format(n=t + 1, Ls=" ".join(map(str, Ls))))
