#!/usr/bin/env python

import numpy as np

wires = {}

def resolveWires(name):
  print name, wires[name]
  if not isinstance(wires[name], list):
    return wires[name]
  if len(wires[name]) == 1:
    if representsInt(wires[name][0]):
      wires[name] = np.uint16(int(wires[name][0]))
    else:
      wires[name] = resolveWires(wires[name][0])
  else:
    if wires[name][0] == 'NOT':
      if representsInt(wires[name][1]):
        wires[name] = ~wires[name][1]
      else:
        wires[name] = ~resolveWires(wires[name][1])
    else:
      if representsInt(wires[name][0]):
        v1 = np.uint16(int(wires[name][0]))
      else:
        v1 = resolveWires(wires[name][0])
      if representsInt(wires[name][2]):
        v2 = np.uint16(int(wires[name][2]))
      else:
        v2 = resolveWires(wires[name][2])
      if wires[name][1] == 'AND':
        wires[name] = v1 & v2
      elif wires[name][1] == 'OR':
        wires[name] = v1 | v2
      elif wires[name][1] == 'LSHIFT':
        wires[name] = v1 << v2
      elif wires[name][1] == 'RSHIFT':
        wires[name] = v1 >> v2
  return wires[name]

def readCommand(command):
  s = command.split()
  name = s[-1:][0]
  wires[name] = s[:-2]

def representsInt(s):
  try:
    int(s)
    return True
  except:
    return False

if __name__ == '__main__':
  with open('input', 'r') as f:
    commands = f.read().splitlines()

  for command in commands:
    readCommand(command)

  a1 = resolveWires('a')

  wires = {}
  for command in commands:
    readCommand(command)

  wires['b'] = a1

  a2 = resolveWires('a')

  print a1, a2
