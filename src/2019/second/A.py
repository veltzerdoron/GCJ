from math import gcd

T = int(input())
for t in range(T):
  n = int(input())
  a = []
  for i in range(n):
    a.append([int(i) for i in input().split(' ')])

  intersections = set()
  for x1, y1 in a:
    for x2, y2 in a:
      nu = y2 - y1
      de = x1 - x2
      if nu * de > 0:
        if nu < 0:
          nu, de = -nu, -de
        g = gcd(nu, de)
        intersections.add((nu / g, de / g))
  result = len(intersections) + 1
  print('Case #{case}: {result}'.format(case=t + 1, result=result))
