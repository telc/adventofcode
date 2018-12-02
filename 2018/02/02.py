#!/usr/bin/env python2.7

import itertools

with open('input', 'r') as f:
  inputlines = f.read()

def part1(inputlines):
  twos = 0
  threes = 0
  ids = inputlines.splitlines()
  for id in ids:
    two = 0
    three = 0
    for c in set(id):
      if id.count(c) == 2:
        two = 1
      if id.count(c) == 3:
        three = 1
    twos += two
    threes += three
  return twos * threes

def part2(inputlines):
  ids = inputlines.splitlines()
  for a, b in itertools.combinations(ids, 2):
    difs = sum(1 for c1, c2 in zip(a, b) if c1 != c2)
    if difs == 1:
      return ''.join([c1 for c1, c2 in zip(a, b) if c1 == c2])

if __name__ == '__main__':
  print part1(inputlines), part2(inputlines)
