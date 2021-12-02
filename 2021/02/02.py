#!/usr/bin/env python

with open('input', 'r') as f:
  input_ = f.read().splitlines()

example = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".splitlines()

def solve(commands, p2=False):
  pos = 0
  depth = 0
  aim = 0
  for c in commands:
    direction, units = c.split()
    units = int(units)
    if direction == 'forward':
      pos += units
      if p2:
        depth += aim * units
    if direction == 'down':
      if not p2:
        depth += units
      else:
        aim += units
    if direction == 'up':
      if not p2:
        depth -= units
      else:
        aim -= units
  return pos * depth

if __name__ == '__main__':
  print solve(input_)
  print solve(input_, True)
