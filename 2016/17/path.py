#!/usr/bin/env python

from hashlib import md5

hashPos = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
frontier = [(0,0,'')]
visited = set()
shortestPath = None
longestPath = None

def isOpen(x,y,direction, h):
  global hashPos
  if ord(h[hashPos[direction]]) >= ord('b'):
    return True
  return False

def nextNode(node):
    (x,y,path) = node
    h = 'pgflpeqp' + path
    h = md5(h).hexdigest()[:4]
    cand = [(0,1,'D'), (0,-1,'U'), (1,0,'R'), (-1,0,'L')]
    return [(x + c[0], y + c[1], path + c[2]) for c in cand if x + c[0] >= 0 and x + c[0] < 4 and y + c[1] >= 0 and y + c[1] < 4 and isOpen(x + c[0], y + c[1], c[2], h)]

while len(frontier) > 0:
    new = frontier.pop()
    if new[0] == 3 and new[1] == 3:
      if not shortestPath or len(new[2]) < len(shortestPath):
        shortestPath = new[2]
      if not longestPath or len(new[2]) > longestPath:
        longestPath = len(new[2])
    else:
      visited.add(new[2])
      nextNodes = nextNode(new)
      frontier += [n for n in nextNodes if not n[2] in visited]
print shortestPath, longestPath
