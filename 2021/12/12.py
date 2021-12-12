#!/usr/bin/env python3

from collections import defaultdict

def findEnd(graph, node, path, twice, completed):
  if node == 'end':
    path = path + ',end'
    if not path in completed:
      completed.append(path)
    return

  for link in graph[node]:
    if link in path.split(',') and link == twice:
      findEnd(graph, link, path + ',' + node, None, completed)
    if link.islower() and link in path.split(','):
      continue
    findEnd(graph, link, path + ',' + node, twice, completed)


def solve(links):
  graph = defaultdict(list)
  for link in links:
    start, stop = link.split('-')
    graph[start].append(stop)
    graph[stop].append(start)
  completed = []
  findEnd(graph, 'start', '', None, completed)
  p1 = len(completed)
  for cave in graph:
    if cave.islower() and not cave == 'start' and not cave == 'end':
      findEnd(graph, 'start', '', cave, completed)
  return p1, len(completed)

def getInput(fn):
  with open(fn, 'r') as f:
    return f.read().splitlines()

def main():
  print(solve(getInput('example3')))

if __name__ == '__main__':
  main()
