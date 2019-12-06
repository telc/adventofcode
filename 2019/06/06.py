#!/usr/bin/env python2.7

from collections import defaultdict

with open('input', 'r') as f:
  input_ = f.read().splitlines()

#input_ = """COM)B
#B)C
#C)D
#D)E
#E)F
#B)G
#G)H
#D)I
#E)J
#J)K
#K)YOU
#I)SAN
#K)L""".splitlines()

def tree(graph, start):
  tree = []
  node = graph[start]
  while node != 'COM':
    tree.append(node)
    node = graph[node]
  tree.append(node)
  return tree

def solve(pairs):
  graph = {}
  for nodes in pairs:
    graph[nodes[1]] = nodes[0]

  edges = 0
  for node in graph:
    while node != 'COM':
      edges += 1
      node = graph[node]

  you = tree(graph, 'YOU')
  san = tree(graph, 'SAN')
  common = [i for i in you if i in san][0]

  return edges, you.index(common) + san.index(common)

if __name__ == '__main__':
  print solve([x.split(')') for x in input_])
