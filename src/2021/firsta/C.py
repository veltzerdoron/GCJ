T = int(input())

for t in range(T):
    N, Q = map(int, input().split())
    As, Ss = zip(*[(str(x[0]), int(x[1])) for _ in range(N) if (x := input().split())])
    # print(N, Q, As, Ss)
    guess = 0
    expectation = 0

    print('Case #{n}: {guess} {expectation}'.format(n=t + 1, guess=guess, expectation=expectation))
