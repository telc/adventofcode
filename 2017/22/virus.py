#!/usr/bin/env python2.7

from collections import defaultdict
from operator import add

with open('input', 'r') as f:
  status = f.read()

test = """..#
#..
..."""

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

directions = [LEFT, UP, RIGHT, DOWN]

def printGrid(grid):
  m = 0
  for k in grid.keys():
    if abs(k[0]) > m:
      m = abs(k[0])
    if abs(k[1]) > m:
      m = abs(k[1])
  for y in range(-m, m+1):
    for x in range(-m, m+1):
      print grid[(y,x)],
    print
  print

def turnLeft(direction):
  return directions[(directions.index(direction)-1)%4]

def turnRight(direction):
  return directions[(directions.index(direction)+1)%4]

def reverse(direction):
  return directions[(directions.index(direction)+2)%4]

def tick(grid, pos, direction, count, part2):
  if part2:
    if grid[pos] == '.':
      direction = turnLeft(direction)
      grid[pos] = 'W'
    elif grid[pos] == 'W':
      grid[pos] = '#'
      count += 1
    elif grid[pos] == '#':
      direction = turnRight(direction)
      grid[pos] = 'F'
    elif grid[pos] == 'F':
      direction = reverse(direction)
      grid[pos] = '.'
  else:
    if grid[pos] == '.':
      direction = turnLeft(direction)
      grid[pos] = '#'
      count += 1
    else:
      direction = turnRight(direction)
      grid[pos] = '.'
  pos = tuple(map(add, pos, direction))
  return pos, direction, count

def solve(status, part2=False):
  y = None
  grid = defaultdict(lambda: '.')
  for line in status.splitlines():
    if y == None:
      y = -(len(line)/2)
    for i in xrange(len(line)):
      x = i - len(line)/2
      grid[(y,x)] = line[i]
    y += 1
  pos = (0,0)
  direction = UP
  count = 0

  rounds = 10000
  if part2:
    rounds = 10000000
  for _ in xrange(rounds):
    pos, direction, count = tick(grid, pos, direction, count, part2)
  return count

if __name__ == '__main__':
  print solve(status)
  print solve(status, True)
