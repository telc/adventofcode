#!/usr/bin/env python

import itertools
import sys

happyness = {}


def parseSeating(line):
  l = line.split()
  if not l[0] in happyness:
    happyness[l[0]] = {}
  if l[2] == 'lose':
    h = int(l[3]) * -1
  else:
    h = int(l[3])
  happyness[l[0]][l[-1].split('.')[0]] = h

def calcHappyness(seating):
  happy = 0
  for i in range(len(seating)):
    happy += happyness[seating[i]][seating[i-1]]
    if i == len(seating)-1:
      happy += happyness[seating[i]][seating[0]]
    else:
      happy += happyness[seating[i]][seating[i+1]]
  return happy

if __name__ == '__main__':
  with open('input', 'r') as f:
    lines = f.read().splitlines()

  for line in lines:
    parseSeating(line)

  most_happy = -10000000
  perms = itertools.permutations(happyness.keys())
  for p in perms:
    happy = calcHappyness(p)
    if happy > most_happy:
      most_happy = happy

  print most_happy,

  me = {}
  for key in happyness.keys():
    me[key] = 0
    happyness[key]['Me'] = 0
  happyness['Me'] = me
  most_happy = -1000000
  perms = itertools.permutations(happyness.keys())
  for p in perms:
    happy = calcHappyness(p)
    if happy > most_happy:
      most_happy = happy
  print most_happy
