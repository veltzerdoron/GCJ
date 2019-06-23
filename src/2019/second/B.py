from sys import stdout
from heapq import heappush, heappop

def put(i, v, D):
    _ = input()
    D[0] -= 1
    print(i+1, v)
    stdout.flush()

P, V = 100, 20
N, S = 60, 14
assert(N + V < P)
for case in xrange(int(input())):
    D = [P]

    # day 1 ~ N
    for i in xrange(N):  # sabotage
        put(i%S, 1, D)

    # day N+1 ~ N+V
    min_heap = []
    for i in xrange(V):  # inspect
        put(i, 0, D)
        heappush(min_heap, (len(raw_input().strip().split()), -i))
    
    # day N+V+1 ~ P-1
    candidate = -heappop(min_heap)[1]
    while D[0] > 1:  # sabotage
        count, i = heappop(min_heap)
        put(-i, 1, D)
        heappush(min_heap, (count+1, i))
 
    # day P
    put(candidate, P, D)
