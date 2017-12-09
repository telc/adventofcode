#!/usr/bin/env python

import itertools

nodes = {}

for node in open('inputfile').readlines():
  n = node.split()
  x, y = map(int, [x.lstrip('x').lstrip('y') for x in n[0].split('-')[1:]])
  used = int(n[2].rstrip('T'))
  avail = int(n[3].rstrip('T'))
  nodes[(x,y)] = (used, avail)

pairs = [pair for pair in itertools.permutations(nodes.keys(), 2) if pair[0] != pair[1] and nodes[pair[0]][0] > 0 and nodes[pair[1]][1] >= nodes[pair[0]][0] ]
print len(pairs)
