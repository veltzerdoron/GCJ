import random
import sys

t = int(input())
for i in range(t):
  a = int(input())

  X = (a // 3) + 1

  A = {(x + 1, y + 1) for x in range(X) for y in [0, 1, 2]}

  while A:
    x, y = random.sample(A, 1)[0]
    x = min(X - 1, max(2, x))
    print(x, 2)
    sys.stdout.flush()
    x_, y_ = [int(s) for s in input().split(" ")]
    if (x_, y_) == (0, 0):
      # done
      # print("COMPLETED with A = {0}".format(A), file=sys.stderr)
      break
    elif (x_, y_) == (-1, -1):
      # error
      # print("Error with output {0},{1} and input {2},{3}".format(x, y, x_, y_), file=sys.stderr)
      break
    elif (x_, y_) in A:
      # print("Removed {0},{1} from A, remaining items {2}".format(x_, y_, len(A)), file=sys.stderr)
      A.remove((x_, y_))

