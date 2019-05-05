for t in range(int(input())):
  a = int(input())
  
  cis = ['0'] * a 
  for i in range(a):
    cis[i] = input()
  
  answer = ""
  
  pis = [0] * a
  valids = set(list(range(a)))
  for _ in range(500):
    RPS = set([cis[i][pis[i]] for i in valids])

    if len(RPS) == 3:
      answer = "IMPOSSIBLE"
      break
    if len(RPS) == 2:
      if 'R' not in RPS:
        answer += 'S'
        valids = [i for i in valids if cis[i][pis[i]] == 'S']
      elif 'P' not in RPS:
        answer += 'R'
        valids = [i for i in valids if cis[i][pis[i]] == 'R']
      elif 'S' not in RPS:
        answer += 'P'
        valids = [i for i in valids if cis[i][pis[i]] == 'P']
      for i in valids:
        pis[i] = ((pis[i] + 1) % len(cis[i]))
    if len(RPS) == 1:
      if 'R' in RPS:
        answer += 'P'
      elif 'P' in RPS:
        answer += 'S'
      elif 'S' in RPS:
        answer += 'R'
      break
  else:
    answer = "IMPOSSIBLE"
  print('Case #{n}: {answer}'.format(n = t + 1, answer=answer))

