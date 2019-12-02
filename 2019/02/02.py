#!/usr/bin/env python2.7

with open('input', 'r') as f:
  input_ = [int(x) for x in f.read().splitlines()[0].split(',')]

#input_ = [1,9,10,3,2,3,11,0,99,30,40,50]

def func(memory, opcode, *args):
  if opcode == 1:
    memory[args[2]] = memory[args[0]] + memory[args[1]]
  elif opcode == 2:
    memory[args[2]] = memory[args[0]] * memory[args[1]]
  return len(args) + 1

def run(memory):
  ip = 0
  while memory[ip] != 99:
    ip += func(memory, *memory[ip:ip+4])
  return memory[0]

def p1():
  memory = input_[:]
  memory[1] = 12
  memory[2] = 2
  return run(memory)

def p2():
  for x in xrange(0, 100):
    for y in xrange(0, 100):
      memory = input_[:]
      memory[1] = x
      memory[2] = y
      if run(memory) == 19690720:
        return 100 * x + y

if __name__ == '__main__':
  print (p1(), p2())
