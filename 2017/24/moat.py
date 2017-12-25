#!/usr/bin/env python2.7

with open('input', 'r') as f:
  components = f.read()

test = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""

def buildBridges(bridge, nextValue, components):
  bridges = [bridge]
  for i in range(len(components)):
    c = components[i]
    if c[0] == nextValue or c[1] == nextValue:
      if c[0] == nextValue:
        n = c[1]
      else:
        n = c[0]
      bridges += buildBridges(bridge + [c], n, components[:i] + components[i+1:])
  return bridges
      

def solve(components):
  components = [tuple(map(int,c.split('/'))) for c in components.splitlines()]
  starters = []
  for c in components:
    if c[0] == 0 or c[1] == 0:
      starters.append(components.pop(components.index(c)))
  bridges = []
  for i in range(len(starters)):
    bridges += buildBridges([starters[i]], max(starters[i]), starters[:i] + starters[i+1:] + components)
  maxBridge = 0
  longest = 0
  maxLongest = 0
  for bridge in bridges:
    l = len(bridge)
    s = sum(map(sum, bridge))
    if s > maxBridge:
      maxBridge = s
    if l > longest:
      longest = l
      maxLongest = s
    elif l == longest and s > maxLongest:
      longest = l
      maxLongest = s
  return maxBridge, maxLongest
if __name__ == '__main__':
    print solve(components)
