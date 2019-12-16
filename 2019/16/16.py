#!/usr/bin/env python2.7

from collections import deque

with open('input', 'r') as f:
  input_ = f.read().splitlines()[0]

#input_ = "12345678"
#input_ = "80871224585914546619083218645595"

def calc(signal):
  base = [0, 1, 0, -1]

  phase = []
  for i in xrange(len(signal)):
    pat = deque([base[p] for p in xrange(4) for _ in xrange(i+1)])
    pat.rotate(-1)
    s = 0
    for j in xrange(len(signal)):
      s += signal[j] * pat[j%len(pat)]
    phase.append(int(str(abs(s))[-1]))
  return phase

def solve(signal):
  signal = [int(s) for s in signal]
  for i in xrange(100):
    signal = calc(signal)
  return ''.join(map(str, signal[:8]))

if __name__ == '__main__':
  print solve(input_)
