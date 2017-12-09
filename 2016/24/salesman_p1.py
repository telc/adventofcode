#!/usr/bin/env python

class Node:
  def __init__(self, value, coord):
    self.value = value
    self.coord = coord
    self.parent = None
    self.H = 0
    self.G = 0

  def __repr__(self):
    return str( self.coord )

  def moveCost(self, other):
    return 0

def isCoordOpen(x, y):
  magic = 1362
  n = x*x + 3*x + 2*x*y + y + y*y + magic
  bits = bin(n).count('1')
  if bits % 2 == 0:
    return True
  return False

def children(node, grid):
  x,y = node.coord
  links = [grid[d[1]][d[0]] for d in [(x-1,y),(x,y-1),(x,y+1),(x+1,y)] if d[0] >= 0 and d[0] < len(grid[0]) and d[1] >= 0 and d[1] < len(grid)]
  return [link for link in links if link.value]

def distance(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def aStar(start, goal, grid):
  openset = set()
  closedset = set()
  current = start
  openset.add(current)
  while openset:
    current = min(openset, key=lambda o:o.G + o.H)
    if current == goal:
      path = []
      while current.parent:
        path.append(current)
        current = current.parent
      path.append(current)
      return path[::-1]
    
    openset.remove(current)
    closedset.add(current)

    for node in children(current, grid):
      if node in closedset:
        continue
      if node in openset:
        new_g = current.G + current.moveCost(node)
        if node.G > new_g:
          node.G = new_g
          node.parent = current
      else:
        node.G = current.G + current.moveCost(node)
        node.H = distance(node.coord, goal.coord)
        node.parent = current
        openset.add(node)
  raise valueError('No path found')

mapSize = 100
goal = (31,39)
maze = []

for y in range(mapSize):
  row = []
  for x in range(mapSize):
    row.append(Node(isCoordOpen(x,y), (x,y)))
  maze.append(row)

path = aStar(maze[1][1], maze[goal[1]][goal[0]], maze)
print len(path) - 1
