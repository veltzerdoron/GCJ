import numpy as np

T = int(input())
for t in range(T):
    N = int(input())

    Ls = list(map(int, input().split()))

    res = 0
    for i in range(N - 1):
        j = np.argmin(Ls[i:])
        Ls[i:i + j + 1] = reversed(Ls[i:i + j + 1])
        res += j + 1
    print("Case #{n}: {res}".format(n=t + 1, res=res))
