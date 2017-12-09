#!/usr/bin/env python

import itertools

nodes = {}
maxx = 0
maxy = 0

for node in open('inputfile').readlines():
  n = node.split()
  x, y = map(int, [x.lstrip('x').lstrip('y') for x in n[0].split('-')[1:]])
  if x > maxx:
    maxx = x
  if y > maxy:
    maxy = y
  used = int(n[2].rstrip('T'))
  avail = int(n[3].rstrip('T'))
  nodes[(x,y)] = (used, avail)

#pairs = [pair for pair in itertools.permutations(nodes.keys(), 2) if pair[0] != pair[1] and nodes[pair[0]][0] > 0 and nodes[pair[1]][1] >= nodes[pair[0]][0] ]
zerox = 0
zeroy = 0
for y in range(maxy):
  for x in range(maxx):
    if nodes[(x,y)][0] == 0:
      print '_',
      zerox = x
      zeroy = y
    elif nodes[(x,y)][0] > 87:
      print '#',
    else:
      print '.',
  print

