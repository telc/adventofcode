#!/usr/bin/env python2.7

with open('input', 'r') as f:
  input_ = [int(x) for x in f.read().splitlines()]

def fuel(mass):
  return max(mass / 3 - 2, 0)

def solve(input_):
  p1 = 0
  p2 = 0
  for m in input_:
    f = fuel(m)
    p1 += f
    while f > 0:
      p2 += f
      f = fuel(f)

  return p1, p2

if __name__ == '__main__':
  print solve(input_)
