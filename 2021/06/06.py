#!/usr/bin/env python3

from collections import deque

def solve(fishes, rate, days):
  ages = deque([0 for x in range(9)])
  for fish in fishes:
    ages[fish] += 1

  for _ in range(days):
    ages.rotate(-1)
    ages[6] += ages[8]

  return sum(ages)

def getInput(fn):
  with open(fn, 'r') as f:
    return [int(x) for x in f.read().splitlines()[0].split(',')]

def main():
  print(solve(getInput('input'), 7, 80))
  print(solve(getInput('input'), 7, 256))

if __name__ == '__main__':
  main()
