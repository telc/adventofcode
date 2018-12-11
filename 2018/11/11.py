#!/usr/bin/env python2.7

import numpy as np

SIZE = 300

def power(x, y, serial):
  rack_id = x + 10
  power = serial + (rack_id * y)
  power *= rack_id
  return (power // 10**2 % 10) - 5

def p1(input_, grid, size):
  regions = sum(grid[x:x-size, y:y-size] for y in xrange(size) for x in xrange(size))
  max_power = regions.max()
  coord = np.where(regions == max_power)
  return max_power, (coord[1][0] + 1, coord[0][0] + 1)

def solve(input_):
  grid = np.array([[power(x, y, input_) for x in xrange(1, SIZE + 1)] for y in xrange(1, SIZE + 1)])
  max_power, max_coord = p1(input_, grid, 3)
  sol1 = max_coord
  max_size = 3

  for s in xrange(4, 25):
    p, c = p1(input_, grid, s)
    if p > max_power:
      max_power = p
      max_coord = c
      max_size = s
  return sol1, (max_coord, max_size)

if __name__ == '__main__':
  print solve(5719)
