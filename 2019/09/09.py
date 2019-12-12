#!/usr/bin/env python2.7

from itertools import permutations
from defaultlist import defaultlist

with open('input', 'r') as f:
  input_ = [int(x) for x in f.read().splitlines()[0].split(',')]

#input_ = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
#input_ = [1102,34915192,34915192,7,4,7,99,0]
#input_ = [104,1125899906842624,99]

def resolveArgs(memory, mode, base, args):
  res = []
  for a in args:
    res.append(a if (mode % 10 == 1) else memory[base+a] if (mode % 10 == 2) else memory[a])
    mode //= 10
  return res

def run(memory, inputs, outputs, ip=0):
  base = 0
  # FIXME
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
    elif opcode == 2:
      res = resolveArgs(memory, mode, base, memory[ip:ip+2])
      memory[pos(ip+2, mode/100)] = res[0] * res[1]
    elif opcode == 3:
      res = resolveArgs(memory, mode, base, memory[ip:ip])
      memory[pos(ip, mode)] = inputs.pop(0)
    elif opcode == 4:
      res = resolveArgs(memory, mode, base, memory[ip:ip+1])
      outputs.append(res.pop(0))
    elif opcode == 5:
      res = resolveArgs(memory, mode, base, memory[ip:ip+2])
      if res[0] != 0:
        ip = res[1]
        continue
      ip -= 1
    elif opcode == 6:
      res = resolveArgs(memory, mode, base, memory[ip:ip+2])
      if res[0] == 0:
        ip = res[1]
        continue
      ip -= 1
    elif opcode == 7:
      res = resolveArgs(memory, mode, base, memory[ip:ip+2])
      memory[pos(ip+2, mode/100)] = 1 if res[0] < res[1] else 0
    elif opcode == 8:
      res = resolveArgs(memory, mode, base, memory[ip:ip+2])
      memory[pos(ip+2, mode/100)] = 1 if res[0] == res[1] else 0
    elif opcode == 9:
      res = resolveArgs(memory, mode, base, memory[ip:ip+1])
      base += res.pop(0)
    else:
      return -2
    ip += len(res) + 1

def solve(program, inp):
  output = []
  memory = defaultlist(int)
  memory.extend(program)
  ip = 0
  while ip >= 0:
    ip = run(memory, [inp], output, ip)
  return output[0]

if __name__ == '__main__':
  print (solve(input_, 1), solve(input_, 2) )
