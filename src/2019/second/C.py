import sys

def getChildren(parent):
  grid = tuple(parent)
  ret = []
  r = len(grid)
  c = len(grid[0])
  if r == 0 or c == 0:
    return []
  for i in range(r):
    if all([grid[i][j] != "#" for j in range(c)]):
      A = grid[:i]
      B = grid[i + 1:]
      child = [A, B]
      ret.append(child)
  for j in range(c):
    if all([grid[i][j] != "#" for i in range(r)]):
      A = [grid[i][:j] for i in range(r)]
      B = [grid[i][j + 1:] for i in range(r)]
      child = [tuple(A), tuple(B)]
      ret.append(child)
  return ret

def NimSum(a, b):
  i = 0
  ans = 0
  while a + b > 0:
    ans += (2 ** i) * ((a + b) % 2)
    a //= 2
    b //= 2
    i += 1
  return ans

nim = {}
nim[()] = (0, 0)

def GetNim(grid):
  if grid not in nim:
    children = getChildren(grid)
    if len(children) == 0:
      nim[grid] = (0, 0)
    else:
      A = [0] * 100
      for child in children:
        a, x = GetNim(child[0])
        b, x = GetNim(child[1])
        c = NimSum(a ,b)
        if len(child[0]) == len(grid):
          A[c] += len(grid)
        else:
          A[c] += len(grid[0])
      nim[grid] = (A.index(0), A[0])
  return nim[grid]


for t in range(int(input())):
    r, c = map(int, input().split())
    grid = tuple([input() for _ in range(r)])
    _, ans = GetNim(grid)
    print("Case #{case}: {answer}".format(case=t + 1, answer=ans))

