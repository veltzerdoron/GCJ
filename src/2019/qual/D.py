t = int(input())

for i in range(t):
    N, B, F = map(int, input().split())

    j = 1
    queries = [
        (("0" * j + "1" * j) * (N // j + 1))[:N] 
        for j in [2 ** k for k in range(min(B.bit_length() + 1, F))]
    ]

    responses = []
    for query in queries:
        print(query)
        responses.append(input())
    query_it = zip(*queries)
    response_it = zip(*responses)
    response_col = next(response_it, None)
    broken = []
    for j, query_col in enumerate(query_it):
        if query_col == response_col:
            response_col = next(response_it, None)
        else:
            broken.append(j )
    print(*broken)

    input()
