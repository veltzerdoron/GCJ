import sys
from collections import Counter

T, F = map(int, input().split())
for t in range(T):
  answer = ""

  valid_sets = list(range(119))

  figures = ['Z'] * 120

  for i in range(4):
    for s in valid_sets:
      print('{pos}'.format(pos=i + s * 5 + 1))
      sys.stdout.flush()
      figures[s] = input()

    count = Counter([figures[s] for s in valid_sets] + [c for c in set("ABCDE") - set(answer)])

    figure_i = min(count, key=count.get)
    answer += figure_i
    valid_sets = [s for s in valid_sets if figures[s] == figure_i]

  answer = answer + next(iter(set('ABCDE') - set(answer)))

  print(answer)
  sys.stdout.flush()
  input()
sys.exit()
