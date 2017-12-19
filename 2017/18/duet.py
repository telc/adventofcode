#!/usr/bin/env python2.7

instructions = """set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 735
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19"""

test1 = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

test2 = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""

def getValue(registers, register):
  try:
    return int(register)
  except:
    pass
  if register in registers:
    return registers[register]
  else:
    return 0

def do1(registers, instruction):
  inst = instruction.split()
  if inst[1] not in registers:
    registers[inst[1]] = 0
  if inst[0] == 'snd':
    registers['play'] = getValue(registers, inst[1])
  elif inst[0] == 'set':
    registers[inst[1]] = getValue(registers, inst[2])
  elif inst[0] == 'add':
    registers[inst[1]] += getValue(registers, inst[2])
  elif inst[0] == 'mul':
    registers[inst[1]] *= getValue(registers, inst[2])
  elif inst[0] == 'mod':
    registers[inst[1]] %= getValue(registers, inst[2])
  elif inst[0] == 'rcv':
    if getValue(registers, inst[1]) != 0:
      registers[inst[1]] = registers['play']
      return 1000
  elif inst[0] == 'jgz':
    if registers[inst[1]] > 0:
      return int(inst[2])
  return 1
    
def part1(instructions):
  registers = {}
  instructions = instructions.splitlines()
  ip = 0
  while ip >= 0 and ip < len(instructions):
    ip += do1(registers, instructions[ip])
  return registers['play']

def part2(instructions):
  instructions = instructions.splitlines()
  count = 0
  ips = [0,0]
  regs = [{'p': 0},{'p': 1}]
  queues = [[],[]]
  states = ['running','running']
  
  pp = 0
  ip = ips[pp]
  registers = regs[pp]
  while ip >= 0 and ip < len(instructions):
    inst = instructions[ip].split()
    if inst[1] not in registers:
      registers[inst[1]] = 0
    if inst[0] == 'snd':
      if pp == 1:
        count += 1
      queues[1-pp].append(getValue(registers, inst[1]))
    elif inst[0] == 'set':
      registers[inst[1]] = getValue(registers, inst[2])
    elif inst[0] == 'add':
      registers[inst[1]] += getValue(registers, inst[2])
    elif inst[0] == 'mul':
      registers[inst[1]] *= getValue(registers, inst[2])
    elif inst[0] == 'mod':
      registers[inst[1]] %= getValue(registers, inst[2])
    elif inst[0] == 'rcv':
      if len(queues[pp]):
        states[pp] = 'running'
        registers[inst[1]] = queues[pp].pop(0)
      else:
        if states[1-pp] != 'running' and len(queues[1-pp]) == 0:
          break
        states[pp] = 'waiting'
        ips[pp] = ip
        pp = 1 - pp
        ip = ips[pp]
        registers = regs[pp]
        continue
    elif inst[0] == 'jgz':
      if getValue(registers, inst[1]) > 0:
        ip += getValue(registers, inst[2])
        continue
    ip += 1
  return count

if __name__ == '__main__':
  print part1(instructions)
  print part2(instructions)
