#!/usr/bin/env python
import itertools
from copy import deepcopy

NUMUNIQUE = 0

class Floor:
  def __init__(self, generators, microchips):
    self.generators = generators
    self.microchips = microchips

  def __eq__(self, other):
    return self.generators == other.generators and self.microchips == other.microchips

  def __str__(self):
    s = ''
    for element in ['O', 'T', 'P', 'R', 'C', 'E', 'D']:
      if element in self.generators:
        s += element + ''
      else:
        s += '.'
      if element in self.microchips:
        s += element + ''
      else:
        s += '.'
    return s

  def __repr__(self):
    return str(self)

class State:
  def __init__(self, elevator, steps, floors):
    self.elevator = elevator
    self.steps = steps
    self.floors = floors

  def __repr__(self):
    s = str(self.steps) + '\n'
    for i in range(len(self.floors)):
      if i == self.elevator:
        s += 'E'
      else:
        s += '.'
      s += str(self.floors[i]) + '\n'
    return s

  def hash(self):
    h = str(self.elevator)
    for floor in self.floors:
      h += str(floor)
    return h

  def isDone(self):
    if len(self.floors[-1].generators) >= NUMUNIQUE and len(self.floors[-1].microchips) >= NUMUNIQUE:
      return True
    return False

  def move(self, gens, chips, direction):
    if self.elevator + direction >= 0 and self.elevator + direction < len(self.floors):
      f = self.elevator
      t = f + direction
      tmpFloors = deepcopy(self.floors)
      tmpFloors[f].microchips = [x for x in tmpFloors[f].microchips if x not in chips]
      tmpFloors[f].generators = [x for x in tmpFloors[f].generators if x not in gens]
      tmpFloors[t].microchips += chips
      tmpFloors[t].generators += gens
      if isStateValid(tmpFloors):
        yield State(t, self.steps+1, tmpFloors)

def isStateValid(floors):
  for floor in floors:
    if floor.generators:
      for m in floor.microchips:
        if m not in floor.generators:
          return False
  return True

def allMoves(floors, elevator):
  for gens in list(itertools.combinations(floors[elevator].generators, 2)) + list(itertools.combinations(floors[elevator].generators, 1)):
    gens = list(gens)
    yield (gens, [], 1)
    yield (gens, [], -1)
  for chips in list(itertools.combinations(floors[elevator].microchips, 2)) + list(itertools.combinations(floors[elevator].microchips, 1)):
    chips = list(chips)
    yield ([], chips, 1)
    yield ([], chips, -1)
  for gen in floors[elevator].generators:
    if gen in floors[elevator].microchips:
      yield ([gen], [gen], 1)
      yield ([gen], [gen], -1)


states = []
visited = set()
startState = State(0, 0, [Floor(['O', 'T', 'P', 'R', 'C', 'E', 'D'], ['T', 'R', 'C', 'E', 'D']),Floor([], ['O', 'P']),Floor([], []),Floor([], [])])
NUMUNIQUE = 7
#startState = State(0, 0, [Floor([], ['O','T']), Floor(['O'], []), Floor(['T'], []), Floor([], [])])
#NUMUNIQUE = 2

visited.add(startState.hash())
for move in allMoves(startState.floors, startState.elevator):
  states += [x for x in startState.move(*move)]

while len(states) > 0:
  state = states.pop(0)
  h = state.hash()
  if h in visited:
#print 'visited before: ' + h
    continue
  visited.add(h)
  if state.isDone():
    print state.steps
    exit()
  for move in allMoves(state.floors, state.elevator):
    states += [x for x in state.move(*move) if x.hash() not in visited]
print 'No solution'
