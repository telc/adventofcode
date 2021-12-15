#!/usr/bin/env python3
from statistics import median

def getNeighbours(grid, coord):
  y, x = coord
  for y in range(coord[0]-1, coord[0]+2):
    for x in range(coord[1]-1, coord[1]+2):
      if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]) or (y == coord[0] and x == coord[1]):
        continue
      yield (y,x)

def flash(grid, flashed, coord):
  flashed.append(coord)
  for n in getNeighbours(grid, coord):
    grid[n[0]][n[1]] += 1
    if n not in flashed and grid[n[0]][n[1]] > 9:
      flash(grid, flashed, n)

def solve(grid):
  p1 = 0
  flashes = []
  for step in range(1000):
    grid = list(map(lambda row: list(map(lambda o: o+1, row)), grid))
    flashed = []
    for y in range(len(grid)):
      for x in range(len(grid[y])):
        if (y,x) not in flashed and grid[y][x] > 9:
          flash(grid, flashed, (y,x))
    for o in flashed:
      grid[o[0]][o[1]] = 0
    flashes.append(len(flashed))
    if step == 99:
      p1 = sum(flashes)
    if len(flashed) == len(grid) * len(grid[0]):
      return p1, step+1

def getInput(fn):
  with open(fn, 'r') as f:
    return [[int(x) for x in line] for line in f.read().splitlines()]

def main():
  print(solve(getInput('input')))

if __name__ == '__main__':
  main()
