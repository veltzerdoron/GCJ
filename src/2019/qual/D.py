from sys import stdout

num_cases = int(input())

for case_idx in range(num_cases):
    n, b, f = map(int, input().split())
    k = min(b.bit_length() + 1, f)
    queries = [
        (("0" * (1 << i) + "1" * (1 << i)) * -(-n >> i + 1))[:n] for i in range(k)
    ]
    responses = []
    for query in queries:
        print(query)
        stdout.flush()
        responses.append(input())
    query_it = zip(*queries)
    response_it = zip(*responses)
    response_col = next(response_it, None)
    broken = []
    for j, query_col in enumerate(query_it):
        if query_col == response_col:
            response_col = next(response_it, None)
        else:
            broken.append(j)
    print(*broken)
    stdout.flush()
    input()
