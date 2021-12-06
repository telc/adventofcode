#!/usr/bin/env python3

def solve(lines, diagonals=False):
  lines = [[int(x) for x in l.split(',')] for line in lines for l in line.split(' -> ')]
  size = max([i for sub in lines for i in sub]) + 1
  grid = [[0 for x in range(size)] for y in range(size)]
  for i in range(0, len(lines), 2):
    x1,y1 = lines[i]
    x2,y2 = lines[i+1]
    xstep = 1
    ystep = 1
    if x2 < x1:
      xstep = -1
    if y2 < y1:
      ystep = -1
    if x1 == x2:
      for y in range(y1, y2+ystep, ystep):
        grid[y][x1] += 1
    elif y1 == y2:
      for x in range(x1, x2+xstep, xstep):
        grid[y1][x] += 1
    else:
      if not diagonals:
        continue
      y = y1
      x = x1
      while y != y2+ystep:
        grid[y][x] += 1
        y += ystep
        x += xstep
  return sum(map(lambda v: 1 if v > 1 else 0, [i for sub in grid for i in sub]))

def getInput(fn):
  with open(fn, 'r') as f:
    return f.read().splitlines()

def main():
  print(solve(getInput('input')))
  print(solve(getInput('input'), True))

if __name__ == '__main__':
  main()
