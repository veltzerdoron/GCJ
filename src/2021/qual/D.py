from sys import stdout
import random
import statistics

T, N, Q = map(int, input().split())
indices = list(range(N))
for case_idx in range(T):
    result = list(range(1, N + 1))
    samples = set()
    for _ in range(Q // T):
        while True:
            i, j, k = random.sample(indices, 3)
            if sorted((result[i], result[j], result[k])) not in samples:
                break
        samples.add(sorted((result[i], result[j], result[k])))
        si, sj, sk = result[i], result[j], result[k]
        m = statistics.median([i, j, k])
        print(result[i], result[j], result[k])
        stdout.flush()
        ri = int(input())
        # print(ri, result[m])
        if ri != result[m]:
            if ri == si:
                result[m], result[i] = result[i], result[m]
            if ri == sj:
                result[m], result[j] = result[j], result[m]
            if ri == sk:
                result[m], result[k] = result[k], result[m]
        # print(result)
    print(' '.join(map(str, result)))
    stdout.flush()

    reply = input()