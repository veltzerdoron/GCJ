for t in range(int(input())):
  p, q = map(int, input().split())
  q = q + 1
  
  hori = [0 for _ in range(q)]
  vert = [0 for _ in range(q)]
  for _ in range(p):
    x, y, d = input().split()
    x = int(x)
    y = int(y)
    if d == 'N':
      vert[y + 1] += 1 
    if d == 'S':
      vert[y] -= 1
      vert[0] += 1
    if d == 'E':
      hori[x + 1] += 1 
    if d == 'W':
      hori[x] -= 1
      hori[0] += 1

  x, y = 0, 0
  cum_sum_h, max_h = 0, 0
  cum_sum_v, max_v = 0, 0
  for i in range(q):
    cum_sum_h += hori[i]
    if cum_sum_h > max_h:
        max_h = cum_sum_h
        x = i
    cum_sum_v += vert[i]
    if cum_sum_v > max_v:
        max_v = cum_sum_v
        y = i
    
  print('Case #{n}: {x} {y}'.format(n = t + 1, x=x, y=y))

