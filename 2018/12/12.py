#!/usr/bin/env python2.7

import re
from collections import defaultdict

with open('input', 'r') as f:
  input_ = f.read().splitlines()

# input_ = """initial state: #..#.#..##......###...###
# 
# ...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #""".splitlines()

def printState(state):
  for i in xrange(-3, 36):
    print state[i],
  print

def solve(input_):
  state = defaultdict(lambda: '.', enumerate(input_.pop(0).split()[2]))
  input_.pop(0)
  pats = defaultdict(lambda: '.')
  for line in input_:
    pat, _, res = line.split()
    pats[pat] = res

  diffs = [0] * 2
  prev_sum = 0
  for g in xrange(50000000000):
    new_state = defaultdict(lambda: '.')
    for i in xrange(min(state.keys())-2, max(state.keys())+3):
      window = state[i-2] + state[i-1] + state[i] + state[i+1] + state[i+2]
      new_state[i] = pats[window]
    state = new_state
    diffs.pop(0)
    gen_sum = sum(map(lambda x: x[0] if x[1] == '#' else 0, state.items()))
    if g == 19: print gen_sum
    diffs.append(gen_sum - prev_sum)
    prev_sum = gen_sum
    if len(set(diffs)) == 1:
      return prev_sum + diffs[0] * (50000000000 - g - 1)

if __name__ == '__main__':
  print solve(input_)
