for t in range(int(input())):
  n, k = map(int, input().split())
  
  cis = list(map(int, input().split()))
  dis = list(map(int, input().split()))
  
  max_cis = [0 for _ in range(n + 1)]
  max_dis = [0 for _ in range(n + 1)]

  fair = 0
  for l in range(n):
    max_cis[0] = cis[l]
    max_dis[0] = dis[l]
    for r in range(l + 1, n + 1):
      max_cis[r - l] = max(max_cis[r - l - 1], cis[r - 1])
      max_dis[r - l] = max(max_dis[r - l - 1], dis[r - 1])
      if abs(max_cis[r - l] - max_dis[r - l]) <= k:
        fair += 1

  print('Case #{n}: {result}'.format(n = t + 1, result=fair))

