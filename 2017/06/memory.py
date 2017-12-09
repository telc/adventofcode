#!/usr/bin/env python

banks = "14 0 15 12 11 11 3 5 1 6 8 4 9 1 8 4"

test = "0 2 7 0"

def solve(banks):
  banks = map(int, banks.split())
  seen = {}
  rounds = 0
  while "".join(map(str, banks)) not in seen:
    seen["".join(map(str, banks))] = rounds
    rounds += 1
    blocks = max(banks)
    i = banks.index(max(banks))
    banks[i] = 0
    while blocks > 0:
      i = (i + 1) % len(banks)
      banks[i] += 1
      blocks -= 1
  return rounds, rounds - seen["".join(map(str, banks))]

print solve(banks)
