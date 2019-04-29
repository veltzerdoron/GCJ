for t in range(int(input())):
  p, q = map(int, input().split())
  
  bins = [[0 for _ in range(q)] for _ in range(q)]
  for _ in range(p):
    x, y, d = input().split()
    x = int(x)
    y = int(y)
    print(x,y,d)
    if d == 'N':
      for i in range(q):
        for j in range(y + 1, q):
          bins[i][j] += 1 
    if d == 'S':
      for i in range(q):
        for j in range(y):
          bins[i][j] += 1
    if d == 'E':
      for i in range(x + 1, q):
        for j in range(q):
          bins[i][j] += 1
    if d == 'W':
      for i in range(x):
        for j in range(q):
          bins[i][j] += 1

    for col in bins:
        print(col)
  cols_max = [max(c) for c in bins]
  i = cols_max.index(max(cols_max))
  col = bins[i]
  j = col.index(max(col))

  print('Case #{n}: {x} {y}'.format(n = t + 1, x=i, y=j))
