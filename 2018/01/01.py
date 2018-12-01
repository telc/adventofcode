#!/usr/bin/env python2.7

with open('input', 'r') as f:
  changes = f.read()

def solve(changes):
  repeat = {0: True}
  changes = map(int, [c for c in changes.splitlines()])
  freq = 0;
  part1 = None
  part2 = None
  while not part2:
    for c in changes:
      freq += c;
      if part2 == None and freq in repeat:
        part2 = freq
      repeat[freq] = True
    if not part1:
      part1 = freq
  return part1, part2

if __name__ == '__main__':
  print solve(changes)
