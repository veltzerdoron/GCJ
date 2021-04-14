T = int(input())
for t in range(T):
    X, Y, S = input().split()
    X = int(X)
    Y = int(Y)
    S = str(S)

    price = 0
    counter = 0
    last = '?'
    for s in S:
        if s == '?':
            counter += 1
            if counter == 1:
                if last == 'C' and X < 0:
                    price += X
                    last = 'J'
                    counter = 0
                if last == 'J' and Y < 0:
                    price += Y
                    last = 'C'
                    counter = 0
            if X + Y < 0 and counter == 2:
                price += X + Y
                counter = 0
            continue
        if s == 'J' and last == 'C':
            price += X
        if s == 'C' and last == 'J':
            price += Y
        last = s
    print("Case #{n}: {price}".format(n=t + 1, price=price))
