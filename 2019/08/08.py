#!/usr/bin/env python2.7

import sys

with open('input', 'r') as f:
  input_ = f.read().splitlines()[0]

def solve(sif, w, h):
  flatten = lambda l: [item for sublist in l for item in sublist]
  sif = [int(x) for x in sif]
  layers = []
  least_zero = sys.maxint
  check = 0
  while len(sif) > 0:
    rows = []
    for y in xrange(h):
      row = []
      for x in xrange(w):
        row.append(sif.pop(0))
      rows.append(row)
    flatt = flatten(rows)
    zeros = flatt.count(0)
    if zeros < least_zero:
      least_zero = zeros
      check = flatt.count(1) * flatt.count(2)
    layers.append(rows)

  render = [[2 for x in xrange(w)] for y in xrange(h)]
  for layer in layers:
    for y in xrange(h):
      for x in xrange(w):
        if render[y][x] == 2:
          render[y][x] = layer[y][x]
  for row in render:
    for r in row:
      print '#' if r else ' ',
    print
  return check

if __name__ == '__main__':
#  print solve("123456789012", 3, 2)
#  print solve("0222112222120000", 2, 2)
  print solve(input_, 25, 6)
