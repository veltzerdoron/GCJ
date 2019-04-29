from collections import defaultdict

for t in range(int(input())):
  n = int(input())
  wis = [input() for i in range(n)]

  count = defaultdict(int)  # suffix count
  words = defaultdict(set)  # words count

  for i, wi in enumerate(wis):
    for suf in [wi[j:] for j in range(len(wi))]:
      count[suf] += 1
      words[suf].add(i)

  good = [suf for suf, x in count.items() if x > 1]
  good.sort(key=len, reverse=True)

  print(good)

  result = 0
  used = set()
  for suf in good:
    available = list(words[suf] - used)
    if len(available) > 1:
      result += 2
      used |= set(available[:2])

  print('Case #{n}: {y}'.format(n=t + 1, y=result))
