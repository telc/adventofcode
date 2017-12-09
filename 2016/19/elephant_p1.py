#!/usr/bin/env python

size = 3014603
elves = [i+1 for i in range(size)]

while len(elves) > 1:
  wasOdd = not len(elves) % 2 == 0
  elves = elves[0::2]
  if wasOdd:
    elves = elves[-1:] + elves[:-1]
print elves[0]
