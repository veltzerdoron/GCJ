import sys

T, W = map(int, input().split())
for t in range(T):
  r = [0] * 6

  print(224)
  ans = int(input())
  r[3] = ans >> 56
  r[4] = (ans % (1 << 56)) >> 44
  r[5] = (ans % (1 << 44)) >> 37

  print(56)
  ans = int(input())
  ans = ans - (r[3] << 14) - (r[4] << 11) - (r[5] << 7)
  r[0] = ans >> 56
  r[1] = (ans % (1 << 56)) >> 28
  r[2] = (ans % (1 << 28)) >> 18

  print(' '.join(map(str, r)))
  input()
