#!/usr/bin/env python2.7

with open('input', 'r') as f:
   particles = f.read()

test = """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>"""

from string import maketrans
from ast import literal_eval
from operator import add
from collections import defaultdict

def parseData(lines):
  particles = []
  i = 0
  trans = maketrans('<>', '()')
  for line in lines.splitlines():
    particle = {'i': i}
    for para in [l.split('=') for l in line.translate(trans).split(', ')]:
      particle[para[0]] = literal_eval(para[1])
    particles.append(particle)
    i += 1
  return particles

def tick(particles):
  for i in xrange(len(particles)):
    particles[i]['v'] = tuple(map(add, particles[i]['v'], particles[i]['a']))
    particles[i]['p'] = tuple(map(add, particles[i]['p'], particles[i]['v']))
    

def distance(particle):
  return sum(map(abs, particle['p']))

def part1(lines):
  particles = parseData(lines)
  maxDistance = 1000000000
  closest = -1
  for _ in xrange(500):
    tick(particles)
  for p in particles:
    d = distance(p)
    if d < maxDistance:
      maxDistance = d
      closest = p['i']
  return closest

def tick2(particles):
  positions = defaultdict(list)
  for i in xrange(len(particles)):
    particles[i]['v'] = tuple(map(add, particles[i]['v'], particles[i]['a']))
    particles[i]['p'] = tuple(map(add, particles[i]['p'], particles[i]['v']))
    positions[particles[i]['p']].append(i)
  pri = False
  delete = []
  for pos, ids in positions.iteritems():
    if len(ids) > 1:
      delete = delete + ids
  for i in sorted(delete, reverse=True):
    del particles[i]

 
def part2(lines):
  particles = parseData(lines)
  for _ in xrange(500):
    tick2(particles)
  return len(particles)

if __name__ == '__main__':
  print part1(particles)
  print part2(particles)
