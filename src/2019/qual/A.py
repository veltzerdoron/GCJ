import sys

t = int(input())
for i in range(t):
  N = int(input())

  s = str(N)

  A = ""
  B = ""
  for d in s:
    if d == '4':
      A += '2'
      B += '2'
    else:
      A += d
      B += '0'

  print("Case #{n}: {A} {B}".format(n=i + 1, A=int(A), B=int(B)))
