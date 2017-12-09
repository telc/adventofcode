#!/usr/bin/env python

input ="""cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 16 c
cpy 17 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""

reg = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

def isInt(s):
  if s[0] == '-':
    return s[1:].isdigit()
  return s.isdigit()

commands = input.split('\n')
i = 0
while i < len(commands):
#  print commands[i]
  l = commands[i].split()
  if l[0] == 'cpy':
    if not isInt(l[1]):
      l[1] = reg[l[1]]
    reg[l[2]] = int(l[1])
  elif l[0] == 'inc':
    reg[l[1]] += 1
  elif l[0] == 'dec':
    reg[l[1]] -= 1
  elif l[0] == 'jnz':
    if not isInt(l[1]):
      l[1] = reg[l[1]]
    if l[1] != 0:
      i += int(l[2])
      continue
  i += 1
#  print i, reg

print reg
