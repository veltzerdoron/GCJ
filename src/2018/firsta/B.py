import sys

def ts(L): #L is a 0-indexed list of integers
  done = False
  while not done:
    done = True
    for i in range(len(L) - 2):
      if L[i] > L[i + 2]:
        done = False
        L[i], L[i + 2] = L[i + 2], L[i]

t = int(input())
for i in range(t):
  n = int(input())
  V = [int(s) for s in input().split(" ")]

  ts(V)
  
  for j in range(len(V) - 1):
    if V[j] > V[j + 1]:
      s = str(j) 
      break
  else:
    s = "OK"
    
  print("Case #{0}: {1}".format(i + 1, s))
