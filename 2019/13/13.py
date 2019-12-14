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
      memory[pos(ip, mode)] = inputs.pop(0)
      ip += 1
    elif opcode == 4:
      res = resolveArgs(memory, mode, base, memory[ip:ip+1])
      outputs.append(res.pop(0))
      ip += 1
      if len(outputs) >= 3:
        return ip
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

def solve(program):
  display = defaultdict(int)
  output = []
  memory = defaultlist(int)
  memory.extend(program)
  ip = 0
  while ip >= 0:
    ip = run(memory, [], output, ip)
    if len(output):
      display[(output[0], output[1])] = output[2]
      output = []
  return display.values().count(2)

if __name__ == '__main__':
  print solve(input_)
