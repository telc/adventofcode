#!/usr/bin/env python2.7

from collections import defaultdict

def test():
  return 6, {'A': (lambda v, p: (0, p-1, 'B') if v else (1, p+1, 'B')), 
             'B': (lambda v, p: (1, p+1, 'A') if v else (1, p-1, 'A'))}

def init():
  return 12794428, {'A': (lambda v, p: (0, p-1, 'F') if v else (1, p+1, 'B')),
                    'B': (lambda v, p: (0, p+1, 'D') if v else (0, p+1, 'C')),
                    'C': (lambda v, p: (1, p+1, 'E') if v else (1, p-1, 'D')),
                    'D': (lambda v, p: (0, p-1, 'D') if v else (0, p-1, 'E')),
                    'E': (lambda v, p: (1, p+1, 'C') if v else (0, p+1, 'A')),
                    'F': (lambda v, p: (1, p+1, 'A') if v else (1, p-1, 'A')),
  }

def solve(init):
  rounds, states = init()
  tape = defaultdict(int)
  cur = 'A'
  pos = 0

  for _ in xrange(rounds):
    tape[pos], pos, cur = states[cur](tape[pos], pos)

  return sum(tape.values())

if __name__ == '__main__':
  print solve(init)
