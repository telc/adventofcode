#!/usr/bin/env python

import sys

names = []
nodes = {}
paths = []
costs = 0

def parseRoute(route):
  r = route.split()
  if not r[0] in names:
    names.append(r[0])
  if not r[2] in names:
    names.append(r[2])
  if not r[0] in nodes:
    nodes[r[0]] = {}
  if not r[2] in nodes:
    nodes[r[2]] = {}
  n1 = nodes[r[0]]
  n2 = nodes[r[2]]
  n1[r[2]] = int(r[-1])
  n2[r[0]] = int(r[-1])

def findShortest(targets):
  shortest_cost = sys.maxint
  shortest_path = None

  for name in targets:
    for n in nodes[name]:
      if nodes[name][n] < shortest_cost:
        if not (name in paths and n in paths):
          shortest_cost = nodes[name][n]
          shortest_path = (name, n)
  return (shortest_path, shortest_cost)

def findLongest(targets):
  longest_cost = 0
  longest_path = None

  for name in targets:
    for n in nodes[name]:
      if nodes[name][n] > longest_cost:
        if not (name in paths and n in paths):
          longest_cost = nodes[name][n]
          longest_path = (name, n)
  return (longest_path, longest_cost)

def appendPath(path_to, path_from):
  global paths
  try:
    if paths[0] == path_from:
      tmp = [path_to]
      tmp.extend(paths)
      paths = tmp
    else:
      paths.append(path_to)
  except:
    paths.append(path_to)

def addPath(path, cost):
  global costs
  new = False
  if not path[0] in paths:
    appendPath(path[0], path[1])
    new = True
  if not path[1] in paths:
    appendPath(path[1], path[0])
    new = True
  if new:
    print path
    costs += cost

if __name__ == '__main__':
  with open('input', 'r') as f:
      routes = f.read().splitlines()

  for route in routes:
    parseRoute(route)

  shortest_cost = sys.maxint
  for i in range(len(names)):
    costs = 0
    paths = []
    addPath(*findShortest([names[i]]))

    while len(paths) < 8:
      addPath(*findShortest([paths[0],paths[-1]]))

    if costs < shortest_cost:
      shortest_cost = costs
  longest_cost = 0
  for i in range(len(names)):
    costs = 0
    paths = []
    addPath(*findLongest([names[i]]))

    while len(paths) < 8:
      addPath(*findLongest([paths[0],paths[-1]]))
    
    if costs > longest_cost:
      longest_cost = costs
  print shortest_cost, longest_cost
