#!/usr/bin/env python2.7

import sys
sys.setrecursionlimit(4000)

from itertools import izip_longest
from collections import defaultdict
from operator import itemgetter

with open('input', 'r') as f:
  input_ = f.read().splitlines()

#input_ = """x=495, y=2..7
#y=7, x=495..501
#x=501, y=3..7
#x=498, y=2..4
#x=506, y=1..2
#x=498, y=10..13
#x=504, y=10..13
#y=13, x=498..504""".splitlines()

def flow(clay, wet, rest, bottom, coord, direction):
  wet.add(coord)
  below = (coord[0], coord[1]+1)
  if not clay[below] and below not in wet and 1 <= below[1] <= bottom:
    flow(clay, wet, rest, bottom, below, (0, 1))
  if not clay[below] and below not in rest:
    return False
  
  left = (coord[0]-1, coord[1])
  right = (coord[0]+1, coord[1])
  left_stop = clay[left] or left not in wet and flow(clay, wet, rest, bottom, left, (-1, 0))
  right_stop = clay[right] or right not in wet and flow(clay, wet, rest, bottom, right, (1, 0))

  if direction == (0, 1) and left_stop and right_stop:
    rest.add(coord)
    while left in wet:
      rest.add(left)
      left = (left[0]-1, left[1])
    while right in wet:
      rest.add(right)
      right = (right[0]+1, right[1])
  return (direction == (-1, 0) and (left_stop or clay[left])) or (direction == (1, 0) and (right_stop or clay[right]))

def solve(input_):
  clay = defaultdict(lambda: False)
  for line in input_:
    l1, l2 = line.split(', ')
    axis, value = l1.split('=')
    value = int(value)
    start, stop = map(int, l2[2:].split('..'))
    r = xrange(start, stop+1)
    if axis == 'x':
      i = izip_longest([value], r, fillvalue=value)
    else:
      i = izip_longest(r, [value], fillvalue=value)
    for x, y in i:
      clay[(x,y)] = True
  
  top = min(clay, key=itemgetter(1))[1]
  bottom = max(clay, key=itemgetter(1))[1]
  wet = set()
  rest = set()
  flow(clay, wet, rest, bottom, (500, 0), (0, 1))

  return len([coord for coord in wet | rest if top <= coord[1] <= bottom]), len([coord for coord in rest if top <= coord[1] <= bottom]),

if __name__ == '__main__':
  print solve(input_)
