#!/usr/bin/env python2.7

from operator import itemgetter
from collections import defaultdict

with open('input', 'r') as f:
  input_ = f.read().splitlines()

#input_ = """1, 1
#1, 6
#8, 3
#3, 4
#5, 5
#8, 9""".splitlines()

def solve(input_):
  coords = [tuple(map(int, line.split(', '))) for line in input_]
  max_x, max_y = max(coords)[0] + 1, max(coords, key=itemgetter(1))[1] + 1
  areas = [[None for x in xrange(max_x)] for y in xrange(max_y)]
  region = set()
  for y in xrange(max_y):
    for x in xrange(max_x):
      node = None
      closest = 1000000
      sum_ = 0
      for (px, py) in coords:
        dist = abs(px - x) + abs(py - y)
        sum_ += dist
        if dist < closest:
          node = (px, py)
          closest = dist
        elif dist == closest and closest != (px, py):
          node = None
      areas[y][x] = node
      if sum_ < 10000:
        region.add((x, y))

  dists = [[0 for x in xrange(max_x)] for y in xrange(max_y)]
  for y in xrange(max_y):
    for x in xrange(max_x):
      if not areas[y][x]:
        continue
      px, py = areas[y][x]
      if x in (0, max_x) or y in (0, max_y):
        dists[py][px] -= 1000000
      dists[py][px] += 1

  return max(map(max, dists)), len(region)

if __name__ == '__main__':
  print solve(input_)
