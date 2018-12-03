#!/usr/bin/env python2.7

import itertools
import re

with open('input', 'r') as f:
  inputlines = f.read()

#inputlines = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""

SIZE = 1000

def printFabric(fabric):
  for y in xrange(SIZE):
    print map(lambda x: x[0] if len(x) == 1 else 0, fabric[y])

def solve(inputlines):
  fabric = [[[] for y in xrange(SIZE)] for x in xrange(SIZE)]
  uniques = set()
  pat = re.compile('[#@,:x\s]')
  for cut in inputlines.splitlines():
    id, x, y, w, h = map(int,filter(None, pat.split(cut)))
    unique = True
    for i in xrange(y, y+h):
      for j in xrange(x, x+w):
        fabric[i][j].append(id)
        if len(fabric[i][j]) > 1:
          unique = False
          for u in fabric[i][j]:
            uniques.discard(u)
    if unique:
      uniques.add(id)
  return sum(map(sum, [map(lambda x: 1 if len(x) > 1 else 0, row) for row in fabric])), uniques.pop()

if __name__ == '__main__':
  print solve(inputlines)
