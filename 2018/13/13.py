#!/usr/bin/env python2.7

from __future__ import print_function
from itertools import izip_longest

with open('input', 'r') as f:
  input_ = f.read().splitlines()

#input_ = r"""/->-\        
#|   |  /----\
#| /-+--+-\  |
#| | |  | v  |
#\-+-/  \-+--/
#  \------/   """.splitlines()

#input_ = r"""/>-<\  
#|   |  
#| /<+-\
#| | | v
#\>+</ |
#  |   ^
#  \<->/""".splitlines()

def turnRight(v):
  if v[1] == 0:
    return (v[1],v[0],v[2])
  else:
    return (-v[1],v[0],v[2])

def turnLeft(v):
  if v[1] == 0:
    return (v[1],-v[0],v[2])
  else:
    return (v[1],v[0],v[2])

def intersection(v):
  if v[2] == 0:
    v = turnLeft(v)
  elif v[2] == 2:
    v = turnRight(v)
  return (v[0], v[1], (v[2]+1) % 3)

def printRails(rail, trains):
  for y in xrange(len(rail)):
    for x in xrange(len(rail[y])):
      if (x,y) not in trains:
        print (rail[y][x], end='', sep='')
      else:
        print ('x', end='')
    print()

def solve(input_):
  rail = [list(line) for line in input_]
  trains = {}
  for y in xrange(len(rail)):
    for x in xrange(len(rail[y])):
      if rail[y][x] in '<>':
        if rail[y][x] == '<':
          trains[(x,y)] = (-1,0,0)
        else:
          trains[(x,y)] = (1,0,0)
        rail[y][x] = '-'
      elif rail[y][x] in '^v':
        if rail[y][x] == '^':
          trains[(x,y)] = (0,-1,0)
        else:
          trains[(x,y)] = (0,1,0)
        rail[y][x] = '|'
  first_crash = None
  count = 0
  while True:
    count += 1
    new_trains = {}
    for train in sorted(trains.keys(), key=lambda x: (x[1],x[0])):
      if train in new_trains:
        if first_crash == None:
          first_crash = train
        del new_trains[train]
        continue
      v = trains[train]
      x, y, _ = tuple([sum(x) for x in izip_longest(train, v, fillvalue=0)])
      if (x,y) in new_trains:
        if first_crash == None:
          first_crash = (x,y)
        del new_trains[(x,y)]
        continue
      if rail[y][x] in '-|':
        new_trains[(x,y)] = v
      elif rail[y][x] == '+':
        new_trains[(x,y)] = intersection(v)
      elif (rail[y][x] == '/' and v[0] != 0) or (rail[y][x] == '\\' and v[1] != 0):
        new_trains[(x,y)] = turnLeft(v)
      elif (rail[y][x] == '/' and v[1] != 0) or (rail[y][x] == '\\' and v[0] != 0):
        new_trains[(x,y)] = turnRight(v)
      else:
        print (x,y)
        exit()

    if len(new_trains) == 1:
      return first_crash, new_trains.keys()[0]
    trains = new_trains
if __name__ == '__main__':
  print (solve(input_))
