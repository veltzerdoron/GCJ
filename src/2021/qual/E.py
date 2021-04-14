# anomaly detection should work perfectly here

import math
import numpy as np
# import random


def sigmoid(x):
    """ sigmoid at x """
    return 1 / (1 + math.exp(-x))


def sigmoid_(x):
    """ sigmoid at x """
    s = sigmoid(x)
    return s * (1 - s)


def sigmoid_1(x):
    """ sigmoid at x """
    return math.log(x / (1 - x))


T = int(input())
P = int(input())

for t in range(T):
    results = [input() for _ in range(100)]

    results = [[1 if result_i[j] == '1' else 0 for j in range(10000)] for result_i in results]

    # initial guess for Ss and Qs
    SPs = [sum(result_i) / 10000 for result_i in results]
    Ss = [sigmoid_1(Sp) for Sp in SPs]
    QPs = [sum([result_i[j] for result_i in results]) / 100 for j in range(10000)]
    Qs = [sigmoid_1(Qp) for Qp in QPs]

    # Ss = np.random.uniform(-3, 3, 100)
    # Qs = np.random.uniform(-3, 3, 10000)

    # iterate to convergence using gradient descent and a heat weight of 1 / h
    # for h in range(1, 10):
    #     for i in range(100):
    #         Ss[i] -= sum([sigmoid_(Ss[i] - Qs[j]) if results[i][j] else - sigmoid_(Ss[i] - Qs[j])
    #                       for j in range(10000)]) / (h * 100000)
    #     for j in range(10000):
    #         Qs[j] += sum([sigmoid_(Ss[i] - Qs[j]) if results[i][j] else - sigmoid_(Ss[i] - Qs[j])
    #                       for i in range(100)]) / (h * 1000)

    # find out the cheater (the one who doesn't adhere to the computed S, Q estimates and wants to change them the most)
    deltaQ = [np.corrcoef(Qs, results[i])[0][1] for i in range(100)]
    res = np.argmin(deltaQ)
    print("Case #{n}: {res}".format(n=t + 1, res=res + 1))
