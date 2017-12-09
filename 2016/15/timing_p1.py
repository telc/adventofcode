#!/usr/bin/env python

input = """Disc #1 has 13 positions; at time=0, it is at position 10.
Disc #2 has 17 positions; at time=0, it is at position 15.
Disc #3 has 19 positions; at time=0, it is at position 17.
Disc #4 has 7 positions; at time=0, it is at position 1.
Disc #5 has 5 positions; at time=0, it is at position 0.
Disc #6 has 3 positions; at time=0, it is at position 1."""

class Disk:
  def __init__(self, size, startPos):
    self.size = size
    self.pos = startPos

  def __repr__(self):
    return '(' + str(self.size) + ', ' + str(self.pos) + ')'

  def tick(self):
    self.pos = (self.pos + 1) % self.size

  def getPosAt(self, time):
    return (self.pos + time) % self.size

disks = []

for line in input.split('\n'):
  l = line.split()
  disks.append(Disk(int(l[3]), int(l[-1].rstrip('.'))))

i = 0
while True:
  aligned = True
  for d in range(len(disks)):
    if disks[d].getPosAt(d+1) != 0:
      aligned = False
      break
  if aligned:
    break
  for disk in disks:
    disk.tick()
  i += 1
print i
