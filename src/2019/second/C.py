from fractions import *

T = int(input())
for t in range(T):
  n = int(input())
  a = []
  for i in range(n):
    a.append([int(i) for i in input().split(' ')])

  intersections = set()
  inf = 10 ** 20
  lower, upper = Fraction(0), Fraction(inf, 1)
  impossible = False
  for i in range(len(a) - 1):
    x1, y1 = a[i]
    x2, y2 = a[i + 1]
    if y1 == y2:
      if x1 >= x2:
        impossible = True
        break
    elif y1 > y2:
      upper = min(upper, Fraction(x2 - x1, y1 - y2))
    else:
      lower = max(lower, Fraction(x2 - x1, y1 - y2))

  if not impossible and 0 <= lower < upper:
    if upper == Fraction(inf, 1):
      de = 1
    else:
      mean = (lower + upper) / 2
      left = 0
      right = 10 ** 20
      while left + 1 < right:
        mid = (left + right) // 2
        tmp = mean.limit_denominator(mid)
        if lower < tmp < upper:
          right = mid
        else:
          left = mid
      de = right
    lower = lower * de
    upper = upper * de
    for i in range(int(lower) - 5, int(upper) + 5):
      if lower < i < upper:
        nu = i
        break
  else:
    impossible = True
  if impossible:
    result = 'IMPOSSIBLE'
  else:
    result = '{} {}'.format(de, nu)
  print('Case #{case}: {result}'.format(case= t + 1, result=result))
