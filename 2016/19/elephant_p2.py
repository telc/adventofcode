#!/usr/bin/env python

class Node:
  def __init__(self, id):
    self.id = id + 1
    self.next = None
    self.prev = None

  def delete(self):
    self.next.prev = self.prev
    self.prev.next = self.next

size = 3014603
elves = map(Node, xrange(size))
for i in xrange(size):
  elves[i].next = elves[(i+1)%size]
  elves[i].prev = elves[(i-1)%size]

active = elves[0]
target = elves[size/2]
for i in xrange(size-1):
  target.delete()
  target = target.next
  if (size - i) % 2 != 0:
    target = target.next
  active = active.next

print active.id
