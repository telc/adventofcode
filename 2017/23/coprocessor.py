#!/usr/bin/env python2.7

from collections import defaultdict

instructions = """set b 99
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23"""

def getValue(registers, register):
  try:
    return int(register)
  except:
    pass
  if register in registers:
    return registers[register]
  else:
    return 0

def do(registers, instruction, debug, count):
  inst = instruction.split()
  if inst[0] == 'set':
    registers[inst[1]] = getValue(registers, inst[2])
  elif inst[0] == 'add':
    registers[inst[1]] += getValue(registers, inst[2])
  elif inst[0] == 'sub':
    registers[inst[1]] -= getValue(registers, inst[2])
  elif inst[0] == 'mul':
    if debug:
      count[0] += 1
    registers[inst[1]] *= getValue(registers, inst[2])
  elif inst[0] == 'mod':
    registers[inst[1]] %= getValue(registers, inst[2])
  elif inst[0] == 'jgz':
    if getValue(registers, inst[1]) > 0:
      return getValue(registers, inst[2])
  elif inst[0] == 'jnz':
    if getValue(registers, inst[1]) != 0:
      return getValue(registers, inst[2])
  return 1
    
def run(instructions, debug=True):
  registers = defaultdict(int)
  if not debug:
    registers['a'] = 1
  instructions = instructions.splitlines()
  ip = 0
  count = [0]
  while ip >= 0 and ip < len(instructions):
    ip += do(registers, instructions[ip], debug, count)
  if debug:
    return count[0]
  return registers['h']

def part2opt1():
  h = 0
  a = 1
  b = 99
  c = 99
  b *= 100
  b -= -100000
  c = b
  c -= -17000
  while True:
    f = 1
    d = 2
    while d - b != 0:
      e = 2
      while e - b != 0:
        if (d * e) - b == 0:
          f = 0
        e += 1
      d += 1
    if f == 0:
      h += 1
    if b - c == 0:
      return h
    b += 17

def part2opt():
  b = 99 * 100 + 100000
  c = b + 17000
  h = 0
  for b in xrange(b, c+1, 17):
    for d in xrange(2, b):
      if b % d == 0:
        h += 1
        break
  return h

if __name__ == '__main__':
  print run(instructions)
  print part2opt()
