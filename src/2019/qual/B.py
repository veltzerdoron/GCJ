import sys

t = int(input())
for i in range(t):
  N = int(input())
  P = str(input())

  y = ""
  for step in P:
    if step == 'E':
      y += 'S'
    else:
      y += 'E'

  print("Case #{n}: {y}".format(n=i + 1, y=y))
