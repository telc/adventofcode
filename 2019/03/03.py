#!/usr/bin/env python2.7

import sys
from collections import defaultdict

with open('input', 'r') as f:
  input_ = f.read().splitlines()

#input_ = """R8,U5,L5,D3
#U7,R6,D4,L4""".splitlines()

#input_ = """R75,D30,R83,U83,L12,D49,R71,U7,L72
#U62,R66,U55,R34,D71,R55,D58,R83""".splitlines()

#input_ = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
#U98,R91,D20,R16,D67,R40,U7,R15,U6,R7""".splitlines()

def solve(wires):
  grid = defaultdict(int)
  first_steps = {}
  first = True
  closest = sys.maxint
  shortest = sys.maxint

  for wire in wires:
    steps = defaultdict(lambda: sys.maxint)
    x = 0
    y = 0
    s = 0
    for w in wire:
      d = int(w[1:])
      while d > 0:
        s += 1
        d -= 1
        if w[0] == 'U':
          y += 1
        elif w[0] == 'D':
          y -= 1
        elif w[0] == 'R':
          x += 1
        elif w[0] == 'L':
          x -= 1
        steps[(x,y)] = min(s, steps[(x,y)])
      if first:
        first = False
        first_steps = steps
    for k,v in steps.iteritems():
      grid[k] += 1
      if grid[k] > 1:
        s = v + first_steps[k]
        if s < shortest:
          shortest = s
        
  for k,v in grid.iteritems():
    if v > 1:
      dist = sum([abs(a) for a in k])
      if dist < closest:
        closest = dist
        
  return closest, shortest

if __name__ == '__main__':
  print solve([x.split(',') for x in input_])
