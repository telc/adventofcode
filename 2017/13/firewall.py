#!/usr/bin/env python2.7

ranges = """0: 3
1: 2
2: 4
4: 8
6: 5
8: 6
10: 6
12: 4
14: 6
16: 6
18: 17
20: 8
22: 8
24: 8
26: 9
28: 8
30: 12
32: 12
34: 10
36: 12
38: 12
40: 8
42: 12
44: 12
46: 10
48: 12
50: 12
52: 14
54: 14
56: 12
58: 14
60: 14
62: 14
64: 14
66: 14
68: 12
70: 14
72: 14
74: 14
76: 14
80: 18
82: 14
90: 18"""

test = """0: 3
1: 2
4: 4
6: 4"""

import operator

class Layer:
  def __init__(self, d, r):
    self.depth = d
    self.size = r
    self.pos = 0
    if self.size <= 1:
      self.direction = 0
    else:
      self.direction = 1

  def tick(self):
    self.pos += self.direction
    if self.pos == 0 or self.pos == (self.size - 1):
      self.direction *= -1


def parseRanges(ranges):
  return {int(d) : Layer(int(d), int(r)) for d, r in map(operator.methodcaller('split', ': '), ranges.splitlines())}

def part1(ranges, delay=0):
  state = parseRanges(ranges)
  end = 1 + max(state.keys())
  severity = 0

  for i in range(-delay, end):
    if i >= 0:
      if i in state and state[i].pos == 0:
        severity += i * state[i].size

    for layer in state.values():
      layer.tick()

  return severity

def part2(ranges):
  state = parseRanges(ranges)
  end = 1 + max(state.keys())
  packets = {}

  i = 0
  while True:
    packets[i] = -1
    for k,v in packets.items():
      packets[k] = v + 1
      if packets[k] in state and state[packets[k]].pos == 0:
        del packets[k]
        continue
      if packets[k] == end:
        return k
        
    for layer in state.values():
      layer.tick()
    i += 1

print part1(ranges)
print part2(ranges)
