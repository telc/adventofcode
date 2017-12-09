#!/usr/bin/env python

code = """cpy a b
dec b
cpy a d
cpy 0 a
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
dec b
cpy b c
cpy c d
dec d
inc c
jnz d -2
tgl c
cpy -16 c
jnz 1 c
cpy 83 c
jnz 78 d
inc a
inc d
jnz d -2
inc c
jnz c -5"""

reg = {'a': 12, 'b': 0, 'c': 0, 'd': 0}

def isInt(s):
  if s[0] == '-':
    return s[1:].isdigit()
  return s.isdigit()

commands = code.split('\n')
i = 0
while i < len(commands):
#  print commands[i]
  l = commands[i].split()
  if l[0] == 'cpy':
    if not isInt(l[1]):
      l[1] = reg[l[1]]
    if not isInt(l[2]):
      reg[l[2]] = int(l[1])
  elif l[0] == 'inc':
    reg[l[1]] += 1
  elif l[0] == 'dec':
    reg[l[1]] -= 1
  elif l[0] == 'jnz':
    if not isInt(l[1]):
      l[1] = reg[l[1]]
    if l[1] != 0:
      if not isInt(l[2]):
        l[2] = reg[l[2]]
      i += int(l[2])
      continue
  elif l[0] == 'tgl':
    if not isInt(l[1]):
      l[1] = reg[l[1]]
    try:
      n = commands[i+l[1]].split()
      if n[0] == 'inc':
        n[0] = 'dec'
      elif n[0] == 'dec' or n[0] == 'tgl':
        n[0] = 'inc'
      elif n[0] == 'jnz':
        n[0] = 'cpy'
      elif n[0] == 'cpy':
        n[0] = 'jnz'
      commands[i+l[1]] = ' '.join(n)
    except:
      pass
  i += 1
#  print i, reg

print reg
