T = int(input())

for t in range(T):
    M = int(input())
    Ps, Ns = zip(*[(map(int, input().split())) for _ in range(M)])
    score = 0

    print('Case #{n}: {y}'.format(n=t + 1, y=score))
