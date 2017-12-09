#!/usr/bin/env python

grid = [[0 for x in range(1000)] for y in range(1000)]

def turnOn(x, y):
  grid[x][y] += 1

def turnOff(x, y):
  grid[x][y] = max(0, grid[x][y]-1)

def toggle(x, y):
  grid[x][y] += 2

def parseCommand(command):
  s = command.split()
  if s[0] == 'turn':
    c1 = s[2].split(',')
    c2 = s[4].split(',')
  else:
    c1 = s[1].split(',')
    c2 = s[3].split(',')

  c1 = map(int, c1)
  c2 = map(int, c2)
  for x in range(c1[0], c2[0]+1):
    for y in range(c1[1], c2[1]+1):
      if s[1] == 'on':
        turnOn(x, y)
      elif s[1] == 'off':
        turnOff(x, y)
      else:
        toggle(x, y)

if __name__ == '__main__':
  with open('input', 'r') as f:
    commands = f.read().splitlines()

  for command in commands:
    parseCommand(command)

  print sum(map(sum, grid))
