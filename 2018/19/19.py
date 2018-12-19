#!/usr/bin/env python2.7

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

#input_ = """#ip 0
#seti 5 0 1
#seti 6 0 2
#addi 0 1 0
#addr 1 2 3
#setr 1 0 0
#seti 8 0 4
#seti 9 0 5""".splitlines()

def run(regs, ip, program):
  while regs[ip] < len(input_):
    if regs[ip] == 1:
      m = max(regs)
      regs[0] = sum([x for x in xrange(1, m+1) if m % x == 0])
      return
    l = input_[regs[ip]].split()
    globals()[l[0]](regs, *map(int, l[1:]))
    regs[ip] += 1

def solve(input_):
  regs = [0] * 6
  ip = int(input_.pop(0)[-1])
  run(regs, ip, input_)
  part1 = regs[0]
  regs = [1] + [0] * 5
  run(regs, ip, input_)
  return part1, regs[0]

if __name__ == '__main__':
  print solve(input_)
