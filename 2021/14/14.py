#!/usr/bin/env python3

from collections import Counter
from itertools import tee 

def pairwise(iterable):
  a, b = tee(iterable)
  next(b, None)
  return zip(a, b)

def solve(polymer, rules, steps):
  pairs_count = Counter([''.join(pair) for pair in pairwise(polymer)])
  element_count = Counter(polymer)
  for _ in range(steps):
    new_pairs_count = Counter()
    for pair in pairs_count.keys():
      pair_count = pairs_count[pair]
      new_element = rules[pair]
      new_pairs_count[pair[0] + new_element] += pair_count
      new_pairs_count[new_element + pair[1]] += pair_count
      element_count[new_element] += pair_count
    pairs_count = new_pairs_count
  common = element_count.most_common()
  return common[0][1] - common[-1][1]


def getInput(fn):
  with open(fn, 'r') as f:
    lines = f.read().splitlines()
    polymer = lines[0]
    rules = {}
    for pair in lines[2:]:
      old, new = pair.split(' -> ')
      rules[old] = new
    return polymer, rules

def main():
  print(solve(*getInput('input'), 10), solve(*getInput('input'), 40))

if __name__ == '__main__':
  main()
