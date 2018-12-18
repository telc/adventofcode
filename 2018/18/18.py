#!/usr/bin/env python2.7

from collections import OrderedDict, defaultdict
from operator import itemgetter, mul

class OrderedDefaultDict(OrderedDict, defaultdict):
  def __init__(self, default_factory=None, *args, **kwargs):
    super(OrderedDefaultDict, self).__init__(*args, **kwargs)
    self.default_factory = default_factory

with open('input', 'r') as f:
  input_ = f.read().splitlines()

# input_ = """.#.#...|#.
# .....#|##|
# .|..|...#.
# ..|#.....#
# #.#|||#|#|
# ...#.||...
# .|....|...
# ||...#|.#|
# |.||||..|.
# ...#.|..|.""".splitlines()

def printArea(area):
  rowlen = max(area)[0]+1
  count = 0
  for a in area.values():
    print a,
    count += 1
    if count % rowlen == 0:
      print

MINUTES = 1000000000

def solve(input_):
  area = [[l for l in line] for line in input_]
  area = OrderedDefaultDict(lambda: '')
  for y in xrange(len(input_)):
    for x in xrange(len(input_[y])):
      area[(x,y)] = input_[y][x]
  minute = 0
  hashes = []
  jumped = False
  while minute < MINUTES:
    minute += 1
    new_area = OrderedDefaultDict(lambda: '')
    for y in xrange(len(input_)):
      for x in xrange(len(input_[y])):
        num_open = 0
        num_trees = 0
        num_yards = 0
        for i in xrange(-1, 2):
          for j in xrange(-1, 2):
            if not (i == 0 and j == 0):
              if area[(x+i,y+j)] == '.': num_open += 1
              if area[(x+i,y+j)] == '|': num_trees += 1
              if area[(x+i,y+j)] == '#': num_yards += 1
        if area[(x,y)] == '.' and num_trees >= 3:
          new_area[(x,y)] = '|'
        elif area[(x,y)] == '|' and num_yards >= 3:
          new_area[(x,y)] = '#'
        elif area[(x,y)] == '#' and (num_yards < 1 or num_trees < 1):
          new_area[(x,y)] = '.'
        else:
          new_area[(x,y)] = area[(x,y)]
    area = new_area
    sums = mul(*map(sum, zip(*map(lambda x: (1,0) if x == '|' else (0,1) if x == '#' else (0,0), area.values()))))
    if minute == 10:
      part1 = sums
    h = ''.join(area.values())
    if not jumped and h in hashes:
      loop_size = len(hashes) - hashes.index(h)
      minute += ((MINUTES - minute) / loop_size) * loop_size
      jumped = True
    hashes.append(h)
  return part1, sums

if __name__ == '__main__':
  print solve(input_)
