#!/usr/bin/env python

input = 'L1, L5, R1, R3, L4, L5, R5, R1, L2, L2, L3, R4, L2, R3, R1, L2, R5, R3, L4, R4, L3, R3, R3, L2, R1, L3, R2, L1, R4, L2, R4, L4, R5, L3, R1, R1, L1, L3, L2, R1, R3, R2, L1, R4, L4, R2, L189, L4, R5, R3, L1, R47, R4, R1, R3, L3, L3, L2, R70, L1, R4, R185, R5, L4, L5, R4, L1, L4, R5, L3, R2, R3, L5, L3, R5, L1, R5, L4, R1, R2, L2, L5, L2, R4, L3, R5, R1, L5, L4, L3, R4, L3, L4, L1, L5, L5, R5, L5, L2, L1, L2, L4, L1, L2, R3, R1, R1, L2, L5, R2, L3, L5, L4, L2, L1, L2, R3, L1, L4, R3, R3, L2, R5, L1, L3, L3, L3, L5, R5, R1, R2, L3, L2, R4, R1, R1, R3, R4, R3, L3, R3, L5, R2, L2, R4, R5, L4, L3, L1, L5, L1, R1, R2, L1, R3, R4, R5, R2, R3, L2, L1, L5'

dirs = ['Y_UP', 'X_UP', 'Y_DOWN', 'X_DOWN']
dirp = 0
x = 0
y = 0
commands = [c.lstrip(' ') for c in input.split(',')]
for i in range(len(commands)):
  if (commands[i][0] == 'L'):
    dirp -= 1
  else:
    dirp += 1
  dirp %= 4
  move = int(commands[i][1:])
  if dirs[dirp] == 'Y_UP':
    y += move
  elif dirs[dirp] == 'X_UP':
    x += move
  elif dirs[dirp] == 'Y_DOWN':
    y -= move
  elif dirs[dirp] == 'X_DOWN':
    x -= move
print abs(x) + abs(y)
