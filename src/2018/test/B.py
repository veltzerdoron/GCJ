t = int(input())
for i in range(t):
  n = int(input())
  ss = [int(s) for s in input().split(" ")]

  s = ""
  while max (ss) > 0:
    m = ""
    for j in range(2):
      i = ss.index(max(ss))
      if ss[i] > 0:
        ss[i] -= 1
        m = m + chr(ord('A') + i)
    s = s + " " + m
  print("Case #{0}: {1}".format(str(t), s))
