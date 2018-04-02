import sys

t = int(input())
for _ in range(t):
  a, b = [int(s) for s in input().split(" ")]
  n = int(input())
  for _ in range(n):
    p = int((a + b) / 2)
    print("hello" + str(p), file=sys.stderr)
    print(p)
    sys.stdout.flush()
    s = input()
    if s == "TOO_BIG":
      b = p - 1
    elif s == "TOO_SMALL":
      a = p
    elif s == "WRONG_ANSWER":
      break
    elif s == "CORRECT": 
      break
    else:
      break
