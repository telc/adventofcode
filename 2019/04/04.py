#!/usr/bin/env python2.7

import sys
from collections import defaultdict

input_ = "372037-905157"

def solve(start, stop):
  p1 = []
  p2 = []
  for p in [str(x) for x in xrange(start, stop + 1)]:
    increasing = True
    double = False
    for i in xrange(1, len(p)):
      if p[i] < p[i-1]:
        increasing = False
      if p[i-1] == p[i]:
        double = True
    if increasing and double:
      p1.append(p)
      if 2 in [p.count(d) for d in p]:
        p2.append(p)
  return len(p1), len(p2)

if __name__ == '__main__':
  print solve(*[int(x) for x in input_.split('-')])
