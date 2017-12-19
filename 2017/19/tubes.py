#!/usr/bin/env python2.7

from operator import add

with open('input', 'r') as f:
  tubes = f.read().splitlines()

def next(loc, direction):
  return tuple(map(add, loc, direction))

def newDirection(loc, direction):
  if direction == UP or direction == DOWN:
    if loc[1] > 0 and tubes[loc[0]][loc[1]-1] not in ' |+':
      return LEFT
    else:
      return RIGHT
  else:
    if loc[0] > 0 and tubes[loc[0]-1][loc[1]] not in ' -+':
      return UP
    else:
      return DOWN

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

letters = ''
direction = DOWN
loc = (0, tubes[0].index('|'))
p = tubes[loc[0]][loc[1]]
steps = 0
while p != ' ':
  steps += 1
  loc = next(loc, direction)
  p = tubes[loc[0]][loc[1]]
  if p not in '|-+':
    letters += p
  elif p == '+':
    direction = newDirection(loc, direction)
print letters, steps
