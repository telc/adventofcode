#!/usr/bin/env python2.7

from itertools import izip

last = [116, 299]
test = [65, 8921]

def generate(generator, last, factor, multiple, picky):
  dividor = 2147483647
  while generator > 0:
    last = (last * factor) % dividor
    if picky and last % multiple != 0:
      continue
    generator -= 1
    yield format(last, '032b')[-16:]


def solve(last, picky=False):
  multiples = [4, 8]
  factors = [16807, 48271]
  count = 0
  generator = 40000000
  if picky:
    generator = 5000000

  genA = generate(generator, last[0], factors[0], multiples[0], picky)
  genB = generate(generator, last[1], factors[1], multiples[1], picky)

  for a, b in izip(genA, genB):
    if a == b:
      count += 1
  return count

print solve(last)
print solve(last, True)
