#!/usr/bin/env python2.7

import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../10'))
import hash as knot
from string import maketrans

test = 'flqrgnkx'
seed = 'wenycdww'

def makeGrid(seed):
  used = 0
  grid = []
  for i in range(128):
    h = knot.part2(seed + '-' + str(i))
    s = [h[i:i+2] for i in xrange(0, len(h), 2)]
    grid.append(''.join(map(lambda x: bin(int(x, 16))[2:].zfill(8), s)).translate(maketrans('01', '.#')))
  return grid

def part1(seed):
  grid = makeGrid(seed)
  return reduce((lambda x, y: x + y.count('#')), grid, 0)

def findNeighbours(grid, group, visited, y, x):
  visited.add((y,x))
  grid[y][x] = group
  for dy, dx in [(y-1,x), (y,x-1), (y+1,x), (y,x+1)]:
    if dy < 0 or dx < 0 or dy >= len(grid) or dx >= len(grid[dy]) or (dy,dx) in visited:
      continue
    if grid[dy][dx] == '#':
      findNeighbours(grid, group, visited, dy, dx)

def part2(seed):
  grid = map(list,makeGrid(seed))
  groups = 0
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if grid[y][x] == '#':
        groups += 1
        findNeighbours(grid, groups, set(), y, x)
  return groups

if __name__ == '__main__':
  print part1(seed)
  print part2(seed) 
