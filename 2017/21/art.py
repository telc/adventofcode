#!/usr/bin/env python2.7

import numpy as np

with open('input', 'r') as f:
  rules = f.read()

test = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#"""

def printGrid(grid):
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      print grid[y][x],
    print
  print

def rotatePart(part):
  permutations = set()
  part = [list(p) for p in part.split('/')]
  for _ in range(4):
    permutations.add('/'.join([''.join(p) for p in part]))
    part = zip(*part[::-1])
  return permutations

def flipPart(part):
  permutations = set()
  a = np.array([list(p) for p in part.split('/')])
  lr = np.fliplr(a)
  ud = np.flipud(a)
  permutations |= rotatePart('/'.join([''.join(p) for p in lr]))
  permutations |= rotatePart('/'.join([''.join(p) for p in ud]))
  return permutations

def partPermutations(part):
  permutations = set()
  permutations |= rotatePart(part)
  permutations |= flipPart(part)
  return permutations

def solve(rules, rounds):
  rules = {k: [list(v) for v in l.split('/')] for k, l in [line.split(' => ') for line in rules.splitlines()]}
  lot = {}
  for r in rules.keys():
    for p in partPermutations(r):
      lot[p] = r
  grid = [list('.#.'), list('..#'), list('###')]

  for _ in range(rounds):
    if len(grid) % 2 == 0:
      size = 2
    else:
      size = 3

    for y in range(len(grid)-size, -1, -size):
      grid.insert(y+size, ['.' for _ in range(len(grid[y]))])
      for x in range(len(grid[y])-size, -1, -size):
        part = ""
        for i in range(size):
          if i > 0:
            part += '/'
          part += ''.join(grid[y+i][x:x+size])
        new = rules[lot[part]]
        for i in range(len(new)):
          grid[y+i][x:x+size] = new[i]
  return sum([r.count('#') for r in grid])

if __name__ == '__main__':
  print solve(rules, 5)
  print solve(rules, 18)
