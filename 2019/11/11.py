#!/usr/bin/env python2.7

from collections import defaultdict
from defaultlist import defaultlist

with open('input', 'r') as f:
  input_ = [int(x) for x in f.read().splitlines()[0].split(',')]

def resolveArgs(memory, mode, base, args):
  res = []
  for a in args:
    res.append(a if (mode % 10 == 1) else memory[base+a] if (mode % 10 == 2) else memory[a])
    mode //= 10
  return res

def run(memory, inputs, outputs, ip=0):
  base = 0
  pos = lambda i,m: memory[i] if m == 0 else base + memory[i]
  while True:
    opcode = memory[ip]
    ip += 1
    mode = opcode / 100
    opcode %= 100
    res = []
    if opcode == 99:
      return -1
    elif opcode == 1:
      res = resolveArgs(memory, mode, base, memory[ip:ip+2])
      memory[pos(ip+2, mode/100)] = res[0] + res[1]
      ip += 3
    elif opcode == 2:
      res = resolveArgs(memory, mode, base, memory[ip:ip+2])
      memory[pos(ip+2, mode/100)] = res[0] * res[1]
      ip += 3
    elif opcode == 3:
      if len(inputs) == 0:
        return ip-1
      memory[pos(ip, mode)] = inputs.pop(0)
      ip += 1
    elif opcode == 4:
      res = resolveArgs(memory, mode, base, memory[ip:ip+1])
      outputs.append(res.pop(0))
      ip += 1
    elif opcode == 5:
      res = resolveArgs(memory, mode, base, memory[ip:ip+2])
      if res[0] != 0:
        ip = res[1]
      else:
        ip += 2
    elif opcode == 6:
      res = resolveArgs(memory, mode, base, memory[ip:ip+2])
      if res[0] == 0:
        ip = res[1]
      else:
        ip += 2
    elif opcode == 7:
      res = resolveArgs(memory, mode, base, memory[ip:ip+2])
      memory[pos(ip+2, mode/100)] = 1 if res[0] < res[1] else 0
      ip += 3
    elif opcode == 8:
      res = resolveArgs(memory, mode, base, memory[ip:ip+2])
      memory[pos(ip+2, mode/100)] = 1 if res[0] == res[1] else 0
      ip += 3
    elif opcode == 9:
      res = resolveArgs(memory, mode, base, memory[ip:ip+1])
      base += res.pop(0)
      ip += 1
    else:
      return -2

def move(x, y, d, right):
  dx, dy = d
  if right:
    d = (-dy, dx)
  else:
    d = (dy, -dx)
  return x + d[0], y + d[1], d

def solve(program, first):
  grid = defaultdict(int)
  x = 0
  y = 0
  d = (0, -1)
  grid[(x,y)] = first
  output = []
  memory = defaultlist(int)
  memory.extend(program)
  ip = 0
  while ip >= 0:
    ip = run(memory, [grid[(x,y)]], output, ip)
    grid[(x,y)] = output.pop(0)
    x, y, d = move(x, y, d, output.pop(0))

  if first == 1:
    xs = [c[0] for c in grid.iterkeys()]
    ys = [c[1] for c in grid.iterkeys()]
    for y in xrange(min(ys), max(ys)+1):
      for x in xrange(min(xs), max(xs)+1):
        if (x,y) in grid:
          print '#' if grid[(x,y)] == 1 else ' ',
        else:
          print ' ',
      print

  return len(grid)

if __name__ == '__main__':
  print solve(input_, 0)
  solve(input_, 1)
