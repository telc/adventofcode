#!/usr/bin/env python2.7

with open('input', 'r') as f:
  input_ = f.read().splitlines()

#input_ = """<x=-1, y=0, z=2>
#<x=2, y=-10, z=-7>
#<x=4, y=-8, z=8>
#<x=3, y=5, z=-1>""".splitlines()

class Moon:
  def __init__(self, pos):
    self.__pos = pos
    self.__vel = (0, 0, 0)

  def pos(self):
    return self.__pos

  def vel(self):
    return self.__vel

  def energy(self):
    return sum(map(abs, self.__pos)) * sum(map(abs, self.__vel))

  def updateGravity(self, other):
    for o in other:
      v = tuple(map(lambda a: 1 if a[0] < a[1] else -1 if a[0] > a[1] else 0, zip(self.__pos, o.pos())))
      self.__vel = tuple(map(sum, zip(self.__vel, v)))

  def move(self):
    self.__pos = tuple(map(sum, zip(self.__pos, self.__vel)))

  def prnt(self):
    pos = self.__pos
    vel = self.__vel
    print "pos=<x={:3d}, z={:3d}, z={:3d}>, vel=<x={:3d}, z={:3d}, z={:3d}>".format(pos[0], pos[1], pos[2], vel[0], vel[1], vel[2])

def solve(lines):
  moons = []
  for line in lines:
    pos = tuple([int(l.split('=')[1].strip('>')) for l in line.split(',')])
    moons.append(Moon(pos))
  states = set()
  states.add( reduce(lambda a,b: a+b, [m.pos() + m.vel() for m in moons]) )
  step = 0
  while True:
    step += 1
    for m in xrange(len(moons)):
      other = moons[:m] + moons[m+1:]
      moons[m].updateGravity(other)
    state = ()
    for moon in moons:
      moon.move()
      state += moon.pos() + moon.vel()
    if step == 1000:
      part1 = sum([m.energy() for m in moons])
    if state in states:
      break
    states.add(state)

  return part1, step

if __name__ == '__main__':
  print solve(input_)
