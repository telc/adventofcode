#!/usr/bin/env python

frontier = [(1,1,0)]
visited = {}

def getWall(x,y):
    magic = 1362
    n = x*x + 3*x + 2*x*y + y + y*y + magic
    return bin(n).count('1') % 2 == 0 and x >= 0 and y >= 0

def nextNode(node):
    (x,y,depth) = node
    cand = [(0,1), (0,-1), (1,0), (-1,0)]
    return [(x + c[0], y + c[1], depth + 1) for c in cand if getWall(x + c[0], y + c[1])]

while len(frontier) > 0:
    new = frontier.pop()
    visited[(new[0], new[1])] = new[2]
    frontier += [n for n in nextNode(new) if not (n[0], n[1]) in visited or visited[(n[0], n[1])] > n[2]]

print len([visited[n] for n in visited if visited[n] <= 50])
