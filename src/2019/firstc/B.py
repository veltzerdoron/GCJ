import sys
MODS = [11, 13, 14, 15, 16, 17, 18]
ans = {}
for i in range(int(1e6+1)):
  ans[tuple(i%m for m in MODS)] = i
T, N, M = map(int, input().split())
for t in range(T):
  rems = []
  for a in MODS:
    print(('%d ' % a) * 18)
    sys.stdout.flush()
    rems.append(sum(map(int, input().split())) % a)
  print(ans[tuple(rems)])
  sys.stdout.flush()
  input()
sys.exit()