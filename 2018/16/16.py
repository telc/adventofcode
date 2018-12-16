#!/usr/bin/env python2.7

from collections import defaultdict
from collections import Counter

with open('input', 'r') as f:
  input_ = f.read().splitlines()

def addr(r,a,b,c):
  r[c] = r[a] + r[b]

def addi(r,a,b,c):
  r[c] = r[a] + b

def mulr(r,a,b,c):
  r[c] = r[a] * r[b]

def muli(r,a,b,c):
  r[c] = r[a] * b

def banr(r,a,b,c):
  r[c] = r[a] & r[b]

def bani(r,a,b,c):
  r[c] = r[a] & b

def borr(r,a,b,c):
  r[c] = r[a] | r[b]

def bori(r,a,b,c):
  r[c] = r[a] | b

def setr(r,a,b,c):
  r[c] = r[a]

def seti(r,a,b,c):
  r[c] = a

def gtir(r,a,b,c):
  r[c] = 1 if a > r[b] else 0

def gtri(r,a,b,c):
  r[c] = 1 if r[a] > b else 0

def gtrr(r,a,b,c):
  r[c] = 1 if r[a] > r[b] else 0

def eqir(r,a,b,c):
  r[c] = 1 if a == r[b] else 0

def eqri(r,a,b,c):
  r[c] = 1 if r[a] == b else 0

def eqrr(r,a,b,c):
  r[c] = 1 if r[a] == r[b] else 0

opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def solve(input_):
  input__ = iter(input_)
  part1 = 0
  test_prog = []
  op_candidates = {opcode : set(opcodes) for opcode in xrange(16)}
  for line in input__:
    if line.find('Before') != -1:
      before = eval(''.join(line.split()[1:]))
      opcode, A, B, C = map(int, next(input__).split())
      after = eval(''.join(next(input__).split()[1:]))
      candidates = set()
      for o in opcodes:
        tmp = before[:]
        if o(tmp, A, B, C) or tmp == after:
          candidates.add(o)
      if len(candidates) >= 3:
        part1 += 1
      op_candidates[opcode].intersection_update(candidates)
      next(input__)
    elif len(line):
      test_prog.append(map(int, line.split()))

  while True:
    unique_ops = {}
    for code, ops in op_candidates.iteritems():
      if len(ops) == 1:
        unique_ops[code] = ops
    for code_, ops_ in unique_ops.iteritems():
      for code, ops in op_candidates.iteritems():
        if code != code_:
          ops.difference_update(ops_)
    if len(unique_ops) == len(op_candidates):
      break
  ophash = { opcode: op_candidates[opcode].pop() for opcode in op_candidates }
  register = [0, 0, 0, 0]
  for o, A, B, C in test_prog:
    ophash[o](register, A, B, C)
  return part1, register[0]

if __name__ == '__main__':
  print solve(input_)
