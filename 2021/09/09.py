#!/usr/bin/env python3

from functools import reduce

def getNeighbours(grid, y, x):
  candidates = [(y-1,x), (y+1, x), (y, x-1), (y, x+1)]
  for cand in candidates:
    if cand[0] < 0 or cand[0] >= len(grid) or cand[1] < 0 or cand[1] >= len(grid[cand[0]]):
      continue
    yield cand

def isLowPoint(grid, y, x):
  for y1, x1 in getNeighbours(grid, y, x):
    if grid[y1][x1] <= grid[y][x]:
      return False
  return True

def fill(seen, grid, y, x):
  if grid[y][x] == 9 or (y,x) in seen:
    return
  seen.add((y,x))
  for y1, x1 in getNeighbours(grid, y, x):
    fill(seen, grid, y1, x1)

def solve(grid):
  sum_low = 0
  low_points = []
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if isLowPoint(grid, y, x):
        sum_low += grid[y][x] + 1
        low_points.append((y,x))

  basins = []
  for p in low_points:
    seen = set()
    fill(seen, grid, p[0], p[1])
    basins.append(len(seen))

  return sum_low, reduce(lambda a,b: a*b, sorted(basins)[-3:])

def getInput(fn):
  with open(fn, 'r') as f:
    return [[int(x) for x in line] for line in f.read().splitlines()]

def main():
  print(solve(getInput('input')))

if __name__ == '__main__':
  main()
