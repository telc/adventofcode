#!/usr/bin/env python3

from functools import reduce

def printGrid(grid):
  for row in grid:
    for d in row:
      print('.' if d == 0 else '#', end='')
    print('')
  print('')

def fold(grid, axis, line):
  if axis == 'x':
    grid = [list(z) for z in zip(*grid[::-1])]

  for y in range(line + 1, len(grid)):
    y1 = line + (line - y)
    if y1 < 0:
      break
    for x in range(len(grid[y1])):
      grid[y1][x] = grid[y][x] | grid[y1][x]
  grid = grid[:line]

  if axis == 'x':
    grid = [list(z) for z in zip(*grid[:line])][::-1]
    
  return grid

def solve(lines):
  folds = []
  coords = []
  coords_input = True
  for line in lines:
    if line == "":
      coords_input = False
      continue
    if coords_input:
      x, y = [int(c) for c in line.split(',')]
      coords.append((x,y))
    else:
      axis, n = line.split()[-1].split('=')
      folds.append((axis, int(n)))

  max_x = reduce(lambda a, b: a if a[0] > b[0] else b, coords)[0]
  max_y = reduce(lambda a, b: a if a[1] > b[1] else b, coords)[1]
  grid = [[0 for x in range(max_x+1)] for y in range(max_y+1)]

  for x, y in coords:
    grid[y][x] = 1

  p1 = 0
  for axis, line in folds:
    grid = fold(grid, axis, line)
    if p1 == 0:
      p1 = sum([d for row in grid for d in row])
  printGrid(grid)

  return p1

def getInput(fn):
  with open(fn, 'r') as f:
    return f.read().splitlines()

def main():
  print(solve(getInput('input')))

if __name__ == '__main__':
  main()
