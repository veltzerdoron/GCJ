from functools import reduce
import math as m
import sys

def matmult(m, v):
  nrows = len(m)
  w = [None] * nrows
  for row in range(nrows):
    w[row] = reduce(lambda x, y: x + y, map(lambda x, y: x * y, m[row], v))
  return w

def area_of_polygon(XYs):
  """ Calculates the area of an arbitrary polygon given its verticies """
  n = len(XYs)  # of corners
  area = 0.0
  for i in range(n):
    j = (i + 1) % n
    area += XYs[i][0] * XYs[j][1]
    area -= XYs[j][0] * XYs[i][1]
  area = abs(area) / 2.0
  # print ("XYs {0} area {1}".format(XYs, area))
  return area

def project_x_y(XYZs):
  return [xyz[0:2] for xyz in XYZs]

def rotate_around_x(As, alpha):
  c = m.cos(alpha)
  s = m.sin(alpha)
  R_alpha = [[1.0, 0, 0],
             [0, c, -s],
             [0, s, c]]

  b = []
  for a in As:
    c = matmult(R_alpha, a)
    b.append(c)
    #  print("Calculated {0}*{1} = {2}".format(R_alpha, a, c), file=sys.stderr)
  return b

def rotate_around_x_y(As, alpha):
  c = m.cos(alpha)
  s = m.sin(alpha)
  oosqrt2 = 1 / m.sqrt(2)
  R_alpha = [[0.5 * (1.0 + c), 0.5 * (1.0 - c), oosqrt2 * s],
             [0.5 * (1.0 - c), 0.5 * (1.0 + c), -oosqrt2 * s],
             [-oosqrt2 * s, oosqrt2 * s, c]]

  b = []
  for a in As:
    c = matmult(R_alpha, a)
    b.append(c)
    #  print("Calculated {0}*{1} = {2}".format(R_alpha, a, c), file=sys.stderr)
  return b

acc = 1.0e-15

t = int(input())
for i in range(t):
  A = float(input())

  Ps = [[0.5, 0.0, 0], [0.0, 0.5, 0.0], [0.0, 0.0, 0.5]]
  Cs = [[0.5, 0.5, 0.5], [0.5, -0.5, 0.5], [-0.5, -0.5, 0.5],
        [-0.5, -0.5, -0.5], [-0.5, 0.5, -0.5], [0.5, 0.5, -0.5]]

  if A < m.sqrt(2) + acc:
    alpha_min = 0.0
    alpha_max = m.pi / 4
    alpha = 0
    A_ = 1
    while (abs(A_ - A)) > acc:
      alpha = (alpha_min + alpha_max) / 2
      A_ = area_of_polygon(project_x_y(rotate_around_x(Cs, alpha)))
      # print("Calculated {1} squared kms using angle {0}".format(alpha, A_), file=sys.stderr)

      if A_ > A:
        alpha_max = alpha
      else:
        alpha_min = alpha
    Rs = rotate_around_x(Ps, alpha)

  else:
    alpha_min = 0.0
    alpha_max = 0.9552271644633687
    alpha = 0
    A_ = 1
    while (abs(A_ - A)) > acc:
      alpha = (alpha_min + alpha_max) / 2
      A_ = area_of_polygon(project_x_y(rotate_around_x_y(Cs, alpha)))
      # print("Calculated {1} squared kms using angle {0}".format(alpha, A_), file=sys.stderr)

      if A_ > A:
        alpha_max = alpha
      else:
        alpha_min = alpha
    Rs = rotate_around_x_y(Ps, alpha)

  s = "\n"
  for r in Rs:
    s += " ".join(map(str, r)) + "\n"

  print("Case #{0}: {1}".format(str(i + 1), s), end='')
