#!/usr/bin/env python

import sys

def move (location, direction):
  if direction == '^':
    location['y'] -= 1
  if direction == '>':
    location['x'] += 1
  if direction == 'v':
    location['y'] += 1
  if direction == '<':
    location['x'] -= 1

if __name__ == '__main__':
  with open('input', 'r') as f:
    directions = f.read()

  santa = {'x': 0, 'y': 0}
  robot = {'x': 0, 'y': 0}
  delivered = [(0,0)]
  count = 0
  for d in directions:
    if count % 2 == 0:
      move(santa, d)
      delivered.append((santa['x'],santa['y']))
    else:
      move(robot, d)
      delivered.append((robot['x'],robot['y']))
    count += 1
  print len(set(delivered))
