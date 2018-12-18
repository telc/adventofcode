#!/usr/bin/env python2.7

from operator import  mul
from itertools import chain

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

MINUTES = 1000000000

def solve(input_):
  area = input_
  minute = 0
  hashes = []
  jumped = False
  while minute < MINUTES:
    minute += 1
    new_area = []
    for y in xrange(len(area)):
      for x in xrange(len(area[y])):
        num_trees = 0
        num_yards = 0
        for i in xrange(-1, 2):
          for j in xrange(-1, 2):
            if 0 <= y+i < len(area) and 0 <= x+j < len(area[y+i]) and not (i == 0 and j == 0):
              if area[y+i][x+j] == '|': num_trees += 1
              if area[y+i][x+j] == '#': num_yards += 1
        if y == len(new_area):
          new_area.append('')
        if area[y][x] == '.' and num_trees >= 3:
          new_area[y] += '|'
        elif area[y][x] == '|' and num_yards >= 3:
          new_area[y] += '#'
        elif area[y][x] == '#' and (num_yards < 1 or num_trees < 1):
          new_area[y] += '.'
        else:
          new_area[y] += area[y][x]
    area = new_area
    if minute == 10:
      part1 = mul(*map(sum, zip(*map(lambda x: (1,0) if x == '|' else (0,1) if x == '#' else (0,0), list(chain(*area)))))
    h = ''.join(area)
    if not jumped and h in hashes:
      loop_size = len(hashes) - hashes.index(h)
      minute += ((MINUTES - minute) / loop_size) * loop_size
      jumped = True
    hashes.append(h)
  return part1, mul(*map(sum, zip(*map(lambda x: (1,0) if x == '|' else (0,1) if x == '#' else (0,0), list(chain(*area)))))

if __name__ == '__main__':
  print solve(input_)
