#!/usr/bin/env python2.7

import re
import numpy as np
from operator import itemgetter
from collections import defaultdict

with open('input', 'r') as f:
  input_ = f.read().splitlines()

#input_ = """position=< 9,  1> velocity=< 0,  2>
#position=< 7,  0> velocity=<-1,  0>
#position=< 3, -2> velocity=<-1,  1>
#position=< 6, 10> velocity=<-2, -1>
#position=< 2, -4> velocity=< 2,  2>
#position=<-6, 10> velocity=< 2, -2>
#position=< 1,  8> velocity=< 1, -1>
#position=< 1,  7> velocity=< 1,  0>
#position=<-3, 11> velocity=< 1, -2>
#position=< 7,  6> velocity=<-1, -1>
#position=<-2,  3> velocity=< 1,  0>
#position=<-4,  3> velocity=< 2,  0>
#position=<10, -3> velocity=<-1,  1>
#position=< 5, 11> velocity=< 1, -2>
#position=< 4,  7> velocity=< 0, -1>
#position=< 8, -2> velocity=< 0,  1>
#position=<15,  0> velocity=<-2,  0>
#position=< 1,  6> velocity=< 1,  0>
#position=< 8,  9> velocity=< 0, -1>
#position=< 3,  3> velocity=<-1,  1>
#position=< 0,  5> velocity=< 0, -1>
#position=<-2,  2> velocity=< 2,  0>
#position=< 5, -2> velocity=< 1,  2>
#position=< 1,  4> velocity=< 2,  1>
#position=<-2,  7> velocity=< 2, -2>
#position=< 3,  6> velocity=<-1, -1>
#position=< 5,  0> velocity=< 1,  0>
#position=<-6,  0> velocity=< 2,  0>
#position=< 5,  9> velocity=< 1, -2>
#position=<14,  7> velocity=<-2,  0>
#position=<-3,  6> velocity=< 2, -1>""".splitlines()

def printPoints(points):
  max_x = max(points.keys())[0]
  min_x = min(points.keys())[0]
  max_y = max(points.keys(), key=itemgetter(1))[1]
  min_y = min(points.keys(), key=itemgetter(1))[1]

  for y in xrange(min_y, max_y+1):
    for x in xrange(min_x, max_x+1):
      if (x,y) in points:
        print '#',
      else:
        print '.',
    print
  print

def solve(input_):
  m = re.compile('-?\d+')
  points = defaultdict(list)
  for line in input_:
    px, py, vx, vy = map(int, re.findall(m, line))
    points[tuple(np.add((px,py), np.multiply(10000, (vx,vy))))].append((vx,vy))
  xlen = max(points.keys())[0]
  sec = 10000
  while True:
    sec += 1
    new_points = defaultdict(list)
    for p in points:
      for v in points[p]:
        new_points[tuple(np.add(p, v))].append(v)
    new_xlen = max(new_points.keys())[0]
    if new_xlen > xlen:
      printPoints(points)
      break
    points = new_points
    xlen = new_xlen
  return sec-1

if __name__ == '__main__':
  print solve(input_)
