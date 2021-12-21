#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Tuple

@dataclass
class Node:
  p: Tuple
  g: int = 0
  parent = None

def distance(p1, p2):
  return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))

def getNeighbours(node, size):
  candidates = [(-1,0),(1,0),(0,-1),(0,1)]
  for cand in candidates:
    p = (cand[0] + node.p[0], cand[1] + node.p[1])
    if p[0] < 0 or p[0] >= size or p[1] < 0 or p[1] >= size:
      continue
    yield Node(p)

def getCost(p, costs, size):
  y = p[0] % len(costs)
  x = p[1] % len(costs[y])
  dist = p[0] // len(costs)
  dist += p[1] // len(costs[y])
  return (((costs[y][x] - 1) + dist) % 9) + 1
  

def solve(costs, size):
  goal = (size-1,size-1)
  
  open = [Node((0,0))]
  closed = set()

  while len(open) > 0:
    cur = None
    for node in open:
      if not cur or node.g < cur.g:
        cur = node
    open.remove(cur)
    closed.add(cur.p)

    if cur.p == goal:
      path = []
      node = cur
      while node is not None:
        path.append(node.p)
        node = node.parent
      return sum(map(lambda p: getCost(p, costs, size), path[:-1]))
    
    for node in getNeighbours(cur, size):
      if node.p in closed:
        continue

      node.g = cur.g + getCost(node.p, costs, size)
      node.parent = cur

      found = False
      for open_node in open:
        if node.p == open_node.p:
          found = True
          if node.g <= open_node.g:
            open_node.g = node.g
            open_node.parent = node.parent
          break
      
      if not found:
        open.append(node)

def getInput(fn):
  with open(fn, 'r') as f:
    return [[int(x) for x in line] for line in f.read().splitlines()]

def main():
  costs = getInput('input')
  print(solve(costs, len(costs)), solve(costs, len(costs)*5))

if __name__ == '__main__':
  main()
