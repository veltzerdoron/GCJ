import sys

t = int(input())
for i in range(t):
  d, P = [s for s in input().split(" ")]
  d = int(d)

  # read the P script and translate it
  shots = [0]
  power = 0
  for p in P:
    if p == 'C':
      power += 1
      shots.append(0)
    elif p == 'S':
      shots[power] += 1

  j = 0
  q = len(shots) - 1
  D = sum([ int(pow(2, x)) * y for x, y in enumerate(shots)])
  while D > d and q > 0:
    if shots[q] > 0:
      j += 1
      shots[q] -= 1
      shots[q - 1] += 1
      D -= pow(2, q - 1)
    else:
      q -= 1
  if D <= d:
    s = str(j)
  else:
    s = "IMPOSSIBLE"

  print("Case #{0}: {1}".format(i + 1, s))
