T = int(input())

for t in range(T):
    N = int(input())
    Xs = list(map(int, input().split()))
    last = 0
    appends = 0
    # print(Xs)

    for x in Xs:
        if x > last:
            last = x
            continue
        else:
            x_, last_ = str(x), str(last)
            if len(x_) == len(last_):
                x *= 10
                appends += 1
            else:
                L = len(last_) - len(x_)
                for c1, c2 in zip(x_, last_):
                    if c1 > c2:
                        x *= pow(10, L)
                        appends += L
                        break
                    if c1 < c2:
                        x *= pow(10, L + 1)
                        appends += L + 1
                        break
                else:
                    indent = last_[-L:]
                    if not all([c == '9' for c in indent]):
                        x = int(x_ + last_[-L:]) + 1
                        appends += L
                    else:
                        x *= pow(10, L + 1)
                        appends += L + 1

        # print(last, x, appends)
        last = x

    print('Case #{n}: {y}'.format(n=t + 1, y=appends))
