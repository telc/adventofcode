#!/usr/bin/env python2.7

from itertools import permutations

with open('input', 'r') as f:
  input_ = [int(x) for x in f.read().splitlines()[0].split(',')]

def resolveArgs(memory, mode, args):
  res = []
  for a in args:
    res.append(a if (mode % 10 == 1) else memory[a])
    mode //= 10
  return res

def run(memory, inputs, outputs, ip=0):
  while True:
    opcode = memory[ip]
    ip += 1
    mode = opcode / 100
    opcode %= 100
    res = []
    if opcode == 99:
      return -1
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
      outputs.append(res[0])
      return ip
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

def part1(program):
  trust = 0
  for perm in permutations(xrange(5)):
    input1 = [perm[0], 0]
    input2 = [perm[1]]
    input3 = [perm[2]]
    input4 = [perm[3]]
    input5 = [perm[4]]
    run(program[:], input1, input2)
    run(program[:], input2, input3)
    run(program[:], input3, input4)
    run(program[:], input4, input5)
    run(program[:], input5, input1)
    if input1[-1] > trust:
      trust = input1[-1]
  return trust

def part2(program):
  trust = 0
  a5 = 0
  for perm in permutations(xrange(5, 10)):
    programs = [program[:], program[:], program[:], program[:], program[:]]
    ips = [0, 0, 0, 0, 0]
    inputs = [[p] for p in perm]
    inputs[0].append(0)
    while ips[4] >= 0:
      for p in xrange(len(programs)):
        ips[p] = run(programs[p], inputs[p], inputs[(p+1) % len(programs)], ips[p])
    if inputs[0][-1] > trust:
      trust = inputs[0][-1]
  return trust

if __name__ == '__main__':
  print (part1(input_), part2(input_))
