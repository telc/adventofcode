#!/usr/bin/env python2.7

with open('input', 'r') as f:
  input_ = [int(x) for x in f.read().splitlines()[0].split(',')]

def resolveArgs(memory, mode, args):
  res = []
  for a in args:
    res.append(a if (mode % 10 == 1) else memory[a])
    mode //= 10
  return res

def run(memory, inputs):
  ip = 0
  output = []
  while True:
    opcode = memory[ip]
    ip += 1
    mode = opcode / 100
    opcode %= 100
    res = []
    if opcode == 99:
      return output
    elif opcode == 1:
      res = resolveArgs(memory, mode, memory[ip:ip+3])
      memory[memory[ip+2]] = res[0] + res[1]
    elif opcode == 2:
      res = resolveArgs(memory, mode, memory[ip:ip+3])
      memory[memory[ip+2]] = res[0] * res[1]
    elif opcode == 3:
      res = resolveArgs(memory, mode, memory[ip:ip+1])
      memory[memory[ip]] = inputs.pop(0)
    elif opcode == 4:
      res = resolveArgs(memory, mode, memory[ip:ip+1])
      output.append(res[0])
    elif opcode == 5:
      res = resolveArgs(memory, mode, memory[ip:ip+2])
      if res[0] != 0:
        ip = res[1]
        continue
    elif opcode == 6:
      res = resolveArgs(memory, mode, memory[ip:ip+2])
      if res[0] == 0:
        ip = res[1]
        continue
    elif opcode == 7:
      res = resolveArgs(memory, mode, memory[ip:ip+3])
      memory[memory[ip+2]] = 1 if res[0] < res[1] else 0
    elif opcode == 8:
      res = resolveArgs(memory, mode, memory[ip:ip+3])
      memory[memory[ip+2]] = 1 if res[0] == res[1] else 0
    ip += len(res)

def solve(program):
  return run(program[:], [1])[-1], run(program[:], [5])[-1]

if __name__ == '__main__':
  print solve(input_)
