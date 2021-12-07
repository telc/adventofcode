#!/usr/bin/env python3

from statistics import median

def part1(positions):
  target = median(positions)
  return int(sum(map(lambda p: abs(target - p), positions)))

def part2(positions):
  fuel_costs = []
  cost = lambda p: int((p**2 + p) / 2)
  for target in range(min(positions), max(positions)):
    fuel_costs.append(sum([cost(abs(target - p)) for p in positions]))
  return min(fuel_costs)


def getInput(fn):
  with open(fn, 'r') as f:
    return [int(x) for x in f.read().splitlines()[0].split(',')]

def main():
  print(part1(getInput('input')))
  print(part2(getInput('input')))

if __name__ == '__main__':
  main()
