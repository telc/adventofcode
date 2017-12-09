#!/usr/bin/env python

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

def mandist(p, q):
  return abs(p[0] - q[0]) + abs(p[1] - q[1])

def getCoords(square):
  x = 0
  y = 0
  i = 1
  steps = 1;
  remaining = steps;
  direction = RIGHT
  while (i < square):
    if direction == RIGHT:
      x += 1
    elif direction == UP:
      y -= 1
    elif direction == LEFT:
      x -= 1
    elif direction == DOWN:
      y += 1
    remaining -= 1
    if remaining <= 0:
      direction += 1
      direction %= 4
      if direction == LEFT or direction == RIGHT:
        steps += 1
      remaining = steps
    i += 1
  return (x,y)

def part1(square):
  return mandist((0,0), getCoords(square))

def getNeighborsValues(grid, coords):
  s = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
#        print (i,j), (coords[0]+i,coords[1]+j)
        if (coords[0]+i,coords[1]+j) in grid:
          s += grid[(coords[0]+i,coords[1]+j)]
  return s

def part2(square):
  grid = {(0,0): 1}
  x = 0
  y = 0
  i = 1
  steps = 1;
  remaining = steps;
  direction = RIGHT
  while (i < square):
    if direction == RIGHT:
      x += 1
    elif direction == UP:
      y -= 1
    elif direction == LEFT:
      x -= 1
    elif direction == DOWN:
      y += 1
    grid[(x,y)] = getNeighborsValues(grid, (x,y))
    if grid[(x,y)] > square:
      return grid[(x,y)]
    remaining -= 1
    if remaining <= 0:
      direction += 1
      direction %= 4
      if direction == LEFT or direction == RIGHT:
        steps += 1
      remaining = steps
    i += 1

print "part1:", part1(361527)
print "part2:", part2(361527)
